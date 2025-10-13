program-1
--------

Syntax:  
# import matplotlib.pyplot as plt 
# import numpy as np 
# x = np.linspace(a, b, n) 
# y1, y2, y3 = f1(x), f2(x), f3(x) 
# plt.figure(figsize=(w, h)) 
# plt.subplot(r, c, 1); plt.plot(x, y1); 
# plt.title('Title1') 
# plt.subplot(r, c, 2); plt.plot(x, y2); 
# plt.title('Title2') 
# plt.subplot(r, c, 3); plt.plot(x, y3); 
# plt.title('Title3') 
# plt.tight_layout() 
# plt.show() 

Program:  
-------
import matplotlib.pyplot as plt 
import numpy as np
# Sample data 
x = np.linspace(0, 2 * np.pi, 100) 
y = np.sin(x) 
y2 = np.cos(x) 
y3 = np.sin(x) * np.cos(x) 
# Create a figure with a series of plots 
plt.figure(figsize=(12, 4)) 
plt.subplot(1, 3, 1) 
plt.plot(x, y, color='blue') 
plt.title('Sine Wave') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.subplot(1, 3, 2) 
plt.plot(x, y2, color='green') 
plt.title('Cosine Wave') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.subplot(1, 3, 3) 
plt.plot(x, y3, color='red') 
plt.title('Product of Sine and Cosine') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.tight_layout() # Adjusts subplot params for a tight layout 
plt.show() 

----------------------------------------------------------------------------------------
program-2
---------

Syntax : 
# import 
# matplotlib.pyplot as 
# plt 
# import numpy as np 
# import pandas as pd 
# # Data 
# df = 
# pd.DataFrame({'Col
#  1':[v1,v2,v3], 
# 'Col2':[v4,v5,v6]}) 
# x1, y1 = 
# np.random.rand(n), 
# np.random.rand(n) 
# x2, y2 = 
# np.arange(a,b),
# np.random.randint(l
#  ow,high,size=b-a) 
# # Subplots 
# fig, ax = 
# plt.subplots(2, 2, 
# figsize=(w, h)) 
# ax[0,0].scatter(x1, 
# y1); 
# ax[0,0].set_title('Sca
#  tter') 
# ax[0,1].plot(x2, y2, 
# marker='o'); 
# ax[0,1].set_title('Lin
#  e') 
# ax[1,0].bar(df['Col1'
#  ], df['Col2']); 
# ax[1,0].set_title('Bar
#  ') 
# ax[1,1].set_visible(F
#  alse) 
# plt.tight_layout() 
# plt.show()

Program : 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
# Sample data 
data = {'Category': ['A', 'B', 'C', 'D'], 
'Value1': [10, 25, 15, 30], 
'Value2': [15, 20, 25, 10]} 
df = pd.DataFrame(data) 
x_scatter = np.random.rand(50) 
y_scatter = np.random.rand(50) 
x_line = np.arange(10) 
y_line = np.random.randint(1, 10, size=10) 
fig, axes = plt.subplots(2, 2, figsize=(10, 8)) 
# Scatter Plot 
axes[0, 0].scatter(x_scatter, y_scatter) 
axes[0, 0].set_title('Scatter Plot') 
axes[0, 0].set_xlabel('X-axis') 
axes[0, 0].set_ylabel('Y-axis') 
# Line Plot 
axes[0, 1].plot(x_line, y_line, marker='o') 
axes[0, 1].set_title('Line Plot') 
axes[0, 1].set_xlabel('X-axis') 
axes[0, 1].set_ylabel('Y-axis') 
# Bar Chart 
axes[1, 0].bar(df['Category'], df['Value1']) 
axes[1, 0].set_title('Bar Chart') 
axes[1, 0].set_xlabel('Category') 
axes[1, 0].set_ylabel('Value1') 
# This subplot is intentionally left empty to match the assignment's implied 2x2 grid 
axes[1, 1].set_visible(False)  
plt.tight_layout() 
plt.show() 

----------------------------------------------------------------------------------------

program-3
--------

Syntax : 
import matplotlib.pyplot as 
plt 
import numpy as np 
import pandas as pd 
df = 
pd.DataFrame({'C1':[v1,v2,
 v3], 'C2':[v4,v5,v6]}) 
x1, y1 = np.random.rand(n), 
np.random.rand(n) 
x2, y2 = np.arange(a,b), 
np.random.randint(low,high,
 size=b-a)
fig, ax = plt.subplots(2, 2, 
figsize=(w, h)) 
ax[0,0].scatter(x1, y1); 
ax[0,0].set_title('Scatter') 
ax[0,1].plot(x2, y2, 
marker='o'); 
ax[0,1].set_title('Line') 
ax[1,0].bar(df['C1'], 
df['C2']); 
ax[1,0].set_title('Bar') 
ax[1,1].set_visible(False) 


Program: 
import matplotlib.pyplot as 
plt 
import pandas as pd 
import numpy as np 
# Sample time-series data 
dates = 
pd.to_datetime(pd.date_range(start='2024-01-01', 
periods=100, freq='D')) 
sales_data = 
np.random.randint(100, 500, 
size=100) + 
np.sin(np.arange(100) * 0.2) 
* 50 
df = pd.DataFrame({'Date': 
dates, 'Sales': sales_data}) 
df = df.set_index('Date') 
plt.figure(figsize=(12, 6)) 
plt.plot(df.index, df['Sales']) 
# Customize axis labels and 
date formats 
plt.xlabel('Date') 
plt.ylabel('Sales') 
plt.title('Daily Sales Over 
Time') 
# Use pandas' built-in 
plotting for automatic date 
formatting
# This is a good practice for 
clean time-series plots 
df.plot(y='Sales', 
figsize=(12, 6), title='Daily Sales Over Time')  
plt.show() 

-------------------------------------------------------------------------------------

program-4
---------

Syntax :  
# import matplotlib.pyplot as plt 
# import numpy as np 
# from mpl_toolkits.mplot3d import Axes3D 
# x, y, z = np.random.rand(50), np.random.rand(50), np.random.rand(50) 
# fig = plt.figure(figsize=(w, h)) 
# ax = fig.add_subplot(111, projection='3d') 
# ax.scatter(x, y, z) 
# ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z') 
# ax.set_title('3D Scatter') 
# plt.show() 

Program :
---------

import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D 
# Sample 3D data 
np.random.seed(42) 
x = np.random.rand(50) 
y = np.random.rand(50) 
z = np.random.rand(50) 
# Create a 3D figure 
fig = plt.figure(figsize=(8, 6)) 
ax = fig.add_subplot(111, projection='3d') 
# Plot the 3D data 
ax.scatter(x, y, z) 
# Set labels for the axes 
ax.set_xlabel('X-axis') 
ax.set_ylabel('Y-axis') 
ax.set_zlabel('Z-axis') 
ax.set_title('3D Scatter Plot') 
plt.show() 

-----------------------------------------------------------------

