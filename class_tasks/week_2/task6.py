# Task 1
favorite_fruits = (input('Enter your first favorite fruit: '), input('Enter your second favorite fruit: '), input('Enter your third favorite fruit: '), input('Enter your fourth favorite fruit: '), input('Enter your fifth favorite fruit: '))
print(favorite_fruits)


#unique names collector 
#collect the names one by one
print("Enter your full name: ")
i= tuple(range(1,100000))
attendance = set()
for x in i:
    user_input = input(f"Enter your full name: ").lower()
    if user_input in attendance:
        print("input is existing")
    attendance.add(user_input)
    print(sorted(attendance))
        