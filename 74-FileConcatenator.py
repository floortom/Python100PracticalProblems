import pandas as pd
# below imports are for solution two
import io
import requests
def solution_one():
    data1 = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
    data2 = pd.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")

    dataConcated = pd.concat([data1, data2])

    dataConcated.to_csv("SampledataConcatenated.txt", index=None)

def solution_two():
    r = requests.get("https://pythonhow.com/media/data/sampledata.txt")
    c = r.content
    data1 = pd.read_csv(io.StringIO(c.decode("utf-8")))
    data2 = pd.read_csv("sampledata2.txt")
    data12 = pd.concat([data1, data2])
    data12.to_csv("sampledata12.txt", index=None)
