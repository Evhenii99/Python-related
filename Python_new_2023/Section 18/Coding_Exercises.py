import PySimpleGUI as sg
from converters import convert

sg.theme("Black")

text1 = sg.Text("Enter feet: ")
input1 = sg.Input(key='feets')

text2 = sg.Text("Enter inches: ")
input2 = sg.Input(key='inches')

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output = sg.Text('', key='output')

window = sg.Window("Convertor",
                   layout=[[text1, input1],
                           [text2, input2],
                           [convert_button, exit_button, output]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    try:
        feet = float(values['feets'])
        inches = float(values['inches'])
        meters = convert(feet, inches)
        window['output'].update(value=f'{meters} m')
    except ValueError:
        sg.popup("Please provide two numbers.", font=("Helvetica", 20))

window.close()

