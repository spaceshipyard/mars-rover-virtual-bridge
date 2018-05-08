from command.sensor import Sensor
from vrep import vrep


class Command():
    clientId = -1
    left_motor_handle = None
    right_motor_handle = None
    sensor = None

    def create_connect(self):
        vrep.simxFinish(-1)
        self.clientId = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

        if self.check_connection():
            self.sensor = Sensor(self.clientId)


    def check_connection(self):
        if self.clientId != -1:
            print("Connected to remote server")
            return True
        else:
            print('Connection not successful')
            return False
            #sys.exit('Could not connect')

    def recognize_command(self,json_command):
        json_object = json_command#json.loads(json_command)
        self.get_parametrs(json_object['cmd'],json_object)

    def get_parametrs(self, x, json_object):
        return {
            'direction': self.move(json_object['params']),

        }[x]

    def move(self,param):
        params = param['offset']
        x = params['x']
        y = params['y']
        self.ini_engins()
        self.set_value_engines(float(x), float(y))
#        self.sensor.get_info_sensor()


    def ini_engins(self):

        error_code_left, self.left_motor_handle = vrep.simxGetObjectHandle(self.clientId, 'Pioneer_p3dx_leftMotor',
                                                                     vrep.simx_opmode_oneshot_wait)
        error_code_right, self.right_motor_handle = vrep.simxGetObjectHandle(self.clientId, 'Pioneer_p3dx_rightMotor',
                                                                      vrep.simx_opmode_oneshot_wait)
        if error_code_left == -1:
            print('Can''t find left or right motor')

        if error_code_right == -1:
            print('Can''t find left or right motor')

    def set_value_engines(self, x, y):
        error_code_left = vrep.simxSetJointTargetVelocity(self.clientId, self.left_motor_handle, x * 0.2,
                                                          vrep.simx_opmode_oneshot_wait)
        error_code_right = vrep.simxSetJointTargetVelocity(self.clientId, self.right_motor_handle, y * 0.2,
                                                         vrep.simx_opmode_oneshot_wait)

        if error_code_left == -1:
            print('Can''t find left or right motor')

        if error_code_right == -1:
            print('Can''t find left or right motor')

