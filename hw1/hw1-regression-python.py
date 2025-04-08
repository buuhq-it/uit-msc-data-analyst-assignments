from pandas import read_excel
from statsmodels.formula.api import ols

df =  read_excel("hw1-regression-excel.xlsx", sheet_name="data")
df.columns = [col.replace(' ', '') for col in df.columns]
#df.head()

model = ols("Price ~ Area + Frontage + AccessRoad + Floors + Bedrooms + Bathrooms", data = df).fit()
# model.summary()
print(model.summary())