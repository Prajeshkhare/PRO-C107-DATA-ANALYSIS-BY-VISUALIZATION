import pandas as pd 
import csv
import plotly.express as px

df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

with open ("data.csv")as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="student_id", y= "level", size = "attempt",color = "student_id")
    fig.show()
