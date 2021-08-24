def register(registred_users:dict , username:str , license:str):
    if not username in registred_users.keys():
        registred_users[username] = license
        print(f"{username} registered {license} successfully")
    else:
        print(f"ERROR: already registered with plate number {license}")

def unregister(registred_users:dict, username:str):
    if not username in registred_users.keys():
        print(f"ERROR: user {username} not found")
    else:
        registred_users.pop(username)
        print(f"{username} unregistered successfully")

regustred_users ={}
number_of_lines = int(input())
for _ in range(number_of_lines):
    command = input().split()
    if command[0] == 'register':
        register(regustred_users, command[1],command[2])
    elif command[0] == 'unregister':
        unregister(regustred_users,command[1])

for username, license in regustred_users.items():
    print(f"{username} => {license}")