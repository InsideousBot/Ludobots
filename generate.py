import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
x = 1
y = 1
z = 1
for i in range(5):
    for j in range(5):
        x = 1
        y = 1
        z = 1
        for k in range(10):
            pyrosim.Send_Cube(name="Box1", pos=[i, j, k + .5], size=[x, y, z])
            x = .9*x
            y = .9*y
            z = .9*z
pyrosim.End()
