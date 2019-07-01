def func1():
    a = 10
    b = 20
    print("func1() 에서 a값 %d" % a)
    print("func1() 에서 b값 %d" % b)

def func2():
    print("func1() 에서 a값 %d" % a)
    print("func1() 에서 b값 %d" % b)
def telcheck(aaa):
    rst = False
    print(aaa)
    if len(aaa) == 11 :
        return True

if __name__ == "__main__" :
    result = False

    tel1 = "010-4088-0"
    tel2 = "010-4088-0116"

    tel1 = tel1.replace('-','')
    tel2 = tel2.replace('-','')

    result = telcheck(tel2)

    if result == True :
        print("핸드폰 전화번호 형식에 맞음")
    else:
        print("핸드폰 전화번호 형식에 맞지 않음")
