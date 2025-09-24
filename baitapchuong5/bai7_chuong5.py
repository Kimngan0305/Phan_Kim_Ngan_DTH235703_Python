# Câu 7: Tối ưu chuỗi danh từ

s = input("Nhập vào chuỗi: ")

# Xóa khoảng trắng dư thừa và chuẩn hóa viết hoa
s_opt = " ".join(s.split()).title()

print("Chuỗi tối ưu:", s_opt)
