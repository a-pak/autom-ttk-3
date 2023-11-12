import matplotlib as plt
import numpy as np
import visualizer 

#############################
#Created by Antti Kuivalainen
#############################

def readLogFile(file):
  titles = []
  data = []

  try:
    with open(file) as f:
      titles = f.readline().split(",")
      titles[-1] = titles[-1].replace("\n", "")

      data = np.loadtxt(f, delimiter=",")

    print("data read from file")

  except Exception as e:
    print("Error", e)

  return  data, titles

def findIndexByValue(arr, value):
    for i, element in enumerate(arr):
        if element == value:
            return i
    return -1 


datalog_1, titles = readLogFile("./data/datalog_1.csv")
datalog_2, _ = readLogFile("./data/datalog_4.csv")

#####################################
#Kuvaaja (plot) - x: TIME, 
#y: PUMP TEMPERATURE
#####################################

TIME = datalog_1[:, findIndexByValue(titles, "TIME")]
TEMPERATURE_1 = datalog_1[:, findIndexByValue(titles, "PUMP TEMPERATURE")]
TEMPERATURE_2 = datalog_2[:, findIndexByValue(titles, "PUMP TEMPERATURE")]
x_label = "Time"
y_label = "Pump Temperature"
graph_1 = [TIME, TEMPERATURE_1]
graph_2 = [TIME, TEMPERATURE_2]
frame = [[0, 5000], [0, 80]]
title = "Kuvaaja (plot) - x: TIME, y: PUMP TEMPERATURE / Antti Kuivalainen 2013582"

visualizer.plotVisualizer(title, x_label, y_label, graph_1, graph_2, frame)


#####################################
#Pistejoukkona (Scatter): 
#PUMP SPEED x-akselilla  
#OUTLET FLOW y-akselilla
#molemmista ajoista samaan kuvaajaan
#####################################

PUMP_SPEED_1 = datalog_1[:, findIndexByValue(titles, "PUMP SPEED")]
PUMP_SPEED_2 = datalog_2[:, findIndexByValue(titles, "PUMP SPEED")]
OUTLET_FLOW_1 = datalog_1[:, findIndexByValue(titles, "OUTLET_FLOW")]
OUTLET_FLOW_2 = datalog_2[:, findIndexByValue(titles, "OUTLET_FLOW")]
x_label = "Pump Speed"
y_label = "Outlet flow"
graph_1 = [PUMP_SPEED_1, OUTLET_FLOW_1]
graph_2 = [PUMP_SPEED_2, OUTLET_FLOW_2]
title = "Pistejoukkona (Scatter): PUMP SPEED x-akselilla ja OUTLET FLOW y-akselilla / Antti Kuivalainen 2013582"

visualizer.scatterVisualizer(title, x_label, y_label, graph_1, graph_2)


######################################
#Kuvaaja (plot)
#TIME x-akselilla
#PUMP SPEED y-akselilla
#
######################################

TIME = datalog_1[:, findIndexByValue(titles, "TIME")]
PUMP_SPEED_1 = datalog_1[:, findIndexByValue(titles, "PUMP SPEED")]
PUMP_SPEED_2 = datalog_2[:, findIndexByValue(titles, "PUMP SPEED")]
x_label = "Time"
y_label = "Pump Speed"
graph_1 = [TIME, PUMP_SPEED_1]
graph_2 = [TIME, PUMP_SPEED_2]
frame = [[4100, 4350], [2300, 2900]]
title = "Kuvaaja (plot) - x: TIME, y: PUMP SPEED / Antti Kuivalainen 2013582"

visualizer.plotVisualizer(title, x_label, y_label, graph_1, graph_2, frame)
