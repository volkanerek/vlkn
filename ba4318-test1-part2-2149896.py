#Volkan Erek / 2149896
import pandas as pd


#Def to get csv files into dataframes

def read_files():
    dfbr = pd.read_csv('tbrazil.csv', usecols = ["temp", "mdct", "tmax"])
    dfmad = pd.read_csv('tmadrid.csv', usecols = ["Mean TemperatureC", "CET"])
    return dfbr, dfmad

dfbr, dfmad = read_files()

#In Brazil dataset if the tmax values have zero, there is not measurement on that hour. So simply by removing them we would have
#removed the not measured hours, and by droping the tmax column, we would have a final date-temp_madrid-temp_brazil temperatures.
dfbr = dfbr.loc[~((dfbr['tmax'] != 0))]
dfbr.drop("tmax", axis=1, inplace=True)

#Lines to have same format of date at two different dataframe
dfbr["mdct"] = pd.to_datetime(dfbr["mdct"]).dt.normalize()
dfmad["CET"] = pd.to_datetime(dfmad["CET"])


#Def to get mean of Brazil data and merge three columns into a final dataframe

def avrg_temp():
    #Averaging temperatures for each date
    dfbr_1 = dfbr.groupby("mdct").mean()
    dfmad_1 = dfmad.groupby("CET").mean()

    #Joining tables for same existing dates
    df_final = dfmad_1.join(dfbr_1,how="inner")

    #Resetting index to include date as a column
    df_final = df_final.reset_index()

    #Renaming columns
    df_final = df_final.rename(columns={"index":"date", "Mean TemperatureC":"temp_madrid", "temp":"temp_brazil"})
    
    return df_final

df_final = avrg_temp()


#Calculating correlation between two columns in a dataframe

correlation = df_final['temp_brazil'].corr(df_final['temp_madrid'])
print("Correlation between temperature of Brazil and temperature of Madrid is", correlation)

#The correlation between two regions temperatures is 0.021 which means there is almost no linear relationship between them,
#There is very weak positive correlation between two region's temperatures.