Description
===========
# Requirements
Python 3.5+

## Installation
    
git clone --recursive https://github.com/spaceshipyard/mars-rover-virtual-bridge

For fast test I saved in project(mars-rover-virtual-bridge/vrep/)  remoteApi.dll for Windows x64
If you no use Windows, you must replace it. 

copy library from V-REP_PRO_EDU\programming\remoteApiBindings\lib\lib\OS to D:\3d\remoteAPIPython\vrep 


Install "Setuptool" https://pypi.org/project/setuptools/:

**python -m pip install --upgrade pip setuptools wheel**

and then packages:

**python setup.py install**

## Run
Run the client from https://github.com/spaceshipyard/mars-rover-dispatcher
Open V-REP with "test/test2" and start simulation.
After it, run: 

**python mars-rover-virtual-bridge/main.py**
