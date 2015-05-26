




#rugbyBugs init.py (startup procedures)
#------------------------------------------------------------------





#Imports
#------------------------------------------------------------------
import sys, os







#Methods
#------------------------------------------------------------------

#setRugbyBugsPluginPathes
def setRugbyBugsPluginPathes(pluginPathList):
	
	for pluginPath in pluginPathList:
		nuke.pluginAppendPath(pluginPath)





	
	
#Startup Routine
#------------------------------------------------------------------


#Set scripts path
#------------------------------------------------------------------
try:
	rugbyBugsPluginPathList = ['\\\\grey09\\rugbybugs\\Production\\Scripts\\deploy']
	setRugbyBugsPluginPathes(rugbyBugsPluginPathList)
	
	#SuccessMsg
	print('Successfully set Plugin Pathes')
	
except:
	#FailMsg
	print('Error setting plugin pathes')
	


	
	



