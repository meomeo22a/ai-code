def find_integer(data_list):
    """
    Tìm và trả về số nguyên đầu tiên trong một danh sách (hoặc iterable) cho trước.

    Hàm này kiểm tra từng phần tử trong `data_list`. Nếu tìm thấy một phần tử
    có kiểu là `int` (bao gồm cả `bool` vì True và False là các thể hiện của int
    trong Python), nó sẽ trả về phần tử đó ngay lập tức.

    Tham số:
        data_list (iterable): Một danh sách, tuple, hoặc bất kỳ đối tượng iterable nào
                              có thể chứa các loại dữ liệu khác nhau.

    Trả về:
        int hoặc None: Số nguyên đầu tiên được tìm thấy trong data_list.
                       Trả về None nếu không tìm thấy số nguyên nào (kể cả True/False).
    """
    for item in data_list:
        # Kiểm tra xem phần tử hiện tại có phải là một số nguyên hay không.
        # isinstance() là cách tốt nhất để kiểm tra kiểu dữ liệu trong Python.
        # Lưu ý: isinstance(True, int) trả về True, isinstance(False, int) trả về True.
        if isinstance(item, int):
            return item  # Trả về số nguyên đầu tiên tìm thấy
    
    # Nếu vòng lặp kết thúc mà không tìm thấy số nguyên nào, trả về None
    return None

# --- Ví dụ Test ---
print("--- Ví dụ Test (Phiên bản tiêu chuẩn: True/False là int) ---")

# 1. Danh sách có số nguyên ở đầu
list1 = [10, "hello", 3.14, None]
print(f"Danh sách: {list1} -> Số nguyên đầu tiên: {find_integer(list1)}") # Expected: 10

# 2. Danh sách có số nguyên ở giữa
list2 = ["apple", False, 42, "banana"]
print(f"Danh sách: {list2} -> Số nguyên đầu tiên: {find_integer(list2)}") # Expected: False (vì False là int, được tìm thấy trước 42)

# 3. Danh sách có số nguyên ở cuối
list3 = [None, 2.5, "world", -7]
print(f"Danh sách: {list3} -> Số nguyên đầu tiên: {find_integer(list3)}") # Expected: -7

# 4. Danh sách không có số nguyên
list4 = ["text", 9.99, None, "end"]
print(f"Danh sách: {list4} -> Số nguyên đầu tiên: {find_integer(list4)}") # Expected: None

# 5. Danh sách rỗng
list5 = []
print(f"Danh sách: {list5} -> Số nguyên đầu tiên: {find_integer(list5)}") # Expected: None

# 6. Danh sách chỉ chứa float
list6 = [1.0, 2.0, 3.0]
print(f"Danh sách: {list6} -> Số nguyên đầu tiên: {find_integer(list6)}") # Expected: None

# 7. Danh sách với boolean (boolean là một kiểu con của int trong Python)
list7 = ["test", True, 100, False]
print(f"Danh sách: {list7} -> Số nguyên đầu tiên: {find_integer(list7)}") # Expected: True

# 8. Danh sách với số 0
list8 = ["a", 0, 1.2]
print(f"Danh sách: {list8} -> Số nguyên đầu tiên: {find_integer(list8)}") # Expected: 0

# 9. Tuple
tuple1 = (30, "xyz", 5.0)
print(f"Tuple: {tuple1} -> Số nguyên đầu tiên: {find_integer(tuple1)}") # Expected: 30



def find_pure_integer(data_list):
    """
    Tìm và trả về số nguyên "thuần túy" (không phải boolean) đầu tiên
    trong một danh sách (hoặc iterable) cho trước.

    Hàm này kiểm tra từng phần tử trong `data_list`. Nếu tìm thấy một phần tử
    có kiểu là `int` VÀ KHÔNG PHẢI là `bool`, nó sẽ trả về phần tử đó ngay lập tức.

    Tham số:
        data_list (iterable): Một danh sách, tuple, hoặc bất kỳ đối tượng iterable nào
                              có thể chứa các loại dữ liệu khác nhau.

    Trả về:
        int hoặc None: Số nguyên "thuần túy" đầu tiên được tìm thấy trong data_list.
                       Trả về None nếu không tìm thấy số nguyên nào không phải boolean.
    """
    for item in data_list:
        # Kiểm tra xem phần tử hiện tại có phải là số nguyên VÀ không phải là boolean hay không.
        # Điều kiện 'not isinstance(item, bool)' giúp loại trừ True/False.
        if isinstance(item, int) and not isinstance(item, bool):
            return item  # Trả về số nguyên "thuần túy" đầu tiên tìm thấy
    
    # Nếu vòng lặp kết thúc mà không tìm thấy số nguyên "thuần túy" nào, trả về None
    return None

# --- Ví dụ Test (Loại trừ Boolean) ---
print("\n--- Ví dụ Test (Phiên bản loại trừ Boolean) ---")

# 1. Danh sách có số nguyên "thuần túy" ở đầu
list1_pure = [10, "hello", True, 3.14]
print(f"Danh sách: {list1_pure} -> Số nguyên đầu tiên (không bool): {find_pure_integer(list1_pure)}") # Expected: 10

# 2. Danh sách chỉ có boolean và các loại khác
list2_pure = ["apple", False, True, "banana"]
print(f"Danh sách: {list2_pure} -> Số nguyên đầu tiên (không bool): {find_pure_integer(list2_pure)}") # Expected: None

# 3. Danh sách có số nguyên "thuần túy" sau boolean
list3_pure = [None, True, 42, "world"]
print(f"Danh sách: {list3_pure} -> Số nguyên đầu tiên (không bool): {find_pure_integer(list3_pure)}") # Expected: 42

# 4. Danh sách rỗng
list4_pure = []
print(f"Danh sách: {list4_pure} -> Số nguyên đầu tiên (không bool): {find_pure_integer(list4_pure)}") # Expected: None

# 5. Danh sách với số 0
list5_pure = ["a", False, 0, 1.2]
print(f"Danh sách: {list5_pure} -> Số nguyên đầu tiên (không bool): {find_pure_integer(list5_pure)}") # Expected: 0