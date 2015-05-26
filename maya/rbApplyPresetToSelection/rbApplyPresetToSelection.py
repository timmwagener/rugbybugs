




#rbApplyPresetToSelection Module
#------------------------------------------------------------------

'''
Description:
Applies an Attribute editor preset to a selection of nodes of the same type 
'''

'''
ToDo:

'''




#Imports
#------------------------------------------------------------------
import pymel.core as pm
import os







#RbApplyPresetToSelection class
#------------------------------------------------------------------

class RbApplyPresetToSelection():
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		
		


	
	
	#TopLevel Methods
	#------------------------------------------------------------------
	
	
	#applyPresetToSelection
	def applyPresetToSelection(self, presetName = ''):
		
		#check if presetName given
		if not(presetName):
			if(self.verbose): print('No preset name given, please enter a preset name.')
			return None
			
		
		#get selectionList
		selectionList = pm.ls(sl = True, fl = True)
		pm.select(cl = True)
		
		#Check if len(selectionList) == 0
		if not(len(selectionList)):
			if(self.verbose): print('No objects selected. Please select at least one object.')
			return None
		
		#get presetPathList
		presetPathList = os.environ['MAYA_PRESET_PATH'].split(';')
		
		
		#append standard user presets directory
		presetPathStart = 'C:/Users/'
		username = os.environ.get('USERNAME')
		presetPathEnd = '/Documents/maya/2012-x64/presets'
		presetPathList.append(presetPathStart +username +presetPathEnd)
		
		
		
		#if verbose print presetPathList
		if(self.verbose):
			print('Preset Path List:')
			for path in presetPathList:
				print(path)
		
		
		
		
		
		
		
		#Iterate selectionList
		for object in selectionList:
			
			#get nodeType
			nodeTypeName = pm.nodeType(object)
			
			#matchingPresetFolderList
			matchingPresetFolderList = []
			
			
			#Check if presetFolder for nodetype exists, if so store in matchingPresetFolderList
			for presetPath in presetPathList:
				presetPathNodeType = presetPath +'/' +'attrPresets' +'/' + nodeTypeName
				if(os.path.exists(presetPathNodeType)):
					matchingPresetFolderList.append(presetPathNodeType)
			
			
			#Check if matchingPresetFolderList == 0 if so continue
			if not(matchingPresetFolderList):
				if(self.verbose): print('No nodeType preset folders for selected nodeType:' +nodeTypeName +' found in toplevel preset folders')
				continue
			
			
			#Execution Boolean
			executeNodePreset = False
			presetFilePath = ''
			
			#Check if preset exists in node folder, and if so set execution boolean
			for nodeFolderPath in matchingPresetFolderList:
				presetFilePath = nodeFolderPath + '/' +presetName +'.mel'
				if(os.path.exists(presetFilePath)):
					executeNodePreset = True
					break
			
			
			
			
			#Apply preset if executeBool
			if(executeNodePreset):
				
				#Correct ServerPath Beginning for MEL
				if(presetFilePath[0:4] == '////'): '\/\/' +presetFilePath[4:]
				
				pm.mel.eval('applyPresetToNode "' +object.name() +'" "" "" "' + presetFilePath +'" 1;')
				if(self.verbose): print('Successfully applied preset: ' +presetName +' to ' +object.name())
			else:
				if(self.verbose): print('No preset of name: ' +presetName +' found for ' +object.name())
			
			
			
	
	
	#printAvailablePresets
	def printAvailablePresets(self):
		
		#get presetPathList
		presetPathList = os.environ['MAYA_PRESET_PATH'].split(';')
		
		#append standard user presets directory
		presetPathStart = 'C:/Users/'
		username = os.environ.get('USERNAME')
		presetPathEnd = '/Documents/maya/2012-x64/presets'
		presetPathList.append(presetPathStart +username +presetPathEnd)
		
		
		#iterate each preset path and print its content
		for presetPath in presetPathList:
			
			
			#presetTopPath
			presetTopPath = presetPath +'/' +'attrPresets' + '/'
			
			if(os.path.exists(os.path.dirname(presetTopPath))):
				
				#Print Top Directory
				print('\n')
				print('Preset top directory: ' +presetTopPath)
				print('--------------------------')
				
				
				
				#get all directories below presetTopPath
				nodeTypePresetDirectoriesList = []
				
				#iterate content of presetTopPath and append to nodeTypePresetDirectoriesList if content is a dir
				for itemName in os.listdir(os.path.dirname(presetTopPath)):
					presetNodeTypePath = presetTopPath  + itemName
					if(os.path.isdir(presetNodeTypePath)): nodeTypePresetDirectoriesList.append(presetNodeTypePath)
					
					
				#iterate nodeTypePresetDirectoriesList and print content of each directory
				for nodeTypePresetDirectory in nodeTypePresetDirectoriesList:
					
					#print nodeType of directory
					print('NodeType: ' +nodeTypePresetDirectory.split('/')[-1])
					
					
					#Iterate and print content of nodyType directory
					for presetName in os.listdir(os.path.dirname(nodeTypePresetDirectory +'/')):
						print('--> ' +presetName)
					
				
					
				print('--------------------------')
				print('--------------------------')
	
	
	
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------
	
	
	
	
	
	
	
	
	
	
#Test Execution
#------------------------------------------------------------------
'''
from rugbyBugs.maya.rbApplyPresetToSelection import rbApplyPresetToSelection

doReload = True
if(doReload): reload(rbApplyPresetToSelection)


rbApplyPresetToSelectionInstance = rbApplyPresetToSelection.RbApplyPresetToSelection()
#rbApplyPresetToSelectionInstance.applyPresetToSelection('rbAntLegStroke01')
rbApplyPresetToSelectionInstance.printAvailablePresets()

'''






	
	
