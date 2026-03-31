# bai1_tong_1_den_5.py

"""
Chương trình này tính tổng các số nguyên từ 1 đến 5.
"""

def tinh_tong_1_den_5():
    """
    Hàm này tính tổng của các số nguyên từ 1 đến 5.
    
    Returns:
        int: Tổng của các số từ 1 đến 5.
    """
    # Khởi tạo biến tổng
    tong = 0
    
    # Duyệt qua các số từ 1 đến 5 (range(1, 6) sẽ sinh ra 1, 2, 3, 4, 5)
    for i in range(1, 6):
        tong += i  # Cộng số hiện tại vào tổng
        
    # Cách khác ngắn gọn hơn (Pythonic):
    # tong = sum(range(1, 6))
    
    return tong

# Phần này chỉ chạy khi script được thực thi trực tiếp, không phải khi được import
if __name__ == "__main__":
    print("--- Bài 1: Tính tổng từ 1 đến 5 ---")
    
    # Gọi hàm để tính tổng
    ket_qua = tinh_tong_1_den_5()
    
    # In ra kết quả
    print(f"Tổng các số từ 1 đến 5 là: {ket_qua}")
    
    # Ví dụ test case đơn giản:
    # Expected output: 1 + 2 + 3 + 4 + 5 = 15
    assert ket_qua == 15, f"Lỗi: Kết quả mong đợi là 15 nhưng nhận được {ket_qua}"
    print("Test case thành công: Tổng 1 đến 5 = 15")




# bai2_giai_phuong_trinh_bac_2.py

"""
Chương trình này giải phương trình bậc hai có dạng ax^2 + bx + c = 0.
Nó xử lý các trường hợp có nghiệm thực, nghiệm kép, nghiệm phức, và cả trường hợp đặc biệt khi a = 0 (phương trình bậc nhất).
"""

import math
import cmath # Sử dụng cmath để xử lý số phức (nghiệm phức)

def giai_phuong_trinh_bac_2(a, b, c):
    """
    Giải phương trình bậc hai có dạng ax^2 + bx + c = 0.

    Args:
        a (float): Hệ số của x^2.
        b (float): Hệ số của x.
        c (float): Hằng số.

    Returns:
        tuple: Một tuple chứa (trạng thái, nghiệm).
               - Trạng thái có thể là:
                 "Phuong trinh vo nghiem"
                 "Phuong trinh co vo so nghiem"
                 "Phuong trinh bac nhat co 1 nghiem"
                 "Phuong trinh co 1 nghiem kep"
                 "Phuong trinh co 2 nghiem thuc phan biet"
                 "Phuong trinh co 2 nghiem phuc phan biet"
               - Nghiệm là một list chứa các nghiệm (có thể rỗng, 1 hoặc 2 nghiệm).
    """
    
    print(f"\nGiải phương trình: {a}x^2 + {b}x + {c} = 0")

    # Trường hợp 1: a = 0 (Không phải phương trình bậc hai)
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phuong trinh co vo so nghiem", [] # 0 = 0
            else:
                return "Phuong trinh vo nghiem", [] # c = 0 (c khác 0)
        else:
            # Phương trình bậc nhất: bx + c = 0 => x = -c/b
            x = -c / b
            return "Phuong trinh bac nhat co 1 nghiem", [x]
    
    # Trường hợp 2: a != 0 (Phương trình bậc hai thực sự)
    
    # Tính delta (biệt thức)
    delta = b**2 - 4*a*c
    
    if delta > 0:
        # Hai nghiệm thực phân biệt
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return "Phuong trinh co 2 nghiem thuc phan biet", [x1, x2]
    elif delta == 0:
        # Một nghiệm kép
        x = -b / (2*a)
        return "Phuong trinh co 1 nghiem kep", [x]
    else:
        # Hai nghiệm phức phân biệt (delta < 0)
        # Sử dụng cmath.sqrt để tính căn bậc hai của số âm
        x1 = (-b - cmath.sqrt(delta)) / (2*a)
        x2 = (-b + cmath.sqrt(delta)) / (2*a)
        return "Phuong trinh co 2 nghiem phuc phan biet", [x1, x2]

