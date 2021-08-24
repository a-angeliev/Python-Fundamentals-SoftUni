piece_numbers = int(input())
pi = {}
for _ in range(piece_numbers):
    piece,compos,key = input().split("|")
    if not piece in pi:
        pi[piece] = {"composer": compos,"key":key}


data = input().split("|")
while not data[0] == "Stop":
    if data[0] ==  "Add":
        piece = data[1]
        compos = data[2]
        key = data[3]
        if not piece in pi:
            pi[piece] = {"composer": compos,"key":key}
            print(f"{piece} by {compos} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    if data[0] == "Remove":
        piece = data[1]
        if piece in pi:
            del pi[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    if data[0] == "ChangeKey":
        piece = data[1]
        new_key = data[2]
        if piece in pi:
            pi[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input().split("|")

for piece,info in sorted(pi.items(),key = lambda kvp: (kvp[0],kvp[1]["composer"])):
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")