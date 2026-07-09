import pandas as pd
import random
import os
from config import OUTPUT_PATH

# -----------------------------
# Product Master Data
# -----------------------------

PRODUCT_CATEGORIES = {
    "Smartphone": [
        ("Apple", "iPhone"),
        ("Samsung", "Galaxy"),
        ("OnePlus", "OnePlus"),
        ("Google", "Pixel"),
        ("Xiaomi", "Redmi")
    ],

    "Laptop": [
        ("Apple", "MacBook"),
        ("Dell", "Inspiron"),
        ("HP", "Pavilion"),
        ("Lenovo", "ThinkPad"),
        ("Asus", "ROG")
    ],

    "Smartwatch": [
        ("Apple", "Watch"),
        ("Samsung", "Galaxy Watch"),
        ("Noise", "ColorFit"),
        ("Boat", "Wave"),
        ("Fire-Boltt", "Ninja")
    ],

    "Headphones": [
        ("Sony", "WH"),
        ("Boat", "Rockerz"),
        ("JBL", "Tune"),
        ("Apple", "AirPods"),
        ("Noise", "Buds")
    ],

    "Tablet": [
        ("Apple", "iPad"),
        ("Samsung", "Galaxy Tab"),
        ("Lenovo", "Tab"),
        ("Xiaomi", "Pad"),
        ("Realme", "Pad")
    ],

    "Camera": [
        ("Canon", "EOS"),
        ("Nikon", "D"),
        ("Sony", "Alpha"),
        ("Fujifilm", "X"),
        ("Panasonic", "Lumix")
    ]
}


def generate_products(num_products=300):

    rows = []

    for product_id in range(1, num_products + 1):

        category = random.choice(list(PRODUCT_CATEGORIES.keys()))

        brand, model = random.choice(PRODUCT_CATEGORIES[category])

        version = random.randint(1, 15)

        product_name = f"{model} {version}"

        price = random.randint(5000, 180000)

        margin = random.randint(8, 45)

        rating = round(random.uniform(3.5, 5.0), 1)

        launch_year = random.choice([2022, 2023, 2024, 2025])

        stock = random.choice([
            "In Stock",
            "Limited Stock",
            "Out of Stock"
        ])

        rows.append({

            "Product_ID": product_id,

            "Product_Name": product_name,

            "Brand": brand,

            "Category": category,

            "Price": price,

            "Profit_Margin(%)": margin,

            "Customer_Rating": rating,

            "Launch_Year": launch_year,

            "Stock_Status": stock

        })

    df = pd.DataFrame(rows)

    os.makedirs(OUTPUT_PATH, exist_ok=True)

    df.to_csv(

        os.path.join(OUTPUT_PATH, "products.csv"),

        index=False

    )

    print("✅ products.csv generated successfully!")

    return df