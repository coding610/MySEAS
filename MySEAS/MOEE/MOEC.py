from MySEAS.MOEE.MOES import *

import threading
from typing import Any

class _MOEC:
    def __init__(self) -> None:
        self.scenes = {}
        self.sceneThreads = {}
        self.targetedScene = None

        self.coreModules = {}

    ###############################################################################################################################################################################
    def targetCoreModule(self, coreModuleInit:Any): # TODO: better name
        self.coreModules[coreModuleName] = coreModuleInit

    ###############################################################################################################################################################################
    def newScene(self, sceneName:str, isTargeted:bool=True, frameLimit:int=60) -> Any:
        self.scenes[sceneName] = MOES(frameLimit, self.coreModules)
        if isTargeted:
            self.targetedScene = {'SceneInit': self.scenes[sceneName], 'SceneName': sceneName, 'SceneThread': threading.Thread(name=sceneName, target=self.scenes[sceneName].update)}
        return self.targetedScene

    ###############################################################################################################################################################################
    def targetScene(self, sceneName:str) -> Any:
        self.stopMOEC()
        try:
            self.targetedScene = [self.scenes[sceneName], sceneName, threading.Thread(name=sceneName, target=self.scenes[sceneName].update)]
            self.startMOEC()
        except AttributeError:
            print("MOEC :: TargetScene() :: Error :: No Scene found with the name " + sceneName)

    ###############################################################################################################################################################################
    def getScene(self, sceneName:str="targetedScene"):
        try:
            if sceneName == "targetedScene": return self.targetedScene
            else: return self.scenes[sceneName]
        except AttributeError:
            print("MOEC :: getScene() :: Error :: No Scene found with the name " + sceneName)

    ###############################################################################################################################################################################
    def startMOEC(self):
        self.targetedScene['SceneThread'].start() # Started thread

    ###############################################################################################################################################################################
    def stopMOEC(self):
        self.targetedScene['SceneThread'].join() # Stop thread # Stop thread

MOEC = _MOEC()
