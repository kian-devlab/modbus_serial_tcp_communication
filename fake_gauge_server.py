import logging
from pymodbus.server import StartSerialServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext

# 1. Dynamically find the right context class
try:
    from pymodbus.datastore import ModbusDeviceContext as ContextClass
except ImportError:
    from pymodbus.datastore import ModbusSlaveContext as ContextClass

logging.basicConfig(level=logging.DEBUG)


def     run_fake_gauge():
    # hr stands for Holding Registers
    # store = ContextClass(hr=ModbusSequentialDataBlock(0, [5000, 20, 25]))
    # Make the memory array 10 slots long so we don't get out-of-bounds errors
    store = ContextClass(hr=ModbusSequentialDataBlock(0, [5000, 20, 25, 0, 0, 0, 0, 0, 0, 0]))
    # 2. The Brute Force Parameter Attack
    # We will try every single keyword the library has ever used until one works.
    context = None
    possible_parameters = [
        {'slaves': {1: store}, 'single': False},  # Oldest versions
        {'device_ids': {1: store}, 'single': False},  # Middle versions
        {'devices': {1: store}, 'single': False},  # Newest versions
    ]

    for params in possible_parameters:
        try:
            context = ModbusServerContext(**params)
            break  # If it works, break out of the loop!
        except TypeError:
            continue  # If it fails, try the next one

    if context is None:
        raise RuntimeError("Failed to start! Could not figure out the ModbusServerContext parameters.")

    print("🟢 Fake Tank Gauge starting...")
    print("Listening for Master requests (Baudrate: 9600)...")

    # 3. Start the RS485 Serial Server
    StartSerialServer(
        context=context,
        port='/dev/pts/2',  # <--- Make sure this matches Terminal 1!
        framer="rtu",
        baudrate=9600,
        timeout=1
    )


if __name__ == "__main__":
    run_fake_gauge()