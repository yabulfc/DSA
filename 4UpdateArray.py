def update(num , index):  # a function that take a number  and update/replace it to a given index

        numbers = [0, 1, 2, 3, 4]

        print('The Element at index', index , 'is: ' , numbers[index])
        numbers[index] = num

        for num in numbers:
                print(num)

update(100 , 2)  
#updated