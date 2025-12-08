"""Analytics Engineering - Python, SQL and LLM
for Extracting Insights in Data Engineering Pipelines"""

# Python - Pipeline for Loading Data into PostgreSQL

# Import native libs
import os

# Import third-party libs
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Create the connection engine
db_url = (
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@localhost:5433/{POSTGRES_DB}"
)

engine = create_engine(db_url)

print("\nStarting data load process!\n")


# Function to load data from CSV files into PostgreSQL within the specified schema
def load_data(csv_file, table_name, schema):

    # try/except block
    try:

        # Read the CSV file
        df = pd.read_csv(csv_file)

        # Write the DataFrame to the specified table
        df.to_sql(table_name, engine, schema=schema, if_exists="append", index=False)
        print(
            f"Data from file {csv_file} was inserted into table {schema}.{table_name}."
        )

    except Exception as e:
        print(
            f"Error inserting data from file {csv_file} "
            f"into table {schema}.{table_name}: {e}"
        )


# Load data into the 'analytics_engineering' schema
load_data("data/raw/customers.csv", "customers", "analytics_engineering")
load_data("data/raw/products.csv", "products", "analytics_engineering")
load_data("data/raw/purchases.csv", "purchases", "analytics_engineering")

print(
    "\nLoad completed successfully! ",
    "Use your preferred IDE for SQL to inspect the data if you wish.\n",
)
