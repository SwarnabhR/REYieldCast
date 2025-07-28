# scripts/ingest/feature_engineering.py

import os
import pandas as pd
import argparse
import logging

# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Default file paths
SOLAR