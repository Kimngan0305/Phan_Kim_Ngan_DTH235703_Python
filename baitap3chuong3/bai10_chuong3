x = int(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0  # tổng
for i in range(1, n+1):
    tu = x**i      # tử số: x^i
    mau = 1        # mẫu số: i!
    for j in range(1, i+1):
        mau *= j
    S += tu/mau    # cộng vào tổng

print("S({0},{1}) = {2}".format(x, n, S))

