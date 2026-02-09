import pandas as pd
import numpy as np
dataset=pd.read_csv(r"C:\Users\Harshita Joshi\OneDrive\Desktop\HDFC loan dataset\Loan payments data.csv")
print(dataset.head(10))
print(dataset.tail(10))
print(dataset.isnull())
print(dataset.shape[0])
print(dataset.shape[1])
print(dataset.notnull())
print(dataset.isnull().sum())
print(dataset.isnull().sum().sum())
print(dataset.isnull().sum()/dataset.shape[0]*100)
print(dataset.isnull().sum().sum()/(dataset.shape[0]*dataset.shape[1])*100)
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(dataset.isnull())
plt.show()

