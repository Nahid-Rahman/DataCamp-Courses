# Problem 01

# Create a histogram
so_numeric_df.hist()
plt.show()



# Problem 02

# Create a boxplot of two columns
so_numeric_df[['Age', 'Years Experience']].boxplot()
plt.show()



# Problem 03

# Create a boxplot of ConvertedSalary
so_numeric_df[['ConvertedSalary']].boxplot()
plt.show()