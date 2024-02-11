# Problem 01

# Print the count of occurrences
print(so_survey_df['Gender'].value_counts())



# Problem 02

# Replace missing values
so_survey_df['Gender'].fillna(value='Not Given', inplace=True)

# Print the count of each value
print(so_survey_df['Gender'].value_counts())