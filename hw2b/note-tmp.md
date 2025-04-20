```text
Algorithm GradientDescent_HousePrice(X, y, w0, alpha, k_max, tolerance)
Input:
  X: tập dữ liệu [[x_{i1}, x_{i2}, x_{i3}], i=1..m],
  x_{i1}: diện tích, x_{i2}: số phòng ngủ, x_{i3}: số phòng tắm
  y: vector giá nhà [y_1, y_2, ..., y_m]
  w0: vector tham số khởi tạo [w1, w2, w3, w4, w5]
  alpha: độ dài bước
  k_max: số bước lặp tối đa
  tolerance: ngưỡng dừng

Output: vector tham số w tối ưu

1. Initialize w = w0
2. Initialize k = 0
3. While k < k_max:
     a. Compute M(w, x_i) = w1 * exp(w2 * x_{i1}) + w3 * x_{i2} + w4 * x_{i3} + w5 for i=1..m
     b. Compute gradient grad = [grad_w1, grad_w2, grad_w3, grad_w4, grad_w5]
        where grad_w1 = -sum_{i=1}^m (y_i - M(w, x_i)) * exp(w2 * x_{i1})
              grad_w2 = -sum_{i=1}^m (y_i - M(w, x_i)) * (w1 * x_{i1} * exp(w2 * x_{i1}))
              grad_w3 = -sum_{i=1}^m (y_i - M(w, x_i)) * x_{i2}
              grad_w4 = -sum_{i=1}^m (y_i - M(w, x_i)) * x_{i3}
              grad_w5 = -sum_{i=1}^m (y_i - M(w, x_i))
     c. Compute norm_grad = sqrt(grad_w1^2 + grad_w2^2 + grad_w3^2 + grad_w4^2 + grad_w5^2)
     d. If norm_grad < tolerance:
          Return w
     e. Update w = w - alpha * grad
     f. k = k + 1
4. Return w
```