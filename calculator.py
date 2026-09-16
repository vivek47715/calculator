def subcalculator(choice,a,b):
  if choice==1:
    return a+b
  elif choice==2:
    return a-b
  elif choice==3:
    return a*b
  elif choice==4:
    return a/b
  else:
    print("enter valid choice")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=int(input("enter your choice:"))
a=int(input("enter first number:"))
b=int(input("enter second number:"))
res=subcalculator(choice,a,b)
print(res)
repeat=input("enter 'y' to cotinue or enter 'n' to exit:")
repeat=repeat.lower()
def calculator():
  global res,repeat
  while(repeat=="y"):
    choice=int(input("enter your choice:"))
    a=res
    b=int(input("enter number to do operation with result:"))
    res=subcalculator(choice,a,b)
    print(res)
    repeat=input("enter 'y' to cotinue or enter 'n' to exit:")
    repeat=repeat.lower()
calculator()
