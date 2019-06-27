# 전역변수
year1 = 0

# 메인코드
if __name__ == "__main__":
    year1 = int(input("연도를 입력: "))

    if((year1 % 4 == 0) and (year1 % 100 !=0)) or (year1 % 400 == 0) :
        print("%d년은 윤년입니다." %year1)
    else:
        print("%d년은 윤년이 아닙니다."%year1)
