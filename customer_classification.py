#KURAL TABANLI SINIFLANDIRMA
import pandas as pd
df = pd.read_csv(r"C:\Users\lenovo\PycharmProjects\pythonProject\VBO_HW\persona.csv")
df.head()
df.nunique()

df["PRICE"].nunique()
df["PRICE"].value_counts()
df["COUNTRY"].value_counts()

df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("SOURCE")["PRICE"].count()
df.groupby("COUNTRY")["PRICE"].aggregate("mean")
df.groupby("SOURCE")["PRICE"].aggregate("mean")
df.groupby(["COUNTRY", "SOURCE"])["PRICE"].aggregate("mean")
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].aggregate("mean")
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].aggregate("mean")

agg_df = df.sort_values(by=['PRICE'], ascending=True)
agg_df = agg_df.reset_index()

df.describe([0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
bins = [0, 17, 20, 24, 27, agg_df["AGE"].max()]
labels = ["0_17", "18_20", "21_24", "25_27", "28+"]
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=labels)

agg_df.columns
agg_df.values[0:5]
agg_df.info()

agg_df["customers_level_based"] = [row[4].upper() + "_" + row[2].upper() + "_" +
                                   row[3].upper() + "_" + row[6].upper()
                                   for row in agg_df.values]

agg_df = agg_df.reset_index()
agg_df.head()
agg_df.value_counts()
agg_df_final = agg_df.groupby("customers_level_based").agg({"PRICE" : "mean"})
agg_df_final.nunique()

agg_df_final["SEGMENT"] = pd.qcut(agg_df_final["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df_final.groupby("SEGMENT").agg({"PRICE": "mean"})

agg_df_final = agg_df_final.reset_index()

new_gamer = "TUR_ANDROID_FEMALE_28+"
agg_df_final[agg_df_final["customers_level_based"] == new_gamer]

new_gamer = "FRA_IOS_FEMALE_28+"
agg_df_final[agg_df_final["customers_level_based"] == new_gamer]

agg_df_final.loc[(agg_df_final["SEGMENT"] == "A")]