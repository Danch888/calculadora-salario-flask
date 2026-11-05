from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        salario = float(request.form['salario'])
        dependentes = int(request.form['dependentes'])

        # Validação de valores negativos
        if salario < 0 or dependentes < 0:
            return "Erro: Salário e número de dependentes devem ser maiores ou iguais a zero."

        # Regras de Negócio
        inss = salario * 0.08

        if salario > 2500.00:
            ir = salario * 0.15
        else:
            ir = 0.0

        bonus_dependentes = dependentes * 200.00

        # Cálculo do Salário Líquido
        salario_liquido = salario - inss - ir + bonus_dependentes

        return f"Salário líquido: R$ {salario_liquido:.2f}"

    except ValueError:
        return "Erro: Insira valores válidos para salário e dependentes."

if __name__ == '__main__':
    app.run(debug=True)