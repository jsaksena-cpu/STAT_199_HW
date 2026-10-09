import math

Dorm_x = 0
Dorm_y = 0
Dining_Hall_x = 120
Dining_Hall_y = 160
Shields_x = 360
Shields_y = 60

leg_1 = math.sqrt((Dining_Hall_x - Dorm_x) ** 2 + (Dining_Hall_y - Dorm_y) ** 2)
leg_2 = math.sqrt((Shields_x - Dining_Hall_x) ** 2 + (Shields_y - Dining_Hall_y) ** 2)
total_walked = leg_1 + leg_2

direct = math.sqrt((Shields_x - Dorm_x) ** 2 + (Shields_y - Dorm_y) ** 2)
detour = total_walked - direct

print(f"Dorm to dining hall: {leg_1} meters")
print(f"Dining hall to Shields: {leg_2} meters")
print(f"Total walked: {total_walked} meters")
print(f"Straight from dorm to Shields: {direct} meters")
print(f"The stop at the dining hall costs you {detour} extra meters.")