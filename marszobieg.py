import csv
from datetime import datetime, timedelta

# input_file = "C:/Users/amusial/Downloads/17714906303_ACTIVITY-record.csv"
input_file = "C:/Users/amusial/Downloads/16496987474_ACTIVITY-record.csv"

running = 0
walking = 0
running_time_sum = timedelta()
walking_time_sum = timedelta()
standing_time_sum = timedelta()
previous_time = 0
previous_distance = -100

input_format = "%m/%d/%Y, %I:%M:%S %p"

with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
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
        # print(distance_difference)
        # print(time, distance, event_type)
        # operation
        if distance_difference > 0:
            # if event_type == "running":
            #     running_time_sum = running_time_sum + time_difference
            #     running = running + 1
            # elif event_type == "walking":
            #     walking_time_sum = walking_time_sum + time_difference
            #     walking = walking + 1
            if cadence > 63:
                running_time_sum = running_time_sum + time_difference
                running = running + distance_difference
            else:
                walking_time_sum = walking_time_sum + time_difference
                walking = walking + distance_difference
        else:
            standing_time_sum = standing_time_sum + time_difference
        # end of oper
        previous_time = time
        previous_distance = distance

running = running / 1000
walking = walking / 1000
print("Sum of running distance: " + "%.2f" % running + " km")
print("Sum of walking distance: " + "%.2f" % walking + " km")

print("Sum of running time: " + str(running_time_sum))
print("Sum of walking time: " + str(walking_time_sum))
print("Sum of standing time: " + str(standing_time_sum))

print("Whole time: " + str(standing_time_sum + walking_time_sum + running_time_sum))