#coding:utf-8
import struct
import wave
import numpy as np
import scipy.signal
from pylab import *

def save(data, fs, bit, filename):
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(bit / 8)
    wf.setframerate(fs)
    wf.writeframes(data)
    wf.close()

if __name__ == '__main__':
    wf = wave.open("record.wav", "r")
    fs = wf.getframerate()

    x = wf.readframes(wf.getnframes())
    x = frombuffer(x, dtype="int16") / 32768.0

    nyq = fs / 2.0  # nyquist frequency

    # make filter
    # normalize nyquist frequency
    fe = 7500.0 / nyq      # cutoff frequency
    numtaps = 255           # number of taps(filter coefficients)

    b = scipy.signal.firwin(numtaps, fe)	# Low-pass

    # filtering
    y = scipy.signal.lfilter(b, 1, x)

    # output filtered data
    y = [int(v * 32767.0) for v in y]
    y = struct.pack("h" * len(y), *y)
    save(y, fs, 16, "whitenoise_filtered.wav")
