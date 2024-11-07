import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
length = 1000
amplitude1 = math.pi/4
frequency1 = 1
phaseOffset1 = 0
amplitude2 = math.pi/4
frequency2 = 15
phaseOffset2 = math.pi/2
backLegSensorValues = numpy.zeros(length)
frontLegSensorValues = numpy.zeros(length)
angles = numpy.linspace(0, 2 * numpy.pi, length)
targetAnglesBack = amplitude1 * numpy.sin(frequency1 * angles + phaseOffset1)
targetAnglesFront = amplitude2 * numpy.sin(frequency2 * angles + phaseOffset2)
for i in range(0, length):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition= targetAnglesBack[i],
        maxForce=60)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition= targetAnglesFront[i],
        maxForce=60)
    time.sleep(1/240)
    print(i)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()