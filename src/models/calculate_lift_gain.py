import pandas as pd
import numpy as np

def calculate_lift_gain(probabilities, actuals):
    """
    Calculate lift and gain for 10 deciles from given probabilities and actual outcomes.
   
    Parameters:
    probabilities (list or np.array): Predicted probabilities.
    actuals (list or np.array): Actual binary outcomes (0 or 1).
   
    Returns:
    pd.DataFrame: DataFrame containing decile, lift, and gain values.
    """
    # Create a DataFrame with probabilities and actuals
    data = pd.DataFrame({'probabilities': probabilities, 'actuals': actuals})
   
    # Sort the DataFrame by probabilities in descending order
    data = data.sort_values(by='probabilities', ascending=False).reset_index(drop=True)
   
    # Add a column for deciles
    data['decile'] = pd.qcut(data.index, 10, labels=False) + 1
   
    # Calculate the total number of positive cases
    total_positives = data['actuals'].sum()
   
    # Calculate the lift and gain for each decile
    lift_gain_data = data.groupby('decile').agg({
        'actuals': ['sum', 'count']
    }).reset_index()
   
    # Rename columns for better clarity
    lift_gain_data.columns = ['decile', 'positive_cases', 'total_cases']
   
    # Calculate cumulative positive cases and cumulative total cases
    lift_gain_data['cumulative_positive_cases'] = lift_gain_data['positive_cases'].cumsum()
    lift_gain_data['cumulative_total_cases'] = lift_gain_data['total_cases'].cumsum()
   
    # Calculate gain
    lift_gain_data['gain'] = (lift_gain_data['cumulative_positive_cases'] / total_positives) * 100
   
    # Calculate lift
    lift_gain_data['lift'] = (lift_gain_data['cumulative_positive_cases'] /
                              lift_gain_data['cumulative_total_cases']) / (total_positives / len(actuals))
   
    return lift_gain_data

# Example usage
probabilities = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01]
actuals = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]

lift_gain_df = calculate_lift_gain(probabilities, actuals)
print(lift_gain_df)
