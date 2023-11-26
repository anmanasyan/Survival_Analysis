import pandas as pd
def dummify_dataframe(df):
    """
    Converts categorical variables in a DataFrame to binary columns using one-hot encoding.
    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with categorical variables converted to binary columns.
    """
    # Identify string variables
    string_variables = df.select_dtypes(include=['object']).columns
    # Filter DataFrame to keep only string variables
    string_df = df[string_variables]
    # Dummify the string variables
    dummies_df = pd.get_dummies(string_df, columns=string_variables, prefix=string_variables,  drop_first=True)
    # Concatenate the dummified variables with the original DataFrame
    output_df = pd.concat([df, dummies_df], axis=1)
    # Drop the original string variables
    output_df = output_df.drop(columns=string_variables)

    return output_df

def calculate_clv(preds, data, MM=1300, r=0.1):
    """
    Calculate Customer Lifetime Value (CLV) for each customer in the DataFrame.

    Parameters:
        - preds (pd.DataFrame): A dataframe of survival function predictions.
        - data (pd.DataFrame): A dataframe of the original dataset, where we want to save results to.
        - MM (float): A constant representing the monetary value.
        - r (float): The periodic interest rate for discounting.

    Returns:
        - pd.Series: Series containing CLV values for each customer.
    """

    # Calculating clv
    sequence = list(range(1, len(preds.columns) + 1))
    # Iterating over each column in data_clv
    for num in sequence:
        # Discount the values in the column based on time-value-of-money calculation
        preds.iloc[:, num - 1] /= (1 + r/12) ** (num - 1)
    # Calculate CLV for each row
    data['CLV'] = MM * preds.sum(axis=1)