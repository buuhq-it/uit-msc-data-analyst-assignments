```text
Prerequisite:

Install R:
https://cran.r-project.org/

Install RStudio:
https://posit.co/download/rstudio-desktop/

Install Anaconda:
https://www.anaconda.com/download/success

```
```shell
## Create virtual environment 
conda create -n machine-learning-ana-env python=3.12 anaconda

## Active environment
conda activate machine-learning-ana-env
```




```R
# Run Regression with R
## Step 0: Open RStudio

## Step 1: install packages
install.packages("readxl")
install.packages("dplyr")

## Step 2: set working directory
setwd("F:\\learning-area\\uit-msc\\subjects\\phan-tich-du-lieu-kinh-doanh\\uit-msc-data-analyst-assignments\\hw1")

## Step 3 run code:
source("hw1-regression-R.R")
source("hw2-nonlinear-regression-R.R")
```

```python
# Run Regression with python

## Step 1: Open code directory with VSCode
## Step 2: Open Terminal
## Step 3: Active conda environment: conda activate machine-learning-ana-env
## Step 4: Run code
python python hw1-regression-python.py

```

```text
===== note to copy to ms word =====
```

```python
## Preprocessor
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

df =  read_excel("hw1-regression-excel.xlsx", sheet_name="data")
df.columns = [col.replace(' ', '') for col in df.columns]
#df.head()

model = ols("Price ~ Area + Frontage + AccessRoad + Floors + Bedrooms + Bathrooms", data = df).fit()
# model.summary()
print(model.summary())
```

```R
setwd("F:\\learning-area\\uit-msc\\subjects\\phan-tich-du-lieu-kinh-doanh\\uit-msc-data-analyst-assignments\\hw1")
getwd()

install.packages("readxl")
install.packages("dplyr")
install.packages("polyreg")
install.packages(c("readxl", "dplyr", "polyreg"))

install.packages("readxl", "dplyr", "polyreg")
conda install r-readxl r-dplyr

# Regression with R
library(readxl)
library(dplyr)

# Đọc dữ liệu
df <- read_excel("hw1-regression-excel.xlsx", sheet = "data")
names(df) <- gsub(" ", "", names(df))

# Hồi quy tuyến tính
model <- lm(Price ~ Area + Frontage + AccessRoad + Floors + Bedrooms + Bathrooms, data = df)

# In kết quả
# summary(model)
print(summary(model))
```

```R
setwd("F:\\learning-area\\uit-msc\\subjects\\phan-tich-du-lieu-kinh-doanh\\uit-msc-data-analyst-assignments\\hw1")
getwd()
source("hw1-regression-R.R")
```

```shell
conda create -n ml-basic-r-python-env python=3.12 r-base=4.4 r-irkernel ipykernel jupyterlab

conda activate ml-basic-r-python-env

conda install jupyter jupyterlab r-readxl r-dplyr pandas matplotlib seaborn scikit-learn


conda create -n ml-r-env python=3.11 r-base=4.3 r-essentials anaconda -c r -c conda-forge


conda env remove -n ml-basic-r-python-env
conda create -n ml-basic-r-python-env python=3.12 r-base=4.4 r-essentials jupyterlab
conda activate ml-basic-r-python-env
R -e "install.packages('IRkernel', repos='https://cran.r-project.org'); IRkernel::installspec()"

## new
conda create -n ml-basic-r-python-env python=3.12 r-base r-irkernel ipykernel jupyterlab
conda activate ml-basic-r-python-env


conda env remove -n ml-basic-r-python-env

install.packages(c("cli", "magrittr", "purrr", "rlang", "vctrs"))
remove.packages("languageserver")
install.packages("languageserver")
install.packages('IRkernel')
IRkernel::installspec(user = FALSE)  # Đăng ký kernel cho Jupyter


### new 2
conda create -n ml-basic-r-python-env python=3.12 r-base=4.4 r-irkernel ipykernel jupyterlab -c conda-forge
conda activate ml-basic-r-python-env

conda activate ml-basic-r-python-env
conda install pandas scikit-learn -c conda-forge
conda install openpyxl -c conda-forge
conda install statsmodels -c conda-forge
conda activate tktmdt

```
```shell
python hw2-nonlinear-regression-python.py
```
```R
source("hw2-nonlinear-regression-R.R")
```