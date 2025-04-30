import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Power in statistics is a chance for a test to correctly detect significant 
# difference between two groups when the difference truly exists. This code 
# generates 2 normal distributions with slitghly different means and tests them
# with t-test, mann-whitney u test and kolmogorov-smirnov test, to see whether
# the distributions are same or no. Simulation runs for 1000 runs for each test
# with different sample sizes.

# Final output - power of each statistical test for each sample size.


# a function to simulate datasets and test them against each other
def simulate_tests(dist1, dist2, n, num_simulations=1000, alpha=0.05):
    ttest_significant = 0
    mannwhitney_significant = 0
    ks_significant = 0

    for _ in range(num_simulations):
        sample1 = dist1(n)
        sample2 = dist2(n)

        ### t-test
        _, p_ttest = stats.ttest_ind(sample1, sample2)
        if p_ttest < alpha:
            ttest_significant += 1

        ### mann-whitney u test
        _, p_mwu = stats.mannwhitneyu(sample1, sample2)
        if p_mwu < alpha:
            mannwhitney_significant += 1

        ### kolmogorov-smirnov test
        _, p_ks = stats.ks_2samp(sample1, sample2)
        if p_ks < alpha:
            ks_significant += 1

    power_results = {
        'T-test': ttest_significant / num_simulations,
        'Mann-Whitney': mannwhitney_significant / num_simulations,
        'Kolmogorov-Smirnov': ks_significant / num_simulations
    }

    return power_results

# 2 normal distributions, with a little different mean
dist1 = lambda n: np.random.normal(loc=0, scale=1, size=n)
dist2 = lambda n: np.random.normal(loc=0.5, scale=1, size=n)

# setting up the parameters for the simulation
sample_sizes = [20, 50, 100]

power_ttest, power_mwu, power_ks = [], [], []

# running the simulation for different sample size
for n in sample_sizes:
    results = simulate_tests(dist1, dist2, n)
    power_ttest.append(results['T-test'])
    power_mwu.append(results['Mann-Whitney'])
    power_ks.append(results['Kolmogorov-Smirnov'])


# visualizing power levels for different tests for different sample sizes
plt.figure(figsize=(8, 5))
plt.plot(sample_sizes, power_ttest, marker='o', label='T-test')
plt.plot(sample_sizes, power_mwu, marker='s', label='Mann-Whitney U')
plt.plot(sample_sizes, power_ks, marker='^', label='Kolmogorov-Smirnov')
plt.title('Statistical Test Power Comparison')
plt.xlabel('Sample Size')
plt.ylabel('Power (Proportion Significant)')
plt.ylim(0, 1.05)
plt.xticks(sample_sizes)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("power_plot.png")

print("plot has been created")
