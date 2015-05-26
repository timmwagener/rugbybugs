

#MayaFunctionality
#------------------------------------------------------------------
'''
Maya Functionality
'''

'''
ToDo:
'''


#Import
#------------------------------------------------------------------
import maya.cmds as cmds
import maya.OpenMayaUI as openMayaUi
import maya.OpenMaya as openMaya
import sip
from PyQt4 import QtGui, QtCore
import os



	
#Functions
#------------------------------------------------------------------	


#Make Dockable
#------------------------------------------------------------------

#makeDockable
def makeDockable(childWidget, areaName, width, label):
	
	slider = cmds.floatSlider() #some throwaway control, feel free to delete this when you're done.
	dock = cmds.dockControl(l = label, content=slider,  area = areaName, w = width ) #Returns the string path to the dock control. The control is a QDockWidget under the hood.
	dockPt = openMayaUi.MQtUtil.findControl(dock) #Find the pointer to the dock control
	dockWidget = sip.wrapinstance(long(dockPt), QtCore.QObject) #Get that pointer as a Qt widget
	childWidget.setParent(dockWidget)
	dockWidget.setWidget(childWidget) #Set the docked widget to be your custom control.




	