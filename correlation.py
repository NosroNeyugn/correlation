import numpy as np
import plotly.express as px
import csv

def get_data_source(data_path):
    marks_in_percentage=[]
    days_present=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return{"x":marks_in_percentage,"y":days_present}

def find_correlation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation Value: ",correlation[0,1])

def setup():
    data_path="studentmarksvsdayspresent.csv"
    data_source=get_data_source(data_path)
    find_correlation(data_source)

setup()
