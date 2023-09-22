import PySimpleGUI as sg

def compute_bmi(mass: float, height: float):
    try:
        mass = float(mass)
        height = float(height)
        bmi = mass / (height ** 2)
        return bmi
    except ValueError:
        return None

def categorize_bmi(bmi: float):
    if bmi is None:
        return "Valores inválidos"
    elif bmi < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= bmi < 24.9:
        return "Peso normal"
    elif 24.9 <= bmi < 29.9:
        return "Sobrepeso"
    elif 29.9 <= bmi < 34.9:
        return "Obesidade Grau I"
    elif 34.9 <= bmi < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

sg.theme('LightGrey1')

layout = [
    [sg.Text('Calculadora de IMC', font=('Helvetica', 16))],
    [sg.Text('Peso (kg):'), sg.InputText(key='peso')],
    [sg.Text('Altura (m):'), sg.InputText(key='altura')],
    [sg.Button('Calcular'), sg.Button('Sair')],
    [sg.Text('', size=(30, 1), key='resultado')],
]

window = sg.Window('Calculadora de IMC', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Calcular':
        mass = values['peso']
        height = values['altura']
        bmi = compute_bmi(mass, height)
        category = categorize_bmi(bmi)
        text_result = f'IMC: {bmi:.2f} - {category}'
        window['resultado'].update(text_result)

window.close()
