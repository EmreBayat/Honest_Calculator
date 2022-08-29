msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

valid_operations = ["+", "-", "/", "*"]
running = True
memory = 0
# Stage 1/5
while running:
    print(msg_0)
    user_input = input()
    x, operation, y = user_input.split()

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if not (operation == '+' or operation == '-' or operation == '*' or operation == '/'):
        print(msg_2)
        continue

    if operation == '+':
        result = x + y
        print(result)
    elif operation == '-':
        result = x - y
        print(result)    
    elif operation == '*':
        result = x * y
        print(result)        
    elif operation == '/' and y!=0:
        result = x / y
        print(result)        
    else :
        print(msg_3)
        continue        
    running = False