def process_children_data(n, m, children_data):
    filtered_children = [
        child.split()
        for child in children_data
        if int(child.split()[2]) >= m
    ]
    
    filtered_children.sort(key=lambda x: x[0])
    
    result = []
    seen_gifts_in_city = {}
    
    for child in filtered_children:
        name, city, score, gift = child
        key = f"{city}_{gift}"
        
        if key not in seen_gifts_in_city:
            result.append((name, city, gift))
            seen_gifts_in_city[key] = (int(score), name)
        elif int(score) > seen_gifts_in_city[key][0]:
            index = next(i for i, item in enumerate(result) if item[1] == city and item[2] == gift)
            result[index] = (name, city, gift)
            seen_gifts_in_city[key] = (int(score), name)
    
    if not result:
        print("No one deserves presents this year!")
    else:
        for name, city, gift in result:
            print(name, city, gift)

n = int(input())
m = int(input())
children_data = [input() for _ in range(n)]

process_children_data(n, m, children_data)