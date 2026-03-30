import math

# --- Chương trình giải phương trình bậc hai: a*x*x + b*x + c = 0 ---

def solve_quadratic_equation():
    """
    Hàm này yêu cầu người dùng nhập các hệ số a, b, c
    và giải phương trình bậc hai tương ứng, sau đó in ra các nghiệm.
    """
    print("--- GIẢI PHƯƠNG TRÌNH BẬC HAI: a*x*x + b*x + c = 0 ---")

    # Bước 1: Nhập các hệ số a, b, c từ bàn phím
    # Sử dụng try-except để xử lý lỗi nếu người dùng nhập không phải là số
    try:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập các giá trị số hợp lệ cho a, b, c.")
        return # Thoát hàm nếu nhập liệu không hợp lệ

    print(f"\nPhương trình bạn đã nhập là: {a}x^2 + {b}x + {c} = 0")

    # Bước 2: Xử lý các trường hợp đặc biệt và tính toán nghiệm

    # Trường hợp 1: a = 0 (Đây không phải là phương trình bậc hai, mà là phương trình bậc nhất hoặc đơn giản hơn)
    if a == 0:
        if b == 0:
            if c == 0:
                print("Đây là phương trình: 0 = 0. Phương trình có vô số nghiệm.")
            else:
                print(f"Đây là phương trình: {c} = 0. Phương trình vô nghiệm.")
        else: # b != 0, phương trình bậc nhất: b*x + c = 0
            x = -c / b
            print(f"Đây là phương trình bậc nhất: {b}x + {c} = 0")
            print(f"Nghiệm duy nhất: x = {x:.4f}") # Làm tròn đến 4 chữ số thập phân
    else:
        # Trường hợp 2: a != 0 (Đây là phương trình bậc hai thực sự)
        # Tính delta (biệt thức)
        delta = b*b - 4*a*c

        if delta > 0:
            # Hai nghiệm thực phân biệt
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            print("Phương trình có 2 nghiệm thực phân biệt:")
            print(f"x1 = {x1:.4f}")
            print(f"x2 = {x2:.4f}")
        elif delta == 0:
            # Nghiệm kép (hai nghiệm thực trùng nhau)
            x = -b / (2*a)
            print("Phương trình có nghiệm kép (hai nghiệm thực trùng nhau):")
            print(f"x1 = x2 = {x:.4f}")
        else: # delta < 0
            # Hai nghiệm phức liên hợp
            # Để tính căn bậc hai của số âm, chúng ta sẽ lấy căn bậc hai của giá trị tuyệt đối của delta
            # và thêm phần 'i' (đơn vị ảo)
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(abs(delta)) / (2*a)
            print("Phương trình có 2 nghiệm phức liên hợp:")
            print(f"x1 = {real_part:.4f} - {imaginary_part:.4f}i")
            print(f"x2 = {real_part:.4f} + {imaginary_part:.4f}i")

# Gọi hàm để chạy chương trình
if __name__ == "__main__":
    solve_quadratic_equation()

    print("\n--- CÁC VÍ DỤ TEST ---")
    print("Vui lòng chạy lại chương trình và nhập các giá trị sau để kiểm tra:")

    # Ví dụ 1: Hai nghiệm thực phân biệt (delta > 0)
    print("\nTEST 1: x^2 - 3x + 2 = 0")
    print("Nhập a = 1, b = -3, c = 2")
    print("Kết quả mong đợi: x1 = 1.0000, x2 = 2.0000")

    # Ví dụ 2: Nghiệm kép (delta = 0)
    print("\nTEST 2: x^2 - 2x + 1 = 0")
    print("Nhập a = 1, b = -2, c = 1")
    print("Kết quả mong đợi: x1 = x2 = 1.0000")

    # Ví dụ 3: Hai nghiệm phức liên hợp (delta < 0)
    print("\nTEST 3: x^2 + x + 1 = 0")
    print("Nhập a = 1, b = 1, c = 1")
    print("Kết quả mong đợi: x1 = -0.5000 - 0.8660i, x2 = -0.5000 + 0.8660i")

    # Ví dụ 4: Phương trình bậc nhất (a = 0)
    print("\nTEST 4: 0x^2 + 2x + 4 = 0 (tức là 2x + 4 = 0)")
    print("Nhập a = 0, b = 2, c = 4")
    print("Kết quả mong đợi: x = -2.0000")

    # Ví dụ 5: Vô nghiệm (a = 0, b = 0, c != 0)
    print("\nTEST 5: 0x^2 + 0x + 5 = 0 (tức là 5 = 0)")
    print("Nhập a = 0, b = 0, c = 5")
    print("Kết quả mong đợi: Phương trình vô nghiệm.")

    # Ví dụ 6: Vô số nghiệm (a = 0, b = 0, c = 0)
    print("\nTEST 6: 0x^2 + 0x + 0 = 0 (tức là 0 = 0)")
    print("Nhập a = 0, b = 0, c = 0")
    print("Kết quả mong đợi: Phương trình có vô số nghiệm.")

    # Ví dụ 7: Nhập liệu không hợp lệ
    print("\nTEST 7: Nhập liệu không phải là số")
    print("Nhập a = abc (hoặc bất kỳ ký tự không phải số nào)")
    print("Kết quả mong đợi: Lỗi: Vui lòng nhập các giá trị số hợp lệ cho a, b, c.")
