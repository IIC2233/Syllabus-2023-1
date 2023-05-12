import random

def generate_user(prefix):
    num = random.randrange(0, 1000000)
    return f'{prefix}{num:06}'

def generate_transaction():
    num = random.randint(0, 100)
    return f'{num}{00}'


if __name__ == '__main__':
    users = {generate_user(21) for _ in range (40)}
    users = users.union({generate_user(20) for _ in range (20)})
    users = users.union({generate_user(19) for _ in range (20)})
    users = users.union({generate_user(18) for _ in range (10)})
    users = list(users.union({generate_user(22) for _ in range (10)}))

    print(len(users))
    with open('usuarios.txt', 'w') as file:
        for user in users:
            print(user)
            file.write(f'{user}\n')

    transactions = [generate_transaction() for _ in range(200)]
    with open('transacciones.txt', 'w') as file:
        for t in transactions:
            start = random.choice(users)
            end = random.choice(users)
            while start == end:
                end = random.choice(users)
            print(f'{start} {t:03} {end}')
            file.write(f'{start} {t} {end}\n')
