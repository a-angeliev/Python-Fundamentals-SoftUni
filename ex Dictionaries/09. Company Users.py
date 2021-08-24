command_line = input().split(" -> ")
company_info = {}
while not command_line[0] == "End":
    company, id = command_line
    if company in company_info.keys():
        if not id in company_info[company]:
            company_info[company].append(id)
    else:
        company_info[company] = []
        company_info[company].append(id)

    command_line = input().split(" -> ")

for company,ids in sorted(company_info.items(), key = lambda kvp:kvp):
    print(f"{company}")
    for id in ids:
        print(f"-- {id}")