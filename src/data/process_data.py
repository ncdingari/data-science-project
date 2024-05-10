import pandas as pd

def load_data():
    """Load raw data from CSV."""
    return pd.read_csv('data-science-project//data/raw/raw_data.csv')

def process_data():
    """Clean and process the raw data."""
    data = load_data()
    data['Salary'] = data['Salary'].round(2)
    return data

def save_processed_data():
    """Save processed data to a CSV."""
    data = process_data()
    data.to_csv('data-science-project/data/processed/processed_data.csv', index=False)

if __name__ == "__main__":
    save_processed_data()
