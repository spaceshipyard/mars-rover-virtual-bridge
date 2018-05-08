import vrep.vrep

import sys

vrep.vrep.simxFinish(-1)

clientID = vrep.vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

errorCode,left_motor_handle= vrep.vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.vrep.simx_opmode_oneshot_wait)

errorCode,right_motor_handle= vrep.vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor',
                                                       vrep.vrep.simx_opmode_oneshot_wait)

if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()

errorCode= vrep.vrep.simxSetJointTargetVelocity(clientID, left_motor_handle, 0.2, vrep.vrep.simx_opmode_oneshot_wait)
errorCode= vrep.vrep.simxSetJointTargetVelocity(clientID, right_motor_handle, 0.2, vrep.vrep.simx_opmode_oneshot_wait)