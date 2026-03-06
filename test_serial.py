import serial
import time

# 1. Open the virtual ports created by socat (update these to match your socat output)
port_A = '/dev/pts/2'  # The Sender
port_B = '/dev/pts/3'  # The Receiver


# Define them first so the 'finally' block doesn't crash if the try block fails
sender = None
receiver = None

try:
    # Set up the connections
    sender = serial.Serial(port_A, baudrate=9600, timeout=1)
    receiver = serial.Serial(port_B, baudrate=9600, timeout=1)

    # 2. Prepare a message (Must be converted to bytes!)
    message_string = "Hello Hardware!"
    message_bytes = message_string.encode('utf-8')  # Converts text to raw bytes

    print(f"Sending: {message_bytes}")

    # 3. Send the bytes out of Port A
    sender.write(message_bytes)

    # Give it a tiny fraction of a second to travel across the "wire"
    time.sleep(0.1)

    # 4. Read the bytes coming into Port B
    # in_waiting tells us how many bytes are sitting in the receiver's buffer
    bytes_to_read = receiver.in_waiting

    if bytes_to_read > 0:
        received_bytes = receiver.read(bytes_to_read)
        print(received_bytes.hex())
        print(f"Received (Raw Bytes): {received_bytes}")
        print(f"Received (Decoded Text): {received_bytes.decode('utf-8')}")
    else:
        print("Nothing received.")

finally:
    if sender is not None:
        sender.close()
    if receiver is not None:
        receiver.close()