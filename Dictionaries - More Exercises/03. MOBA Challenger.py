player_info = {}
data = input()
fight_flag = False
both_skill = None
while not data =="Season end":
    if '->' in data:
        player, position,skill  = data.split(" ->")
        skill = int(skill)
        if not player in player_info:
            player_info[player]  = {position:skill}
        elif not position in player_info[player]:
            player_info[player][position] = skill
        else:
            if player_info[player][position] < skill:
                player_info[player][position] = skill

    if 'vs' in data:
        player1,player2 = data.split(' vs ')
        if player1 in player_info and player2 in player_info:
            for skill in player_info[player1].keys():
                if skill in player_info[player2].keys():
                    fight_flag = True
                    both_skill = skill
                    break
            if fight_flag:
                if player_info[player1][both_skill] < player_info[player2][both_skill]:
                    del player_info[player1]
                elif player_info[player1][both_skill] > player_info[player2][both_skill]:
                    del player_info[player2]
    data = input()

pos = 1
for player,info in sorted(player_info.items(), key = lambda kvp: (-sum(kvp[1].values()),kvp[0])):
    print(f"{player}: {sum(player_info[player].values())} skill")
    for skill,points in sorted(info.items(),key = lambda kvp: (-kvp[1],kvp[0])):
        print(f"-{skill} <::> {points}")
