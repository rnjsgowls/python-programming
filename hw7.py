shopping_bag={}

while True:
  item=input("상품명? ")

  if item=="":
    shopping_bag[""]=0
    del shopping_bag[""]
    print()
    print(f">>> 장바구니 보기: {shopping_bag}")
    break

  else:
    num=int(input("수량은? "))
    print(f"장바구니에 {item} {num}개가 담겼습니다.\n")
    shopping_bag[item]=num

print("\n[검색]")
find=input("장바구니에서 확인하고자 하는 상품은? ")
print(f"{find}은(는) {shopping_bag[find]}개 담겨 있습니다.")
input()
