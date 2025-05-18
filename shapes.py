def print_star_shape():
    print("Choose a shape to print with stars:")
    print("1. Triangle")
    print("2. Square")
    print("3. Pyramid")
    
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        height = int(input("Enter the height of the triangle: "))
        for i in range(1, height + 1):
            print('*' * i)

    elif choice == '2':
        size = int(input("Enter the size of the square: "))
        for i in range(size):
            print('*' * size)

    elif choice == '3':
        height = int(input("Enter the height of the pyramid: "))
        for i in range(1, height + 1):
            spaces = ' ' * (height - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print_star_shape()
