#data compression and filtration tool depolyment
import pandas as pd

#data loading
data = pd.read_csv('transactions.csv', parse_dates=['date'], index_col='date')

#filtering data
filtered_data = data[data['amount'] > 256]
print(filtered_data)
