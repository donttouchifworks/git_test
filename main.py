

def calculate(text_input):
    if text_input[1] == "+":
        return int(text_input[0])+int(text_input[-1])

def main():
    print("Welcome to the calculator")
    calculation = input("What do you want to calculate?")
    answer = calculate(calculation)
    print(f"The result is {answer}")

if __name__ == "__main__":
    main()
