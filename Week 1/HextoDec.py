hexNumbers={ '0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
           'A':10,'B':11,'C':12,'D':13}
def hexToDec(HexNum):
    for char in HexNum:
        if char not in hexNumbers:
            return None

    if len(HexNum)==3:

        return hexNumbers[HexNum[0]]*256+hexNumbers[HexNum[1]]*16+hexNumbers[HexNum[2]]
hex_str='1B2'

decimal_num=hexToDec(hex_str)
print(decimal_num) #output 434