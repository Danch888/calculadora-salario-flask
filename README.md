# Calculadora de Salário Líquido com Flask

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Jinja2](https://img.shields.io/badge/Template-Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Aplicação web desenvolvida com o microframework **Flask (Python)** para cálculo de salário líquido com base em regras simplificadas da legislação trabalhista (CLT). O projeto demonstra a captura e sanitização de dados de formulário, validação defensiva no backend e renderização de respostas dinâmicas.

> 📸 **Prints e Demonstrações**: Todas as capturas de tela dos testes funcionais, validação de regras de negócio e execução no terminal estão organizadas na pasta [`prints/`](./prints) deste repositório.

---

## 🎯 Contexto e Objetivos

Projeto desenvolvido no curso de **Análise e Desenvolvimento de Sistemas (ADS)**, com foco em:
- Arquitetura de aplicações web interativas com o microframework Flask.
- Validação estrita de dados no servidor (*Backend Validation*), prevenindo manipulação maliciosa de parâmetros.
- Implementação de regras de negócio financeiras e tratamento de exceções com `try/except`.
- Configuração e isolamento de dependências com ambiente virtual Python (`venv`).

---

## 💼 Regras de Negócio e Fórmula de Cálculo

A aplicação calcula o salário líquido a partir do salário bruto e da quantidade de dependentes informados:

| Rubrica | Regra Aplicada | Alíquota / Valor |
| :--- | :--- | :--- |
| **INSS** | Desconto obrigatório sobre o salário bruto | **8,0%** fixo |
| **IRRF** | Isenção para salários até R$ 2.500,00 | **0,0%** (Isento) |
| **IRRF** | Para salários superiores a R$ 2.500,00 | **15,0%** sobre o salário bruto |
| **Bônus Dependentes** | Acréscimo por dependente informado | **+ R$ 200,00** por dependente |

$$\text{Salário Líquido} = \text{Salário Bruto} - \text{INSS} - \text{IRRF} + (\text{Dependentes} \times 200{,}00)$$

---

## 🧪 Casos de Testes Documentados

A aplicação foi submetida a uma bateria de testes cobrindo fluxos felizes e cenários de exceção:

| Cenário de Teste | Salário Bruto | Dependentes | Resultado Esperado / Obtido |
| :--- | :---: | :---: | :--- |
| **Teste 1** | R$ 3.000,00 | 2 | `Salário líquido: R$ 2710.00` |
| **Teste 2** | R$ 2.000,00 | 0 | `Salário líquido: R$ 1840.00` |
| **Teste 3** | R$ 2.500,00 | 1 | `Salário líquido: R$ 2500.00` |
| **Teste 4** | R$ 4.000,00 | 3 | `Salário líquido: R$ 3680.00` |
| **Teste 5 (Entrada Inválida)** | `abc` | 2 | `Erro: Insira valores válidos para salário e dependentes.` |
| **Teste 6 (Valor Negativo)** | R$ 2.500,00 | -1 | `Erro: Salário e número de dependentes devem ser maiores ou iguais a zero.` |

---

## 📂 Estrutura do Repositório

```
calculadora-salario-flask/
├── templates/
│   └── form.html              # Interface do formulário HTML
├── prints/                    # Capturas de tela de execução e testes
├── app.py                     # Rotas Flask ('/' e '/resultado') e lógica de cálculo
├── requirements.txt           # Dependências do projeto (Flask>=3.0.0)
├── .gitignore                 # Ignora venv/, __pycache__/ e temporários
├── LICENSE
└── README.md
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- **Python 3.8+** instalado.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Danch888/calculadora-salario-flask.git
   cd calculadora-salario-flask
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   # No Windows (PowerShell):
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # No Linux / macOS:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor Flask:**
   ```bash
   python app.py
   ```
   *Ou utilizando a CLI do Flask:*
   ```bash
   flask run
   ```

5. **Acesse no navegador:**
   ```
   http://127.0.0.1:5000
   ```

---

## 📸 Demonstração e Testes

As capturas de tela da aplicação e dos testes estão na pasta [`prints/`](./prints). Exemplos:

| Formulário de Entrada | Resultado do Cálculo |
| :---: | :---: |
| ![Formulário de Entrada](prints/7%20-%20Testando%20Valores%20-%20Teste%201.png) | ![Resultado do Cálculo](prints/8%20-%20Testando%20Valores%20-%20Resultado%201.png) |

---

## 👤 Autor

Desenvolvido por **Daniel Lima**  
Estudante de Análise e Desenvolvimento de Sistemas (ADS).

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)](https://github.com/Danch888)
