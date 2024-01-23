import logging
from strategy_registry import CategorizationStrategy
from openai import OpenAI
import time

class GPTBasedCategorization(CategorizationStrategy):

  def __init__(self, openai_api_key):
    self.client = OpenAI(api_key=openai_api_key)
    self.cached_categories = {}
    self.payees_processed = 0

  def categorize(self, payee):
    # Check if payee is already categorized.
    if payee in self.cached_categories:
      category = self.cached_categories[payee]
      logging.debug(f"Payee {payee} already categorized as {category}")
      return category, 2  # Return the cached category with a confidence score of 2

    # If the payee is not cached, use OpenAI APIs to categorize the payee
    self.payees_processed += 1
    logging.debug(f"Payee {payee} not cached, using OpenAI API to categorize")
    response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":
            "system",
            "content":
            "You are a bookkeeping expert trained in the art of categorization."
        }, {
            "role":
            "assistant",
            "content":
            "I will respond in the format 'Category', nothing else. No explanations."
        }, {
            "role":
            "user",
            "content":
            f"Please categorize the following payee based on their name: {payee}"
        }])
    # Extract the category from the response
    category = response.choices[0].message.content.strip()
    # Cache the category for future reference
    self.cached_categories[payee] = category

    self._log_statistics()
    return category, 2  # Assume a confidence score of 2 for GPT-based categorization 

  def _log_statistics(self):
    cached_count = len(self.cached_categories)
    logging.info(f"Count of entries in cache: {cached_count}, "
                  f"Count payees sent to OpenAI APIs for categorization: {self.payees_processed}")