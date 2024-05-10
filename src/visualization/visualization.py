import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Load processed data."""
    return pd.read_csv('../../data/processed/processed_data.csv')

def plot_salary_by_department():
    """Plot average salary by department."""
    data = load_data()
    avg_salary = data.groupby('Department')['Salary'].mean()
    plt.figure(figsize=(8, 5))
    avg_salary.plot(kind='bar', color='green')
    plt.title('Average Salary by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Salary')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../../reports/figures/salary_by_department.png')
    plt.close()

if __name__ == "__main__":
    plot_salary_by_department()
