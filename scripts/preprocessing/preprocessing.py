import os
import argparse
import logging
from typing import Tuple
import pandas as pd


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

def load_and_prepare_config(path: str, config_type: str) -> pd.DataFrame:
    """
    Load and set index of configuration file.

    Args:
        path (str): File path to the config.
        config_type (str): 'solar' or 'wind'.

    Returns:
        pd.DataFrame: Config DataFrame indexed by plant_code_unique.
    """
    logging.info(f"Loading {config_type} config from {path}")
    try:
        df = pd.read_csv(path)
        return df.set_index("plant_code_unique")
    except Exception as e:
        logging.error(f"Failed to load {config_type} config: {e}")
        raise

def convert_cf_to_mw(cf_df: pd.DataFrame, config_df: pd.DataFrame, config_type: str) -> pd.DataFrame:
    """
    Convert hourly capacity factor to MW.

    Args:
        cf_df (pd.DataFrame): Raw capacity factor data.
        config_df (pd.DataFrame): Plant configuration DataFrame.
        config_type (str): 'solar' or 'wind'.

    Returns:
        pd.DataFrame: Hourly generation in MW.
    """
    logging.info(f"Converting {config_type} capacity factors to MW")

    # Parse datetime and set index
    cf_df = cf_df.rename(columns={cf_df.columns[0]: "datetime"})
    cf_df["datetime"] = pd.to_datetime(cf_df["datetime"], errors='coerce')
    cf_df.set_index("datetime", inplace=True)

    # Normalize plant codes
    config_df.index = config_df.index.astype(str)
    cf_df.columns = cf_df.columns.astype(str)

    # Filter to valid plant codes
    valid_plants = cf_df.columns.intersection(config_df.index)
    cf_df = cf_df[valid_plants]
    capacities = config_df.loc[valid_plants, "system_capacity"]

    # Convert to MW
    cf_mw_df = cf_df.multiply(capacities, axis=1)

    logging.info(f"{config_type.capitalize()} generation shape (MW): {cf_mw_df.shape}")
    return cf_mw_df

def process_all(
    solar_config_path: str,
    wind_config_path: str,
    solar_cf_path: str,
    wind_cf_path: str,
    output_dir: str
) -> None:
    """
    Complete preprocessing pipeline from raw CF to MW output.

    Args:
        solar_config_path (str): Path to solar config CSV.
        wind_config_path (str): Path to wind config CSV.
        solar_cf_path (str): Path to solar capacity factor CSV.
        wind_cf_path (str): Path to wind capacity factor CSV.
        output_dir (str): Directory to store processed MW CSVs.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Load configs
    solar_config = load_and_prepare_config(solar_config_path, "solar")
    wind_config = load_and_prepare_config(wind_config_path, "wind")

    # Load generation data
    solar_cf = pd.read_csv(solar_cf_path)
    wind_cf = pd.read_csv(wind_cf_path)

    # Convert to MW
    solar_mw = convert_cf_to_mw(solar_cf, solar_config, "solar")
    wind_mw = convert_cf_to_mw(wind_cf, wind_config, "wind")

    # Save outputs
    solar_out = os.path.join(output_dir, "solar_gen_2020_mw.csv")
    wind_out = os.path.join(output_dir, "wind_gen_2020_mw.csv")

    solar_mw.to_csv(solar_out)
    wind_mw.to_csv(wind_out)
    logging.info("MW generation files saved successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess solar and wind CF data to MW.")
    parser.add_argument("--solar-config", default="data/raw/configs/eia_solar_configs.csv", help="Path to solar config CSV")
    parser.add_argument("--wind-config", default="data/raw/configs/eia_wind_configs.csv", help="Path to wind config CSV")
    parser.add_argument("--solar-cf", default="data/raw/solar/solar_gen_cf_2020_bc.csv", help="Path to solar capacity factor CSV")
    parser.add_argument("--wind-cf", default="data/raw/wind/wind_gen_cf_2020.csv", help="Path to wind capacity factor CSV")
    parser.add_argument("--output-dir", default="data/processed", help="Output directory for MW CSV files")

    args = parser.parse_args()
    process_all(
        solar_config_path=args.solar_config,
        wind_config_path=args.wind_config,
        solar_cf_path=args.solar_cf,
        wind_cf_path=args.wind_cf,
        output_dir=args.output_dir
    )
