import numpy as np

"""
Test inputs see at delay 5 there is perfect correlation
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
y=np.array([1,1,1,1,1,2,3,4,5,6,34,54,1,3,45,33,2,2,23,43,54,54])
"""
loop = 1

from sklearn import preprocessing
# print(x)
# print(y)

import pandas as pd
import matplotlib.pyplot as plt

""" Read inputs"""

bitcoin = pd.read_csv('C:\Business Analytics Bsc\DISS\CRYPTO DATA\Bitcoin\gemini_BTCUSD_2020_1min.csv', delim_whitespace=False, skiprows=0,
                      index_col=False)
print(bitcoin.columns)

print(bitcoin.head(10))
lightcoin = pd.read_csv('C:\Business Analytics Bsc\DISS\CRYPTO DATA\Lightcoin\gemini_LTCUSD_2020_1min.csv', delim_whitespace=False, skiprows=0,
                       index_col=False)
print(lightcoin.columns)

print(lightcoin.head(10))
# Select closing price
bitcoin1 = bitcoin['Close']  # Use Close Price
lightcoin1 = etherium['Close']

x1 = np.flip(bitcoin1)  # Flip the data so we start from earliest time to latest
y1 = np.flip(etherium1)

window_start = 0
window_end = 500

for l in range(967):
    print("START WINDOW " + str(window_start))
    print("END WINDOW " + str(window_end))

    x = x1[window_start:window_end]  # only select 500 values for now
    length = len(x)
    y = y1[window_start:int(
        window_end + 0.5 * length)]  # The ethereum window is always 250 bigger than bitcoin window. Hence we can delay up to a maximum of 250


    # Calculate Standard Deviation
    def stdev(pricelist1, pricelist2):
        standartdeviation1 = np.std(pricelist1)
        standartdeviation2 = np.std(pricelist2)
        return standartdeviation1, standartdeviation2


    # Calculate mean
    def meanfunc(prices1, prices2):
        average1 = sum(prices1) / len(prices1)
        average2 = sum(prices2) / len(prices2)
        return average1, average2


    def calculate_DCF(x_values, y_values, delay):
        x_values = np.asarray(x_values)  # as array
        y_values = np.asarray(y_values)
        # print(x_values)
        # print(y_values)
        # print(x_values.dtype)
        # print("DELAY " + str(delay))

        DCF_array = np.zeros(len(x_values))  # create empty array for individual (x-x_mean)*(y-y_mean)

        y_values = np.roll(y_values, -delay)
        """Move the ethereum array to the left according to delay value"""
        # print(x_values)
        # print(y_values)
        """Normalise our data """
        x_values = preprocessing.normalize([x_values])
        y_values = preprocessing.normalize([y_values[0:length]])
        #    print(x_values)
        #    print((x_values.shape))
        x_values = x_values.flatten()  # Flatten array
        y_values = y_values.flatten()
        #    print(x_values)
        #    print((x_values.shape))
        x_average, y_average = meanfunc(x_values, y_values[0:length])  # calculate average
        x_stdev, y_stdev = stdev(x_values, y_values[0:length])  # calcualte standard deviation
        #
        #    print(x_average)
        #    print(y_average)
        #    print(x_stdev)
        #    print(y_stdev)
        for i in range(len(
            x_values)): """len is 500 only do the calculation for the current 500 window, note the ethereum array already shifted beforehand"""

        # j=i+delay #used to shift bottom array
        # print(x_values[i])
        # print(y_values[j % len(y)])
        DCF_array[i] = (x_values[[i]] - x_average) * (y_values[[i]] - y_average)  # Dot product


    # print(DCF_array)
    DCF_sum = np.sum(DCF_array) / (x_stdev * y_stdev)  # callucate sum of dot products
    DCF = DCF_sum / (length)  # Divide by multiples of Std and number of elemts
    # print("sum DCF = " + str(DCF_sum))
    # print("total DCF = " + str(DCF))

 return DCF, delay

DCF_values = np.zeros(len(y) - length)
delays = np.arange(0, len(y) - length, 1)
# print(delays)
"""Loop through for different time delays"""

for i in range(len(delays)):
    DCF_values[i], delays[i] = calculate_DCF(x, y, delays[i])
"""
    f = open("DCF100_no_loop.txt", "a")
    f.write(str(DCF_values[i]) + "\n")
    f.close()
    z = open("delays100_no_loop.txt", "a")
    z.write(str(delays[i]) + "\n")
    z.close()
"""
print(DCF_values)
print(delays)
# Do plots


"""Plot Correlation here"""

normalized_x = preprocessing.normalize([x])
normalized_y = preprocessing.normalize([y[0:length]])

plt.scatter(delays, DCF_values[0:len(delays)])
plt.savefig("Desktop/Bitcoin/plots/" + str(loop) + ".png")
#    plt.show()
plt.clf()
maximum = np.argmax(DCF_values)
print(DCF_values[maximum])
print(delays[maximum])

"""plot normalised prices in the current 500 minute window """
time = np.arange(0, length, 1)
plt.scatter(time, normalized_x, label='bitcoin')
plt.scatter(time, normalized_y, label='etherium')
plt.legend(loc='upper right', frameon=False, fontsize=20)
#    plt.show()[[
plt.savefig("/Desktop/Bitcoin/price plot/" + str(loop) + ".png")
plt.clf()

"""Write the peak delay and the subsequent DCF of the current 500 minute indow"""
f = open("DCF.txt", "a")
f.write(str(DCF_values[maximum]) + "\n")
f.close()
z = open("delays.txt", "a")
z.write(str(delays[maximum]) + "\n")
z.close()

"""Shift our window by another 500"""

window_start = window_start + 500
window_end = window_end + 500
loop = loop + 1
