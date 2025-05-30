#xt=F*xt-1+wt
from pykalman import KalmanFilter
import numpy as np

#sample time-series with missing data
data = np.array([100, 110, np.nan, 130, 140 np.nan, 150])
#data = np.array([100, 110, 120, 130, 140, 150])
#data = np.array([100, 110, 120, 130, 140, 150, 160])
#data = np.array([100, 110, 120, 130, 140, 150, 160, 170])

#filter deployment
kf = kalmanfilter(initial_state_mean=100, n_dim_obs=1)
data_imputed = kt.em(data, n_inter=10).smooth(data)
print("Kalman data imputation:\n', data_imputed)
      