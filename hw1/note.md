```python
from pandas import read_csv, ExcelWriter
from sklearn.model_selection import train_test_split

def split_text(text):
    text = text.split(',')[-1].strip()
    if '.' in text:
        return text[:-1]
    return text

df = read_csv('./datasets/vietnam_housing_dataset.csv')
df.dropna(inplace=True)
df['Province'] = df['Address'].map(split_text)
df['Province'].unique()
df_train, df_text = train_test_split(df)

cols = ['Address', 'Province',  'House direction',
       'Balcony direction', 'Legal status',
       'Furniture state', 'Area', 'Frontage', 'Access Road', 'Floors', 'Bedrooms', 'Bathrooms',  'Price']

with ExcelWriter('./datasets/housing_data_preprocessor.xlsx') as writer:
    df_train[cols].to_excel(writer, sheet_name='train_data', index=None)
    df_text[cols].to_excel(writer, sheet_name='test_data', index=None)
    df[cols].to_excel(writer, sheet_name='data', index=None)
```

```python
# Regression with python
from pandas import read_excel
from statsmodels.formula.api import ols

df =  read_excel("hw1-group11-regression-excel.xlsx", sheet_name="data")
df.columns = [col.replace(' ', '') for col in df.columns]
#df.head()

model = ols("Price ~ Area + Frontage + AccessRoad + Floors + Bedrooms + Bathrooms", data = df).fit()
model.summary()
```