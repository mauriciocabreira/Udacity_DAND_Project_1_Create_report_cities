# We import Pandas as pd into Python
import pandas as pd

Temperatures = pd.read_csv('./temp_data_from_db.csv')

print("data is of type:", type(Temperatures))
print("Temperature shape: ", Temperatures.shape)

print(Temperatures)

print(Temperatures.head(10))

print(Temperatures.tail(20))

print(Temperatures.isnull().any())

print("Describe: ", Temperatures.describe())
#print("Describe YEAR: ", Temperatures['Year'].describe())
print("Describe Guarulhos: ", Temperatures['Guarulhos'].describe())
#print("Describe Global: ", Temperatures['Global'].describe())
