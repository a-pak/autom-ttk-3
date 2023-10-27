import visualizer

#####################################
#Kuvaaja (plot) - x: TIME, 
#y: PUMP TEMPERATURE
#####################################
def graphBuilder(datalog_1, datalog_2):
  TIME = datalog_1[:, find_index_by_value(titles, "TIME")]
  TEMPERATURE_1 = datalog_1[:, find_index_by_value(titles, "PUMP TEMPERATURE")]
  TEMPERATURE_2 = datalog_2[:, find_index_by_value(titles, "PUMP TEMPERATURE")]
  x_label = "Time"
  y_label = "Pump Temperature"
  graph_1 = [TIME, TEMPERATURE_1]
  graph_2 = [TIME, TEMPERATURE_2]

  title = "Kuvaaja (plot) - x: TIME, y: PUMP TEMPERATURE / Antti Kuivalainen 13582"
  visualizer.plotVisualizer(title, x_label, y_label, graph_1, graph_2)
