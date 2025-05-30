import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#sample data incomplete
data =pd.DataFrame([
    'Age:': [None,18,26,36,46,56,66],
    'Income Extimate:': [None, 25000, 50000, 75000, 100000, 125000, 126000],
    'Gender:': [None, 'Male', 'Female', 'Felosapian', 'Other', 'Various', 'Unknown'], 
    'Marital Status:': [None, 'Single', 'Married', 'Divorced', 'Widowed'],
    'Education Level:': [None, 'High School', 'Associate Degree', 'Bachelor Degree', 'Master Degree', 'Doctorate'],
])

#Visualizing data with heatmap
plt.figure(figsize=(10, 6)) #adjust for better visibility
sns.heatmap(data.insull().sum().mean(), cbar=True, cmap='viridis')
plt.title('Missing Data Visualizer  - Heatmap')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()

