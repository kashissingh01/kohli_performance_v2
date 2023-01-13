import pandas as pd
data={
    "apples":[4,3,6,1],
    "oranges":[3,7,4,1]
}
index_titles = [
    "Aaron","Shaun","James","Williams"
]
df = pd.DataFrame(data,index_titles) #creates blank dataframe

#print(df)
print(df.loc["Aaron"])
#print(df["oranges"].iloc[0:1]) individual
print(type(df))