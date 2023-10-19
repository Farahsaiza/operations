print('exercice3')
A= int(input('enter the first number '))
B= int(input('enter the second number '))
OP=input("type the necessary operator")
if OP == "+":
    print("thesum is:  ", A+B)
elif OP== "-":
    print("the difference is: ",A-B)
elif OP== "*":
    print("the product is: ", A*B)
elif OP== "/":
    print("the division is: " , A/B)
elif OP== "%":
    print("the modulo is:  ", A%B)
else:
    print("error! please enter another operator")