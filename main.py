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

class GeoFencing:
    
    def __init__(self, office_latitude, office_longitude, radius):
        self.office_latitude = office_latitude
        self.office_longitude = office_longitude
        self.radius = radius

    def is_within_geofence(self, user_latitude, user_longitude):
        # Use the geofence_lib to check if the user's location is within the geofence
        return geofence_lib.is_within_radius(
            user_latitude,
            user_longitude,
            self.office_latitude,
            self.office_longitude,
            self.radius
        )
'''


"""