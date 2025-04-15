from pandas import read_csv, ExcelWriter
from sklearn.model_selection import train_test_split

def split_text(text):
    text = text.split(',')[-1].strip()
    if '.' in text:
        return text[:-1]
    return text

# input file: vietnam_housing_dataset.csv
df = read_csv('./datasets/vietnam_housing_dataset.csv')
df.dropna(inplace=True)
df['Province'] = df['Address'].map(split_text)
df['Province'].unique()
df_train, df_text = train_test_split(df)

cols = ['Address', 'Province',  'House direction',
       'Balcony direction', 'Legal status',
       'Furniture state', 'Area', 'Frontage', 'Access Road', 
       'Floors', 'Bedrooms', 'Bathrooms',  'Price']

# output file: hw2-nonlinear-regression-excel.xlsx
with ExcelWriter('./datasets/hw2-nonlinear-regression-excel.xlsx') as writer:
    df_train[cols].to_excel(writer, sheet_name='train_data', index=None)
    df_text[cols].to_excel(writer, sheet_name='test_data', index=None)
    df[cols].to_excel(writer, sheet_name='data', index=None)