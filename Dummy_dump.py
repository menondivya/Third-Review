#!/usr/bin/env python3

from influxdb import InfluxDBClient
import uuid
import random
import time
import numpy as np

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('GCS_Database')

measurement_name = 'Sensor_Data'
number_of_points = 200
data_end_time = int(time.time() * 1000) #milliseconds

Flame = ["0",
"1"]
Difficulty = ["0", 
"1"] 
Distance = np.arange(0, 150, 1).tolist()
Condition = np.arange(0, 50, 1).tolist()

data = []
data.append(
        {
                "measurement": "Sensor_Data",
                "tags": {
                        "Flame": random.choice(Flame), 
                        "Difficulty": random.choice(Difficulty),
                        "Distance": random.choice(Distance),
			"Condition": random.choice(Condition)
                },
                "fields": {
                        "x": random.randint(1,4),
                        "y": random.randint(1,4),
                        "z": random.randint(0,50)
                },
                "time": data_end_time
        }
)
current_point_time = data_end_time

for i in range(number_of_points-1):
        current_point_time = current_point_time - random.randrange(1,100)
        data.append(
                {
	                "measurement": "Sensor_Data",
        	        "tags": {
                	        "Flame": random.choice(Flame), 
                        	"Difficulty": random.choice(Difficulty),
                       		"Distance": random.choice(Distance),
	                       	"Condition": random.choice(Condition)
	        		},
			"fields": {
                        	"x": random.randint(1,4),
	                        "y": random.randint(1,4),
        	                "z": random.randint(0,50)
                	        },
	                "time": current_point_time
                }
	)

#client_write_start_time = time.perf_counter()

client.write_points(data, database='GCS_Database', time_precision='ms', batch_size=20, protocol='json')



