import os

from config import OUTPUT_PATH
from generate_channels import generate_channels
from generate_products import generate_products
from generate_customers import generate_customers
from generate_locations import generate_locations
from generate_campaigns import generate_campaigns
from generate_campaign_performance import generate_campaign_performance
from generate_transactions import generate_transactions
from generate_customer_journey import generate_customer_journey

os.makedirs(OUTPUT_PATH, exist_ok=True)

print("=" * 60)
print(" AI Marketing Campaign Intelligence Platform ")
print("=" * 60)

generate_channels()
generate_products()
generate_customers()
generate_locations()
generate_campaigns()
generate_campaign_performance()
generate_transactions()
generate_customer_journey()

print("=" * 60)
print("Dataset Generation Completed Successfully!")
print("=" * 60)