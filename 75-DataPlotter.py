import pandas as pd
import pylab as plt

data = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data.plot(x="x", y="y", kind="scatter")
plt.show()
