import os

# Hàm lấy tên file kèm đuôi
def lay_ten_file(path):
    return os.path.basename(path)   # ví dụ: muabui.mp3

# Hàm lấy tên file không có đuôi
def lay_ten_bai_hat(path):
    return os.path.splitext(os.path.basename(path))[0]  # ví dụ: muabui


# --- Test thử ---
duong_dan = r"d:\music\muabui.mp3"
print("Tên file:", lay_ten_file(duong_dan))      # muabui.mp3
print("Tên bài hát:", lay_ten_bai_hat(duong_dan)) # muabui
