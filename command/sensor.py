import math

from vrep import vrep

class Sensor:
    SENSOR_NAME = "Pioneer_p3dx_ultrasonicSensor"
    COUNT_SENSOR = 16
    def __init__(self, clientId):
        self.clientId = clientId
        self.ini_sensors()

    def ini_sensors(self):


        self.sensor_list = {}
        for i in range(0,self.COUNT_SENSOR):
            name_of_sensor = self.SENSOR_NAME + str(i)
            error_code_left, sensor = vrep.simxGetObjectHandle(self.clientId,
                                                                          name_of_sensor,
                                                                          vrep.simx_opmode_blocking)
            self.sensor_list[name_of_sensor] = sensor

        # error_code_left,  self._left_sensor = vrep.simxGetObjectHandle(self.clientId, 'Pioneer_p3dx_ultrasonicSensor3', vrep.simx_opmode_oneshot_wait)

    def get_info_sensor(self):
        sensor_dist = []
        for sensor in self.sensor_list:
            err_code, detectionState, detectedPoint, detectedObjectHandle,\
            detectedSurfaceNormalVector = vrep.simxReadProximitySensor(self.clientId,self.sensor_list[sensor], vrep.simx_opmode_streaming )


            err_code, detectionState, detectedPoint, detectedObjectHandle, \
            detectedSurfaceNormalVector = vrep.simxReadProximitySensor(self.clientId, self.sensor_list[sensor],
                                                                       vrep.simx_opmode_buffer)

            if err_code != -1 and (detectionState):
                data = {}
                data['name'] = sensor
                data['distance'] = self.norm(detectedPoint) * 100
                sensor_dist.append(data)

        return sensor_dist

    def norm(self, vec_sensor):

        return math.sqrt(vec_sensor[0] ** 2 + vec_sensor[1] ** 2 + vec_sensor[2] ** 2)