
import pandas as pd

# Load the dataset
data = pd.read_csv('fire_data.csv', delimiter='\t')

# Display 
print(data)
import matplotlib.pyplot as plt

# Extract the required columns
total_incidents = data['TOTAL_INCIDENTS']
financial_year = data['FINANCIAL_YEAR']

# Create a line plot
plt.plot(financial_year, total_incidents)
plt.xlabel('Financial Year')
plt.ylabel('Total Incidents')
plt.title('Total Incidents vs Financial Year')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Display the plot
plt.show()

import matplotlib.pyplot as plt

# Extract the required columns
total_incidents = data['TOTAL_INCIDENTS']
frs_name = data['FRS_NAME']

# Plot the graph
plt.figure(figsize=(10, 6))
plt.bar(frs_name, total_incidents)
plt.xlabel('FRS Name')
plt.ylabel('Total Incidents')
plt.title('Total Incidents by FRS Name')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


import pandas as pd
import numpy as np
from scipy.stats import poisson, gamma

# Read the dataset into a Pandas DataFrame
data = pd.read_csv('fire_data.csv')

# Filter the dataset for the relevant columns
filtered_data = data[['FINANCIAL_YEAR', 'INCIDENT_TYPE', 'TOTAL_INCIDENTS']]

# Filter the dataset for the UK region
uk_data = filtered_data[filtered_data['FINANCIAL_YEAR'].str.contains('2022/23')]

# Estimate the distribution of N (number of claims)
claim_counts = uk_data.groupby('INCIDENT_TYPE')['TOTAL_INCIDENTS'].sum()

# Calculate the average number of claims per incident type
claim_means = claim_counts.mean()

# Fit a Poisson distribution to the claim counts
claim_distribution = poisson(claim_means)

# Estimate the distribution of X_i (size of claims)
claim_sizes = uk_data['TOTAL_INCIDENTS']

# Fit a gamma distribution to the claim sizes
shape, loc, scale = gamma.fit(claim_sizes)

# Create a function to calculate the probability distribution of S
def estimate_sum_distribution(n_distribution, x_distribution, num_samples=1000):
    n_samples = n_distribution.rvs(num_samples)
    x_samples = x_distribution.rvs(num_samples)
    s_samples = np.multiply(n_samples, x_samples)
    return s_samples

# Calculate the probability distribution of S
s_distribution = estimate_sum_distribution(claim_distribution, gamma(shape, loc, scale))

# Print the mean and standard deviation of S
print("Mean of S:", np.mean(s_distribution))
print("Probability distribution of S:", np.std(s_distribution))
