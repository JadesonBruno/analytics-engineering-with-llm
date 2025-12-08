"""Lab 5 - Analytics Engineering - Python, SQL and LLM
for Extracting Insights in Data Engineering Pipelines"""

# Python - Runs the pipelin


# Import native libs
import subprocess  # nosec B404
import sys


# Function to run other Python scripts
def run_pipeline(script_name):
    try:
        result = subprocess.run(  # nosec B603
            [sys.executable, script_name], check=True, capture_output=True, text=True
        )
        print(f"\nScript {script_name} executed successfully.")
        print("\nOutput:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"\nError running script {script_name}.")
        print("\nError:\n", e.stderr)
        raise


# List of scripts
scripts = ["src/1_create_db.py", "src/2_load_db.py", "src/3_query.py", "src/4_llm.py"]

if __name__ == "__main__":
    try:
        # Run the scripts in a loop
        for script in scripts:
            run_pipeline(script)
        print("\nPipeline executed successfully.\n")
    except Exception as e:
        print(f"\nPipeline execution failed: {e}\n")
