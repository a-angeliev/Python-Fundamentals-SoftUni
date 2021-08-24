A = [1,2,3,4,5,6,7,8,9,10,11]
B = [1,2,3,4,5,6,7,8,9,10,11]
cards = input().split()

is_terminated = False

for card in range(len(cards)):
    card_info = cards[card].split('-')
    team = card_info[0]
    player = int(card_info[1])
    if team == 'B' and player in B:
        B.remove(player)
    elif team =='A' and player in A:
        A.remove(player)
    if len(A)<7 or len(B)<7:
        is_terminated = True
        break
print(f"Team A - {len(A)}; Team B - {len(B)}")
if is_terminated:
    print("Game was terminated")

