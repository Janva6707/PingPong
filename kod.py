fruits = list()
ans = input('Name your favourite fruit (to stop programm enter: 0)')
while ans != '0':
    if ans in fruits:
        print('Fruit already added')
    else:
        fruits.append(ans)
    ans = input('Name your favourite fruit (to stop programm enter: 0)')
print('Thank u for ur favourite fruits! Here r them:',fruits)