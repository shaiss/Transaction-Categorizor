import logging
from strategy_registry import CategorizationStrategy
from serpapi import GoogleSearch
from openai import OpenAI

class SearchBasedCategorization(CategorizationStrategy):

  def __init__(self, serpapi_api_key, openai_api_key, categories_dict):
    self.serpapi_api_key = serpapi_api_key
    self.client = OpenAI(api_key=openai_api_key)
    self.categories = categories_dict
    self.cached_categories = {} 
    self.payees_processed = 0

  def analyze_with_gpt4(self, payee, search_results):
    response = self.client.chat.completions.create(
    model="gpt-4-1106-preview",
    #model="gpt-3.5-turbo",
    max_tokens=2000,
    messages=[{
        "role":
        "system",
        "content":
        "You are a bookkeeping expert trained in the art of categorization."
    }, {
        "role":
        "assistant",
        "content":
        f"I will analyze and use the {search_results} for my archsech data. I will respond in the format 'Category', nothing else. No explanations. "
    }, {
        "role":
        "user",
        "content":
        f"Please categorize the {payee} based on your analysis of provided data"
    }])
    # log the messages to logging.debug
   
    logging.debug(f"GPT4 response: {response}")
    # Extract the category from the response
    category = response.choices[0].message.content.strip()
    return category

  def categorize(self, payee):
    logging.info(f"Processing payee: {payee}")
    # Check if payee is already categorized.
    if payee in self.cached_categories:
      category = self.cached_categories[payee]
      logging.debug(f"Payee {payee} already categorized as {category}")
      return category, 2  # Return the cached category with a confidence score of 2
    
    # If the payee is not cached, use OpenAI APIs and google data to categorize the payee
    self.payees_processed += 1
    logging.info(f"Payee {payee} not cached, using OpenAI API and Google Data to categorize")
    params = {
        "api_key": self.serpapi_api_key,
        "engine": "google",
        "q": f"what company is this charge from: {payee}",
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    combined_text = " ".join([
        res.get('snippet', '')
        for res in results.get('organic_results', [])[:5]
    ])

    logging.info(f"payee: {payee}")
    
    # logging.info results value 
    #logging.info(f"results: {results}")
  
    # logging.debug the combined_text
    logging.debug(f"Combined text: {combined_text}")
    
    category = self.analyze_with_gpt4(payee, combined_text)
    # Cache the category for future reference
    self.cached_categories[payee] = category

    self._log_statistics()
    return category, 2  # Confidence score 2
  def _log_statistics(self):
    cached_count = len(self.cached_categories)
    logging.info(f"Count of entries in cache: {cached_count}, "
                  f"Count payees sent to OpenAI APIs for categorization: {self.payees_processed}")