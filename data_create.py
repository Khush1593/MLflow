import pandas as pd

data = [
    {"name":"Khush","age":21},
    {"name":"Harsh","age":20},
    {"name":"Pujan","age":22},
        ]

df = pd.DataFrame(data)

df.to_csv("data/data.csv", index=False)