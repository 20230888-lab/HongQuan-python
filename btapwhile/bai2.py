n = int(input("Nhập n: "))

i = 1
giai_thua = 1

while i <= n:
    giai_thua *= i
    i += 1

print("Giai thừa của", n, "là:", giai_thua)
