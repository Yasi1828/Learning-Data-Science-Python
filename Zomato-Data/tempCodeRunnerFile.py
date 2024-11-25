import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def RatetoFloat(v):
    v=str(v).split('/')
    v=v[0]
    return float(v)
Data = pd.read_csv("F:/Learning-Data-Science-Python/Zomato-Data/Zomato data .csv")
print(Data.head())

Data['rate'] = Data['rate'].apply(RatetoFloat)
print(Data.head())
Data.info()


Data['AveRate'] = Data['rate'] * Data['votes']
GroupedData = Data.groupby('listed_in(type)')['AveRate'].sum().reset_index()
GroupedData.columns = ['listed_in(type)', 'Average rate']
print(GroupedData)
MaxAveRate = GroupedData['Average rate'].max()
BestRes = GroupedData.loc[GroupedData['Average rate'] == MaxAveRate,'listed_in(type)']
print(f"The best type of restaurant according to the votes: {BestRes}")

plt.figure(figsize=(8,8))
sns.barplot(x='listed_in(type)', y='Average rate',data=GroupedData)
plt.xlabel("Type of restaurant")
plt.ylabel("Total votes")

GroupedDataonlineOrder = Data.groupby('listed_in(type)')
plt.figure(figsize=(8,8))
sns.countplot(data=Data, x='listed_in(type)', hue='online_order' )
plt.xlabel('Restaurant Type')
plt.ylabel('Count')
plt.xticks(rotation=90)


plt.show()

