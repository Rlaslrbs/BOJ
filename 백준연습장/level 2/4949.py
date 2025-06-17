
while True:
    stack = []
    string = input()
    if string != ".": #정상
        for i in string:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(']')
                    break
            elif i == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
                    break

    else:
        break
    if len(stack) == 0:
        print("yes")
    else:
        print("no") 


#([]()) - yes
#[]() - yes
#)( - no
#][ - no
# ) - yes([ (([( [ ] ) ( ) (( ))] )) ]