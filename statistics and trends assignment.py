def csvFile(d):
    """Original data"""
    d = pd.read_csv(d)
    display(d.head())
    return d

def t(d):
    """Transposed data"""
    print("Transpose of data : ")
    display(d.T)
    
def linePlot(d):
    """Line plot"""
    plt.figure(figsize=(20,5))
    d.plot(kind='line',x='Country Name')
    plt.xlabel("Country Name")
    plt.ylabel("Areable Land in Hectors")
    plt.title("Areable land in different countries")
    plt.show()

def pieChart(d):
    """Pie chart"""
    l = list(d.columns)[1:]
    cuba = d.loc[2, :].values.flatten().tolist()[1:]
    plt.pie(cuba,labels = l,autopct='%1.0f%%', pctdistance=0.5, labeldistance=1.2)
    plt.title("Areable land for cuba country for different years(in hectors)")
    plt.show()
    uk = d.loc[5, :].values.flatten().tolist()[1:]
    plt.pie(uk,labels = l,autopct='%1.0f%%', pctdistance=0.5, labeldistance=1.2)
    plt.title("Areable land for U.K country for different years(in hectors)")
    plt.show()
    
def statf(year):
    """Statistical properties"""
    print("Average: ", np.mean(year))
    print("Standard deviations :", np.std(year))
    print("Maximum Value :", np.max(year))
    print("Minimum value :", np.min(year))
    print("Gmean : ", st.gmean(year))
    print("Hmean : ", st.hmean(year))
    print()

def pearsonCorrelation(d):
    """Person Correlation"""
    print("Pearson Correlation : ")
    display(d.corr())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st

d = csvFile("Arable_land.csv")
t(d)
linePlot(d)
pieChart(d)
print("Statistical properties for the year 2006 : ")
statf(d["2006"])
print("Statistical properties for the year 2006 : ")
statf(d["2007"])
print("Statistical properties for the year 2006 : ")
statf(d["2008"])
print("Statistical properties for the year 2006 : ")
statf(d["2009"])
print("Statistical properties for the year 2006 : ")
statf(d["2010"])
pearsonCorrelation(d)