data = [0,0,0]
for i in range(3):
    x = input()
    if x not in ['FizzBuzz','Fizz','Buzz']:
         data[i] = int(x)
    else:
        data[i] = x
count = 3
for i in data:
    if type(i) == int:
        result = count + i
        if result % 3 == 0 and result % 5 == 0:
            print('FizzBuzz')
        elif result % 3 == 0 and result % 5 !=0:
            print('Fizz')
        elif result % 3 != 0 and result % 5 == 0:
            print('Buzz')
        else:
            print(result)
        break
    else:
        count-=1