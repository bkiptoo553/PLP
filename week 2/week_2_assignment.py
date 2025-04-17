def Assignment_week_2():
    # 1. create an empty list
    my_list = [] 
    print(my_list)
    
    #Append the following elements to my_list: 10, 20, 30, 40.
    my_list.append( 20)
    my_list.append( 10)
    my_list.append( 30)
    my_list.append( 40)
    print(my_list)

    #Insert the value 15 at the second position in the list.
    my_list.insert(1, 15)
    print(my_list)

    #Extend my_list with another list: [50, 60, 70].
    SecondList = [50, 60, 70]
    my_list.extend(SecondList)
    print(my_list)

    #Remove the last element from my_list.
    my_list.pop()
    print(my_list)

    #Sort my_list in ascending order.
    my_list.sort()
    print(my_list)

    #Find and print the index of the value 30 in my_list.
    for i in range(len(my_list)):
        if my_list[i] == 30:
            print(i)

Assignment_week_2()