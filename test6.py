
# *을 1부터 5까지 출력하세요.

a = ""

for k in range(0, 5):
    a += "*"
    print(a)
    k += 1

for i in range(0,4):
    for j in range(4-i):
        print("*",end="")
    print()



