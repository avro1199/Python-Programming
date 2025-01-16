def main():
    #task 01
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    print(f"{x} + {y} = {x + y}")

    #task 02
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # print(f"\nYour name is, {first_name} {last_name}!")
    print("\nYour name is, ", first_name + " " + last_name)

if __name__ == "__main__":
    main()