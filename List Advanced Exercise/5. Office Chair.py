rooms = int(input())
free_chairs = 0
game_on = True
for room in range(1, rooms+1):
    chairs, ppl = input().split()
    if len(chairs) < int(ppl):
        print(f"{int(ppl) - len(chairs)} more chairs needed in room {room}")
        game_on = False
    else:
        free_chairs += (len(chairs) - int(ppl))

if game_on:
    print(f"Game On, {free_chairs} free chairs left")