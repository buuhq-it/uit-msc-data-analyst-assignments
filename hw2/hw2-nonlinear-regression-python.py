import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from statsmodels.api import OLS, add_constant

## 1: Đọc data
df =  pd.read_excel("hw2-nonlinear-regression-excel.xlsx", sheet_name="data")
## print (df.head())

# 2. Chọn X và y
X = df[["Area", "Bedrooms", "Bathrooms"]]
y = df["Price"]
# print(X)

# 3. Biến đổi đa thức bậc 2
poly = PolynomialFeatures(degree=2, include_bias=False)
Z = poly.fit_transform(X)
Z_df = pd.DataFrame(Z, columns=poly.get_feature_names_out(X.columns))
# print(Z_df)

# 4. Thêm hằng số và chạy OLS
Z_df = add_constant(Z_df)  # thêm cột intercept
# print(Z_df)
model = OLS(y, Z_df).fit()

# 5. In kết quả
print(model.summary())
