# Câu 5: Xử lý chuỗi với các hàm cơ bản

s = input("Nhập vào chuỗi: ")

# Khởi tạo biến đếm
hoa = thuong = so = dac_biet = khoang_trang = nguyen_am = phu_am = 0
nguyen_am_set = "aeiouAEIOU"

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    
    if ch.isdigit():
        so += 1
    elif ch.isspace():
        khoang_trang += 1
    elif not ch.isalnum() and not ch.isspace():
        dac_biet += 1

    if ch.isalpha():  # nếu là chữ
        if ch in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1

# Xuất kết quả
print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ là chữ số:", so)
print("Số ký tự đặc biệt:", dac_biet)
print("Số ký tự khoảng trắng:", khoang_trang)
print("Số nguyên âm:", nguyen_am)
print("Số phụ âm:", phu_am)
