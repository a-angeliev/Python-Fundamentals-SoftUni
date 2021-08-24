countrys = input().split(", ")
capitals = input().split(", ")
country_dict = dict(zip(countrys,capitals))
for kay, value in country_dict.items():
    print(f"{kay} -> {value}")