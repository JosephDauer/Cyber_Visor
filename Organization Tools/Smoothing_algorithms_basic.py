import pandas as pd
from sklearn.impute import SimpleImputer

#sample data with missing values
data = pd.DataFrame({
    'Age': [None, 18, 26, 36, 46, 56, 66],
    'Gender:': [None, 'Male', 'Female', 'Felosapian', 'Other', 'Various', 'Unknown'], 
    'Marital Status:': [None, 'Single', 'Married', 'Divorced', 'Widowed'],
    'Education Level:': [None, 'GED', 'High School', 'Associate Degree', 'Bachelor Degree', 'Master Degree', 'Doctorate'],
})

#input smoothing algorithm (a) continuous data 
mean_inputer = SimpleImputer(strategy='mean')
data['Age'] = mean_inputer.fit_transform(data[['Age']])

#input smoothing algorithm (b) categorical data
mode_inputer = SimpleImputer(strategy='most_frequent')
data['Gender:'] = mode_inputer.fit_transform(data[['Gender']]
                                             
print('Post data Smoothing:\n', data)
