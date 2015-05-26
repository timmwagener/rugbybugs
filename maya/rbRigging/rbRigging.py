




#rbRigging Module
#------------------------------------------------------------------

'''
Description:
Module that provides an interface to all rigging modules and functionalities
'''

'''
ToDo:

'''




#Imports
#------------------------------------------------------------------
import os, sys
import maya.cmds as cmds
import pymel.core as pm



#Reload boolean
doReload = True


#rbFootRigA
from rugbyBugs.maya.rbRigging import rbFootRigA
if(doReload): reload(rbFootRigA)

#rbFootRigB
from rugbyBugs.maya.rbRigging import rbFootRigB
if(doReload): reload(rbFootRigB)

#rbDynamicChain
from rugbyBugs.maya.rbRigging import rbDynamicChain
if(doReload): reload(rbDynamicChain)

#rbIkFkBlendArm
from rugbyBugs.maya.rbRigging import rbIkFkBlendArm
if(doReload): reload(rbIkFkBlendArm)

#rbDynamicChainFromCurves
from rugbyBugs.maya.rbRigging import rbDynamicChainFromCurves
if(doReload): reload(rbDynamicChainFromCurves)



#RbRigging class
#------------------------------------------------------------------

class RbRigging():
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		
		#footRigA
		self.footRigAInstance = rbFootRigA.RbFootRigA()
		
		#footRigB
		self.footRigBInstance = rbFootRigB.RbFootRigB()
		
		#dynamicChain
		self.dynamicChainInstance = rbDynamicChain.RbDynamicChain()
		
		#ikFkBlendArm
		self.ikFkBlendArmInstance = rbIkFkBlendArm.RbIkFkBlendArm()
		
		#dynamicChainFromCurves
		self.dynamicChainFromCurvesInstance = rbDynamicChainFromCurves.RbDynamicChainFromCurves()


	
	
	#Toplevel Methods
	#------------------------------------------------------------------
	
	
	#FootRigA
	#-----------------------------------------------
	
	#createFootRigAPosLocators
	def createFootRigAPosLocators(self , prefix = ''):
		self.footRigAInstance.createPositionLocators(prefix)
		
	#createFootRigA
	def createFootRigA(self, prefix = ''):
		self.footRigAInstance.createFootRigA(prefix)
		
		
		
		
	#FootRigB
	#-----------------------------------------------
	
	#createFootRigBPosLocators
	def createFootRigBPosLocators(self , prefix = ''):
		self.footRigBInstance.createFootRigBLocators(prefix)
		
	#createFootRigB
	def createFootRigB(self, prefix = ''):
		self.footRigBInstance.createFootRigB(prefix)
		
		
		
		
	#DynamicChain
	#-----------------------------------------------
	
	#createDynamicChainLocators
	def createDynamicChainLocators(self , prefix = ''):
		self.dynamicChainInstance.createDynamicChainLocators(prefix)
		
	#createDynamicChain
	def createDynamicChain(self, prefix = '', jointCount = 5):
		self.dynamicChainInstance.createDynamicChain(prefix, jointCount)
	

	
	#IkFkBlendArm
	#-----------------------------------------------
	
	#createIkFkBlendArmLocators
	def createIkFkBlendArmLocators(self , prefix = ''):
		self.ikFkBlendArmInstance.createIkFkBlendArmLocators(prefix)
		
	#createIkFkBlendArm
	def createIkFkBlendArm(self, prefix = ''):
		self.ikFkBlendArmInstance.createIkFkBlendArm(prefix)
		
		
	
	#DynamicChainFromCurves
	#-----------------------------------------------
		
	#createDynamicChainFromCurves
	def createDynamicChainFromCurves(self, prefix = ''):
		self.dynamicChainFromCurvesInstance.createDynamicChainFromCurves(prefix)
	
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	#Shared Methods
	#------------------------------------------------------------------
	
	
	
	
	
	
	
	
#Execute TMP
#------------------------------------------------------------------
'''
TMP
'''
	
	
