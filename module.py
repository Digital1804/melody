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
        di = [] # массив комплексных чисел
        for i in range(0, len(data_array), 2):
            b2i = data_array[i]
            b2i1 = data_array[i+1]
            real = (1 - 2 * b2i) / math.sqrt(2)
            imag = (1 - 2 * b2i1) / math.sqrt(2)
            di.append(complex(real, imag))
        return di

def QAM16(data_array):
    if (len(data_array) % 4 != 0):
        print("Error, check data_array length(QAM16)")
        return 0
    else:
        di = []
        for i in range(0, len(data_array), 4):
            b4i = data_array[i]
            b4i1 = data_array[i+1]
            b4i2 = data_array[i+2]
            b4i3 = data_array[i+3]
            real = (1 - 2 * b4i) * (2 - (1 - 2 * b4i2)) / math.sqrt(10)
            imag = (1 - 2 * b4i1) * (2 - (1 - 2 * b4i3)) / math.sqrt(10)
            di.append(complex(real, imag))
        return di
    
def QAM64(data_array):
    if (len(data_array) % 6 != 0):
        print("nError, check data_array length(QAM64)")
        return 0
    else:
        di = []
        for i in range(0, len(data_array), 6):
            b6i = data_array[i]
            b6i1 = data_array[i+1]
            b6i2 = data_array[i+2]
            b6i3 = data_array[i+3]
            b6i4 = data_array[i+4]
            b6i5 = data_array[i+5]
            real = (1 - 2 * b6i) * (4 - (1 - 2 * b6i2) * (2 - (1 - 2 * b6i4))) / math.sqrt(42)
            imag = (1 - 2 * b6i1) * (4 - (1 - 2 * b6i3) * (2 - (1 - 2 * b6i5))) / math.sqrt(42)
            di.append(complex(real, imag))
        return di
    
def QAM256(data_array):
    if (len(data_array) % 8 != 0):
        print("Error, check data_array length(QAM256)")
        return 0
    else:
        di = []
        for i in range(0, len(data_array), 8):
            b8i = data_array[i]
            b8i1 = data_array[i+1]
            b8i2 = data_array[i+2]
            b8i3 = data_array[i+3]
            b8i4 = data_array[i+4]
            b8i5 = data_array[i+5]
            b8i6 = data_array[i+6]
            b8i7 = data_array[i+7]
            real = (1 - 2 * b8i) * (8 - (1 - 2 * b8i2) * (4 - (1 - 2 * b8i4) * (2 - (1 - 2 * b8i6)))) / math.sqrt(170)
            imag = (1 - 2 * b8i1) * (8 - (1 - 2 * b8i3) * (4 - (1 - 2 * b8i5) * (2 - (1 - 2 * b8i7)))) / math.sqrt(170)
            di.append(complex(real, imag))
        return di
    
def Decode(s, bits, func):
    result = []
    for i in s:
        didx = []
        dmin = 2
        for b in range(0, 2 ** bits):
            array = []
            for j in range(0, bits):
                array.append(b & 1)
                b = b >> 1
            res = func(array)[0]
            dx = res.real - i.real
            dy = res.imag - i.imag
            d = dx * dx + dy * dy
            if d < dmin:
                didx = array
                dmin = d
        result = result + didx
    return result

array = randomDataGenerator(24)
print("1. Generated array =", array)
print("2. QPSK =", QPSK(array))
print("2.1. Decode_QPSK =", Decode(QPSK(array), 2, QPSK))
print("3. QAM16 =", QAM16(array))
print("3.1. Decode_QAM16 =", Decode(QAM16(array), 4, QAM16))
print("4. QAM64 =", QAM64(array))
print("4.1. Decode_QAM64 =", Decode(QAM64(array), 6, QAM64))
print("5. QAM256 =", QAM256(array))
print("5.1. Decode_ QAM256 =", Decode(QAM256(array), 8, QAM256))
