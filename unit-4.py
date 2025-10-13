program-1
--------

Syntax: 
# import pandas as pd 
# pd.Series(data) 
# series.tolist() 
 
Program: 
import pandas as pd 
data = [10, 20, 30, 40, 50] 
Series = pd.Series(data) 
print("one dimensional array-like object(Pandas Series):") 
print(Series) 

------------------------------------------------------------------------------------------

program-2
--------

Program:  
import pandas as pd 
data = pd.Series([10, 20, 30, 40, 50]) 
print("Pandas Series:") 
print(data) 
py_list=data.tolist() 
print(py_list) 
print("\nType of the converted object:", type(py_list))

-----------------------------------------------------------------------------------------

program-3
--------

Syntax: 
# import pandas as pd 
# df = pd.DataFrame(data, index=labels) 
# df.loc[row_index, 'column'] = new_value 
# df['new_column'] = values 
 
Program: 
Write a Pandas program to create and display a DataFrame from a specified dictionary data 
which has the index labels. 
import pandas as pd 
import numpy as np 
# Given dictionary data 
exam_data = { 
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
                         'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 
                'yes', 'yes', 'no', 'no', 'yes'] 
# Custom labels 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
# Create DataFrame with index labels 
df = pd.DataFrame(exam_data, index=labels) 
# Display DataFrame 
print("Pandas DataFrame with index labels:") 
print(df) 

------------------------------------------------------------------------------------------------------

program-4
---------

import pandas as pd 
import numpy as np 
# Given dictionary data 
exam_data = { 
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 
                'yes', 'yes', 'no', 'no', 'yes'] 
} 
# Custom labels 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
# Create DataFrame with index labels 
df = pd.DataFrame(exam_data, index=labels) 
# Display DataFrame 
print("Original dataframe") 
print(df) 
df.loc[df['name']== 'James','name']='Suresh' 
print("\nDataframe after changing 'James' to 'suresh:") 
print(df)

----------------------------------------------------------------------------------------------

program-4
--------

Program:  
Write a Pandas program to insert a new column in existing DataFrame. 
import pandas as pd 
import numpy as np 
# Original Data 
exam_data = { 
    'name': ['Anastasia', 'Dima', 'Katherine', 'Suresh', 'Emily', 
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 
                'yes', 'yes', 'no', 'no', 'yes'] 
} 
labels = ['a','b','c','d','e','f','g','h','i','j'] 
df = pd.DataFrame(exam_data, index=labels) 
#  Insert a new column 
df['age'] = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30] 
print(df)

-----------------------------------------------------------------------------------------

program-5
---------

import pandas as pd 
import numpy as np 
# Original Data 
exam_data = { 
    'name': ['Anastasia', 'Dima', 'Katherine', 'Suresh', 'Emily', 
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 
                'yes', 'yes', 'no', 'no', 'yes'] 
} 
labels = ['a','b','c','d','e','f','g','h','i','j'] 
df = pd.DataFrame(exam_data, index=labels) 
col_list =df.columns.tolist() 
print("List of column headers:") 
print(col_list) 

----------------------------------------------------------------------------------------




