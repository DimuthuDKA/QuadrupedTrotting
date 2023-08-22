# QuadrupedTrotting
Run QuadrupedTrottingMainFile.m for generating trotting trajectories as per the below instructions. 

This is my main file I use to generate curve parameters for different gaits. Make sure this file stays with fwdKin.m, GaitCalc.m, invKin.m, phaseGaitCalc.m, plotQuadruped.m, Rx.m, Ry.m, Rz.m
Set generateAnimation to 1 if you want to have animations. If 0, these will skip the center of mass calculations anyway. This also is quite time intensive
Set makeGraphs to 1 if you want to save all the output graphs for X Y positions and curve parameters as files in the working directory.
Set writeCurveParameterFiles to 1 if you want to save the curve parameters into named files based on the phase and and turn direction.
Check the value for n to make sure you are generating the number of "frames" you want.
Check values for r, x0, y0, and zeta to customize your fundamental shape.
Set del to your desired delay between .gif frames so they are a nice speed.
Change the phase array to set which phases you want to generate curve parameters for.
Change the turnDirection array to set which types of turns you want to generate for each phase. This can either be "Trotting", "TurnRight", or "TurnLeft".
Run it.
