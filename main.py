# Standard library imports
import argparse
import os
import logging  # Import the logging library
import time
import json


# Third-party imports
import pandas as pd
from dotenv import load_dotenv

# Local application/library specific imports
import strategy_selector
from utils import load_csv_sample, output_to_csv
from strategy_registry import CategorizationStrategyRegistry
#from categorization_strategies.keyword_based import KeywordBasedCategorization
#from categorization_strategies.gpt_based import GPTBasedCategorization
#from categorization_strategies.search_based import SearchBasedCategorization

# Read the categories config file.
with open('categories_config.json', 'r') as file:
    categories_dict = json.load(file)
# Initialize the search-based strategy passing the categories_dict.
#search_based = SearchBasedCategorization(categories_dict)

# Load environment variables for API keys, etc.
load_dotenv()

# Configure logging to output to both file and console
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler('app.log', mode='w'),
                        logging.StreamHandler()                   
                    ])

logging.debug('Script started')  # Log script start

def main():
  # Log the start of the main function
  logging.debug('Entered main function')  
  
  # Register the categorization strategies
  """CategorizationStrategyRegistry.register_strategy(
      "keyword", KeywordBasedCategorization(categories_dict))
  CategorizationStrategyRegistry.register_strategy(
      "gpt", GPTBasedCategorization(os.getenv('OPENAI_API_KEY')))
  CategorizationStrategyRegistry.register_strategy(
    "search",
    SearchBasedCategorization(os.getenv('SERPAPI_API_KEY'),
                              os.getenv('OPENAI_API_KEY'),categories_dict))
  """
  strategy_selector.register_strategies(categories_dict)

  # Parse command-line arguments for configuration
  parser = argparse.ArgumentParser(description="Categorize Payees")
  """parser.add_argument("--strategy",
                      help="Categorization strategy to use",
                      #default="keyword")
                      default="search")"""
  parser.add_argument("--csv_file",
                      help="Path to the transactions CSV file",
                      default="transactions.csv"
                     )
  args = parser.parse_args()
  """
    # Log the chosen strategy using logging.debug
    chosen_strategy_name = args.strategy  # Get the chosen strategy from the parsed arguments
    logging.debug(f"Chosen strategy: {chosen_strategy_name}")  # Log the chosen strategy after obtaining it from args
  
    # Start Logging
    logging.info('Starting categorization process')
    
    # Get the chosen categorization strategy from the registry
    chosen_strategy = CategorizationStrategyRegistry.get_strategy(args.strategy)
  """
  # Load and process CSV data
  csv_data = load_csv_sample(args.csv_file)
  # Strategy selection based on the CSV file
  chosen_strategy_name = strategy_selector.select_strategy(categories_dict, args.csv_file)
  
  # Log the chosen strategy
  logging.debug(f"Using strategy: {chosen_strategy_name}")

  # Get the chosen categorization strategy from the registry
  chosen_strategy = CategorizationStrategyRegistry.get_strategy(chosen_strategy_name)

  # Load and process CSV data
  #file_path = "transactions.csv"
  #csv_data = load_csv_sample(file_path)

  # Categorizing the transactions
  categorized_results = []
  start_time = time.time()

  # use a python set to store the unique payees in csv_data['Description'] 
  #Desctiption is the column name in the csv file that contains the payee names.
  unique_payees = set(csv_data['Description']) 
  
  for payee in unique_payees:
      logging.debug(f"Processing payee: {payee}")
      category, confidence = chosen_strategy.categorize(payee)
      categorized_results.append({
          'payee': payee,
          'category': category,
          'confidence': confidence
      })
      logging.info(f'Categorized payee: {payee} as {category} with confidence {confidence}')

  end_time = time.time()
  elapsed_time = end_time - start_time
  logging.info(f"{chosen_strategy_name} executed in {elapsed_time:.4f} seconds")
  
  # Convert the results to a DataFrame and save to CSV
  output_to_csv(categorized_results, 'categorized_payees.csv')

  logging.info("Categorization complete. Results saved to 'categorized_payees.csv'.")
  logging.debug('Exiting main function')  # Log script exit
if __name__ == "__main__":
  main()