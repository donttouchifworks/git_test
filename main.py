def calculate(text_input):
    if text_input[1] == "+":
        return int(text_input[0])+int(text_input[-1])
calculation = input("What do you want to calculate?")
answer = calculate(calculation)
print(f"The result is {answer}")

# TODO 1. **Add welcome message to calculator.**
# TODO 2. **Add empty lines after the calculate function definition.**
# TODO 3. **Create main function and put code in it**
# TODO 4. **Add a dunder main**
# TODO 5. **Add functionality for subtraction**
# TODO 6. **Add functionality for multiplication**
# TODO 7. **Add functionality for division**
# TODO 8. **Add functionality to ask user to do multiple calculations**
# TODO 9. **Improve the README.md file and add project description**