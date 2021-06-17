import random 
import plotly.figure_factory as ff
import statistics
import pandas as pd 
import csv 

df=pd.read_csv("data.csv")                                                        
data=df["temp"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("population_mean: ",population_mean)
print("std_deviation: ",std_deviation)


dataset=[]
for i in range(1,10000):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
sample_mean=statistics.mean(dataset)
sample_std_deviation=statistics.stdev(dataset)
print("sample_mean: ",sample_mean)
print("sample_std_deviation: ",sample_std_deviation)
fig=ff.create_distplot([dataset],["temp"],show_hist=False)
fig.show()