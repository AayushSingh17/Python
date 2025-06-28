#Pandas....


#it is an open source python library used for data manupulation and analysis.

#it provides data structures like dataframes and series (which are designs to handle tabular and time series data efficiently.)

#stands for python data analysis

#It is not a databases but it can work with data from various souces souch as CSV files, Excel Files and SQL databases


import pandas as pd

#Series...

# It is a one dimensional label array which can store any data type.It consist of value and lables (index)

s = pd.Series([1,3,5], index = ["Aayu", "Aayush", "Singh"])
print(s["Aayush"])
print(s)
print(s.values)



#Data Frame


#it is s two dimensional table which consist of rows, column and it offers labels

data = {
    "Name": ["Aayush", "Aayu", "Sam"],
    "Age": [19,9,15],
    "Score":[90,99,95]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])

print(df[df["Score"]>90])

df["Grade"]=["A", "O", "A+"]
print(df)

df.drop("Age", axis=1,inplace=True)
print(df)

df.rename(columns={"Score":"Marks"}, inplace=True)
print(df)

df1= pd.DataFrame({
    "Name" :["Alice", None, "Charlie"],
    "Marks": [89, None, 96]
})
print(df1.isnull())
df1.fillna("unknown", inplace=True)
print(df1)
df1.dropna(inplace=True)


print(df.describe())   #Summary Stats

print(df.mean(numeric_only=True))   # Mean for numeric columns

print(df.groupby("Grade")["Marks"].mean())   #Grouping

print(df[0:2])

df.set_index("Name", inplace=True)
print(df)

df.reset_index("Name", inplace=True)
print(df)


#CSV...


#CSV stand for Comma Separated Value
# A simple way to store big data 
#CSV file contains plain text and can be read using pandas


df2 = pd.read_csv("day.csv")
print(df2.head())

df.to_csv("output.csv", index=False)

# df = pd.read_excel("data.xlsx")
# df.to_excel("output.xlsx")

s = pd.Series([1,2,3], index=["Aayush", "Aayu","Charlie"])
print(s[["Aayush", "Aayu"]])
print(s)
print(s.values)
print(s.size)
print(s.shape)
s["Sam"]=4
print(s)
s.drop("Sam", inplace=True)

s1 = pd.Series([1,2,3])
print(s1+2)
print(s1*2)
print(s1**100)
print(s1[s1>2])
print(s1.sum)
print(s1.mean)
print(s1.min(), s1.max())
print(s1.std())

names = pd.Series(["Aayush", "Aayu","Charlie", "Singh"])
print(names.str.upper())
print(names.str.capitalize())
print(names.str.contains("a"))

s = pd.Series([30,20,10,40], index=['d', 'b', 'a', 'c'])

print(s2.sort_value())
print(s2.sort_index())
print(s2.rank())

s3 = pd.Series([10,20,30], index=['a', 'b', 'c'])
s3 = pd.Series([50,15,9], index=['a', 'b', 'c'])

print(s3 + s4)