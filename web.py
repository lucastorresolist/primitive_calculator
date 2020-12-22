from flask import Flask
import calculator


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '''
            <h1>Calculator</h1>
            <h3>Options</h3>
            <ol>
                <li>
                    <a href="/sum">Sum</a>
                </li>
                <li>
                    <a href="/subtraction">Subtracion</a>
                </li>
                <li>
                    <a href="/division">Division</a>
                </li>
                <li>
                    <a href="/multiplication">Multiplication</a>
                </li>
            </ol>
        '''

    @app.route('/sum')
    def cal_sum():
        number_1 = 3.0
        number_2 = 7.0

        result = calculator.sum(number_1, number_2)
        return f'''
            <h1>SUM</h1>
            <br>
            <p>The result of the sum {number_1} + {number_2} = {result}</p>

            <a href="/">Back</a>
        '''
    
    @app.route('/subtraction')
    def cal_subtracion():
        number_1 = 3.0
        number_2 = 7.0

        result = calculator.subtracion(number_1, number_2)
        return f'''
            <h1>Subtraction</h1>
            <br>
            <p>The result of the subtraction {number_1} - {number_2} = {result}</p>
            <a href="/">Back</a>
        '''

    @app.route('/division')
    def cal_division():
        number_1 = 3.0
        number_2 = 7.0

        result = calculator.division(number_1, number_2)
        return f'''
            <h1>Division</h1>
            <br>
            <p>The result of the division {number_1} / {number_2} = {result}</p>
            <a href="/">Back</a>
        '''

    @app.route('/multiplication')
    def cal_multiplication():
        number_1 = 3.0
        number_2 = 7.0

        result = calculator.multiplication(number_1, number_2)
        return f'''
            <h1>Multiplication</h1>
            <br>
            <p>The result of the multiplication {number_1} * {number_2} = {result}</p>
            <a href="/">Back</a>
        '''
    app.run()
