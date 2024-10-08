import pandas as pd

file_path = 'dataProject4.xlsx'

def lower_case(df: pd.DataFrame) -> pd.DataFrame:
    """
    Lower case all the text for consistency
    """
    return df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove empty rows if any
    """
    return df.dropna(how="all")

def remove_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove empty columns if any
    """
    return df.dropna(axis=1, how="all")



def clean_data(file_path: str) -> pd.DataFrame:
    """
    Run all data cleaning functions on the provided Excel file.
    
    :param file_path: Path to the input Excel file.
    :return: Cleaned DataFrame.
    """
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Print columns for debugging
    print("Initial Columns:", df.columns.tolist())

    # Apply cleaning functions
    df = lower_case(df)
    df = remove_empty_rows(df)
    df = remove_empty_columns(df)


    return df

# Clean the data, using the first column (index 0) as the customer number column
cleaned_df = clean_data(file_path)

# Save the cleaned DataFrame to a new Excel file
output_file_path = 'cleaned_dataProject4.xlsx'
cleaned_df.to_excel(output_file_path, index=False)

print(f"Cleaned data has been saved to {output_file_path}.")
