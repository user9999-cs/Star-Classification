import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_read_data(filepath):
    read_data = pd.read_csv(filepath)
    return read_data


data = load_read_data("6 class csv.csv")

# inspect the dataset
print("First 5 rows:")
print(data.head())
print(f"\nDataset shape: {data.shape}")
print("\nData types:")
print(data.dtypes)

# summary stats
print("\nSummary statistics: ")
print(data.describe())

# check for missing values
print("\nMissing values for each column:")
print(data.isnull().sum())

# data visualization
plt.figure(figsize=(6, 4))
sns.countplot(data=data, x="Star type")
plt.title("Star Type Counts")
plt.show()
