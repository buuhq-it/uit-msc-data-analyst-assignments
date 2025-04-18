# 1. Load các gói cần thiết
library(readxl); library(dplyr); library(polyreg) # nolint

# 2. Đọc dữ liệu từ Excel
df <- read_excel("hw2-nonlinear-regression-excel.xlsx", sheet = "data")
names(df) <- gsub(" ", "", names(df))

# 3. Chọn biến X và y
X <- select(df, Area, Bedrooms, Bathrooms) # nolint
y <- df$Price

# 4. Tạo biến đa thức bậc 2
X_poly <- model.matrix(~ poly(Area, 2, raw = TRUE) + # nolint
                         poly(Bedrooms, 2, raw = TRUE) +
                         poly(Bathrooms, 2, raw = TRUE) +
                         I(Area * Bedrooms) +
                         I(Area * Bathrooms) +
                         I(Bedrooms * Bathrooms),
                       data = X)[, -1]  # bỏ intercept mặc định
# Đổi tên cột lại để hiển thị cho đẹp
colnames(X_poly) <- c("Area", "Area_2", "Bedrooms", "Bedrooms_2", # nolint
                      "Bathrooms", "Bathrooms_2",
                      "AreaBedrooms", "AreaBathrooms", "BedroomsBathrooms")
# 5. Tạo data frame cho hồi quy
data_poly <- data.frame(Price = y, X_poly)

# 6. Hồi quy tuyến tính OLS
model <- lm(Price ~ ., data = data_poly)

# 7. Hiển thị kết quả
#print(summary(model))

# 8. Dự đoán với dữ liệu mới
X_new_poly <- model.matrix(
  ~ poly(Area, 2, raw = TRUE) +
    poly(Bedrooms, 2, raw = TRUE) +
    poly(Bathrooms, 2, raw = TRUE) +
    I(Area * Bedrooms) +
    I(Area * Bathrooms) +
    I(Bedrooms * Bathrooms),
  data = X_new
)[, -1, drop = FALSE]

colnames(X_new_poly) <- colnames(X_poly)

# Đổi tên cột cho giống với data_poly
colnames(X_new_poly) <- c("Area", "Area_2", "Bedrooms", "Bedrooms_2",
                          "Bathrooms", "Bathrooms_2",
                          "AreaBedrooms", "AreaBathrooms", "BedroomsBathrooms")

# Đưa vào data.frame để predict
X_new_df <- as.data.frame(X_new_poly)

# 9. Dự đoán
predicted_price <- predict(model, newdata = X_new_df)

# 10. Hiển thị kết quả
cat("Giá nhà dự đoán:", round(predicted_price, 2), "\n")