num=int(input("세 자리 정수 입력: "))

def read_single_digit(n):
  if n==1:
    print("일",end=" ")
  elif n==2:
    print("이",end=" ")
  elif n==3:
    print("삼",end=" ")
  elif n==4:
    print("사",end=" ")
  elif n==5:
    print("오",end=" ")
  elif n==6:
    print("육",end=" ")
  elif n==7:
    print("칠",end=" ")
  elif n==8:
    print("팔",end=" ")
  elif n==9:
    print("구",end=" ")
  else:
    print("영",end=" ")

def read_number(num):
  a=num//100
  b=(num-100*a)//10
  c=num-100*a-10*b
  read_single_digit(a)
  read_single_digit(b)
  read_single_digit(c)

read_number(num)
input()
