import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

n =128

duration = 0.3
amplitude = 0.3  # амплитуда  (в пределах: +-1.0)
fr = 0
fr_a = 392
fr_b = 493
fr_c = 261
fr_d = 293
fr_e = 329
fr_f = 349
fr_g = 415
fs = 50000
timeSamples = np.arange(np.ceil(duration * fs)) / fs
timeSamples1 = np.arange(np.ceil(duration-0.05 * fs)) / fs

zero = amplitude * np.sin(2 * np.pi * fr * timeSamples)
col = amplitude * np.sin(2 * np.pi * fr_a * timeSamples)
col1 = amplitude * np.sin(2 * np.pi * fr_a * timeSamples1)
col_de = amplitude * np.sin(2 * np.pi * fr_g * timeSamples)
col_de1 = amplitude * np.sin(2 * np.pi * fr_g * timeSamples1)
do = amplitude * np.sin(2 * np.pi * fr_c * timeSamples)
mi = amplitude * np.sin(2 * np.pi * fr_e * timeSamples * 1.2)
fa = amplitude * np.sin(2 * np.pi * fr_f * timeSamples)

arr1= []
arr1 = np.concatenate((mi,do,mi,do,mi,fa,fa,zero))
arr2= []
arr2 = np.concatenate((fa,do,fa,do,fa,mi,mi,zero))
arr3= []
arr3 = np.concatenate((mi,do,mi,do,mi,fa,zero))
arr4= []
arr4 = np.concatenate((fa,col,col1,col,col1,col,col_de1,col_de,col_de1,col_de,zero))
arr5= []
arr5 = np.concatenate((col_de1,col_de,col,fa,mi,fa,fa))
arr= []
arr = np.concatenate((arr1,arr2,arr1,arr3,arr4,arr5,arr4,arr5))


# Расчет преобразования Фурье
signalFFT = np.fft.rfft(arr)
signalFFTabs = 2*np.abs(signalFFT) / n

new_sig = np.fft.irfft(signalFFT)

# Построение графика
fig = plt.figure(figsize=(16, 5), dpi=100)

plt.title('Начальный сигнал')
plt.plot(arr[:500])
plt.show()
plt.title('Конечный сигнала')
plt.plot(new_sig[:500])
plt.show()

#sd.play(arr, fs, None,1)
#sd.play(new_sig, fs, None,1)
fs1=44000
duration1 = 3  # seconds
myrecording = sd.rec(duration1 * fs1, samplerate=fs1, channels=1,dtype='float64')
print ("Recording Audio")
sd.wait()
print ("Audio recording complete , Play Audio")
sd.play(myrecording, fs)
sd.wait()
print ("Play Audio Complete")

voiceFFT = np.fft.rfft(myrecording)
voiceFFTabs = 2*np.abs(voiceFFT) / n

plt.plot(voiceFFTabs)
plt.show()
