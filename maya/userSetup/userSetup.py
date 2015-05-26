


#userSetup.py
#------------------------------------------------------------------









#Imports
#------------------------------------------------------------------
import sys, os, shutil
import maya.mel as mel
import maya.cmds as cmds
import maya.utils






#Methods
#------------------------------------------------------------------

#getUser
def getUser():
	return os.environ.get('USERNAME')


#getUserSetupDestinationDir
def getUserSetupDestinationDir():
	
	pathStart = 'C:\\Users\\'
	username = getUser()
	pathEnd = '\\Documents\\maya\\2012-x64\\scripts'
	
	return pathStart + username + pathEnd
	

#getShelfDestinationDir
def getShelfDestinationDir():
	
	pathStart = 'C:\\Users\\'
	username = getUser()
	pathEnd = '\\Documents\\maya\\2012-x64\\prefs\\shelves'
	
	return pathStart + username + pathEnd
	
	

#copyFile
def copyFile(sourceFile, sourceDir, destinationDir):
	
	source = sourceDir + sourceFile
	
	shutil.copy(source, destinationDir)
	

#addScriptsPathes
def addScriptsPathes(scriptPathList):
	
	for scriptPath in scriptPathList:
		#Python
		sys.path.append(scriptPath)
		#MEL
		os.environ['MAYA_SCRIPT_PATH'] = os.environ['MAYA_SCRIPT_PATH'] +';' + scriptPath


	

	


#Startup Procedures
#------------------------------------------------------------------



#Copy userSetup.py
#------------------------------------------------------------------
try:
	sourceUserSetupDir = '\\\\grey09\\rugbybugs\\Production\\Scripts\\deploy\\rugbyBugs\\maya\\userSetup\\'
	sourceUserSetupFile = 'userSetup.py'

	userSetupDestinationDir = getUserSetupDestinationDir()

	copyFile(sourceUserSetupFile, sourceUserSetupDir, userSetupDestinationDir)

	#SuccessMsg
	print('Successfully copied userSetup.py')

except:
	#FailMsg
	print('Failed to copy userSetup.py')




#Copy Shelf
#------------------------------------------------------------------
try:
	sourceShelfDir = '\\\\grey09\\rugbybugs\\Production\\Scripts\\deploy\\rugbyBugs\\maya\\shelf\\'
	sourceShelfName = 'shelf_RugbyBugs.mel'

	shelfDestinationDir = getShelfDestinationDir()

	copyFile(sourceShelfName, sourceShelfDir, shelfDestinationDir)

	#SuccessMsg
	print('Successfully copied shelf')

except:
	#FailMsg
	print('Failed to copy shelf')
	
	

	



#Add Project Scripts Location
#------------------------------------------------------------------
try:
	scriptPathList = ['\\\\grey09\\rugbybugs\\Production\\Scripts\\deploy', '\\\\grey09\\rugbybugs\\Production\\Scripts\\deploy\\rugbyBugs\\maya\\scripts']
	addScriptsPathes(scriptPathList)

	#SuccessMsg
	print('Successfully added scriptpath list')

except:
	#FailMsg
	print('Failed to add scriptpath list')
	
	

	
	

	
#Add Icons Path
#------------------------------------------------------------------	

try:
	iconsPathList = [r'//grey09/rugbybugs/Production/Scripts/deploy/rugbyBugs/maya/icons']
	
	for iconPath in iconsPathList:
		os.environ['XBMLANGPATH'] = os.environ['XBMLANGPATH'] +';' + iconPath
	
	#SuccessMsg
	print('Successfully added Icons Path list')
	
	
except:
	#FailMsg
	print('Failed to add Icons Path list')

	
	


	
	
#Add Preset Path
#------------------------------------------------------------------	

try:
	
	#presetPathList
	presetPathList = [r'//grey09/rugbybugs/Production/Scripts/deploy/rugbyBugs/maya/presets']
	
	for presetPath in presetPathList:
		os.environ['MAYA_PRESET_PATH'] = os.environ['MAYA_PRESET_PATH'] +';' + presetPath
	
	#SuccessMsg
	print('Successfully added Preset Path list')
	
	
