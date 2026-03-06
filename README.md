# intelligent_level_gauge
A bulletproof Python implementation and simulation guide for Modbus RTU (Serial RS485) and Modbus TCP (Wi-Fi/LAN) communication. Built to integrate industrial hardware (like Intelligent Level Gauges) into modern software backends.

# Modbus Master-Slave Integration (Serial RTU & TCP)

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![pymodbus](https://img.shields.io/badge/pymodbus-supported-brightgreen.svg)

This repository contains a robust Python implementation for reading data from industrial hardware using the Modbus protocol. It serves as a "Hardware API" bridge, fetching physical data (e.g., Oil Level, Water Level, Temperature) from an Intelligent Level Gauge and bringing it into the software world.



## 🌟 Features

* **Dual Transport Layer Support:** Seamlessly switch between **Modbus RTU** (Serial over RS485/USB) and **Modbus TCP** (Wireless/Ethernet).
* **Indestructible PyModbus Wrapper:** The `pymodbus` library frequently changes its API (`slave` vs. `device_id` vs. `unit`). This code includes a nested fallback mechanism to guarantee execution across all major versions of the library.
* **Software-Only Simulation:** Includes configurations and scripts to completely simulate physical hardware on your local machine using Virtual COM ports and localhost networking.

## 🛠️ Prerequisites

To run the Python client:
```bash
pip install pymodbus

Gemini said
Here is a complete, professional GitHub Repository Description and README.md file based on everything we built and debugged today.

It is structured to perfectly explain the project to other web developers who might be new to hardware integration.

GitHub Repository Description (For the "About" section)
A bulletproof Python implementation and simulation guide for Modbus RTU (Serial RS485) and Modbus TCP (Wi-Fi/LAN) communication. Built to integrate industrial hardware (like Intelligent Level Gauges) into modern software backends.

README.md
Markdown
# Modbus Master-Slave Integration (Serial RTU & TCP)

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![pymodbus](https://img.shields.io/badge/pymodbus-supported-brightgreen.svg)

This repository contains a robust Python implementation for reading data from industrial hardware using the Modbus protocol. It serves as a "Hardware API" bridge, fetching physical data (e.g., Oil Level, Water Level, Temperature) from an Intelligent Level Gauge and bringing it into the software world.



## 🌟 Features

* **Dual Transport Layer Support:** Seamlessly switch between **Modbus RTU** (Serial over RS485/USB) and **Modbus TCP** (Wireless/Ethernet).
* **Indestructible PyModbus Wrapper:** The `pymodbus` library frequently changes its API (`slave` vs. `device_id` vs. `unit`). This code includes a nested fallback mechanism to guarantee execution across all major versions of the library.
* **Software-Only Simulation:** Includes configurations and scripts to completely simulate physical hardware on your local machine using Virtual COM ports and localhost networking.

## 🛠️ Prerequisites

To run the Python client:
```bash
pip install pymodbus
Simulation Tools (For testing without physical hardware)
If you do not have the physical RS485 hardware yet, you can simulate the Level Gauge using the following GUI tools:

Windows:

Master/Client Simulator: QModMaster

Slave/Server Simulator: pyModSlave or Modbus Slave

Virtual COM Ports: com0com (For RTU testing)

Linux:

Virtual COM Ports: socat (e.g., socat -d -d pty,raw,echo=0 pty,raw,echo=0)

🚀 Quick Start
1. Modbus RTU (Serial / RS485)
Used when connecting to the hardware via a USB-to-RS485 adapter cable.

Ensure your port matches your OS designation (e.g., /dev/ttyUSB0 for Linux or COM3 for Windows) and matches the baud rate of the manufacturer's Register Map.

from pymodbus.client import ModbusSerialClient

client = ModbusSerialClient(
    port='/dev/ttyUSB0', 
    baudrate=9600,
    framer="rtu",
    timeout=2
)
# Run the client to fetch Holding Registers

2. Modbus TCP (Network / Wi-Fi)
Used when the gauge is connected to the local network or Wi-Fi router.

from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(
    host='0.0.0.0', your ip address server
    port=5020,
    framer="socket",
    timeout=3
)
# Run the client to fetch Holding Registers

Gemini said
Here is a complete, professional GitHub Repository Description and README.md file based on everything we built and debugged today.

It is structured to perfectly explain the project to other web developers who might be new to hardware integration.

GitHub Repository Description (For the "About" section)
A bulletproof Python implementation and simulation guide for Modbus RTU (Serial RS485) and Modbus TCP (Wi-Fi/LAN) communication. Built to integrate industrial hardware (like Intelligent Level Gauges) into modern software backends.

README.md
Markdown
# Modbus Master-Slave Integration (Serial RTU & TCP)

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![pymodbus](https://img.shields.io/badge/pymodbus-supported-brightgreen.svg)

This repository contains a robust Python implementation for reading data from industrial hardware using the Modbus protocol. It serves as a "Hardware API" bridge, fetching physical data (e.g., Oil Level, Water Level, Temperature) from an Intelligent Level Gauge and bringing it into the software world.



## 🌟 Features

* **Dual Transport Layer Support:** Seamlessly switch between **Modbus RTU** (Serial over RS485/USB) and **Modbus TCP** (Wireless/Ethernet).
* **Indestructible PyModbus Wrapper:** The `pymodbus` library frequently changes its API (`slave` vs. `device_id` vs. `unit`). This code includes a nested fallback mechanism to guarantee execution across all major versions of the library.
* **Software-Only Simulation:** Includes configurations and scripts to completely simulate physical hardware on your local machine using Virtual COM ports and localhost networking.

## 🛠️ Prerequisites

To run the Python client:
```bash
pip install pymodbus
Simulation Tools (For testing without physical hardware)
If you do not have the physical RS485 hardware yet, you can simulate the Level Gauge using the following GUI tools:

Windows:

Master/Client Simulator: QModMaster

Slave/Server Simulator: pyModSlave or Modbus Slave

Virtual COM Ports: com0com (For RTU testing)

Linux:

Virtual COM Ports: socat (e.g., socat -d -d pty,raw,echo=0 pty,raw,echo=0)

🚀 Quick Start
1. Modbus RTU (Serial / RS485)
Used when connecting to the hardware via a USB-to-RS485 adapter cable.

Ensure your port matches your OS designation (e.g., /dev/ttyUSB0 for Linux or COM3 for Windows) and matches the baud rate of the manufacturer's Register Map.

Python
from pymodbus.client import ModbusSerialClient

client = ModbusSerialClient(
    port='/dev/ttyUSB0', 
    baudrate=9600,
    framer="rtu",
    timeout=2
)
# Run the client to fetch Holding Registers
2. Modbus TCP (Network / Wi-Fi)
Used when the gauge is connected to the local network or Wi-Fi router.

Python
from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(
    host='192.168.1.15', 
    port=5020,
    framer="socket",
    timeout=3
)
# Run the client to fetch Holding Registers
🧠 The Modbus "Gotchas" (Troubleshooting)
If you are testing this and hitting errors, check these 3 common industrial automation traps:

The "Off-By-One" Quirk (Illegal Data Address): Different software packages start counting at 0, while others start at 1. If your script requests Address 0 and gets an Illegal Data Address error, change your request to Address 1.

The Localhost Trap (Connection Refused): If you are testing Modbus TCP between two computers, ensure your Server Simulator (pyModSlave) is bound to 0.0.0.0 or your actual IPv4 address (e.g., 192.168.x.x). If it is bound to 127.0.0.1, it will block incoming Wi-Fi requests.

Windows Defender Firewall (Connection Timed Out): Windows aggressively blocks custom TCP ports (like 502 or 5020). You must create an Inbound Rule in Windows Defender Firewall to allow traffic through your specific port before the Python script can connect.

Framer Mismatches:
If the TCP connection connects but immediately drops without sending data, ensure the client is using framer="socket" and the server is strictly set to TCP (not RTU over TCP).

📄 Interpreting the Data
Hardware registers do not return labeled JSON. They return raw 16-bit integers. You must obtain the Modbus Register Map from your hardware manufacturer to decode the array.

Example:

Index 0 (Address 0) = Oil Level

Index 1 (Address 1) = Water Level

Index 2 (Address 2) = Temperature

(Note: Always check the manufacturer's manual for scaling factors, such as dividing the temperature by 10).