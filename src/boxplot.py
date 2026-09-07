from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Boxplot of Median Income
plt.figure(figsize=(6, 4))
plt.boxplot(df['MedInc'])
plt.title('Boxplot of Median Income')
plt.ylabel('MedInc')
plt.savefig('figs/boxplot.png')
plt.show()
