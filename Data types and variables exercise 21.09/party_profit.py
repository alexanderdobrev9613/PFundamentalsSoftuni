companions = int(input())
days = int(input())
coins = 0
for current_day in range(1, days + 1): #zashoto trqbva da trugnem ot edno za da sledim na koi den sme
    if current_day % 10 == 0:
        companions -= 2
    if current_day % 15 == 0:
        companions += 5
    if current_day % 3 == 0:
        coins -= companions * 3
    if current_day % 5 == 0:
        coins += companions * 20
        if current_day % 3 == 0:
            coins -= companions * 2
    coins += 50
    coins -= companions * 2
print(f'{companions} companions received {coins // companions} coins each.')