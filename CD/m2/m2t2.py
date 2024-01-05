def expressionEvaluation():
    print("<--------HIGHLEVEL CODE-------->")
    print()
    print("(a<b or c<d ) and e>notf")
    print()

    print("<--------INTERMEDIATE CODE-------->")
    print()

    print('1.t0=a')
    print('2.if t0<b goto(4)')
    print('3.goto(7)')
    print('4.t1=not f')
    print('5.if e>t1 goto(10)')
    print('6.goto(10)')
    print('t2=c')
    print('if t2<d goto(10)')
    print('goto(10)')

def whileconditionEvaluation():
    print("<--------HIGHLEVEL CODE-------->")
    print()

    print("while (A< C(i) and B > D[i] ) {")
    print("if A==1 then")
    print("   C[i]++")
    print("else")
    print("while A<=D[i] do")
    print("D[i]=D[i]+C[i]")
    print("i++ }")
    

    print("<--------INTERMEDIATE CODE-------->")
    print()

    print("1.t0=4*i")
    print('2.t1=c[t0]')
    print('3.if A<t1 goto(5)')
    print('4.goto(27)')
    print('5.t2=4*i')
    print('6.t3=D[t2]')
    print('7.if B<t3 goto(9)')
    print('8.if A==1 goto(11)')
    print('9.if A==1 goto(11)')
    print('10.goto(15)')
    print('11.t4=4*i')
    print('12.t5=C[t4]')
    print('13.C[t4]=t5+1')
    print('14.goto(24)')
    print('15.t6=4*i')
    print('16.t7=D[t6]')
    print('17.if A<=t7 goto(19)')
    print('18.goto(24)')
    print('19.t8=4*i')
    print('20.t9=C[t8]')
    print('21.t10=t9+D[t8]')
    print('22.D[t8]=t10')
    print('23.goto(17)')
    print('24.t11=i')
    print('25.i=t11+1')
    print('26.goto(1)')
    print('27.')

def ifelseconditionEvaluation():
    print("<--------HIGHLEVEL CODE-------->")
    print()

    print('if [(a<b) and ((c>d) or (a>d))] then')
    print('z=x+y*z')
    print('else')
    print('z=z+1')
    print()

    print("<--------INTERMEDIATE CODE-------->")
    print()

    print('1.t0=a')
    print('t1=c')
    print('t2=z')
    print('if t1>d goto(6)')
    print('goto(12)')
    print('if t0<b goto(8)')
    print('goto(12)')
    print('t3=4*t2')
    print('t4=x+t3')
    print('z=t4')
    print('goto(14)')
    print('t3=t2+1')
    print('z=t3')
def simplecalculator():
    print("<--------HIGHLEVEL CODE-------->")
    print()
    
    print('int cal(int num1,int num2,int op)')
    print('{')
    print('int result;')
    print('switch(op)')
    print('{')
    print('case +:') 
    print('result = num1 + num2;')
    print('break;')
    print('case -: ')
    print('result = num1 - num2;')
    print('break;')
    print('case *: ')
    print('result = num1 * num2;')
    print('break;')
    print('case /: ')
    print('result = num1 / num2;')
    print('break;')
    print('default: ')
    print('printf(Invalid operator);')
    print('}')
    print('return result;')
    print('}')
def calculator():
    print("<--------INTERMEDIATE CODE-------->")
    print()
    
    print('t0=num1')
    print('t1=op')
    print('if t1==+ goto(7)')
    print('if t1==- goto(9)')
    print('if t1==* goto(11)')
    print('if t1==/ goto(13)')
    print('goto(15)')
    print('result=t0+b')
    print('goto(17)')
    print('result=t0-b')
    print('goto(17)')
    print('result=t0*b')
    print('goto(17)')
    print('result=t0/b')
    print('goto(17)')
    print('return invalid')
    print('goto(18)')
    print('return result')

def generate_three_address_code(cleaned_code):
    final_code = []
    current_temp = 1

    for codeline in cleaned_code:
        if '=' in codeline:  # Assignment statement
            parts = codeline.split("=")
            variable = parts[0].strip()
            expression = parts[1].strip()
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
        elif 'END' in codeline:  # End statement
            final_code.append("END")

    return final_code

def main():
    while True:
        print()
        print('1.expression evaluation purpose')
        print('2.while condition Evaluation purpose')
        print('3.ifelse condition Evaluation purpose')
        print('4.High level code for simple calculator')
        print('5.Intermediate code for simple calculator in method -1')
        print('6.Intermediate code for simple calculator in method -2')
        print()
        
        choice = input("Enter your choice: ")

        if choice == "1":
            expressionEvaluation()
        elif choice == "2":
            whileconditionEvaluation()
        elif choice=='3':
            ifelseconditionEvaluation()
        elif choice=='4':
            simplecalculator()
        elif choice=='5':
            calculator()
        elif choice =='6':
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

            cleaned_code = []
            for line in code:
                cleaned_code.append(line.strip())
            final_code = generate_three_address_code(cleaned_code)

            print('\nThree Address Code:')
            for i in range(len(final_code)):
                print('{}: {}'.format(i + 1, final_code[i]))
        else:
            print("Invalid choice.")
            break

if __name__ == "__main__":
    main()
