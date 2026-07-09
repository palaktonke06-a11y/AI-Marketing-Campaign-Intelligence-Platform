from faker import Faker
import random

# Reproducible results
SEED = 42
random.seed(SEED)

fake = Faker("en_IN")
Faker.seed(SEED)

# -----------------------------
# Dataset Sizes
# -----------------------------
NUM_CUSTOMERS = 50000
NUM_PRODUCTS = 500
NUM_CAMPAIGNS = 1000
NUM_LOCATIONS = 20

# We will generate the Date table dynamically
START_DATE = "2023-01-01"
END_DATE = "2025-12-31"

# -----------------------------
# Output Folder
# -----------------------------
OUTPUT_PATH = "data/raw"