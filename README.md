# FRC Team 1571 BunnyBots 2019
 BunnyBots 2019 Code. Offseason learning experience. Python RobotPy framework based code implementation. 6 wheel, 4 motor drivetrain. Rear wheels are omni-wheels.

- https://robotpy.readthedocs.io/en/stable/guide/index.html 
- https://robotpy-websim.readthedocs.io/en/latest/physics-intro.html

Recommended  Setup:  
1. Install VScode  
2. Install Python  
3. Install Git  
4. Install Python Extension  
5. Install Python Linter  

# Setup WPILib Extention
Search in Extensions for WPILib
Click on install

# Setup Python Virtual Environment
python3 -m venv venv
robotVenv

# Activate Venv
.\venv\Scripts\activate.bat

# Deactivate Venv
.\venv\Scripts\dectivate.bat

# Install RobotPy
Unzip the downloaded RobotPy zipfile on your computer (not on the roboRIO), and there should be an installer.py there. 
- Open up a command line, 
- Change directory to the installer location, and run this:  

Windows:  
> py -3 installer.py install-robotpy


# PyFRC install
Installing pyfrc will install all of the packages needed to help you write and test Python-based Robot code on your development computer. These tools include WPILib, pynetworktables, unit testing support, and the robot simulator.
> py -3 -m pip install pyfrc
* ***Inside VS Code, add `--user` option at end of command to execute with permission***

# Install RobotPy-CTRE : motor controllers
Install robotpy-ctre Module
Setup (tests/simulator)  
> py -3 -m pip install -U robotpy-ctre  


# Real Joystick support via pygame
pip install pygame

# Run Robot.py in WPILib
    py -3 robot.py
    py -3 robot.py --help


# Run Python Simulator
Windows Setup:
> .\sim\config.json  
> .\physics.js   
> .\robot.py   

Run :
> py -3 robot.py sim

# Web Simulator
Install on Windows: 
> pip3 install robotpy-websim  

Config :  
Enable physics: create 'sim' directory and config.json file.  
 > .\sim\config.json 

 Create a physics.js file in 'sim' directory and create a MyUserPhysics class that extends UserPhysics. 
 > .\sim\physics.js 

Run:   
> py -3 robot.py websim


-----
# Setup Unit Test Framework
> pip3 --install PyTest

# Run Unit Tests - py.test python testing tool
Windows:  
> py -3 robot.py test

Built-in Tests to start with:
> py -3 robot.py add-tests

