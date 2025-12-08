"""Analytics Engineering - Python, SQL and LLM
for Extracting Insights in Data Engineering Pipelines"""

# Python - Pipeline for Extracting Insights with LLM

# Import native libs
import csv
import os

# Import third-party libs
import psycopg2
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Load environment variables from .env file
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Instantiation of the Llama3 LLM through Ollama
llm = OllamaLLM(model="llama3")

# Creation of the parser for the language model output
output_parser = StrOutputParser()


# Function to generate text based on PostgreSQL data
def dsa_gera_insights():

    # Connect to the PostgreSQL database with the provided credentials
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host="localhost",
        port="5433",
    )

    # Create a cursor to execute SQL commands
    cursor = conn.cursor()

    # Define the SQL query to get data from customers, purchases, and products
    query = """
        SELECT
            c.name,
            COUNT(p.purchase_id) AS total_purchases,
            SUM(pr.price) AS total_spent
        FROM
            analytics_engineering.customers c
        JOIN
            analytics_engineering.purchases p ON c.customer_id = p.customer_id
        JOIN
            analytics_engineering.products pr ON p.product_id = pr.product_id
        GROUP BY
            c.name;
    """

    # Execute the SQL query
    cursor.execute(query)

    # Get all query results
    rows = cursor.fetchall()

    # Initialize a list to store the insights
    insights = []

    # Creation of the prompt template for the chatbot
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """Você é um analista de dados especializado.
                Analise os dados sobre os padrões de compras dos clientes
                e forneça feedback em português do Brasil.""",
            ),
            ("user", "question: {question}"),
        ]
    )

    # Definition of the execution chain: prompt -> LLM -> output_parser
    chain = prompt | llm | output_parser

    # Iterate over the result rows
    for row in rows:

        # Unpack the values from each row
        name, total_purchases, total_spent = row

        # Create the prompt for the LLM based on client data
        consulta_cliente = f"Cliente {name} fez {total_purchases} \
            compras totalizando ${total_spent:.2f}."

        # Generate insight text using the LLM
        response = chain.invoke({"question": consulta_cliente})

        # Add the generated text to the insights list
        insights.append(response)

    # Close the database connection
    conn.close()

    # Save the insights to a CSV file
    with open(
        file="data/outputs/insights.csv", mode="w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["insight"])
        for insight in insights:
            writer.writerow([insight])

    # Return the list of insights
    return insights


# Generate insights by calling the defined function
insights = dsa_gera_insights()

# Print each generated insight
for insight in insights:
    print(insight)
