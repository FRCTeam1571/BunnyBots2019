from cscore import CameraServer

# Defines a function to get the instances for the canmera/network
def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    usb1 = cs.startAutomaticCapture(dev=0)
    usb2 = cs.startAutomaticCapture(dev=1)
    print("Camera is active.")

    cs.waitForever()