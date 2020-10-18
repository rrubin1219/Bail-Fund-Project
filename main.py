#Rachel Rubin
#10/18/20
#Owlhacks : Bail Fund Project
#Program graphs a comparison of offenders' age and how much their bail is to see if they is a significant correltion between the two
	#Uses panda and matplotlib as starters, and seaborn to see relationship graphs

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


df = pd.read_csv('all.csv') #read csv
df.drop(columns = ['docket_no','bail_set_by','bail_type', 'prelim_hearing_time'], inplace= True) #removes specified columns

df['arrest_dt'] = pd.to_datetime(df['arrest_dt']) #rearranges as datetime standard
df['dob'] = pd.to_datetime(df['dob']) #rearranges as datetime standard

df['Age'] = (df['arrest_dt'] - df['dob']).dt.days #gets ages in days
df['Age'] = abs(df['Age'] / 365) #get ages in years

'''
#Using Panda
df['Age'].plot.hist(title = 'Age', color = 'red', edgecolor = 'blue' ,linewidth = 1.5,bins = 40)
plt.show()

#using Matplotlib
plt.bar(x = df['Age'].values, height = df['bail_amount'].values, width = 3, edgecolor = 'red', linewidth = .4)
plt.xticks(rotation = 'vertical')
plt.title('Bail Amount vs. Age')
plt.ylabel('Bail Amount');
plt.show()
'''

#Still trying to figure out how to increment Y-axis by a higher amount than 1

sns.pairplot(df, kind = 'reg');
plt.show()
