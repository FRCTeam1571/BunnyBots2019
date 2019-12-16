# BunnyBots2019
 BunnyBots 2019 Code

Install VScode
Install Python
Install Git
Install Python Extension
Install Python Linter

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

# Real Joystick support via pygame
pip install pygame

# Install WPILib
install robotpy  
install ctre Module  
robotpy-ctre install  
Setup (tests/simulator)  
> py -3 -m pip install -U robotpy-ctre  

***Inside VS Code, add `--user` option at end of command to execute with permission***

# Run Robot.py in WPILib
    py -3 robot.py
    py -3 robot.py --help


# Run Python Simulator
Windows:   
> py -3 robot.py sim

# Setup Unit Test Framework
> pip3 --install PyTest

# Run Unit Tests - py.test python testing tool
Windows:  
> py -3 robot.py test

Buitin Tests to start with:
> Windows:   py -3 robot.py add-tests

# pyfrc install
Installing pyfrc will install all of the packages needed to help you write and test Python-based Robot code on your development computer. These tools include WPILib, pynetworktables, unit testing support, and the robot simulator.
> py -3 -m pip install pyfrc
