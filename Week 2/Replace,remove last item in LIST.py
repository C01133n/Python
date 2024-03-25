hat_list = [1, 2, 3, 4, 5]  

hat_list[int(len(hat_list)/2)] = int(input("Enter an integer number to replace the middle number in the list: "))


hat_list.pop()

print("Length of the list:", len(hat_list))

print(hat_list)