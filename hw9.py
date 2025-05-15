#개념확인과제 (연습문제 11.3)

class point:
  def __init__(self,x=0,y=0):
    self.__x=x
    self.__y=y
  def show(self):
    print(f"({self.__x},{self.__y})")
  def set(self,x,y):
    self.__x=x
    self.__y=y
  def get(self):
    return (self.__x,self.__y)

class rectangle:
  def __init__(self,x1,y1,x2,y2):
    self.__lt=point(x1,y1)
    self.__rb=point(x2,y2)
  
  def show(self): #어떨 때 메소드 괄호에 뭐 넣는지 헷갈림
    print(f"좌측 상단 꼭짓점이 {self.__lt.get()}이고 우측 하단 꼭짓점이 {self.__rb.get()}인 사각형입니다.")
  def getwidth(self):
    width= self.__rb.get()[0]-self.__lt.get()[0]
    return width
  def getheight(self):
    height=self.__rb.get()[1]-self.__lt.get()[1] #어떨 때 self.__쓰고 어떨 때 그냥 쓰는지도
    return height
  def getarea(self):
    area=self.getwidth()*self.getheight()
    return area

  def getperimeter(self):
    perimeter=self.getwidth()*2+self.getheight()*2
    return perimeter

r1 = rectangle(5, 5, 20, 10)
a = r1.getarea()
p = r1.getperimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')

input()
