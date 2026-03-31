import math # Không thực sự cần thiết cho bài này nhưng thói quen import đầu file

def sum_1_to_n_loop(n):
    """
    Tính tổng các số nguyên từ 1 đến n sử dụng vòng lặp.

    Args:
        n (int): Số nguyên dương mà ta muốn tính tổng đến.

    Returns:
        int: Tổng của các số từ 1 đến n.

    Raises:
        ValueError: Nếu n không phải là số nguyên hoặc n âm.
    """
    # --- Bước 1: Kiểm tra đầu vào ---
    # Đảm bảo rằng n là một số nguyên.
    if not isinstance(n, int):
        raise ValueError("Lỗi: n phải là một số nguyên.")
    
    # Đảm bảo rằng n không âm.
    # Nếu n là 0, vòng lặp sẽ không chạy và current_sum sẽ vẫn là 0, điều này là chính xác.
    if n < 0:
        raise ValueError("Lỗi: n không thể là số âm. Hãy nhập một số nguyên không âm.")

    # --- Bước 2: Khởi tạo biến tổng ---
    current_sum = 0

    # --- Bước 3: Vòng lặp để tính tổng ---
    # Lặp qua các số từ 1 đến n (bao gồm cả n).
    # Hàm range(start, stop) sẽ tạo ra một chuỗi số từ 'start' đến 'stop-1'.
    # Vì vậy, để bao gồm 'n', chúng ta cần 'n + 1'.
    for i in range(1, n + 1):
        current_sum += i  # Cộng số hiện tại (i) vào tổng
        
    # --- Bước 4: Trả về kết quả ---
    return current_sum

def sum_1_to_n_formula(n):
    """
    Tính tổng các số nguyên từ 1 đến n sử dụng công thức toán học.
    Công thức tổng của cấp số cộng từ 1 đến n là: n * (n + 1) / 2.

    Args:
        n (int): Số nguyên dương mà ta muốn tính tổng đến.

    Returns:
        int: Tổng của các số từ 1 đến n.

    Raises:
        ValueError: Nếu n không phải là số nguyên hoặc n âm.
    """
    # --- Bước 1: Kiểm tra đầu vào ---
    # Tương tự như phương pháp vòng lặp, kiểm tra n.
    if not isinstance(n, int):
        raise ValueError("Lỗi: n phải là một số nguyên.")
    if n < 0:
        raise ValueError("Lỗi: n không thể là số âm. Hãy nhập một số nguyên không âm.")

    # --- Bước 2: Áp dụng công thức ---
    # Sử dụng công thức n * (n + 1) / 2.
    # Phép chia nguyên (//) được sử dụng để đảm bảo kết quả là số nguyên,
    # vì tổng của các số nguyên luôn là số nguyên.
    total = n * (n + 1) // 2
    
    # --- Bước 3: Trả về kết quả ---
    return total

# --- Ví dụ test ---

print("--- Test với phương pháp vòng lặp (sum_1_to_n_loop) ---")

# Các trường hợp hợp lệ
test_cases_valid = [0, 1, 5, 10, 100]

for n_val in test_cases_valid:
    try:
        result = sum_1_to_n_loop(n_val)
        print(f"Tổng từ 1 đến {n_val} là: {result}")
    except ValueError as e:
        print(f"Lỗi khi tính tổng với n={n_val}: {e}")

# Các trường hợp không hợp lệ (để kiểm tra xử lý lỗi)
test_cases_invalid = [-1, 3.5, "abc", None]

print("\n--- Test các trường hợp lỗi với vòng lặp ---")
for n_val in test_cases_invalid:
    try:
        result = sum_1_to_n_loop(n_val)
        print(f"Tổng từ 1 đến {n_val} là: {result}") # Dòng này sẽ không được chạy nếu có lỗi
    except ValueError as e:
        print(f"Lỗi dự kiến với n={n_val}: {e}")

print("\n" + "="*50 + "\n") # Dấu phân cách

print("--- Test với phương pháp công thức (sum_1_to_n_formula) ---")

# Các trường hợp hợp lệ
for n_val in test_cases_valid:
    try:
        result = sum_1_to_n_formula(n_val)
        print(f"Tổng từ 1 đến {n_val} là: {result}")
    except ValueError as e:
        print(f"Lỗi khi tính tổng với n={n_val}: {e}")

# Các trường hợp không hợp lệ (để kiểm tra xử lý lỗi)
print("\n--- Test các trường hợp lỗi với công thức ---")
for n_val in test_cases_invalid:
    try:
        result = sum_1_to_n_formula(n_val)
        print(f"Tổng từ 1 đến {n_val} là: {result}") # Dòng này sẽ không được chạy nếu có lỗi
    except ValueError as e:
        print(f"Lỗi dự kiến với n={n_val}: {e}")