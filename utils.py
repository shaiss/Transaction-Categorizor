import pandas as pd
import logging

def load_csv(file_path):
  """
    Loads the entire CSV file.
    :param file_path: Path to the CSV file.
    :return: DataFrame containing the CSV data.
    """
  # Implementation for loading entire CSV
  df = pd.read_csv(file_path)
  return df


def output_to_csv(data, output_path):
  """
    Outputs categorized data to a CSV file.
    :param data: Data to be written to the CSV.
    :param output_path: Path for the output CSV file.
    """
  # Implementation for writing data to CSV
  pd.DataFrame(data).to_csv(output_path, index=False)

def load_csv_sample(file_path, sample_size=100):
  """
    Loads a sample of the CSV file.
    :param file_path: Path to the CSV file.
    :param sample_size: Number of rows to sample from the file.
    :return: DataFrame containing the sampled data.
    """
  df = pd.read_csv(file_path, nrows=sample_size)
  df.columns = df.columns.str.strip()  # Strip whitespace from the column names
  logging.debug(f'Sample dataset from first {sample_size} in file {file_path}: {df}')
  return df