import pandas as pd
# data = {
#     "name":["abc","pqr","xyz"],
#     "marks":[1,2,3]
# }
# df=pd.DataFrame(data)
# print(df)
data = {
    "Name":["rugved","tanmay","yash","Sneha"],
    "Dept" : ["CSE","IT","CSE","IT"],
    "Marks":[97,92,60,45]
}
df=pd.DataFrame(data)
print(df)
print("Original data:\n",df)
print("\nSubset  (Marks > 50):\n",df[df["Marks"] > 50])
print("Sorted by Marks (Ascending) :\n",
df.sort_values("Marks"))
print("Sorted by Marks :(Descending) :\n",
      df.sort_values("Marks",ascending=False))
print("\nGrouped (Average Marks by Department):\n",
      df.groupby("Dept")["Marks"].mean())
print("\nMean =",df["Marks"].mean())
print("Meadia =",df["Marks"].median())
print("Mode =")
print(df["Marks"].mode())
