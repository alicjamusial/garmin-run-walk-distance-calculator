import csv
import os
import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Path to the CSV garmin activity file")
parser.add_argument("-c", "--cadence", type=int, default=63, help="Your threshold run/walk cadence (default: 63)")
args = parser.parse_args()

# Check if file exists
if not os.path.isfile(args.input_file):
    print("The specified file does not exist.")
    exit(1)

print(f"Opening CSV activity file: {args.input_file}")
print(f"Threshold cadence: {args.cadence}")

running = 0
walking = 0
running_time_sum = timedelta()
walking_time_sum = timedelta()
standing_time_sum = timedelta()
previous_time = 0
previous_distance = -100

input_format = "%m/%d/%Y, %I:%M:%S %p"

first_row = None
last_row = None

with open(args.input_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        if first_row is None:
            first_row = row
        last_row = row

        time = datetime.strptime(row[0], input_format)
        cadence = int(row[4])
        distance = float(row[5])
        event_type = row[11]

        if previous_time == 0:
            previous_time = time
        if previous_distance == -100:
            previous_distance = distance

        time_difference = time - previous_time # shall be 1 second
        distance_difference = distance - previous_distance

        if distance_difference > 0:
            if cadence > args.cadence:
                running_time_sum = running_time_sum + time_difference
                running = running + distance_difference
            else:
                walking_time_sum = walking_time_sum + time_difference
                walking = walking + distance_difference
        else:
            standing_time_sum = standing_time_sum + time_difference
        
        previous_time = time
        previous_distance = distance

t1 = datetime.strptime(first_row[0], input_format)
t2 = datetime.strptime(last_row[0], input_format)

diff = t2 - t1

running = running / 1000
walking = walking / 1000
print("\nSum of running time: " + str(running_time_sum))
print("Sum of running distance: " + "%.2f" % running + " km\n")

print("Sum of walking time: " + str(walking_time_sum))
print("Sum of walking distance: " + "%.2f" % walking + " km\n")

print("Sum of idle time: " + str(standing_time_sum))

print("\nSum of distance: " + "%.2f" % (running + walking) + " km")
print("\nWhole activity time: " + str(standing_time_sum + walking_time_sum + running_time_sum))

print("\n\nIf some of the above data doesn't match information from the Garmin software, try to adjust the cadence value to match your running/walking style.")