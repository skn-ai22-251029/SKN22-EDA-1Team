import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/train.csv')
df.head()

class AgeGrouper:
    def __init__(self, ages):
      
        self.df = pd.DataFrame({'Age': ages})
    
    def assign_group(self):
        self.df['Age_Group'] = self.df['Age'].apply(
            lambda x: 'Youth' if x <= 19 else
                      'Young_Adult' if x <= 39 else
                      'Middle_aged' if x <= 59 else
                      'Senior'
        )
        return self.df
    
    def show(self):
       
        print(self.df)


ages = [5, 22, 45, 67, 15, 38, 52]
grouper = AgeGrouper(ages)    
df_result = grouper.assign_group()  
grouper.show()                 