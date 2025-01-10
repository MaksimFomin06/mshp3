def count_lights(garlands):
    on_count = 0
    off_count = 0
    miss_count = 0
    
    for garland in garlands:
        on_count += garland.count('o')
        off_count += garland.count('x')
        miss_count += garland.count('-')
        
    return on_count, off_count, miss_count


n = int(input())
garlands = [input() for _ in range(n)]

on, off, miss = count_lights(garlands)

print(f'On: {on}')
print(f'Off: {off}')
print(f'Miss: {miss}')