# TinyPrinterController
Controlling a HP officejet Printer via Raspberry Pi and Arduino

Arduino sketch currently running on ATtiny45, with python script executed on Raspberry Pi.

ATtiny is wired to internal printer contacts. One pin is connected to the printer's power LED anode contact, while the other is connected to one end of the power switch. This side of the switch is held at 3V, and is pulled to ground on button press. To simulate a button press, the pin can be pulled to ground from the ATtiny.

The Raspberry Pi is connected to the ATtiny via two GPIO pins. The first is to signal the current printer state (high for on, low for off), while the other is used to signal a request to toggle the printer state. The ATtiny constantly reads the level of this line, and simulates a button press whenever it is high. To avoid double presses, it can only issue a button press every 1000 ms.
