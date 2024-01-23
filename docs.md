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

## Function Descriptions

Below are descriptions of key functions in the application:

### `load_csv(file_path)`
This function is responsible for loading the entire CSV file specified by the `file_path` parameter. It returns a pandas DataFrame containing all the data from the CSV file.

### `output_to_csv(data, output_path)`
After categorizing the payee information, this function can be used to output the data to an output CSV file. The `data` parameter is the DataFrame or list of dictionaries that need to be written, and the `output_path` is the desired path for the output file.

### `load_csv_sample(file_path, sample_size)`
In cases where you want to work with a subset of your dataset, this function allows you to load a sample of your data. It takes the `file_path` to the CSV file and an optional `sample_size` that specifies the number of rows to sample.

### `KeywordBasedCategorization.categorize(payee)`
Part of the Keyword Based Categorization strategy, this function categorizes a payee by checking if any of the predefined keywords match the payee's name. It returns the category if a match is found or `None` if not, along with a confidence score.

### `GPTBasedCategorization.categorize(payee)`
This function is a method of the GPT Based Categorization strategy. It uses an OpenAI GPT model to determine the category of a payee. It employs natural language understanding by sending the payee name to the model and receiving a categorical prediction.

### `SearchBasedCategorization.categorize(payee)`
As a part of the Search Based Categorization strategy, this method combines the results from search engine queries and GPT model inferences to find the most appropriate category for a payee name.

### `select_strategy(categories_dict, csv_file)`
This function is used to determine the appropriate categorization strategy based on the csv file analysis. It returns a string identifier of the chosen strategy.

### `register_strategies(categories_dict)`
This function registers available categorization strategies into the strategy registry, allowing the application to utilize different strategies interchangeably.



## Contributing
If you wish to contribute to the categorization strategies or enhance the existing application, follow these steps:

Clone the repository.
Create a new branch for your feature.
Implement your changes.
Test your changes.
Submit a pull request.