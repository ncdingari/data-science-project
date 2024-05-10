import pandas as pd
import numpy as np

def generate_raw_data():
    """Generate synthetic raw data."""
    np.random.seed(0)
    data = pd.DataFrame({
        'Age': np.random.randint(18, 65, size=100),
        'Salary': np.random.normal(50000, 15000, 100),
        'Department': np.random.choice(['HR', 'Tech', 'Marketing'], 100)
    })
    return data

def save_raw_data():
    """Save the raw data to a CSV file."""
    data = generate_raw_data()
    data.to_csv('../data/raw/raw_data.csv', index=False)

if __name__ == "__main__":
    save_raw_data()
