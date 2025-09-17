total_inches = int(input("Please enter total inches: "))
inches_per_foot = 12
feet_per_mile = 5280
inches_per_mile = 12 * 5280

miles = total_inches / inches_per_mile
total_inches = total_inches % inches_per_mile

feet = total_inches / inches_per_foot
inches = total_inches % inches_per_foot


print(f'{miles} miles')