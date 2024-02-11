# Problem 01

# Print the number of rows and columns
print(so_survey_df.shape)



# Problem 02

# Create a new DataFrame dropping all incomplete rows
no_missing_values_rows = so_survey_df.dropna()

# Print the shape of the new DataFrame
print(no_missing_values_rows.shape)



# Problem 03

# Create a new DataFrame dropping all columns with incomplete rows
no_missing_values_cols = so_survey_df.dropna(how='any',  axis=1)

# Print the shape of the new DataFrame
print(no_missing_values_cols.shape)



# Problem 04

# Drop all rows where Gender is missing
no_gender = so_survey_df.dropna(subset=['Gender'])

# Print the shape of the new DataFrame
print(no_gender.shape)