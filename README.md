# FRC Team 1571 BunnyBots 2019
 BunnyBots 2019 Code. Offseason learning experience. Python RobotPy framework based code implementation. 6 wheel, 4 motor drivetrain. Rear wheels are omni-wheels.

- https://robotpy.readthedocs.io/en/stable/guide/index.html 
- https://robotpy-websim.readthedocs.io/en/latest/physics-intro.html

Recommended  Setup:  
1. Install VScode  
https://github.com/wpilibsuite/allwpilib/releases 
2. Install Python  
3. Install Git  
4. Install Python Extension  
5. Install Python Linter  
6. Install GitLens

## Setup WPILib Extension - separately if skipped
Search in Extensions for WPILib
Click on install

## Setup Python Virtual Environment
    python3 -m venv venv  
    optional name: robotVenv

### Activate Venv
> .\venv\Scripts\activate.bat

### Deactivate Venv
> .\venv\Scripts\dectivate.bat

## Install RobotPy
Unzip the downloaded RobotPy zipfile on your computer (not on the roboRIO), and there should be an installer.py there. 
- Open up a command line, 
- Change directory to the installer location, and run this:  

Windows:  
> py -3 installer.py install-robotpy


# PyFRC install
Installing pyfrc will install all of the packages needed to help you write and test Python-based Robot code on your development computer. These tools include WPILib, pynetworktables, unit testing support, and the robot simulator.
> py -3 -m pip install pyfrc
* ***Inside VS Code, add `--user` option at end of command to execute with permission***

## Install RobotPy-CTRE : motor controllers
Install robotpy-ctre Module
Setup (tests/simulator)  
> py -3 -m pip install -U robotpy-ctre  


## Real Joystick support via pygame
pip install pygame

## Run Robot.py in WPILib
    py -3 robot.py run
    py -3 robot.py --help


# Run Python Simulator
Windows Setup:
> .\sim\config.json  
> .\physics.js   
> .\robot.py   

Run :
> py -3 robot.py sim

## Web Simulator
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

## Run Unit Tests - py.test python testing tool
Windows:  
> py -3 robot.py test

Built-in Tests to start with (add tests/ use default tests from pyfrc):
> py -3 robot.py add-tests  
> py -3 .\robot.py --builtin

## Code Coverage checks
Check code coverage in you tests or with the simulator: 
Windows:   
> py -3 robot.py coverage test  
> py -3 robot.py coverage sim

## Run Unit Tests - Visual Studio Code
- Configure - select pytest as testing framework
- Select Test folder
- Configure Test Runner  

Verbose test, with printf statements passed to console:
> pytest -v -s

- pytest moduleName, myModule
- pytest DirectoryName/, myDirectory/
- pytest -k "expression"
- pytest -m "expression", uses "pytest.mark" decorator
- -v : verbose, -q : quiet, -s : don't capture console output, --ignore, --maxfail


## Code Check
> pip install --upgrade pyflakes  
> py -3 -m pyflakes .   

PyLint - install in VS Code

## Check Git Setup
> git config --list


## vJOY - Virtual Joystick
Bypass method to allow computer to control simulator without physical Xbox Controller or Joystick present.  
- http://vjoystick.sourceforge.net/site/

## UCR - Universal Control Remapper - Map Keyboard to HID Controller
- https://github.com/snoothy/ucr/releases


###