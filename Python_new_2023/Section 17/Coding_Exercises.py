import PySimpleGUI as sg
from converters import convert

text1 = sg.Text("Enter feet: ")
input1 = sg.Input(key='feets')

text2 = sg.Text("Enter inches: ")
input2 = sg.Input(key='inches')

convert_button = sg.Button("Convert")
output = sg.Text('', key='output')

window = sg.Window("Convertor",
                   layout=[[text1, input1],
                           [text2, input2],
                           [convert_button, output]])

while True:
    event, values = window.read()
    feet = float(values['feets'])
    inches = float(values['inches'])

    meters = convert(feet, inches)
    window['output'].update(value=f'{meters} m')


window.close()

# import PySimpleGUI as sg
#
#
# def km_to_miles(km):
#     return km / 1.6
#
#
# label = sg.Text("Kilometers: ")
# input_box = sg.InputText(tooltip="Enter todo", key="kms")
# miles_button = sg.Button("Convert")
#
# output = sg.Text(key="output")
#
# window = sg.Window('Km to Miles Converter',
#                    layout=[[label, input_box], [miles_button, output]],
#                    font=('Helvetica', 20))
#
# while True:
#     event, values = window.read()
#     match event:
#         case "Convert":
#             km = float(values["kms"])
#             result = km_to_miles(km)
#             window['output'].update(value=result)
#         case sg.WIN_CLOSED:
#             break
#
# window.close()