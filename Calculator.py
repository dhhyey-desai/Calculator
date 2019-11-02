import re
print("Our Magical Calculator")
print("Type 'quit' to exit\n")
previous = 0
run=True
def performMath():
    global run
    global previous
    equation = input("Enter equation:")
    if equation == 'quit':
        print("Goodbye,human.")
        run = False
    else:
        previous = eval(equation)
        print("You answer", previous)
while run:
    performMath()