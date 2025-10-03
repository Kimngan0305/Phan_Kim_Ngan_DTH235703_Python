# Hàm tính tổng ước số của n (không kể n)
def tong_uoc(n):
    tong = 1  # luôn có 1 là ước
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            tong += i
    return tong if n != 1 else 0  # trường hợp n=1 thì không có ước

# Kiểm tra số hoàn thiện
def la_so_hoan_thien(n):
    return tong_uoc(n) == n

# Kiểm tra số thịnh vượng
def la_so_thinh_vuong(n):
    return tong_uoc(n) > n

# ============================
# Thử nghiệm
ds = [6, 12, 28, 15, 18, 20]

for x in ds:
    if la_so_hoan_thien(x):
        print(f"{x} là số hoàn thiện")
    elif la_so_thinh_vuong(x):
        print(f"{x} là số thịnh vượng")
    else:
        print(f"{x} là số thiếu (deficient)")
