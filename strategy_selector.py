from categorization_strategies.keyword_based import KeywordBasedCategorization
from categorization_strategies.gpt_based import GPTBasedCategorization
from categorization_strategies.search_based import SearchBasedCategorization
from strategy_registry import CategorizationStrategyRegistry
import os

def select_strategy(categories_dict, csv_file):
    # Logic for selecting a strategy based on data analysis will go here
    # Placeholder example:
    # if some_condition_based_on_csv(csv_file):
    #     return 'gpt'
    # else:
    #     return 'keyword'

    # For now, returning a default strategy as a placeholder
    return 'search'  # or 'keyword' or 'gpt' based on implementation

def register_strategies(categories_dict):
    # Register the categorization strategies
    CategorizationStrategyRegistry.register_strategy(
        "keyword", KeywordBasedCategorization(categories_dict))
    CategorizationStrategyRegistry.register_strategy(
        "gpt", GPTBasedCategorization(os.getenv('OPENAI_API_KEY')))
    CategorizationStrategyRegistry.register_strategy(
        "search",
        SearchBasedCategorization(os.getenv('SERPAPI_API_KEY'),
                                  os.getenv('OPENAI_API_KEY'), categories_dict))