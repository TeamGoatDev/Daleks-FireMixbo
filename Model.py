#!/usr/bin/python
# -*- coding: utf-8 -*-
#Python 3.x
from ReturnCodes import *
from Gameboard import *
from GameObjects import *
from UserActions import *
import random

class Model(object):
    """ """

    def __init__(self):
        super(Model, self).__init__()
        self.level = 1
        self.doctor = Doctor()
        self.daleks = []
        self.scrapHeaps = []

        self.reset()


    def reset(self):
        self.scrapHeaps = []
        self.initGameboard(30,20)
        self.initDoctor()
        self.doctor.nbZappeurs += 1
        self.initDalekArmy()

    def changeLevel(self):
        self.level += 1
        self.reset()
        
    def initGameboard(self,x,y):
        self.gameboard = Gameboard(x,y)

    def initDalekArmy(self):
        self.daleks = []
        for i in range(self.level*5):
            self.daleks.append(Dalek())

        for i in range(len(self.daleks)):
            collisionFound = 1
            while(collisionFound == 1):
                x = random.randint(0,self.gameboard.x-1)
                y = random.randint(0,self.gameboard.y-1)

                positionTempo = Position(x,y)
                collisionFound = 0

                for j in range(i):
                    if positionTempo == self.daleks[j].position:
                        collisionFound = 1

                if positionTempo == self.doctor.position:
                    collisionFound = 1

            self.daleks[i].position = positionTempo


    def initDoctor(self):
        self.doctor.position.x = int(self.gameboard.x/2)
        self.doctor.position.y = int(self.gameboard.y/2)

    def isDoctorSafe(self, positionTempo):
        for scrap in self.scrapHeaps:
            if scrap.position.x == positionTempo.x and scrap.position.y == positionTempo.y:
                return False #PAS SAFE

        for i in range(3):
            for j in range(3):
                x = -1+i
                y = -1+j

                #print("(",x,y,")")
                posDalekRange = Position(positionTempo.x+x,positionTempo.y+y)

                if self.getDaleksAtPosition(posDalekRange):
                    return False 

        return True


    def zap(self):
        if self.doctor.nbZappeurs > 0:
            self.doctor.nbZappeurs -= 1
            N = self.detTargetDoctorPos(UserAction.MOVE_N)
            S = self.detTargetDoctorPos(UserAction.MOVE_S)
            E = self.detTargetDoctorPos(UserAction.MOVE_E)
            W = self.detTargetDoctorPos(UserAction.MOVE_W)
            NW = self.detTargetDoctorPos(UserAction.MOVE_NW)
            NE = self.detTargetDoctorPos(UserAction.MOVE_NE)
            SW = self.detTargetDoctorPos(UserAction.MOVE_SW)
            SE = self.detTargetDoctorPos(UserAction.MOVE_SE)

            zapPos = [N, S, E, W, NW, NE, SW, SE]
            for position in zapPos:
                deadDaleks = self.getDaleksAtPosition(position)
                if deadDaleks:
                    for dalek in deadDaleks:
                        self.killDalek(dalek)
        return ReturnCodes.SUCCESS



    def teleportDoctor(self):

        collisionFound = 0
        while not collisionFound:
            x = random.randint(0,self.gameboard.x-1)
            y = random.randint(0,self.gameboard.y-1)

            positionTempo = Position(x,y)
            collisionFound = self.getDaleksAtPosition(positionTempo)
            if not collisionFound:
                collisionFound = self.isDoctorSafe(positionTempo)
                
        self.doctor.position = positionTempo
        return ReturnCodes.SUCCESS



    def moveDoctor(self, direction):
        """ the direction parameter is a UserAction MOVE_* """
        targetPosition = self.detTargetDoctorPos(direction)
        if self.canDoctorMove(targetPosition):
            self.doctor.position = targetPosition
            return ReturnCodes.SUCCESS
        else:
            return ReturnCodes.INVALID_MOVE
            





    def detTargetDoctorPos(self, direction):
        targetPosition = None
        if direction == UserAction.MOVE_N:
            targetPosition = Position(0,-1)
        if direction == UserAction.MOVE_S:
            targetPosition = Position(0,1)
        if direction == UserAction.MOVE_E:
            targetPosition = Position(1,0)
        if direction == UserAction.MOVE_W:
            targetPosition = Position(-1,0)

        if direction == UserAction.MOVE_NW:
            targetPosition = Position(-1,-1)
        if direction == UserAction.MOVE_NE:
            targetPosition = Position(1,-1)
        if direction == UserAction.MOVE_SW:
            targetPosition = Position(-1,1)
        if direction == UserAction.MOVE_SE:
            targetPosition = Position(1,1)
        if direction == UserAction.MOVE_NULL:
            targetPosition = Position(0,0)
        targetPosition.add(self.doctor.position)
        return targetPosition



    def canDoctorMove(self, position):
        if position.x < 0 or position.x >= self.gameboard.x-1:
            return False
        if position.y < 0 or position.y >= self.gameboard.y-1:
            return False
        if self.isDoctorDead(position): #Test whether or not the doctor is commiting suicide
            return False
        return True



    def moveDaleks(self):
        for dalek in self.daleks:
            dalek.move(self.doctor.position)
        self.detectCollision()
        if self.isDoctorDead(self.doctor.position):
            return ReturnCodes.DEAD_DOCTOR
        elif not self.daleks:
            self.scrapHeaps = []
            return ReturnCodes.END_WAVE
        else:
            return ReturnCodes.SUCCESS

    def createScrapHeap(self, position):
        scrapHeap = ScrapHeap()
        scrapHeap.position = position
        self.scrapHeaps.append(scrapHeap)

    def killDalek(self, dalek):
        self.daleks.remove(dalek)
        self.doctor.nbPoints += 12

    def getDaleksAtPosition(self, position):
        daleksAtPos = []
        for dalek in self.daleks:
            if dalek.position.x == position.x and dalek.position.y == position.y:
                daleksAtPos.append(dalek)
        return daleksAtPos

    def detectCollision(self):
                for dalek in self.daleks:
                    deadDaleks = self.getDaleksAtPosition(dalek.position)
                    deadDaleks.remove(dalek)
                    if deadDaleks:
                        for deadDalek in deadDaleks:
                            self.createScrapHeap(dalek.position)
                            self.killDalek(deadDalek)

                for scrapHeap in self.scrapHeaps:
                    deadDaleks = self.getDaleksAtPosition(scrapHeap.position)
                    if deadDaleks:
                        for deadDalek in deadDaleks:
                            self.killDalek(deadDalek)





    def isDoctorDead(self, doctorPosition):
        for dalek in self.daleks:
            if dalek.position.x == doctorPosition.x and  dalek.position.y == doctorPosition.y:
                return True
        for scrapHeap in self.scrapHeaps:
            if scrapHeap.position.x == doctorPosition.x and  scrapHeap.position.y == doctorPosition.y:
                return True
