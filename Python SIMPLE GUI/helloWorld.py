# helloWorld.py

import PySimpleGUI as sg

# Create the window
# window = sg.Window("Demo", layout)

window = sg.Window(
  title="Hello World",
  layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]],
  margins=(100, 50)
)

# Create an event loop
while True:

  event, values = window.read()
  
  # End program if user closes window or presses the OK button
  if event == "OK" or event == sg.WIN_CLOSED:
    break

window.close()