from calculator import division, multiplication, sum, subtracion
from textwrap import dedent

if __name__ == "__main__":

    number1: float = 0
    number2: float = 0
    
    # option_selected = 1
    while True:
        # print(
        #     '----------MENU----------\n'
        #     'options: \n'  
        #     '1 - Sum\n'
        #     '2 - subtraction\n'
        #     '3 - division\n'
        #     '4 - multiplication\n'
        #     '0 - Exit\n'
        # )

        print(dedent("""
                    ----------MENU----------
                    options:
                    1 - Sum
                    2 - subtraction
                    3 - division
                    4 - multiplication
                    0 - Exit
        """
        ))

        while True:
            try:
                option_selected = int(input('Select an option: '))

                if option_selected <= 0 or option_selected > 4:
                    break

                number1 = float(input('\nInsert the first number: '))
                number2 = float(input('Insert the second number: '))
                break
            except:
                print("Insert only numeric")

        if option_selected <= 0 or option_selected > 4:
            exit(0)

        elif option_selected == 1:
            print('\n----------SUM----------')
            result = sum(number1, number2)
            print(f'{number1} + {number2} = {result: .2f}')

        elif option_selected == 2:
            print('\n----------Subtraction----------')
            result = subtracion(number1, number2)
            print(f'{number1} - {number2} = {result: .2f}')

        elif option_selected == 3:
            print('\n----------Division----------')
            result = division(number1, number2)
            print(f'{number1} / {number2} = {result: .2f}')

        elif option_selected == 4:
            print('\n----------Multiplication----------')
            result = multiplication(number1, number2)
            print(f'{number1} * {number2} = {result: .2f}')
