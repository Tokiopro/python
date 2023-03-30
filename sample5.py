# try:
#     int_a = int(input('整数a:'))
#     int_b = int(input('整数b:'))
#     print(int_a ** 2)
#     print((int_a ** 2) / int_b)
# except(ValueError) as v:
#     print(type(v))
#     print('C')
# except(ZeroDivisionError) :
#     print('D')
# except:
#     print('E')
# else:
#     print('F')
# finally:
#     print('G')
    
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
    print(user)
    print(status)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
    print(user)
    print(status)
    
