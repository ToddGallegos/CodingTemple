# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods

# mystring = ''
# for index, object in enumerate(my_foods):
#     mystring += object + " "
# print(mystring)


my_list = [1, 2, 0.5, ['a', 'b', ['A', 'B', 'C'], "c"], "John"]

for member in my_list:
    if isinstance(member, list):
        for m in member:
            if isinstance(m, list):
                print(m, end="*")