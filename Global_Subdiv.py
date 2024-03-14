#======================================================================================================================
#	Global Arnold Subdivision Modifier
#======================================================================================================================
# 
# DESCRIPTION:
#	This script allows to change the subdivision type to all selected objects
# 
# REQUIRES:
# 	Select the objects before running
# 
# AUTHOR:
# 	Sebastian Camargo Buendia ---- camargo3d@gmail.com
#	
#	https://sebascamargo.myportfolio.com/home
# 	Copyright 2023 Sebastian Camargo Buendia - All Rights Reserved.
# 
# CHANGELOG:
#	0.1 - 10/28/2023 - Creation of Interface and Subdiv options
# ====================================================================================================================


import maya.cmds as cmds

#Creates the constants for the UI's dimensions

WIDTH = 250
HEIGHT = 100

#Stores the list of selected objects
meshSel = cmds.ls(sl = True)
#Creates variables for the attributes to be changed
sSubdiv = ".aiSubdivType"
siter = ".aiSubdivIterations"


def openWin():
    
    # Check if window exists, if it does, delete
    if cmds.window("Global_Subdiv", exists = True):
        cmds.deleteUI("Global_Subdiv")
    cmds.window("Global_Subdiv", w=WIDTH, h=HEIGHT, sizeable = False )
    cmds.rowColumnLayout( adjustableColumn=True, numberOfColumns=1,columnAttach=(1, 'right', 0), columnWidth=[(1, 105), (2, 150), (3, 255)])
    #Crates a title
    cmds.text(label='Apply subdivision to all selected meshes',w=50,al="center",h=50)
    #Creates dropdown menu
    cmds.optionMenu("UI_Subdiv", w = 20, label = "Subdivision Type:")
    cmds.menuItem(label = "None")
    cmds.menuItem(label = "Catclark")
    cmds.menuItem(label = "Linear")
    #Executes the slider function
    sliderGRP()
    #This creates a button that executes the scripts main function
    cmds.button('Apply',w=2,c= selSubDiv)
    #Opens window
    cmds.showWindow( "Global_Subdiv" )
    return

#This function creates the slider and assigns it to global var
def sliderGRP():
    global iteVar
    iteVar = cmds.floatSliderGrp(label = 'Subdiv Iterations:', f=True,max = 10, min = 0,fieldMaxValue = 20,fieldMinValue = 0,fs=1,ss=1,s=1,pre=0,cl3=['left','left','left'],cw3=[92,30,30])
    
#This function takes the iteVar slider current value and turns it into an integer
def sliderInt():
    global iteNum
    floatiteNum = cmds.floatSliderGrp(iteVar, q=True, v=True)
    iteNum = int(floatiteNum)
    
#This function executes the command
def selSubDiv(*args):
    
    #First the sliderInt function is executed to create the iteNum value
    sliderInt()
    #Then a loop with if conditions is used to decide what type of subdivision is used
    for c in meshSel:
        sdType = cmds.optionMenu("UI_Subdiv", query=True, value=True)
        if sdType == "None":
            cmds.setAttr( c + sSubdiv, 0)
        elif sdType == "Catclark":
            cmds.setAttr( c + sSubdiv, 1)
        elif sdType == "Linear":
            cmds.setAttr( c + sSubdiv, 2)
    #Another loop pulls the iteNum value (slider number) to apply the Subdiv Iterationn    
    for d in meshSel:
        cmds.setAttr( d + siter, iteNum)
    #Deselects objects and closes window
    cmds.select(cl=True)
    cmds.deleteUI("Global_Subdiv")    
    print('Done')

def main():
    openWin()
    return

main()