def check_reindeer(n, m, t, h):
    total_work_hours = n * t
    
    max_total_hours = m * h
    
    if total_work_hours <= max_total_hours:
        print("All is good!")
    else:
        additional_hours_needed = total_work_hours - max_total_hours
        
        additional_reindeer_needed = (additional_hours_needed + h - 1) // h
        
        print(f"Need {additional_reindeer_needed} more reindeer!")

n = int(input())
m = int(input())
t = int(input())
h = int(input())

check_reindeer(n, m, t, h)