from py532lib.i2c import Pn532_i2c
from py532lib.mifare import *

class Scan_Raspberry:
    def __init__(self):
        self.pn532 = Pn532_i2c()
        self.pn532.SAMconfigure()
        self.mifare_card = Mifare()

    def read_card(self):
        print("Place the card to be read on the PN532...")
        print('==============================================================')
        print('WARNING: DO NOT REMOVE CARD FROM PN532 UNTIL FINISHED WRITING!')
        print('==============================================================')
        print('')
        data_card = self.mifare_card.scan_field()
        data = str(data_card)
        print(data[12:len(data) - 2])
        print(data_card)
        print("Successful")
        return data[12:len(data) - 2]

