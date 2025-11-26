import numpy as np
import pandas as pd

class AgeGrouper:
    def __init__(self):
        self.bins = [0, 19, 39, 59, 1000]
        self.labels = ['Youth', 'Young_Adult', 'Middle_Aged', 'Senior']

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df['Age_Group'] = pd.cut(df['Age'], bins=self.bins, labels=self.labels)
        
        return df


# ages = [5, 22, 45, 67, 15, 38, 52]
# grouper = AgeGrouper(ages)    
# df_result = grouper.assign_group()  
# grouper.show()                 


'''

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


'''