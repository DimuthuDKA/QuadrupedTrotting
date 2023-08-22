import mob as m
import time
import math
import matlab.engine
import numpy as np

import matlab.engine

eng = matlab.engine.start_matlab()
eng.cd(r'C:\Users\Dimuthu\OneDrive - DePaul University\Depaul University\Research\4-Legged Robot\Trotting\PybulletWork\Dimuthumatlab', nargout=0)
# C:\Users\Dimuthu\OneDrive - DePaul University\Depaul University\Research\4-Legged Robot\Trotting\PybulletWork\Dimuthumatlab

sim = m.Simulation("walker", gui=True)
sim.start()


#try using pyevolve
sim.setFollowCamera(True)
'''
sim.frontRight(0.2, 0, 0)
sim.frontLeft(0.2, 0, 0)
sim.rearRight(0.2, 0, 0)
sim.rearLeft(0.2, 0, 0)
'''


phase = 0

turnRadius = matlab.double([2])
turnDirection = "RightIP"

if phase == 0:
    r = 0.03
    T = 1
    x0 = 0
    y0 = -0.05
    zeta = 2.5*math.pi/4 
    if turnDirection == "RightIP" or turnDirection == "LeftIP":
        r = 0.03
elif phase == 1:
    r = 0.03
    T = 1
    x0 = 0
    y0 = -0.05
    zeta = 2.5*math.pi/4 
    if turnDirection == "RightIP" or turnDirection == "LeftIP":
        r = 0.04
elif phase == 2:
    r = 0.03
    T = 1
    x0 = 0
    y0 = -0.05
    zeta = 2.5*math.pi/4
    if turnDirection == "RightIP" or turnDirection == "LeftIP" or turnDirection == "Right" or turnDirection == "Left":
        r = 0.035
elif phase == 4:
    r = 0.02
    T = 1
    x0 = 0
    y0 = -0.05
    zeta = 2.5*math.pi/4
    if turnDirection == "RightIP" or turnDirection == "LeftIP":
        r = 0.03
    
    
def leg0phaseWalkFunc(t, i):
    gaitInput = matlab.double([t,T,x0,y0,r,zeta])
    XY = eng.phaseGaitCalc(gaitInput, turnRadius, turnDirection,  0, phase)
    curveParams = eng.invKin(XY)
    theta = np.float32(curveParams[0][0])
    phi = np.float32(curveParams[1][0])
    (strength, direction, expansion) = (phi, theta, 0)
    direction = -math.pi-direction;
    return (strength, direction, expansion)
    
def leg1phaseWalkFunc(t, i):
    gaitInput = matlab.double([t,T,x0,y0,r,zeta])
    XY = eng.phaseGaitCalc(gaitInput, turnRadius, turnDirection, 1, phase)
    curveParams = eng.invKin(XY)
    theta = np.float32(curveParams[0][0])
    phi = np.float32(curveParams[1][0])
    (strength, direction, expansion) = (phi, theta, 0)
    return (strength, direction, expansion)
    
def leg2phaseWalkFunc(t, i):
    gaitInput = matlab.double([t,T,x0,y0,r,zeta])
    XY = eng.phaseGaitCalc(gaitInput, turnRadius, turnDirection, 2, phase)
    curveParams = eng.invKin(XY)
    theta = np.float32(curveParams[0][0])
    phi = np.float32(curveParams[1][0])
    (strength, direction, expansion) = (phi, theta, 0)
    return (strength, direction, expansion)

def leg3phaseWalkFunc(t, i):
    gaitInput = matlab.double([t,T,x0,y0,r,zeta])
    XY = eng.phaseGaitCalc(gaitInput, turnRadius, turnDirection, 3, phase)
    curveParams = eng.invKin(XY)
    theta = np.float32(curveParams[0][0])
    phi = np.float32(curveParams[1][0])
    (strength, direction, expansion) = (phi, theta, 0)
    direction = -math.pi-direction;
    return (strength, direction, expansion)
    
def leg4phaseWalkFunc(t, i):
    gaitInput = matlab.double([t,T,x0,y0,r,zeta])
    XY = eng.phaseGaitCalc(gaitInput, turnRadius, turnDirection, 4, phase)
    curveParams = eng.invKin(XY)
    theta = np.float32(curveParams[0][0])
    phi = np.float32(curveParams[1][0])
    (strength, direction, expansion) = (phi, theta, 0)
    direction = direction - math.pi/2
    return (strength, direction, expansion)

def walkfunc(t, i):
    result = (i + t) * 2 * math.pi
    #print(result)
    return result
    
def altfunc(t, i):
	return (i + t) * 2 * math.pi + math.pi

def slither(t, i):
	# comment
	return (math.sin(t * 2 * math.pi + 0) * 0.3)

def slither2(t, i):
	return (math.sin(t * 2 * math.pi + 1 * math.pi / 3+math.pi) * 0.3)

def slither3(t, i):
	return (math.sin(t * 2 * math.pi + 2 * math.pi /3) * 0.3)

# These are frequency values that I found to have worked well
trotFrequency = 1
onePhaseFrequency = 1
twoPhaseFrequency = 1
fourPhaseFrequency = 1.4

sim.registerPeriodical(sim.frontRight, leg0phaseWalkFunc, trotFrequency)
sim.registerPeriodical(sim.frontLeft, leg1phaseWalkFunc, trotFrequency)
sim.registerPeriodical(sim.rearLeft, leg2phaseWalkFunc, trotFrequency)
sim.registerPeriodical(sim.rearRight, leg3phaseWalkFunc, trotFrequency)
sim.registerPeriodical(sim.spine, leg4phaseWalkFunc, trotFrequency)



#f=.5;
#sim.registerPeriodical(sim.headStrength, slither, f)
#sim.registerPeriodical(sim.middleStrength, slither2, f)
#sim.registerPeriodical(sim.tailStrength, slither3, f)

while True:
	time.sleep(.1)
	#print(sim.getPosition())