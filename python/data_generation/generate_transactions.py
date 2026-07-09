"""
Generate Transaction Fact Table
--------------------------------
Creates realistic customer purchase transactions for the
AI Marketing Campaign Intelligence Platform.
"""

import os
import random
import logging

import pandas as pd

from config import OUTPUT_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s : %(message)s"
)

logger = logging.getLogger(__name__)


def generate_transactions():

    logger.info("Generating Transactions...")

    customers = pd.read_csv(
        os.path.join(
            OUTPUT_PATH,
            "customers.csv"
        )
    )

    products = pd.read_csv(
        os.path.join(
            OUTPUT_PATH,
            "products.csv"
        )
    )

    campaigns = pd.read_csv(
        os.path.join(
            OUTPUT_PATH,
            "campaigns.csv"
        )
    )

    customer_ids = customers["Customer_ID"].tolist()
    customer_orders = dict(
    zip(
        customers["Customer_ID"],
        customers["Total_Orders"]
    )
)
    product_ids = products["Product_ID"].tolist()
    campaign_ids = campaigns["Campaign_ID"].tolist()

    transactions = []

    transaction_id = 1

    payment_methods = [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "Cash",
        "Wallet"
    ]

    order_status = [
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Returned",
        "Cancelled"
    ]

    coupon_codes = [
        "NEW10",
        "SAVE20",
        "FEST50",
        "WELCOME",
        "NONE"
    ]

    for customer in customer_ids:
        if customer % 1000 == 0:
            print(f"Processed {customer} customers...")

        total_orders = customer_orders[customer]

        for _ in range(total_orders):

            product_id = random.choice(product_ids)

            campaign_id = random.choice(campaign_ids)

            quantity = random.randint(1, 5)

            unit_price = random.randint(
                500,
                50000
            )

            discount = random.randint(
                0,
                40
            )

            gross_amount = quantity * unit_price

            discount_amount = round(
                gross_amount * discount / 100,
                2
            )

            net_amount = round(
                gross_amount - discount_amount,
                2
            )

            payment = random.choice(
                payment_methods
            )

            status = random.choice(
                order_status
            )

            coupon = random.choice(
                coupon_codes
            )

            transaction_date = pd.Timestamp(
                random.choice(
                    pd.date_range(
                        "2023-01-01",
                        "2025-12-31"
                    )
                )
            )

            transactions.append({

                "Transaction_ID": transaction_id,
                "Customer_ID": customer,
                "Campaign_ID": campaign_id,
                "Product_ID": product_id,

                "Transaction_Date": transaction_date,

                "Quantity": quantity,
                "Unit_Price": unit_price,

                "Gross_Amount": gross_amount,
                "Discount_Percentage": discount,
                "Discount_Amount": discount_amount,
                "Net_Amount": net_amount,

                "Coupon_Code": coupon,
                "Payment_Method": payment,
                "Order_Status": status

            })

            transaction_id += 1

    # ======================================================
    # Convert to DataFrame
    # ======================================================

    df = pd.DataFrame(transactions)

    logger.info(
        f"{len(df)} transactions generated successfully."
    )

    # ======================================================
    # Save CSV
    # ======================================================

    os.makedirs(
        OUTPUT_PATH,
        exist_ok=True
    )

    output_file = os.path.join(
        OUTPUT_PATH,
        "transactions.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    logger.info(
        "transactions.csv saved successfully."
    )

    return df


# ==========================================================
# Run Independently
# ==========================================================

if __name__ == "__main__":
    generate_transactions()