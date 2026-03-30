def kiem_tra_chia_het():
    """
    Chương trình nhập một số nguyên dương và kiểm tra xem số đó 
    có chia hết cho 2, cho 3, hoặc cả hai hay không.
    """
    so = 0 # Khởi tạo biến để lưu số nguyên dương
    
    # Vòng lặp để đảm bảo người dùng nhập đúng một số nguyên dương
    while True:
        try:
            # Nhập số từ người dùng
            so_str = input("Vui lòng nhập một số nguyên dương: ")
            so = int(so_str) # Chuyển đổi chuỗi nhập vào thành số nguyên
            
            # Kiểm tra xem số có phải là số dương hay không
            if so <= 0:
                print("Lỗi: Vui lòng nhập một số nguyên dương (lớn hơn 0).")
            else:
                # Nếu số hợp lệ, thoát khỏi vòng lặp
                break 
        except ValueError:
            # Xử lý trường hợp người dùng nhập không phải là số nguyên
            print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

    print(f"\nKiểm tra số {so}:")

    # Kiểm tra điều kiện chia hết
    chia_het_cho_2 = (so % 2 == 0) # True nếu số chia hết cho 2, ngược lại False
    chia_het_cho_3 = (so % 3 == 0) # True nếu số chia hết cho 3, ngược lại False

    # Logic kiểm tra và in ra kết quả
    if chia_het_cho_2 and chia_het_cho_3:
        # Trường hợp chia hết cho cả 2 và 3
        print(f"Số {so} chia hết cho CẢ 2 và 3.")
    elif chia_het_cho_2:
        # Trường hợp chỉ chia hết cho 2 (không chia hết cho 3)
        print(f"Số {so} chia hết cho 2 nhưng KHÔNG chia hết cho 3.")
    elif chia_het_cho_3:
        # Trường hợp chỉ chia hết cho 3 (không chia hết cho 2)
        print(f"Số {so} chia hết cho 3 nhưng KHÔNG chia hết cho 2.")
    else:
        # Trường hợp không chia hết cho cả 2 và 3
        print(f"Số {so} KHÔNG chia hết cho 2 và cũng KHÔNG chia hết cho 3.")

# Khối lệnh chính để chạy chương trình
if __name__ == "__main__":
    # Gọi hàm để bắt đầu chương trình kiểm tra chia hết
    kiem_tra_chia_het()

    print("\n" + "="*40)
    print("--- VÍ DỤ KIỂM TRA TỰ ĐỘNG ---")
    print("="*40)

    # Hàm trợ giúp để chạy các ví dụ test mà không cần nhập thủ công
    def chay_vi_du(num):
        print(f"\nKiểm tra số: {num}")
        # Kiểm tra điều kiện chia hết tương tự như trong hàm chính
        chia_het_cho_2 = (num % 2 == 0)
        chia_het_cho_3 = (num % 3 == 0)

        if chia_het_cho_2 and chia_het_cho_3:
            print(f"-> Số {num} chia hết cho CẢ 2 và 3.")
        elif chia_het_cho_2:
            print(f"-> Số {num} chia hết cho 2 nhưng KHÔNG chia hết cho 3.")
        elif chia_het_cho_3:
            print(f"-> Số {num} chia hết cho 3 nhưng KHÔNG chia hết cho 2.")
        else:
            print(f"-> Số {num} KHÔNG chia hết cho 2 và cũng KHÔNG chia hết cho 3.")

    # Các trường hợp kiểm thử
    print("\n--- Test case 1: Chia hết cho cả 2 và 3 ---")
    chay_vi_du(6)   # Kết quả: Chia hết cho CẢ 2 và 3
    chay_vi_du(12)  # Kết quả: Chia hết cho CẢ 2 và 3
    chay_vi_du(18)  # Kết quả: Chia hết cho CẢ 2 và 3

    print("\n--- Test case 2: Chỉ chia hết cho 2 ---")
    chay_vi_du(2)   # Kết quả: Chia hết cho 2 nhưng KHÔNG chia hết cho 3
    chay_vi_du(4)   # Kết quả: Chia hết cho 2 nhưng KHÔNG chia hết cho 3
    chay_vi_du(10)  # Kết quả: Chia hết cho 2 nhưng KHÔNG chia hết cho 3

    print("\n--- Test case 3: Chỉ chia hết cho 3 ---")
    chay_vi_du(3)   # Kết quả: Chia hết cho 3 nhưng KHÔNG chia hết cho 2
    chay_vi_du(9)   # Kết quả: Chia hết cho 3 nhưng KHÔNG chia hết cho 2
    chay_vi_du(15)  # Kết quả: Chia hết cho 3 nhưng KHÔNG chia hết cho 2

    print("\n--- Test case 4: Không chia hết cho cả 2 và 3 ---")
    chay_vi_du(1)   # Kết quả: KHÔNG chia hết cho 2 và cũng KHÔNG chia hết cho 3
    chay_vi_du(5)   # Kết quả: KHÔNG chia hết cho 2 và cũng KHÔNG chia hết cho 3
    chay_vi_du(7)   # Kết quả: KHÔNG chia hết cho 2 và cũng KHÔNG chia hết cho 3
    chay_vi_du(11)  # Kết quả: KHÔNG chia hết cho 2 và cũng KHÔNG chia hết cho 3

    print("\n" + "="*40)
    print("--- KẾT THÚC CHƯƠNG TRÌNH ---")
    print("="*40)