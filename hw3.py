def get_fixed_price(cost):
    global disc
    cost=cost*(100/(100-disc))
    return cost

disc=float(input("할인률은?"))
a=float(input("A 상품의 할인된 가격은?"))
b=float(input("B 상품의 할인된 가격은?"))


print("A 상품의 정가는",get_fixed_price(a),"원")
print("B 상품의 정가는",get_fixed_price(b),"원")
input()
