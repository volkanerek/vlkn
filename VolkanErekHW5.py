# Volkan Erek / 2149896

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import Holt 
from statsmodels.tsa.stattools import adfuller
import warnings

# Code in order to make warnings suppressed.
warnings.filterwarnings("ignore")

# To load data from necessary columns of CSV files.
df_bra = pd.read_csv("tbrazil.csv", usecols = ["temp", "date"])
df_mad = pd.read_csv("tmadrid.csv", usecols = ["Mean TemperatureC", "CET"])

# We need to make column name of date times of datas to make them available for merge function.
df_bra = df_bra.rename(columns = {"temp" : "tempbra"})
df_mad = df_mad.rename(columns = {"Mean TemperatureC" : "tempmad"})
df_mad = df_mad.rename(columns = {"CET" : "date"})


# To have mean of every day of brazil data.
tempbramean = df_bra.groupby("date").mean()


# To have final dataframe that consisted from necessary data.
df_fin = pd.merge(df_mad,tempbramean, how = "inner", on = "date")


# The function to decompose data into level, trend, seasonality and noise.
def decomp(frame,name,f,mod='Additive'):
    series = frame[name]
    array = np.asarray(series, dtype=float)
    result = sm.tsa.seasonal_decompose(array,freq=f,model=mod,two_sided=False)
    result.plot()
    plt.show() 
    return result

# The function to see whether data is stationary or not.
def test_stationarity(timeseries):
    rolmean = pd.Series(timeseries).rolling(window=12).mean()
    rolstd = pd.Series(timeseries).rolling(window=12).std()
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    print("Results of Dickey-Fuller Test:")
    array = np.asarray(timeseries, dtype='float')
    np.nan_to_num(array,copy=False)
    dftest = adfuller(array, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)
    
seriesname1 = 'tempbra'
seriesname2 = 'tempmad'

series1 = df_fin[seriesname1]
series2 = df_fin[seriesname2]
test_stationarity(series1)

result1 = decomp(df_fin,seriesname1, f=52)
result2 = decomp(df_fin,seriesname2, f=52)
test_stationarity(result1.trend)

#Because p-values of both temperature data are below 0.05, we can say that these two temperature data
#have no unit root and they are stationary.
#Also there is an upward trend in the temperature datas, and their peak points are getting higher comparing to past data of temperatures.