# Phần này chỉ chạy khi script được thực thi trực tiếp, không phải khi được import
if __name__ == "__main__":
    print("--- Bài 2: Giải phương trình bậc 2 (ax^2 + bx + c = 0) ---")

    # --- Các ví dụ test ---

    # Test Case 1: Hai nghiệm thực phân biệt (x^2 - 3x + 2 = 0 => x=1, x=2)
    status, roots = giai_phuong_trinh_bac_2(1, -3, 2)
    print(f"Trạng thái: {status}")
    if roots:
        print(f"Nghiệm: {roots}")
    assert status == "Phuong trinh co 2 nghiem thuc phan biet" and sorted([round(r, 5) for r in roots]) == [1.0, 2.0], "Test Case 1 LỖI"
    print("Test Case 1 THÀNH CÔNG: x^2 - 3x + 2 = 0")

    # Test Case 2: Một nghiệm kép (x^2 - 2x + 1 = 0 => x=1)
    status, roots = giai_phuong_trinh_bac_2(1, -2, 1)
    print(f"Trạng thái: {status}")
    if roots:
        print(f"Nghiệm: {roots}")
    assert status == "Phuong trinh co 1 nghiem kep" and round(roots[0], 5) == 1.0, "Test Case 2 LỖI"
    print("Test Case 2 THÀNH CÔNG: x^2 - 2x + 1 = 0")

    # Test Case 3: Hai nghiệm phức (x^2 + x + 1 = 0)
    status, roots = giai_phuong_trinh_bac_2(1, 1, 1)
    print(f"Trạng thái: {status}")
    if roots:
        print(f"Nghiệm: {roots}")
    # Kiểm tra nghiệm phức đòi hỏi so sánh cẩn thận hơn
    expected_roots_complex = [(-0.5+0.866025j), (-0.5-0.866025j)]
    assert status == "Phuong trinh co 2 nghiem phuc phan biet" and \
           (abs(roots[0] - expected_roots_complex[0]) < 1e-6 and abs(roots[1] - expected_roots_complex[1]) < 1e-6) or \
           (abs(roots[0] - expected_roots_complex[1]) < 1e-6 and abs(roots[1] - expected_roots_complex[0]) < 1e-6), "Test Case 3 LỖI"
    print("Test Case 3 THÀNH CÔNG: x^2 + x + 1 = 0")

    # Test Case 4: Phương trình bậc nhất (0x^2 + 2x + 4 = 0 => 2x + 4 = 0 => x = -2)
    status, roots = giai_phuong_trinh_bac_2(0, 2, 4)
    print(f"Trạng thái: {status}")
    if roots:
        print(f"Nghiệm: {roots}")
    assert status == "Phuong trinh bac nhat co 1 nghiem" and round(roots[0], 5) == -2.0, "Test Case 4 LỖI"
    print("Test Case 4 THÀNH CÔNG: 0x^2 + 2x + 4 = 0")

    # Test Case 5: Phương trình vô nghiệm (0x^2 + 0x + 5 = 0 => 5 = 0)
    status, roots = giai_phuong_trinh_bac_2(0, 0, 5)
    print(f"Trạng thái: {status}")
    if roots:
        print(f"Nghiệm: {roots}")
    assert status == "Phuong trinh vo nghiem" and not roots, "Test Case 5 LỖI"
    print("Test Case 5 THÀNH CÔNG: 0x^2 + 0x + 5 = 0")
    
    # Test Case 6: Phương trình vô số nghiệm (0x^2 + 0x + 0 = 0 => 0 = 0)
    status, roots = giai_phuong_trinh_bac_2(0, 0, 0)
    print(f"Trạng thái: {status}")
    if roots:
        print(f"Nghiệm: {roots}")
    assert status == "Phuong trinh co vo so nghiem" and not roots, "Test Case 6 LỖI"
    print("Test Case 6 THÀNH CÔNG: 0x^2 + 0x + 0 = 0")