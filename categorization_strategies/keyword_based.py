import logging
from strategy_registry import CategorizationStrategy
from fuzzywuzzy import process


class KeywordBasedCategorization(CategorizationStrategy):
    def __init__(self, categories):
      self.categories = categories
      """
      Keyword-based categorization strategy.
      """
    def categorize(self, payee):
        """
        Categorize payee based on predefined keywords.
        :param payee: Payee to categorize.
        :return: Categorized payee information.
        """
        # Implementation of keyword-based categorization
        payee_lower = payee.lower()
        for category, keywords in self.categories.items():
            for keyword in keywords:
                if keyword in payee_lower:
                    logging.debug(f"Categorized '{payee}' as '{category}' with keyword match: '{keyword}'")
                    return category, 100  # Assuming full confidence for a direct match
        logging.debug(f"No suitable category found for '{payee}'")
        return None, 0