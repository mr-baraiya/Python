try : 
    n = int(input("Enter the Number : "))
    with open(f'table_{n}','w') as f:
        for i in range(1,11):
            f.write(f'{n} * {i} = {n*i}\n')
except Exception as e:
    print(e)

