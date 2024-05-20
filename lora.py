# from SX127x.LoRa import *
# from SX127x.board_config import BOARD

# # Constants for LoRa
# LORA_FREQUENCY = 915e6
# LORA_TX_POWER = 17
# LORA_SF = 7
# LORA_BW = 125e3
# LORA_CODING_RATE = LoRa.CODING_RATE_4_5

# class MyLoRa(LoRa):
#     def __init__(self, verbose=False):
#         super(MyLoRa, self).__init__(verbose)
#         self.set_mode(MODE.SLEEP)
#         self.tx_counter = 0

#     def on_tx_done(self):
#         self.set_mode(MODE.SLEEP)
#         super(MyLoRa, self).on_tx_done()
#         print("Transmission done!")

#     def setup(self):
#         BOARD.setup()
#         self.set_pa_config(pa_select=1)
#         self.set_frequency(LORA_FREQUENCY)
#         self.set_tx_power(LORA_TX_POWER)
#         self.set_spreading_factor(LORA_SF)
#         self.set_bw(LORA_BW)
#         self.set_coding_rate(LORA_CODING_RATE)
#         self.set_mode(MODE.STDBY)

#     def send_data(self, data):
#         self.write_payload([ord(char) for char in data])
#         self.set_mode(MODE.TX)

# if __name__ == "__main__":
#     lora = MyLoRa(verbose=True)
#     lora.setup()
    
#     lora.send_data(data)

