def calculate_energy_and_cities(names):
    total_energy = 0
    even_cities = 0
    odd_cities = 0
    
    for city_name in names:
        length = len(city_name)
        if length % 2 == 0:
            energy_cost = length * 2
            even_cities += 1
        else:
            energy_cost = length * 3
            odd_cities += 1
            
        total_energy += energy_cost
    
    return total_energy, even_cities, odd_cities


n = int(input())
names = [input() for _ in range(n)]

energy, even, odd = calculate_energy_and_cities(names)

print(f'Total energy: {energy}')
print(f'Even cities: {even}')
print(f'Odd cities: {odd}')