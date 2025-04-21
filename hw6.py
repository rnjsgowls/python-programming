def display():
  for j in range(1,10):
    for i in range(2,6):
      print(f"{i} X {j} = {i*j:2d}",end="   ")
    print("")
  print()
  for j in range(1,10):
    for i in range(6,10):
      print(f"{i} X {j} = {j*i:2d}",end="   ")
    print("")
  print()

display()
input()
