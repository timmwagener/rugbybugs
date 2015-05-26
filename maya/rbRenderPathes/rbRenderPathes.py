




#rbRenderPathes Module
#----------------------------------------------------

'''
Description:
Set correct render pathes for lighting file output and rnd

ToDo:
-

'''



#Import
#----------------------------------------------------
import pymel.core as pm
import maya.cmds as cmds
import os, sys






#RbRenderPathes Class
#----------------------------------------------------

class RbRenderPathes():
	
	
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#----------------------------------------------------
		
		#Debug
		self.verbose = True
		
			
	
	
	
	
	
	
	
	
	
	#Toplevel Methods
	#----------------------------------------------------
	
	
	
	#setPathLighting
	def setPathLighting(self):
		
		
		#Check if vray is loaded
		
		#exit if vray for maya plugin is not loaded
		if not(self.vrayLoaded()):
			if(self.verbose): print('Vray Plugin not loaded')
			return None
			
		#exit if vray rendersettings node doesnt exist
		if not(self.vrayRenderSettingsNode()): 
			if(self.verbose): print('Vray Rendersettings node not found')
			return None
			
		
		
		
		#Build Path
		#----------------------------------------------------
		
		
		#get scene path and fileType
		scenePath, fileType = os.path.splitext(cmds.file(query=True,sceneName=True))
		
		
		#check if file in lighting folder
		if not('lighting' in scenePath.split('/')[:-1]): 
			if(self.verbose): print('Scene is not located in a lighting directory of a shot. Rendering it would result in a nukular mayhem')
			return None
		
		
		#get scenenameShotIdentifier
		sceneNameShotIdentifierString = scenePath.split('/')[-1].split('_')[0] + '_' + scenePath.split('/')[-1].split('_')[1]
		
		
		#Iterate scenepath split list and assign shotName if match occurs
		shotName = ''
		for partString in scenePath.split('/'):
			if(partString == sceneNameShotIdentifierString): 
				shotName = partString
				break
				
		#If shotname not found set to default
		if not(shotName): shotName = 'unknownShot'
		
		#Assemble Render Path
		renderPath = 'lighting/' + shotName +'/<Scene>/<Layer>/<Scene>_<Layer>_'
				
		
		
		
		#Set Path
		#----------------------------------------------------
		
		#Get Vray rendersettings node
		vrayRenderSettingsNode = self.vrayRenderSettingsNode()
		
		pm.setAttr(vrayRenderSettingsNode.fileNamePrefix, renderPath)
	
	
		#success msg
		if(self.verbose): print('Successfully set renderpath')
	
	
	
	
	
	
	
	#setPathTesting
	def setPathTesting(self):
		
		
		#Check if vray is loaded
		
		#exit if vray for maya plugin is not loaded
		if not(self.vrayLoaded()):
			if(self.verbose): print('Vray Plugin not loaded')
			return None
			
		#exit if vray rendersettings node doesnt exist
		if not(self.vrayRenderSettingsNode()): 
			if(self.verbose): print('Vray Rendersettings node not found')
			return None
			
		
		
		
		#Build Path
		#----------------------------------------------------
		
		#get Current user
		currentUser = os.environ.get('USERNAME')
		
		#Assemble Render Path
		renderPath = currentUser +'/<Scene>/<Scene>_<Layer>_'
		
		
		#Set Path
		#----------------------------------------------------
		
		#Get Vray rendersettings node
		vrayRenderSettingsNode = self.vrayRenderSettingsNode()
		
		pm.setAttr(vrayRenderSettingsNode.fileNamePrefix, renderPath)
	
	
		#success msg
		if(self.verbose): print('Successfully set renderpath')
		
		
	
	
	
	
	
	#Methods
	#----------------------------------------------------
	
	
	
	
	
	
	
	
	
	#Shared Methods
	#----------------------------------------------------
	
	
	
	#vrayLoaded
	def vrayLoaded(self):
		#Get list of all loaded plugIns
		plugInList = pm.pluginInfo( query=True, listPlugins=True )
		
		#Return true if loaded else setStatus and return false
		if('vrayformaya' in plugInList): return True
		
		#else
		return False
		
	
	
	
	#vrayRenderSettingsNode
	def vrayRenderSettingsNode(self):
		
		#deselct all
		pm.select(cl = True)
		#select all nodes of type vraysettingsNode
		selList = pm.ls(fl = True, typ = 'VRaySettingsNode')
		
		#If selList < 1 return false and set status
		if not(selList):
			return False
		
		return selList[0]
	
	
	
	
	
	
	
	
#Execute Temp
#----------------------------------------------------

'''
from rugbyBugs.maya.rbRenderPathes import rbRenderPathes

#Reload if true
doReload = True
if(doReload): reload(rbRenderPathes)

#Create Instance
rbRenderPathesInstance = rbRenderPathes.RbRenderPathes()

#set final path
#rbRenderPathesInstance.setPathLighting()
rbRenderPathesInstance.setPathTesting()
'''


	
	
	