import matplotlib.pyplot as plt


def plotVisualizer (title, x_label, y_label, line_1, line_2, frame):
  plt.figure(figsize=(16,8))
  plt.title(title)
  plt.grid(True)
  plt.xlim(frame[0])
  plt.ylim(frame[1])
  plt.plot( line_1[0], line_1[1], label="Set 1" )
  plt.plot( line_2[0], line_2[1], label="Set 2" ) 
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.legend()
  plt.show()

def scatterVisualizer (title, x_label, y_label, line_1, line_2):
  plt.figure(figsize=(16,8))
  plt.title(title)
  plt.grid(True)
  plt.scatter( line_1[0], line_1[1], s=2, label="Set 1" )
  plt.scatter( line_2[0], line_2[1], s=2, label="Set 2" ) 
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.legend()
  plt.show()