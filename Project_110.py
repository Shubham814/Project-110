import csv
import random
import pandas as pd
import statistics as st
import plotly.graph_objects as go
import plotly.figure_factory as ff

file = pd.read_csv("./medium_data.csv")

data = file["claps"].tolist()

mean_pop = st.mean(data)
mode_pop = st.mode(data)
median_pop = st.median(data)
stdev_pop = st.stdev(data)


print("Population Mean: " + str(mean_pop))
print("Population Stdev: " + str(stdev_pop))



# figure = ff.create_distplot([data],["Temprature"],show_hist = False)
# figure.add_trace(go.Scatter(x=[mean_pop,mean_pop],y=[0,1],mode="lines",name="Mean"))
# figure.show() 

def randomSetOfMean(counter):
    dataset = []
    # print(len(data))
    # print(data)
    # print(counter)
    for i in range(1,int(counter)):
        randomIndex = random.randint(0,len(data) - 1)
        value = data[randomIndex]
        dataset.append(value)

    mean = st.mean(dataset)
    return mean

def showFigure(meanList):
    mean = st.mean(meanList)
    stdev = st.stdev(meanList)
    print("\n\nSampling Mean: " + str(mean))
    print("Sampling Stdev: " + str(stdev))
    fig = ff.create_distplot([meanList],["Temprature"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,12],mode="lines",name="mean"))
    fig.show()


def setup():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(30)
        meanList.append(setOfMeans)

    showFigure(meanList)


setup()
