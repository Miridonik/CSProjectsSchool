import pandas

data = pandas.read_csv("wine.csv")
data = data.drop("region_1",axis=1)
data = data.dropna(subset="country")
mean_price = data["price"].sum()/data["price"].count()
data["price"] = data["price"].fillna(mean_price)
#print(data.describe())
#print(data.isna().sum())
#print(data[ (data["price"]>300) & (data["country"]=="Italy") ])
print(data.groupby(["country","price"]).count())