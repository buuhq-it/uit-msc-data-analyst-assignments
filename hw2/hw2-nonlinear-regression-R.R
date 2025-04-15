#setwd("F:\\learning-area\\uit-msc\\subjects\\phan-tich-du-lieu-kinh-doanh\\uit-msc-data-analyst-assignments\\hw1")
library(readxl)
library(dplyr)

# Đọc dữ liệu
df <- read_excel("hw2-regression-excel.xlsx", sheet = "data")
names(df) <- gsub(" ", "", names(df))

# Hồi quy tuyến tính
model <- lm(Price ~ Area + Frontage + AccessRoad + Floors + Bedrooms + Bathrooms, data = df)

# In kết quả
#summary(model)
print(summary(model))