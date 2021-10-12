from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 3
for a in range(3):
    robotArm.grab()
    for b in range(2):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(2):
        robotArm.moveLeft()
robotArm.moveRight()
for a in range(3):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
        
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()