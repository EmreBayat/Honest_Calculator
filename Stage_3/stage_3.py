msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

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
        if x =='M':
            x = memory
        elif y == 'M':
            y = memory
        else:
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
        
    continuing = True
    while continuing:
        print(msg_4)
        answer = input()
        if answer == 'y':
            memory = result
            print(msg_5)
            answer2 = input()
            if answer2 == 'y':
                running = True
            elif answer2 == 'n':
                running = False
            else:
                continue
        elif answer == 'n':
            print(msg_5)
            answer2 = input()
            if answer2 == 'y':
                running = True
            elif answer2 == 'n':
                running = False
            else:
                continue
        else:
            continue
        continuing = False
    if running == True:
        continue
    else:
        pass
    running = False