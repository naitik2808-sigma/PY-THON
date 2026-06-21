import pandas as pd
import zipfile

# Define the path to the sample CSV dataset
csv_file_path = r'C:\Users\naiti\OneDrive\Documents\housing.csv'

print(f"Loading data from: {csv_file_path}")

# Load and inspect the CSV dataset
try:
    if zipfile.is_zipfile(csv_file_path):
        with zipfile.ZipFile(csv_file_path) as archive:
            csv_names = [name for name in archive.namelist() if name.lower().endswith('.csv')]
            if not csv_names:
                raise ValueError('ZIP archive does not contain any CSV file.')
            with archive.open(csv_names[0]) as csv_file:
                df = pd.read_csv(csv_file, encoding='latin1')
    else:
        df = pd.read_csv(csv_file_path, encoding='latin1')
    print("\nDataset loaded successfully!")

    # Display the first few rows of the DataFrame
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Display basic information about the DataFrame (columns, non-null counts, data types)
    print("\nDataset Information:")
    df.info()

    # Display descriptive statistics of the numerical columns
    print("\nDescriptive Statistics:")
    print(df.describe())

except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found. Please ensure it's in the correct path.")
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")