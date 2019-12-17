''' 
BunnyBots 2019

Code Authors:
Cole Sonnichsen (Captain)
Jay Dougan (2nd Year)
Bruce Baird (2nd Year)
Jasper Black
Yollaine Brooks

Team 1571 [CALibrate Robotics]
'''

# Necessary modules
# WPI Lib
import wpilib
from wpilib import drive, Timer, SendableChooser
import ctre
from networktables import NetworkTables
# import funct
# import oi

class George(wpilib.TimedRobot):
    
    # Initial Sequence
    def robotInit(self):
        ''' Network Tables '''
        self.table = NetworkTables.getTable('SmartDashboard')

        self.controller = wpilib.XboxController(0)
        
        #Jay Programing
        # wpilib.CameraServer.launch("vision.py:main")
        '''self.sortSwitch = wpilib.DigitalInput(0) #Switch to stop sorting motor''' # Input for potential switch

        self.intake = wpilib.Talon(1) #intake motor

        # Talon SRX #
        # Right drivetrain 
<<<<<<< HEAD
        self.fr_motor = ctre.WPI_talonsrx.WPI_TalonSRX(2)
        self.rr_motor = ctre.wpi_talonsrx.WPI_TalonSRX(3)
=======
        self.fr_motor = ctre.WPI_TalonSRX(2)
        self.rr_motor = ctre.WPI_TalonSRX(3)
>>>>>>> 494ed2793840d3d331d54b12b77d315240f147cc
        self.right = wpilib.SpeedControllerGroup(self.fr_motor, self.rr_motor)

        # # Left drivetrain
        self.fl_motor = ctre.WPI_TalonSRX(0) # 0
        self.rl_motor = ctre.WPI_TalonSRX(1) # 1
        self.left = wpilib.SpeedControllerGroup(self.fl_motor, self.rl_motor)

        # [Six wheels; four motors--one for each gearbox]
        # Class for driving the differential train
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

        # Triggers/Controls
        self.kLeft = self.controller.Hand.kLeft
        self.kRight = self.controller.Hand.kRight

    # def disabledInit(self):
    #     self.timer.reset()
    #     self.timer.start()

    def disabledPeriodic(self):
        pass

    # function is called at the beginning of the autonomous
    def autonomousInit(self):
        ''' Setup '''

    # teleop
    def teleopInit(self):
        ''' Initialization of Teleop '''

    # teleop
    def teleopPeriodic(self):
        ''' During teleop '''
        ''' Called during operator control '''
        
<<<<<<< HEAD
        while self.isOperatorControl() and self.isEnabled():
            #Get trigger values and set the to find speed
            self.TriggerLeft = self.controller.getTriggerAxis(self.kLeft)
            self.TriggerRight = self.controller.getTriggerAxis(self.kRight)
            self.speed = (self.TriggerRight - self.TriggerLeft) * 0.9

            #Get rotation of the left stick
            self.XLeftStick = self.controller.getX(Hand.kLeft) * 0.9
            #self.YLeftStick = self.controller.getY(Hand.kLeft)

            #Activate the motors
            self.drive.arcadeDrive(self.speed, self.XLeftStick)
=======
        self.drive.arcadeDrive()
>>>>>>> 494ed2793840d3d331d54b12b77d315240f147cc

'''if __name__ == "__main__":
    wpilib.run(robot.physics_enabled = True)'''
if __name__ == '__main__':
    wpilib.run(George)