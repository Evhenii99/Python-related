import PySimpleGUI as sg

text1 = sg.Text("Enter feet: ")
input1 = sg.Input()

text2 = sg.Text("Enter inches: ")
input2 = sg.Input()

convert = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[text1, input1],
                           [text2, input2],
                           [convert]])

window.read()
window.close()
