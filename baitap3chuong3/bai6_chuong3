def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 10:
        return don_vi[n].capitalize()
    else:
        hang_chuc = n // 10
        hang_dv = n % 10
        if hang_dv == 0:
            return chuc[hang_chuc].capitalize()
        else:
            return (chuc[hang_chuc] + " " + don_vi[hang_dv]).capitalize()

# Test
n = int(input("Nhập số n (tối đa 2 chữ số): "))
print("Cách đọc:", doc_so(n))
