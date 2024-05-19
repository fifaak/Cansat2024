from time import sleep
from sx127x.LoRa import LoRa
from sx127x.board_config import BOARD

# Raspberry Pi SPI pins
BOARD.setup()

# LoRa parameters
frequency = 915.0  # Change this to match your frequency
tx_power = 17  # dBm
spreading_factor = 7
coding_rate = 5
bandwidth = 125000

# Initialize LoRa
lora = LoRa(frequency, tx_power, spreading_factor, coding_rate, bandwidth)

# Initialize LoRa in receive mode
lora.set_mode_rx()

try:
    while True:
        if lora.received_packet():
            packet = lora.read_payload()
            print("Received:", packet.decode('utf-8'))
            # You can add your processing code here

        sleep(1)

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")
    lora.set_mode_sleep()
