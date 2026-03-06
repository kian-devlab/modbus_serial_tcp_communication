# RTU, Wired connection
# from pymodbus.client import ModbusSerialClient
#
#
# def run_client():
#     # 1. Setup the Physical Layer (Connecting to the wire)
#     client = ModbusSerialClient(
#         port='/dev/pts/3',  # Make sure this matches your socat output
#         baudrate=9600,
#         framer="rtu",
#         timeout=2
#     )
#
#     print("🟡 Master attempting to connect to RS485 line...")
#     if client.connect():
#         print("🟢 Connected to serial port!\n")
#
#         # 2. The Application Layer (Speaking Modbus)
#         print("Sending Modbus PDU Request...")
#
#         # Handling the PyModbus API version differences
#         try:
#             # Older Pymodbus 3.x
#             response = client.read_holding_registers(address=0, count=3, slave=1)
#         except TypeError:
#             try:
#                 # Newest Pymodbus (3.11+) replaced 'slave' with 'device_id' or 'slave_id'
#                 response = client.read_holding_registers(address=0, count=3, device_id=1)
#             except TypeError:
#                 try:
#                     response = client.read_holding_registers(address=0, count=3, slave_id=1)
#                 except TypeError:
#                     # Very old Pymodbus (< 3.0)
#                     response = client.read_holding_registers(address=0, count=3, unit=1)
#
#         # 3. Parse the Reply
#         if not response.isError():
#             oil = response.registers[0]
#             water = response.registers[1]
#             temp = response.registers[2]
#
#             print("✅ Data successfully decoded from Slave:")
#             print(f"🛢️  Oil Level:   {oil} Liters")
#             print(f"💧 Water Level: {water} Liters")
#             print(f"🌡️  Temperature: {temp} °C")
#         else:
#             print(f"❌ Device returned a Modbus Exception (Error): {response}")
#
#         client.close()
#     else:
#         print("❌ Failed to open serial port.")
#
#
# if __name__ == "__main__":
#     run_client()


# TCP/IP wireless
from pymodbus.client import ModbusTcpClient


def run_wireless_client():
    # 1. Setup the Network Layer (Connecting over Wi-Fi)
    client = ModbusTcpClient(
        host='192.168.170.120',
        port=5020,
        framer="socket",
        timeout=3
    )

    print("📡 Master attempting to connect over Wi-Fi...")
    if client.connect():
        print("🟢 Connected to network device!\n")

        print("Sending Modbus TCP Request...")

        # 2. Handling the PyModbus API version differences (The Fix!)
        try:
            # Older Pymodbus 3.x
            response = client.read_holding_registers(address=0, count=3, slave=1)
        except TypeError:
            try:
                # Newest Pymodbus (3.11+) replaced 'slave' with 'device_id' or 'slave_id'
                response = client.read_holding_registers(address=0, count=3, device_id=1)
            except TypeError:
                try:
                    response = client.read_holding_registers(address=0, count=3, slave_id=1)
                except TypeError:
                    # Very old Pymodbus (< 3.0)
                    response = client.read_holding_registers(address=0, count=3, unit=1)

        # 3. Parse the Reply
        if not response.isError():
            oil = response.registers[0]
            water = response.registers[1]
            temp = response.registers[2]

            print("✅ Data successfully decoded over Wi-Fi:")
            print(f"🛢️  Oil Level:   {oil} Liters")
            print(f"💧 Water Level: {water} Liters")
            print(f"🌡️  Temperature: {temp} °C")
        else:
            print(f"❌ Device returned an Error: {response}")

        client.close()
    else:
        print("❌ Failed to connect to IP address. Check your Wi-Fi or Firewalls!")


if __name__ == "__main__":
    run_wireless_client()