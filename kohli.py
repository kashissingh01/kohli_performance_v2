import pandas as pd

df = pd.read_csv("dataset.csv")

#print(df.head(10))

#print(df.tail(10))

#print(df.info)
#print(df.shape)
#print(df.describe())
#print(df["Opposition"].describe())
run_frequency = df["Runs"].value_counts()
print(run_frequency)

new_df = df[["Runs","SR","Opposition"]]
print(new_df)

#conditional statements

vs_aussies = df[df["Opposition"]== "v Australia"]
print(vs_aussies)

#find all the matches where Virat scored a century
v_cent = df[df["SR"]>100]   
print(v_cent)

def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"

df["centuries"] = df["Runs"].apply(find_centuries)
print(df.tail(10))