except:
	#FailMsg
	print('Failed to add Preset Path list')	


	

	

#Add PlugIn Path
#------------------------------------------------------------------	

try:
	plugInPathList = [r'//grey09/rugbybugs/Production/Scripts/deploy/rugbyBugs/maya/plugins']
	
	#Add custom test path if user is twagener
	if(getUser() == 'twagener'): plugInPathList.append('H:/scripts/temp/mayaPluginsTest')
	
	for plugInPath in plugInPathList:
		os.environ['MAYA_PLUG_IN_PATH'] = os.environ['MAYA_PLUG_IN_PATH'] +';' + plugInPath
	
	#SuccessMsg
	print('Successfully added PlugIn Path list')
	
	
except:
	#FailMsg
	print('Failed to add PlugIn Path list')
	
	

	
	
#Load PlugIns
#------------------------------------------------------------------	

try:
	
	
	
	#PlugIn List
	plugInList = ['DisplaceD.mll', 'rbRoll.py', 'cvShapeInverter.py', 'poseDeformer.mll', 'poseReader.mll', 'resetSkinJoint.mll', 'objExport.mll', 'AbcExport.mll', 'AbcImport.mll', 'OpenEXRLoader.mll']
		
	#iterate plugInList and load plugin shouldnt it be already loaded
	for plugIn in plugInList:
			
		try:
			if not(cmds.pluginInfo(plugIn , query = True, loaded = True)):
				cmds.loadPlugin(plugIn)
				print('->Successfully loaded ' +plugIn +' plugin')
			else:
				print('->Skipped loading ' +plugIn +' plugin. Plugin was already loaded.')
		except:
			print('->Error loading ' +plugIn +' plugin')
			
			
		
		
	#loadPluginsDeferred
	def loadPluginsDeferred():
		
		#plugInList
		plugInList = ['iCollide.mll', 'iDisplace.mll','iSkinDeform.mll', 'vrayformaya.mll']
		
		#iterate pluginList and load
		for pluginName in plugInList:
			try:
				if not(cmds.pluginInfo(pluginName , query = True, loaded = True)):
					cmds.loadPlugin(pluginName)
					#Print to console instead of script editor
					sys.__stdout__.write('->Successfully loaded ' +pluginName +' deferred\n')
				else:
					sys.__stdout__.write('->Skipped loading ' +pluginName +' deferred. Plugin was already loaded\n')
			except:
				sys.__stdout__.write('->Error loading ' +pluginName +' deferred\n')
	
	cmds.evalDeferred(loadPluginsDeferred)
	
	
except:
	#FailMsg
	print('->Failed to load RugbyBugs Plugins')





#Set Project
#------------------------------------------------------------------
try:
	mel.eval(' setProject "//grey09/rugbybugs/Production/3d/maya"')

	#SuccessMsg
	print('Successfully set Rugby Bugs project')

except:
	#FailMsg
	print('Failed to set Rugby Bugs project')
	
	
	


#Set Grid
#------------------------------------------------------------------

try:
	
	#setGrid
	def setGridRugbyBugsDefault():
		#set correct grid units and display settings
		cmds.grid(spacing = 5, divisions = 5, size = 10)
		cmds.displayColor( 'gridHighlight', 12, dormant=True )
		cmds.displayColor( 'grid', 3, dormant=True )
		#Turn grid on by default
		gridState = cmds.grid( toggle=True, q=True )
		if not(gridState): cmds.grid( toggle = True )
		
		#Print to console instead of script editor
		sys.__stdout__.write('Successfully set Rugby Bugs standard grid deferred\n')
	
	#eval deferred
	cmds.evalDeferred(setGridRugbyBugsDefault)
	

except:
	#FailMsg
	print('Failed to set Rugby Bugs standard grid')
	
	
	

	
	
	

	
	
	





