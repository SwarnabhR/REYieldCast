# scripts/ingest/ingest_processed.py

import os
import pandas as pd
import logging 
from typing import Literal

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Constants
PROCESSED_DIR = "data/processed"
GEN_FILE_NAMES = {
    "solar": "solar_gen_2020_mw.csv",
    "wind": "wind_gen_2020_mw.csv"
}

def load_processed_generation(source: Literal["solar", "wind"]) -> pd.DataFrame:
    """Load processed generation data from CSV file.
    """
    if source not in GEN_FILE_NAMES:
        raise ValueError("Source must be 'solar' or 'wind'")
    
    path = os.path.join(PROCESSED_DIR, GEN_FILE_NAMES[source])
    logging.info(f"Loading processed {source} generation from: {path}")
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"File doesn't exist: {path}")
    
    df = pd.read_csv(path, index_col="datetime", parse_dates=["datetime"])
    logging.info(f"{source.capitalize()} data loaded with shape {df.shape}")
    return df

if __name__ == "__main__":
    try:
        solar_gen = load_processed_generation("solar")
        wind_gen = load_processed_generation("wind")
    except Exception as e:
        logging.error(f"Failed to load generation data: {e}")
    else:
        logging.info("Solar generation sample:\n%s", solar_gen.head(2))
        logging.info("Wind generation sample:\n%s", wind_gen.head(2))
    