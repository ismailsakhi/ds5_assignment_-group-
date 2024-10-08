import pandas as pd

df = pd.read_excel('hotelBookings.xlsx')

def uniques(df: pd.DataFrame, column: str):
    """
    check for the unique values for most columns where no uniques values are expected

    :param df: an excel sheet data frame
    :param column: the column that you want to check
    """
    unique_answers = df[column].unique()

    for answers in unique_answers:
        print(answers)
#using this I found that one arrival year unique value is 2099, which does not seem correct

def simple_replacement(df: pd.DataFrame, column: str, wrong: int, correct: int):
    """"
    replacing values that are simple to fix and don't require mean, mode or median

    """
    df[column] = df[column].replace(wrong, correct)

def replace_empty_months_based_on_week(df: pd.DataFrame, week_column: str, month_column: str) -> pd.DataFrame:
    """
    Replace empty values in the arrival_date_month column based on the week number.

    :param df: The input DataFrame.
    :param week_column: The column name containing the week numbers.
    :param month_column: The column name to replace empty values with corresponding months.
    :return: A DataFrame with empty month values replaced according to the week number.
    """

    # Define a mapping of week numbers to months
    week_to_month = {
        27: 'July', 28: 'July',
        29: 'August', 30: 'August', 31: 'August'
    }

    # Replace empty values in the month column based on the week number
    for index, row in df.iterrows():
        if pd.isnull(row[month_column]):  # Check if the month cell is empty
            week_number = row[week_column]
            if week_number in week_to_month:  # If the week number is valid
                df.at[index, month_column] = week_to_month[week_number]  # Replace with the corresponding month

    return df

def replace_with_mean(df:pd.DataFrame, column: str, wrong, int ):
    mean_value = df[df[column] != wrong][column].mean()
    round_mean = round(mean_value)
    df[column] = df[column].replace(wrong, round_mean)
    return df



simple_replacement(df, 'arrival_date_year', 2099, 2015)

replace_empty_months_based_on_week(df, 'arrival_date_week_number', 'arrival_date_month')

simple_replacement(df, 'stays_in_week_nights', 4.3, 4.0)

replace_with_mean(df, 'adults', 3500)