# Specify array of percentiles: percentiles
percentiles = np.array([2.5,25,50,75,97.5])


# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length,percentiles)


# Print the result
print(ptiles_vers)

# Create box plot with Seaborn's default settings
sns.boxplot(x='species',y='petal length (cm)',data = df)


# Label the axes
plt.xlabel('hehe')
plt.ylabel('haha')



# Show the plot
plt.show()


