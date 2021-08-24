import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('pulse_data.txt','r') as csvfile:

    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))  #pulse from ist sensor
        y.append(int(row[1]))  #pulse from second sensor

print(x)
print(y)
iterations=len(x)  #we are ploting aganist iteration versus amplitude
print("iterations:" + str(iterations))
x_value=[]
for i in range(iterations):
    x_value.append(int(i+1))
print(x_value)
plt.subplot(221)
plt.plot(x_value,y, label="pulse wave" )
plt.title("Raw data",)
plt.xlabel("Iterations")
plt.ylabel("Amplitude")
plt.show()




