import random
import time

#configuration
temperature_limit = 75 # degrees Celsius
interval_seconds = 2 # time between readings
number_of_readings = 10 # total readings to simulate

print("Starting temperature monitoring...\n")

for i in range(number_of_readings):
    temperature = random.uniform(60, 85)
    print(f"Reading {temperature:.2f} ºC")

    if temperature > temperature_limit:
        print("WARNING: Temperature above safe limit!\n")
    else: 
        print("Temperature is within the safe limit. \n")
 
    time.sleep(interval_seconds) #Pause the program for a while

print("Temperature monitoring finished.")