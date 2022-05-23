import random
import math

def randomDataGenerator(size):
    data = [random.randint(0, 1) for i in range(size)]
    return data

def QPSK(data_array):
    if (len(data_array) % 2 != 0):
        print("Error, check data_array length(QPSK)", len(data_array))
        return 0
    else:
        arr = [] # массив комплексных чисел
        for i in range(0, len(data_array), 2):
            bit = data_array[i]
            bit1 = data_array[i+1]
            real = (1 - 2 * bit) / math.sqrt(2)
            imag = (1 - 2 * bit1) / math.sqrt(2)
            arr.append(complex(real, imag))
        return arr

def QAM16(data_array):
    if (len(data_array) % 4 != 0):
        print("Error, check data_array length(QAM16)")
        return 0
    else:
        arr = []
        for i in range(0, len(data_array), 4):
            bit = data_array[i]
            bit1 = data_array[i+1]
            bit2 = data_array[i+2]
            bit3 = data_array[i+3]
            real = (1 - 2 * bit) * (2 - (1 - 2 * bit2)) / math.sqrt(10)
            imag = (1 - 2 * bit1) * (2 - (1 - 2 * bit3)) / math.sqrt(10)
            arr.append(complex(real, imag))
        return arr
    
def QAM64(data_array):
    if (len(data_array) % 6 != 0):
        print("nError, check data_array length(QAM64)")
        return 0
    else:
        arr = []
        for i in range(0, len(data_array), 6):
            bit = data_array[i]
            bit1 = data_array[i+1]
            bit2 = data_array[i+2]
            bit3 = data_array[i+3]
            bit4 = data_array[i+4]
            bit5 = data_array[i+5]
            real = (1 - 2 * bit) * (4 - (1 - 2 * bit2) * (2 - (1 - 2 * bit4))) / math.sqrt(42)
            imag = (1 - 2 * bit1) * (4 - (1 - 2 * bit3) * (2 - (1 - 2 * bit5))) / math.sqrt(42)
            arr.append(complex(real, imag))
        return arr
    
def QAM256(data_array):
    if (len(data_array) % 8 != 0):
        print("Error, check data_array length(QAM256)")
        return 0
    else:
        arr = []
        for i in range(0, len(data_array), 8):
            bit = data_array[i]
            bit1 = data_array[i+1]
            bit2 = data_array[i+2]
            bit3 = data_array[i+3]
            bit4 = data_array[i+4]
            bit5 = data_array[i+5]
            bit6 = data_array[i+6]
            bit7 = data_array[i+7]
            real = (1 - 2 * bit) * (8 - (1 - 2 * bit2) * (4 - (1 - 2 * bit4) * (2 - (1 - 2 * bit6)))) / math.sqrt(170)
            imag = (1 - 2 * bit1) * (8 - (1 - 2 * bit3) * (4 - (1 - 2 * bit5) * (2 - (1 - 2 * bit7)))) / math.sqrt(170)
            arr.append(complex(real, imag))
        return arr
    
def decode(s, bitts, func):
    result = []
    for i in s:
        didx = []
        dmin = 2
        for b in range(0, 2 ** bitts):
            array = []
            for j in range(0, bitts):
                array.append(b % 2)
                b = int(b / 2)
            res = func(array)[0]
            dx = res.real - i.real
            dy = res.imag - i.imag
            d = dx ** 2 + dy ** 2
            if d < dmin:
                didx = array
                dmin = d
        result = result + didx
    return result

array = randomDataGenerator(24)
print("1. Generated array =", array)
print("2. QPSK =", QPSK(array))
print("2.1. Decode_QPSK =", decode(QPSK(array), 2, QPSK))
print("3. QAM16 =", QAM16(array))
print("3.1. Decode_QAM16 =", decode(QAM16(array), 4, QAM16))
print("4. QAM64 =", QAM64(array))
print("4.1. Decode_QAM64 =", decode(QAM64(array), 6, QAM64))
print("5. QAM256 =", QAM256(array))
print("5.1. Decode_ QAM256 =", decode(QAM256(array), 8, QAM256))
