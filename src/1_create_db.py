"""Analytics Engineering - Python, SQL and LLM
for Extracting Insights in Data Engineering Pipelines"""

# Python - Database Creation Pipeline

# Import native libs
import os

# Import third-party libs
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")


# Function to execute a SQL script
def execute_script_sql(filename):

    # Connect to the PostgreSQL database with the provided credentials
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host="localhost",
        port="5433",
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Read the contents of the SQL file
    with open(filename, "r") as file:
        sql_script = file.read()

    try:
        # Execute the SQL script
        cur.execute(sql_script)

        # Commit the changes to the database
        conn.commit()
        print("\nScript executed successfully!\n")
    except Exception as e:
        # Roll back changes on error
        conn.rollback()
        print(f"Error executing script: {e}")
    finally:
        # Close communication with the database
        cur.close()
        conn.close()


# Execute the SQL script
execute_script_sql("sql/script.sql")
