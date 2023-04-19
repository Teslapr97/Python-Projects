#Python Project # 9: OPC Communication Test with Codesys and GUI Python
#Made by Joshua Ian Carrera-Sanchez

#Importing libraries
from opcua import Client
import tkinter

# Connect to the OPC UA server
client = Client("opc.tcp://localhost:4840")
client.connect()

# Read a variable
var_start = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.START")
var_stop = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.STOP")
var_light = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.LIGHT")
value = var_start.get_value()
value2 = var_stop.get_value()
value3 = var_light.get_value()

# Write a variable
#var_start.set_value(False)
#value = var_start.get_value()
#print("Value of START:", value)

#var_stop.set_value(False)
#value2 = var_stop.get_value()
#print("Value of STOP:", value)
# Disconnect from the OPC UA server
#client.disconnect()

#Define a function to activate the start button:
def start_button_on(event):
    var_start.set_value(True)

#Define a function to deactivate the start button:
def start_button_off(event):
    var_start.set_value(False)

#Define a function to activate the stop button:
def stop_button_on(event):
    var_stop.set_value(True)

#Define a function to deactivate the stop button:
def stop_button_off(event):
    var_stop.set_value(False)



#Creating a HMI/GUI Screen
m = tkinter.Tk()

#Widgets are added here
start_button = tkinter.Button(m, text='START', width=10, height=5)
start_button.bind("<ButtonPress-1>", start_button_on)
start_button.bind("<ButtonRelease-1>", start_button_off)
start_button.pack(side="left")

stop_button = tkinter.Button(m, text='STOP', width=10, height=5)
stop_button.bind("<ButtonPress-1>", stop_button_on)
stop_button.bind("<ButtonRelease-1>", stop_button_off)
stop_button.pack(side="right")

m.mainloop()
