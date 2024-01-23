# Documentation

## Overview

This application categorizes payees (i.e., entities to which payments are made) from transactional data using various strategies including keyword matching, GPT-based categorization, and search-based categorization.

The application is built with several Python scripts and follows an object-oriented approach to define categorization strategies that can be utilized within a flexible architecture.

## File Structure

- `categories_config.json`: Contains the keyword configurations for the different transaction categories.
- `requirements.txt`: Lists the Python package dependencies for the application.
- `categorization_strategies` module: Contains the different categorization strategy classes:
  - `keyword_based.py`: Defines the `KeywordBasedCategorization` class for categorizing payees based on a list of keywords.
  - `gpt_based.py`: Defines the `GPTBasedCategorization` class that uses OpenAI's GPT model for categorizing payees.
  - `search_based.py`: Defines the `SearchBasedCategorization` class that leverages search engine results and GPT models for categorization.
- `strategy_registry.py`: Implements the strategy pattern with `CategorizationStrategy` (abstract base class) and `CategorizationStrategyRegistry` (registry class).
- `strategy_selector.py`: Contains logic for selecting the suitable categorization strategy.
- `utils.py`: Includes utility functions for data loading and CSV operations.
- `main.py`: The main script of the application that orchestrates the categorization process.

## Dependencies

The application relies on several external Python libraries which can be installed using the following command:

```shell
pip install -r requirements.txt
```

## Usage
To run the categorization process, use the following command:
```
python main.py --csv_file=<path-to-csv>
```

where <path-to-csv> is the file path to your transactions CSV file.

## Configuration
Before running the application, ensure that the necessary API keys and environment variables are set:

`OPENAI_API_KEY`: Your OpenAI API key for access to the GPT models.
`SERPAPI_API_KEY`: Your SERP API key for access to search engine results.
These keys should be included in a `.env` file at the root of the project.

## Logging
The application logs its activity into `app.log`, making it easier to track the flow and troubleshoot potential issues.

## Categorization Output
The result of the categorization process is saved to a CSV file named `categorized_payees.csv` in the project's root directory.

## Contributing
If you wish to contribute to the categorization strategies or enhance the existing application, follow these steps:

Clone the repository.
Create a new branch for your feature.
Implement your changes.
Test your changes.
Submit a pull request.