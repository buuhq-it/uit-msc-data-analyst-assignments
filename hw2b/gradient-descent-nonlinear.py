import math

# Dữ liệu
X = [
    [50, 1, 1],   # diện tích (m²), số phòng ngủ, số phòng tắm
    [70, 2, 1],
    [90, 2, 2],
    [100, 3, 2],
    [120, 3, 3],
    [150, 4, 3]
]
y = [0.96, 1.12, 1.31, 1.43, 1.65, 1.95]  # Giá nhà (triệu USD)
m = len(X)

# Hàm mục tiêu F(w)
def compute_F(w):
    total = 0
    for i in range(m):
        x = X[i]
        prediction = (w[0] * math.exp(w[1] * x[0]) + 
                      w[2] * x[1] + 
                      w[3] * x[2] + 
                      w[4])  # M(w, x) = w1 * exp(w2 * x1) + w3 * x2 + w4 * x3 + w5
        residual = y[i] - prediction
        total += residual * residual
    return total / 2

# Gradient F'(w)
def compute_gradient(w):
    grad = [0, 0, 0, 0, 0]
    for i in range(m):
        x = X[i]
        exp_w2x1 = math.exp(w[1] * x[0])
        prediction = w[0] * exp_w2x1 + w[2] * x[1] + w[3] * x[2] + w[4]
        residual = y[i] - prediction
        grad[0] += -residual * exp_w2x1
        grad[1] += -residual * (w[0] * x[0] * exp_w2x1)
        grad[2] += -residual * x[1]
        grad[3] += -residual * x[2]
        grad[4] += -residual
    return grad

# Tìm kiếm độ dài bước alpha (line search đơn giản)
def line_search(w, grad):
    alpha_values = [0.0000001, 0.0000005, 0.000001, 0.000005, 0.00001]  # Giá trị alpha nhỏ vì dữ liệu lớn
    best_alpha = 0
    best_F = compute_F(w)
    
    for alpha in alpha_values:
        w_new = [w[j] - alpha * grad[j] for j in range(5)]
        F_new = compute_F(w_new)
        if F_new < best_F:
            best_F = F_new
            best_alpha = alpha
    
    return best_alpha

# Gradient Descent
def gradient_descent(w0, k_max=1000, tolerance=0.001):
    w = w0[:]
    k = 0
    
    while k < k_max:
        # Tính gradient
        grad = compute_gradient(w)
        
        # Tính norm của gradient
        grad_norm = 0
        for j in range(5):
            grad_norm += grad[j] * grad[j]
        grad_norm = grad_norm ** 0.5
        
        # Kiểm tra điều kiện dừng
        if grad_norm < tolerance:
            print(f"Đã hội tụ sau {k} bước lặp. Gradient norm: {grad_norm}")
            break
        
        # Tìm độ dài bước alpha
        alpha = line_search(w, grad)
        if alpha == 0:
            print("Không tìm được alpha phù hợp, dừng lại.")
            break
        
        # Cập nhật w
        for j in range(5):
            w[j] = w[j] - alpha * grad[j]
        
        k += 1
        
        # In thông tin mỗi 100 bước lặp
        if k % 100 == 0:
            print(f"Bước {k}: w = {w}, F(w) = {compute_F(w)}")
    
    return w

# Chạy thuật toán
w0 = [0, 0, 0, 0, 0]  # Điểm bắt đầu
w_opt = gradient_descent(w0)
print(f"Tham số tối ưu: w1 = {w_opt[0]}, w2 = {w_opt[1]}, w3 = {w_opt[2]}, w4 = {w_opt[3]}, w5 = {w_opt[4]}")
print(f"Giá trị F tại điểm tối ưu: {compute_F(w_opt)}")