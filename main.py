'''
OFFICE COORDINATES
LANTITUDE : 18.491256079845726
LONGITUDE : 73.85505103564057
RADIUS    : 60m from office loc point

multiple braches access

'''

'''
control flow of project
 user ka data  ==> geofencing tak pahuchana ==> hum uspe operation karenge 
 => post method se hum output ko frontend mein tranfer karenge 
 ==>  frontend wale notify karenge hr ko
'''



# psedo code :
"""
step-1 -creating a dictionary to fetch users location in key as his username and attribute as his coordinate.

example - location = { "shivam": "18.491256079845726, 73.85505103564057" }

step-2 - logic defination -

   * to fetch user coordinates.
   * storing that coordinate differ list/tuple.
   *applying if else ladder in condition according to project need.
   *using attributes of geofencing api to connect with coordinate.
    example - 28.9.00.88 => standard geofencing mein jo location dala rahega ussey compare karna hai.
   * phir usko endpoint se connect karna hai -- @geofencing 
   * phir harsh usko get/post method se backend mein synchronize karega.
   *proceeding how to deliever output to website of hrm.

step-3 required contexts for project

*fastapi -"to create endpoint for fetching it t"
*asynco = "to create asynchronous function so that multiple request can be handled that was collected from backend"
geofencelib = "to use functions of it to perform geofencing operation"
*env file "for securing credencials" 

'''

sample code for geofencing operation using fastapi and geofencing library
import geofence_lib as geofence_lib

"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import math
import sqlite3
import time
import requests
import geopandas as gpd

app = FastAPI()
ab = requests.get("http://127.0.0.1:5500/geo.html")

# branches = {
#     "pune": {
#         "Lantitude": 18.491256079845726,
#         "Longitude": 73.85505103564057,
#         "Radius" : 60
#     }
# }

# @app.post("/geofence")
# async def geofence(user_Location: dict):
#       try:
#          user_latitude = user_Location.get("latitude")
#          user_longitude = user_Location.get("longitude")
#          branch_name = user_Location.get("branch")
   
#          if branch_name not in branches:
#                raise HTTPException(status_code=404, detail="Branch not found")
   
#          branch_info = branches[branch_name]
#          branch_latitude = branch_info["Lantitude"]
#          branch_longitude = branch_info["Longitude"]
#          radius = branch_info["Radius"]
   
#          # Calculate distance using Haversine formula
#          distance = geofence_lib.calculate_distance(user_latitude, user_longitude, branch_latitude, branch_longitude)
   
#          if distance <= radius:
#                return {"status": "success", "message": "User is within the geofence."}
#          else:
#                return {"status": "failure", "message": "User is outside the geofence."}
   
#       except Exception as e:
#          raise HTTPException(status_code=500, detail=str(e))

# def calculate_distance(lat1, lon1, lat2, lon2):
#     # Haversine formula to calculate distance between two points on the Earth
#     R = 6371000  # Radius of the Earth in meters
#     phi1 = math.radians(lat1)
#     phi2 = math.radians(lat2)
#     delta_phi = math.radians(lat2 - lat1)
#     delta_lambda = math.radians(lon2 - lon1)

#     a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a ))
#       distance = R * c
#       return distance

# @app.get("/branches")
# async def get_branches():
#     return branches

# def add_branch(branch_name: str, latitude: float, longitude: float, radius: float):
#     branches[branch_name] = {
#         "Lantitude": latitude,
#         "Longitude": longitude,
#         "Radius": radius
#     } 

# def remove_branch(branch_name: str):
#     if branch_name in branches:
#         del branches[branch_name]
#     else:
#         raise ValueError("Branch not found") 

# def update_branch(branch_name: str, latitude: float, longitude: float, radius: float):
#     if branch_name in branches:
#         branches[branch_name] = {
#             "Lantitude": latitude,
#             "Longitude": longitude,
#             "Radius": radius
#         }
#     else:
#         raise ValueError("Branch not found")
