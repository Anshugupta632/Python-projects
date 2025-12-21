HISTORY_FILE = "calculation_history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()  
    if len(lines) == 0:
        print("No calculation history found.")
    else:
        for lines in lines:
            print(lines.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("Calculation history cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(f"{equation} = {result}\n")
    file.close()

def calculation(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Error: Invalid format. Use: number1 operator number2")
        return
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2
    else:
        print("Error: Unsupported operator. Use +, -, *, or /.")
        return
    
    if int(result) == result:
        result = int(result)

    print(f"{user_input} = {result}")
    save_to_history(user_input, result)

def main():
    print("Welcome to the Calculator with History!")
    while True:
        user_input = input("Enter calculation (or 'history', 'clear', 'exit'): ").strip().lower()
        
        if user_input == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculation(user_input)
main()