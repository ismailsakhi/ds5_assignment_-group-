import pandas as pd

df = pd.read_excel('dataProject4.xlsx')

def lower_case(df: pd.DataFrame) -> pd.DataFrame:
    """
    Lower case all the text for consistency

    """
    return df.applymap(lambda x: x.lower() if isinstance(x, str) else x)


def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove empty rows if any
    """
    return df.dropna(how= "all")

def remove_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    removing empty columns if any
    """
    return df.dropna(axis=1, how= "all")

def mean_for_empty_values(df: pd.DataFrame, customer_column: str) -> pd.DataFrame:
    """
    fill in missing vlaues with the mean of that column for that specific customer number
    
    :param df: input dataframe
    :param customer_column: teh column name that represents the customer numbers
    """
    grouped = df.groupby(customer_column)
    
    def fill_row(row, group_mean):
        for col in columns:
            if pd.isnull(row[col]):
                row[col] - group_mean[col]
        return row
    
    df_filled = df.copy()
    for customer, group in grouped:
        group_mean = group.mean(numeric_only=True)
        df.filled.loc[group.index] = group.apply(lambda row: fill_row(row, group_mean), axis=1)
    return df_filled

   
