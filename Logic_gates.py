#Github accont : shantiarashidy


import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

clear_screen()
print_with_color("Welcome to the logic gates program for Logic circuits with Dr. Ranjkeshan", "36")  
print_with_color("written by Shantia Rashidy\n\n\n\n", "36")  

choice = int(input("Enter 1 if you want to continue: "))

if choice == 1:
    def AND(a, b):
        if a == 1 and b == 1:
            return True
        else:
            return False

    def NAND(a, b):
        if a == 1 and b == 1:
            return False
        else:
            return True

    def OR(a, b):
        if a == 1 or b == 1:
            return True
        else:
            return False

    def XOR(a, b):
        if a != b:
            return True
        else:
            return False

    def NOT(a):
        return not a

    def NOR(a, b):
        if a == 0 and b == 0:
            return True
        else:
            return False

    def XNOR(a, b):
        if a == b:
            return True
        else:
            return False

    def print_truth_table(gate_func, gate_name):
        clear_screen()
        if gate_name in ["AND", "NAND", "OR", "XOR", "NOR", "XNOR"]:
            print(f"+---------------+----------------+")
            print(f" | {gate_name} Truth Table | Result |")
            print(f" A = False, B = False | A {gate_name} B =", gate_func(False, False), " | ")
            print(f" A = False, B = True  | A {gate_name} B =", gate_func(False, True), " | ")
            print(f" A = True, B = False  | A {gate_name} B =", gate_func(True, False), " | ")
            print(f" A = True, B = True   | A {gate_name} B =", gate_func(True, True), " | ")
        elif gate_name == "NOT":
            print(f"+---------------+----------------+")
            print(f" | NOT Truth Table | Result |")
            print(f" A = False | A NOT =", gate_func(False), " | ")
            print(f" A = True  | A NOT =", gate_func(True), " | ")

    def menu():
        while True:
            print("\nLogic Gate Menu:")
            print("1. AND")
            print("2. NAND")
            print("3. OR")
            print("4. XOR")
            print("5. NOT")
            print("6. NOR")
            print("7. XNOR")
            print("8. Exit")
            
            choice = input("Choose a logic gate (1-8): ")
            
            if choice == '1':
                print_truth_table(AND, "AND")
            elif choice == '2':
                print_truth_table(NAND, "NAND")
            elif choice == '3':
                print_truth_table(OR, "OR")
            elif choice == '4':
                print_truth_table(XOR, "XOR")
            elif choice == '5':
                print_truth_table(NOT, "NOT")
            elif choice == '6':
                print_truth_table(NOR, "NOR")
            elif choice == '7':
                print_truth_table(XNOR, "XNOR")
            elif choice == '8':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please select a valid option.")
    
    menu()
else:
    print("Exiting the program.")
