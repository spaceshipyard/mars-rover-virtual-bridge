import json
from aiohttp import web
import socketio
from command.manager import Command


sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

manager_command = None



@sio.on('connect')
def connect(sid, val):
    global manager_command
    if manager_command is None:
        manager_command = Command()
    manager_command.create_connect()

    print("start")
    print("connect ", sid)

@sio.on('echo')
def echo(sid, environ):
    print("start")
    print("connection ", sid)

@sio.on('message')
async def message(sid, msg):
    global  manager_command
    #print(msg)
    manager_command.recognize_command(msg)

@sio.on('sensor.data')
async def my_custom_event(sid, msg):
    await sio.emit('my reply')


async def background_task():
    """Example of how to send server generated events to clients."""
    #count = 0
    while True:
        if manager_command is None:
            return
        await sio.sleep(1)
        #count += 1
        await sio.emit('message', json_message_sensor())
        #await sio.emit('message', {'cmd': 'sensor.data', 'params': { 'type': 'proximity-data', 'data': [{'name': 'front-right', 'distance':'99'}] } })

def json_message_sensor():
    list_sensor = manager_command.sensor.get_info_sensor()
    if list_sensor is None:
        return ""
    message = {'cmd': 'sensor.data', 'params': {'type': 'proximity-data', 'data':list_sensor}}# json.dumps(
    return message

def run_server():
    sio.start_background_task(background_task)
    web.run_app(app, host='127.0.0.1', port=8080)


