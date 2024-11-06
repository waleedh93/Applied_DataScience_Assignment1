# importing libararies in Python
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
# importing csv file in Python 
df = pd.read_csv("HCI_2020.csv", index_col = 'Year')
print(df)
# replacing all the alphabets and symbols in the Country column with a space
df = df.replace({'Country':'[A-Za-z,. - (())]'},'',regex=True)
print(df)
# droping rows which have NaN value
new_df = df.dropna( )
print(new_df)
# entering the value of HCI from a user, HCI should be in range between 0-1
while True:
    x = float(input('enter the value of x '))
    if x>=0 and x<=1:
        new_df = df[df['HCI'] <= x]
        break
    else:
        print('Enter the value between 0 and 1')
print(new_df)
mean = print(new_df.loc[:,'HCI'].mean())
median = (new_df.loc[:,'HCI'].median())
describe = print(new_df.loc[:,'HCI'].describe())
standard_deviation = print(new_df.loc[:,'HCI'].std())
print(new_df.loc[:,'HCI'].cov(new_df['HCI']))
new_dfff =  print(new_df.corr(method ='pearson',numeric_only = True))
#Create the scatter plot
plt.figure(figsize=(12,6))
sns.scatterplot(x = new_df['Code'], y = new_df['HCI'])
for i, Code in enumerate(new_df['Code']):
    # Format the annotation text to display both code and HCI value 
    plt.annotate(new_df['HCI'].iloc[i], (Code, new_df['HCI'].iloc[i]), textcoords="offset points", xytext=(0, 5))
plt.xticks(rotation=90)
plt.title("HCI Scatter Plot by Country Code")
plt.xlabel("Country Code")
plt.ylabel("HCI Value")
plt.tight_layout()
plt.show()


# creating a bar plot
plt.figure(figsize=(20,6))
plt.bar(new_df['Code'], new_df['HCI'], color='skyblue', label='HCI Value')
for i, Code in enumerate(new_df['Code']):
    # Format the annotation text to display both code and HCI value
    plt.annotate(new_df['HCI'].iloc[i], (Code, new_df['HCI'].iloc[i]), textcoords="offset points", xytext=(0, 5))
plt.title("HCI Values by Country Code")
plt.xlabel("Country Code")
plt.ylabel("HCI Value")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# plotting the box and violin plot
#sns.boxplot(new_df['HCI'])
sns.boxplot(y=new_df['HCI'], color='lightgreen')
plt.title("Box Plot of HCI Values")
plt.ylabel("HCI Value")
plt.tight_layout()
plt.show()
plt.violinplot(new_df['HCI'])
plt.title("Violin Plot of HCI Values")
plt.ylabel("HCI Value")
plt.tight_layout()  # Adjust layout for rotated labels and landscape orientation
plt.show()