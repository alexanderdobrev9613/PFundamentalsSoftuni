employee1_capacity = int(input())
employee2_capacity = int(input())
employee3_capacity = int(input())
students_count = int(input())
students_assisted = 0
time = 0

while students_count > students_assisted:
    students_assisted += employee3_capacity + employee2_capacity + employee1_capacity
    time += 1
    if time % 4 == 0:
        time += 1

print(f'Time needed: {time}h.')


