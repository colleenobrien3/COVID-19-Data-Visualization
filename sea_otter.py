import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline

df = pd.read_csv('full_data.csv', encoding='unicode_escape', index_col=0)

# print(df.head())

dc = pd.read_json('data.txt', encoding='unicode_escape')

print(dc.head())
