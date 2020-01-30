import pandas as pd
import numpy as np

data = pd.read_csv('adult.data.csv')

# EX20_1
print('How many men and women are represented in dataset?')
print(data.sex.value_counts(normalize=True),'\n')

# EX20_2
print('What is the average age (age feature) of women?')
print('Male:',data[data.sex == 'Male']['age'].mean())
print('Female:',data[data.sex == 'Female']['age'].mean(),'\n')

# EX20_3
print('What is the percentage of German citizens (native-country feature)?')
print(data['native-country'].value_counts(normalize=True),'\n')

# EX20_4
print('What are the mean and standard deviation of age for those who earn more than 50K per year (salary feature) and those who earn less than 50K per year?')
print('>50K:\n',data[data.salary == '>50K']['age'].agg([np.mean, np.std]))
print('<=50K:\n',data[data.salary == '<=50K']['age'].agg([np.mean, np.std]),'\n')

# EX20_5
print('Is it true that people who earn more than 50K have at least high school education? (education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters or Doctorate feature)')
print(data[data.salary == '>50K']['education'].value_counts(normalize=True),'\n')