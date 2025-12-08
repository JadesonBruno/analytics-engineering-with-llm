"""Analytics Engineering - Python, SQL and LLM
for Extracting Insights in Data Engineering Pipelines"""

# Python - Pipeline for Querying the Database

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


def execute_query(filename):

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
        # split produces -> ["SELECT 1", " SELECT 2", " ", ""]
        sql_commands = [c.strip() for c in sql_script.split(";") if c.strip()]
        # sql_commands -> ["SELECT 1", "SELECT 2"]
        for command in sql_commands:
            cur.execute(command)

            # Check if the command returned rows (e.g., SELECT)
            if cur.description:
                rows = cur.fetchall()
                for row in rows:
                    print(row)

        # Commit changes to the database
        conn.commit()
        print("\nScript executed successfully.\n")

    except Exception as e:
        # Roll back changes on error
        conn.rollback()
        print(f"Error executing script: {e}")

    finally:
        # Close communication with the database
        cur.close()
        conn.close()


# Executa o script SQL
execute_query("sql/query.sql")
