class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def multi(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 == 0:
            return "Error: Division by zero!"
        return self.num1 / self.num2

    def exponential(self):
        return self.num1 ** self.num2

    def modulus(self):
        if self.num2 == 0:
            return "Error: Modulus by zero!"
        return self.num1 % self.num2

    def floor_div(self):
        if self.num2 == 0:
            return "Error: Floor division by zero!"
        return self.num1 // self.num2

# Main program loop
while True:
    try:
        # Display menu and get choice
        choice = int(input('''Choose an option:
1. Sum
2. Subtract
3. Multiply
4. Divide
5. Exponential
6. Modulus
7. Floor Division
8. Quit
What would you like to perform? '''))

        # Exit condition
        if choice == 8:
            print("Okay, as you wish... Exiting.")
            break

        # Check if user wants to proceed with the operation
        print(f"You selected: {['Sum', 'Subtract', 'Multiply', 'Divide', 'Exponential', 'Modulus', 'Floor Division'][choice-1]}")
        ans = input("Proceed? (Yes/No): ").lower()
        if ans not in ['yes', 'y']:
            print("Okay, enjoy your day!")
            continue

        # Get input values
        x = int(input("Enter the first value: "))
        y = int(input("Enter the second value: "))
        ob = Calculator(x, y)

        # Perform the selected operation
        if choice == 1:
            print(f"Sum: {ob.sum()}")
        elif choice == 2:
            print(f"Subtract: {ob.sub()}")
        elif choice == 3:
            print(f"Multiply: {ob.multi()}")
        elif choice == 4:
            print(f"Divide: {ob.div()}")
        elif choice == 5:
            print(f"Exponential: {ob.exponential()}")
        elif choice == 6:
            print(f"Modulus: {ob.modulus()}")
        elif choice == 7:
            print(f"Floor Division: {ob.floor_div()}")
        else:
            print("Invalid entry!")

    except ValueError:
        print("Please enter a valid number!")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
