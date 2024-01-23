# Transactions Categorization Application

## Introduction

This application is designed to categorize payees from transactional data using several strategies. These strategies include matching against predefined keywords, utilizing GPT-based natural language understanding, and engaging search-based categorization to enhance accuracy.

## Installation

Before running the application, make sure you have installed all the necessary packages:
```
pip install -r requirements.txt
```

The `requirements.txt` file includes all the dependencies required for the application to run.

## Configuration

Categorization strategies rely on various external services. Hence, it is essential to set up the following environment variables:

- `OPENAI_API_KEY`: for GPT-based categorization strategy.
- `SERPAPI_API_KEY`: for search-based categorization strategy.

Place these keys in a `.env` file at the root of your project directory.

## Usage

To initiate the payee categorization process, use the following command:
```
python main.py --csv_file "path/to/your/transactions.csv"
```

Replace `"path/to/your/transactions.csv"` with the actual path to your transactions CSV file.

## Features

- **Keyword-based Categorization**: Utilizes a list of predefined keywords associated with various categories to determine the appropriate category for each payee.

- **GPT-based Categorization**: Leverages OpenAI's GPT models to categorize payees based on natural language understanding.

- **Search-based Categorization**: Combines the results from search engines and GPT models to ascertain the most fitting category for the payees.

## Output

The application outputs the categorized payees into a CSV file named `categorized_payees.csv` in the project's root directory.

## Documentation

For further details on all aspects of the application such as file structure, additional configurations, and contribution guidelines, please refer to the `docs.md` file.

## Logging

The categorization process is logged into `app.log`, which facilitates tracking progress and debugging issues as they arise.

## Contributing

Contributions to the development and enhancement of the application's categorization strategies are welcome. Please refer to `docs.md` for guidelines on contributing to the project.

## License

This project is licensed under [insert appropriate license here], which allows for modification, distribution, and private use.

## Acknowledgements

The categorization strategies used in this application may utilize services and products provided by OpenAI and SERPAPI among others.

## Support

If you encounter any issues or require assistance, please open an issue on the project's GitHub repository.