# Create a DataFrame of the features
cv_tri_df = pd.DataFrame(cv_trigram.toarray(),
                         columns=cv_trigram_vec.get_feature_names()).add_prefix('Counts_')

# Print the top 5 words in the sorted output
print(cv_tri_df.sum().sort_values(ascending=False).head())