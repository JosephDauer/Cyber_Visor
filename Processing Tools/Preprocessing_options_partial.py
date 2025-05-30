import pandas as pd
from sklearn.preprocessing import OneHotEncoder

#Sample
data = pd.dataframe({'parameter': ['A', 'B', 'C', 'D', 'E']})

#one-hot encoding
one_hot_encoder_data = pd.get_dummies(data['parameter'])
print('Encoder data (pandas):\n' one_hot_encoder_data)

#skilearn depolyment
encoder = OneHotEncoder(sparse=False)
encoded_data = encoder.fit_transform(data[['parameter']])
print('Encoder data (sklearn):\n', encoded_data)

