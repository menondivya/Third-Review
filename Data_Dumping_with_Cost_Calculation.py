#!/usr/bin/env python3

from influxdb import InfluxDBClient
import uuid
import random
import time
import numpy as np
import TSPFuzzyCost as fuzzy

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('GCS_Database_Final')

Flame = ['0','1']
Difficulty = ['0','1'] 
Distance = np.arange(0, 500, 1).tolist()
Condition = np.arange(0, 50, 1).tolist()

f1 = random.randint(0,1)
f2 = random.randint(0,1)
f3 = random.randint(0,1)
f4 = random.randint(0,1)
f5 = random.randint(0,1)

dif1 = random.randint(0,1)
dif2 = random.randint(0,1)
dif3 = random.randint(0,1)
dif4 = random.randint(0,1)
dif5 = random.randint(0,1)

dis1 = random.randint(0,500)
dis2 = random.randint(0,500)
dis3 = random.randint(0,500)
dis4 = random.randint(0,500)
dis5 = random.randint(0,500)

c1 = random.choice(Condition)
c2 = random.choice(Condition)
c3 = random.choice(Condition)
c4 = random.choice(Condition)
c5 = random.choice(Condition)

cost=fuzzy.getCost(max(dis1,dis2,dis3,dis4,dis5),max(dif1,dif2,dif3,dif4,dif5),max(c1,c2,c3,c4,c5))
print("Weight for TSP:")
print(cost)

json_body = [
    {
        "measurement": "Flame",
        "tags": {
            "Building1":f1,
	    "Building2":f2,
	    "Building3":f3,
	    "Building4":f4,
	    "Building5":f5
        },
        "fields": {
            "Max": max(f1,f2,f3,f4,f5),
	    "Cost":cost
        }
    },{"measurement": "Difficulty",
     "tags": {"Building1":dif1,
              "Building2":dif2,
	      "Building3":dif3,
	      "Building4":dif4,
	      "Building5":dif5
        },
        "fields": {
            "Max": max(dif1,dif2,dif3,dif4,dif5),
	    "Cost":cost
        }
    },{"measurement": "Distance",
     "tags": {"Building1":dis1,
	    "Building2":dis2,
	    "Building3":dis3,
	    "Building4":dis4,
	    "Building5":dis5
	},
        "fields": {
            "Max": max(dis1,dis2,dis3,dis4,dis5),
	    "Cost":cost
        }
    },{"measurement": "Condition",
     "tags": {"Building1":c1,
	    "Building2":c2,
	    "Building3":c3,
	    "Building4":c4,
	    "Building5":c5,
        },
        "fields": {
            "Max": max(c1,c2,c3,c4,c5),
	    "Cost":cost
        }
    }
]

client.write_points(json_body, database='GCS_Database_Final', time_precision='ms',protocol='json')




