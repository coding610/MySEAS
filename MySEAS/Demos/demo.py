import MySEAS
import time


# COREMODS
MySEAS.MOEC.targetCoreModule('Window', MySEAS.MOEW())

# SCENES
MySEAS.MOEC.newScene(sceneName="mainScene", isTargeted=True)

# Start scene
MySEAS.MOEC.startMOEC()
time.sleep(1)
MySEAS.MOEC.stopMOEC()
