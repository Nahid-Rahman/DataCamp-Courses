# Problem 01

# Import packages
import matplotlib.pyplot as plt
import seaborn as sns

# Plot pairwise relationships
sns.pairplot(so_numeric_df)

# Show plot
plt.show()



# Problem 02

# Print summary statistics
print(so_numeric_df.describe())