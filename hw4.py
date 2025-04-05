def draw_line_string(nstr,msg1):
  print("-"*(nstr+2))
  print(f" Hello {name},\n Welcome to Seoul.")
  print("-"*(nstr+2))

name=input("Input his/her name:")
msg1="Hello "+name+","
msg2="Welcome to Seoul."
nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
draw_line_string(nstr,msg1)
input()
