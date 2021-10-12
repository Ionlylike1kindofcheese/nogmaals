from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

tiles = 9
while tiles > 0:
    robotArm.grab()
    for x in range(tiles):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(tiles):
        robotArm.moveLeft()
    tiles = tiles - 2
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()