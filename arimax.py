# -*- coding: utf-8 -*-
"""Arimax.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hJr_pX_QfNA0gREJPGWR1yi7kkI2SAxE
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np #imported numpy and Assigned as np
import pandas as pd #imported pandas and Assigned as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt #Used to plot the Graph by plt
# %matplotlib inline

#Used to Mount the Drive for Storage(kpsr6442GMAIL.COM(ML DATA))
from google.colab import drive
drive.mount('/content/drive')

df=pd.read_csv('/content/drive/My Drive/Placement Fee/train_sample3_1(arima1.1).csv')
#DATA SET OF CSV FORMAT
#READING THE CSV DATA SET

df.tail()
#THE END DATA OF DATA SET IS DISPLAYED

#df.drop(105,axis=0,inplace=True)
#Above command to remove a row from the data set
#105 indicates the index number or row number in the DATA SET

df.tail()

#df.drop(106,axis=0,inplace=True)

df.columns=['Month','Waiting List Conformed' ]
#CLASSIFING THE X AND Y AXIS.

df.head()
#THE TOP DATA OF DATA SET IS DISPLAYED

df['Month']=pd.to_datetime(df['Month'])
#THE MONTH COLUMN IN DATA SET IS TAKEN AS MONTH AND WHICH IS USED AS X AXIS ALSO.

df.head()

df.set_index('Month',inplace=True)
#MONTH VALUE IS VALID OR NULL IN THE ROW

df.head()

df.plot()
#PLOTING THE GRAPH by using X_axis and Y_axis as Month(X) && Waiting List Conformed(Y).

#Need to find order && Seasonal_order ,its a Proto-type Model Values
#Seasonal AutoRegressive Integrated Moving Average with exogenous regressors model
model=sm.tsa.statespace.SARIMAX(df['Waiting List Conformed'],order=(1, 0, 0),seasonal_order=(1,1,1,12))
results=model.fit()
#Best fitting model

#start value is starting value to predict
#END Value is Ending value to predict.
df['forecast']=results.predict(start=100,end=120,dynamic=True)
#figsize is size of below graph window.
df[['Waiting List Conformed','forecast']].plot(figsize=(15,8))

from pandas.tseries.offsets import DateOffset
#days can be replaced with years,months,days etc.
#range is the range of values to predict in the graph.
future_dates=[df.index[-1]+ DateOffset(days=x)for x in range(0,15)]

future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)

future_datest_df
#future values to be needed to predict

#combining past and future values   
future_df=pd.concat([df,future_datest_df])

b=future_df['forecast'] = results.predict(start = 105, end = 120, dynamic= True)
#future predicted values are saved in form of b.
#index value start and end in csv data set.dynamic true is no null values in between.
future_df[['Waiting List Conformed', 'forecast']].plot(figsize=(15, 8))
#print(pyplot.show())

b
#we can use b to use the data values to Sent it to the web server.