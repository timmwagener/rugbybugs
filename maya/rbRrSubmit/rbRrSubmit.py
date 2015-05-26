






#rbRrSubmit Module
#------------------------------------------------------------------

'''
Description:
Saves and submits the current scene to the rrSubmitter
'''

'''
ToDo:

'''




#Imports
#------------------------------------------------------------------
import os, sys
import maya.cmds as cmds
import pymel.core as pm





#RbRrSubmit class
#------------------------------------------------------------------

class RbRrSubmit():
	
	#Constructor / Main Procedure
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		
		
		
	
	

	#Methods
	#------------------------------------------------------------------
	

	#saveAndSubmitToRr
	@staticmethod
	def saveAndSubmitToRr(*args, **kwargs):
		try:
			
			
			# Get the current scene name.
			curName, curExt = os.path.splitext(cmds.file(query=True, sceneName=True))
			
			# Determine the file type.
			if(curExt == ".ma"): curType = "mayaAscii"
			if(curExt == ".mb"): curType = "mayaBinary"
			
			#save file
			cmds.file(f=True, type=curType, save=True)
			
			#Check if animation in Render settings is on, otherwise print warning
			if(pm.getAttr('defaultRenderGlobals.animation') == 0): 
				print('No Animation specified in Renderglobals. RRSubmitter will not open file to get settings')
				#print to output window
				sys.__stdout__.write('No Animation specified in Renderglobals. RRSubmitter will not open file to get settings \n')
			
			#get rrSubmiterDir
			rrSubmiterDir = os.environ['RR_Root']
			
			#get scenePath
			scenePath = cmds.file(q = True, sceneName = True)
			
			#Check if scene path true, if so start submit
			if (scenePath):
				if ((sys.platform.lower() == "win32") or (sys.platform.lower() == "win64")):
					os.system(rrSubmiterDir+"\\win__rrSubmitter.bat  \""+scenePath+"\"")
				elif (sys.platform.lower() == "darwin"):
					os.system(rrSubmiterDir+"/bin/mac/rrSubmitter.app/Contents/MacOS/rrSubmitter  \""+scenePath+"\"")
				else:
					os.system(rrSubmiterDir+"/lx__rrSubmitter.sh  \""+scenePath+"\"")
			
			print('Successfully submited scene to RRSubmitter')
			
		except:
			print('Error submitting scene to RRSubmitter')
	
	
	#Shared Methods
	#------------------------------------------------------------------
	
	
	
	
	
	
	
	
#Execute TMP
#------------------------------------------------------------------
'''
from rugbyBugs.maya.rbRrSubmit import rbRrSubmit
reload(rbRrSubmit)
rbRrSubmit.RbRrSubmit.saveAndSubmitToRr()

RbRrSubmitInstance = rbRrSubmit.RbRrSubmit()
RbRrSubmitInstance.saveAndSubmitToRr()
'''
	
	
