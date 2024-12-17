import pandas

data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data2 = data * 2
data2.to_csv("sampledata2.txt", index=None)
