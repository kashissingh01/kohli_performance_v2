import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
print(df.head())


#total number of runs kohli scored

print("total nums: ",df["Runs"].sum())

#total number of balls
print("total balls faced: ",df["BF"].sum())

print("average: ",df["SR"].mean())

#number of matches he has played at different positions

print(df["Pos"].head(10))

positions=df["Pos"].unique()
print(positions)

df["Pos"]=df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6"

    
})
#print(df[["Runs","Pos"]])
pos_counts = df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))
#total runs scored in different positions
pos_counts_values = pos_counts.values
pos_counts_labels = pos_counts.index
fig = plt.figure(figsize=(10,7)) #width=10 height=7
plt.pie(pos_counts_values, labels=pos_counts_labels)
#plt.show()



#total number of matches he has played with diff oppositoins
def show_pie_plots(df,key):
    counts= df[key].value_counts()
    print(counts)
    count_values = counts.values
    count_labels = counts.index
    fig = plt.figure(figsize=(10,7)) #width=10 height=7
    plt.pie(count_values, labels=count_labels)
    #plt.show()
#show_pie_plots(df,"Opposition")



#number of centuries scored by him in 1st  and 2nd inings


#number of matches he has played at Grounds
#show_pie_plots(df,"Ground")

#total sixes scored in different postions
runs_at_pos = df.groupby("Pos")["6s"].sum()
print("okay",runs_at_pos)
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index
fig = plt.figure(figsize=(10,10))
plt.bar(
    runs_at_pos_labels,runs_at_pos_values,color="green",width=0.3
)
#plt.show()


#total run scored in diff countries
runs_at_cntry = df.groupby('Opposition')['Runs'].sum()
print("diff countries",runs_at_cntry)
runs_at_cnt_values = runs_at_cntry.values
runs_at_cnt_labels = runs_at_cntry.index
fig = plt.figure(figsize=(10,10))
plt.bar(
    runs_at_cnt_labels,runs_at_cnt_values,color="red",width=0.3
)
plt.show()


#number of centuries scored by him in 1st and 2nd innings
centuries = df.query("Runs >= 100")
print(centuries)

innings = centuries["Inns"].value_counts()
plt.pie(innings.values,labels=innings.index)
plt.show()
#tons = centuries["Runs"]
#plt.bar(innings,width=0.3,color="pink")
#plt.show()

#calculate the dismissals of kohli


#against which teams he has scored the most



#Analyze the strike rate


#Kohli's strike rate in first innings vs second