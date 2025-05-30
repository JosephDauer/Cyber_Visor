#Min-max program prarameters
from sklearn.preprocessing import MinMaxScaler
import numpy as np

#data input
data = np.array([[24, 50000], [30, 70000], [45, 100000]])

#min-maxing
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

print("Scaled data:\n ", scaled_data)
#print("Inverse transformed data:\n ", scaler.inverse_transform(scaled_data))