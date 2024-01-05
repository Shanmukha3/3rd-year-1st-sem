def generate_intermediate(cleaned_code):
    final_code = []
    current_temp = 1

    for codeline in cleaned_code:
        if '=' in codeline:  # Assignment statement
            variable, expression = map(str.strip, codeline.split("="))
            temp_var = f"temp{current_temp}"
            final_code.append(f"{temp_var} = {expression}")
            final_code.append(f"{variable} = {temp_var}")
            current_temp += 1
        elif 'if' in codeline:  # If statement
            condition = codeline.split('if')[1].split('goto')[0].strip()
            goto_line = codeline.split('goto')[1].strip('()')
            final_code.append(f"if {condition} goto {goto_line}")
        elif 'goto' in codeline:  # Goto statement
            goto_line = codeline.split('goto')[1].strip('()')
            final_code.append(f"goto {goto_line}")
        elif 'print' in codeline:  # Print statement
            value = codeline.split('print')[1].strip('()')
            final_code.append(f"print({value})")
        elif 'input' in codeline:  # Input statement
            variable, prompt = map(str.strip, codeline.split('='))
            final_code.append(f"{variable} = input({prompt})")
        elif 'return' in codeline:  # Return statement
            value = codeline.split('return')[1].strip()
            final_code.append(f"return {value}")
        elif 'END' in codeline:  # End statement
            final_code.append("END")

    return final_code

# Example code
code = [
    "def add(x, y):",
    "    return x + y",
    "",
    "def subtract(x, y):",
    "    return x - y",
    "",
    "def multiply(x, y):",
    "    return x * y",
    "",
    "def divide(x, y):",
    "    if y != 0:",
    "        return x / y",
    "    else:",
    "        return 'Error: Division by zero'",
    "",
    "# Input reading and function invocation",
    "operation = input('Enter operation (+, -, *, /): ')",
    "num1 = float(input('Enter first number: '))",
    "num2 = float(input('Enter second number: '))",
    "",
    "result = 0",
    "",
    "if operation == '+':",
    "    result = add(num1, num2)",
    "elif operation == '-':",
    "    result = subtract(num1, num2)",
    "elif operation == '*':",
    "    result = multiply(num1, num2)",
    "elif operation == '/':",
    "    result = divide(num1, num2)",
    "else:",
    "    print('Invalid operation')",
    "",
    "# Output the result",
    "print(f'Result: {result}')",
]

cleaned_code = [line.strip() for line in code]
final_code = generate_intermediate(cleaned_code)

print('\nIntermediate code is:')
for i, line in enumerate(final_code, 1):
    print(f'{i}: {line}')
