#Problem 01

# Inspect the unique values of the cuisine_type column
print(restaurants['cuisine_type'].unique())



#Problem 02

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'],limit=len(restaurants))

# Inspect the first 5 matches
print(matches[0:5])



#Problem 03
# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))
    # Iterate through the list of matches to 'italian'
for match in matches:
    # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
        # Select all rows where the cuisine_type is spelled this way and set them to the correct cuisine
        restaurants.loc[restaurants['cuisine_type'] == match[0], 'cuisine_type'] = 'italian'



#Problem 04

# Iterate through categories
for cuisine in categories:  
    # Create a list of matches, comparing cuisine with the cuisine_type column
    matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

    # Iterate through the list of matches
    for match in matches:
        # Check whether the similarity score is greater than or equal to 80
        if match[1] >= 80:
            # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
            restaurants.loc[restaurants['cuisine_type'] == match[0], 'cuisine_type'] = cuisine

# Inspect the final result
print(restaurants['cuisine_type'].unique())