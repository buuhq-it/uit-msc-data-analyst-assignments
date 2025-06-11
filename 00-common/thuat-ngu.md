# Thuật ngữ Machine Learning

## 1. Ensemble learning (học tập tổ hợp)

```text
Là kỹ thuật trong machine learning nhằm kết hợp nhiều mô hình yếu (weak learners) để tạo ra một mô hình mạnh hơn (strong learner)
Cấu trúc mô hình ensemble:
    Ensemble = nhiều mô hình nhỏ + cơ chế kết hợp
    Các mô hình nhỏ (base learners): thường là decision tree, SVM, neural net, etc.
    Cách kết hợp:
        Voting/Averaging: cho classification/regression
        Weighting: mỗi mô hình được cho trọng số khác nhau
        Stacking: sử dụng mô hình meta để tổng hợp dự đoán
```

Phân loại mô hình Ensemble

| Loại        | Kỹ thuật              | Ý tưởng chính                                             | Ví dụ                       |
| ----------- | --------------------- | --------------------------------------------------------- | --------------------------- |
| Bagging  | Bootstrap Aggregation | Huấn luyện các mô hình trên các tập con dữ liệu khác nhau | Random Forest               |
| Boosting | Trọng số cho lỗi      | Tăng trọng số cho các mẫu bị đoán sai                     | AdaBoost, XGBoost, LightGBM |
| Stacking | Mô hình tổ hợp        | Mô hình meta học từ đầu ra của các mô hình con            | StackingClassifier          |
| Blending | Biến thể stacking     | Giống stacking nhưng dùng tập validation nhỏ              | Kaggle blending tricks      |

So sánh nhanh Bagging vs Boosting

| Tiêu chí    | Bagging                | Boosting                |
| ----------- | ---------------------- | ----------------------- |
| Dữ liệu con | Ngẫu nhiên (bootstrap) | Tập trung vào mẫu sai   |
| Huấn luyện  | Song song              | Tuần tự, theo lỗi trước |
| Mục tiêu    | Giảm variance          | Giảm bias               |
| Ví dụ       | Random Forest          | AdaBoost, XGBoost       |

Một vài mô hình ensemble phổ biến

| Mô hình                         | Loại     | Mô tả                                         |
| ------------------------------- | -------- | --------------------------------------------- |
| **Random Forest**               | Bagging  | Tập hợp nhiều cây quyết định, vote theo đa số |
| **AdaBoost**                    | Boosting | Mỗi mô hình học từ lỗi của mô hình trước      |
| **Gradient Boosting / XGBoost** | Boosting | Tối ưu hóa hàm mất mát qua gradient           |
| **VotingClassifier**            | Voting   | Tổng hợp kết quả từ nhiều mô hình khác nhau   |
| **StackingClassifier**          | Stacking | Dự đoán đầu ra được tổng hợp bởi mô hình meta |

## 2. Correlation (tương quan)

### Khái niệm

Correlation đo lường mức độ liên kết tuyến tính giữa hai biến số.
Giá trị thường nằm trong khoảng [-1, 1]:

- +1: Tương quan dương hoàn hảo (cùng tăng)
- 0: Không có tương quan tuyến tính
- -1: Tương quan âm hoàn hảo (một tăng, một giảm)

### Vai trò của correlation trong Machine Learning

#### Giữa các feature (biến đầu vào): feature correlation

- Giúp phát hiện multicollinearity – nhiều đặc trưng mang thông tin trùng lặp → ảnh hưởng đến mô hình tuyến tính.

- Giảm hiệu quả học, gây overfitting, đặc biệt với:

  - Linear Regression

  - Logistic Regression

  - Naive Bayes (giả định độc lập)

- Giải pháp:

  - Feature selection (e.g. loại bỏ biến tương quan cao)

  - PCA (Principal Component Analysis) để giảm chiều

#### Giữa mô hình trong ensemble learning

Trong Random Forest / Bagging:

- Các base models (cây quyết định) nên khác nhau (diverse).

- Nếu chúng quá giống nhau (tương quan cao), thì sẽ dẫn đến redundancy → mô hình ensemble không mạnh hơn nhiều so với 1 cây.

- Giảm correlation giữa models bằng:

  - Bootstrap sampling (dữ liệu khác nhau)

  - Random subspace (random chọn feature)

  - Tree pruning

#### Trong mô hình hóa chuỗi thời gian / hồi quy

- Phân tích tương quan giữa biến đầu vào và biến mục tiêu để hiểu ý nghĩa mô hình.

- Sử dụng cross-correlation để phát hiện độ trễ (lag) phù hợp trong mô hình ARIMA, LSTM.

### Các phương pháp đo correlation phổ biến

| Tên phương pháp       | Mô tả                                         | Áp dụng tốt khi              |
| --------------------- | --------------------------------------------- | ---------------------------- |
| Pearson               | Đo tương quan tuyến tính                      | Dữ liệu chuẩn, liên tục      |
| Spearman (rank-based) | Đo tương quan xếp hạng (không tuyến tính)     | Dữ liệu ordinal, không chuẩn |
| Kendall Tau           | Dựa trên số cặp tăng/giảm                     | Nhỏ, robust                  |
| Cosine Similarity     | Đo góc giữa hai vector (định hướng)           | Đo vector đặc trưng mô hình  |
| Mutual Information    | Đo lượng thông tin chia sẻ                    | Dữ liệu phi tuyến            |
| Dot Product / Angle   | Đo tương đồng giữa mô hình / vector đặc trưng | Ensemble learning            |


```text
các
```