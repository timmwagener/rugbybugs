




#rbGrouping Module
#------------------------------------------------------------------

'''
Description:
Creates Basic Groups for Lights, Geo, Cameras etc. according to our pipeline standards
'''

'''
ToDo:

'''




#Imports
#------------------------------------------------------------------
import pymel.core as pm
import maya.OpenMaya as openMaya







#RbGrouping class
#------------------------------------------------------------------

class RbGrouping():
	
	#Constructor / Main Procedure
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		
		
		
	
	
	#Top Level Methods
	#------------------------------------------------------------------
	
	
	#createBaseGroups
	def createBaseGroups(self, setStatus = False):
		
		#createGroups
		self.createGroups()
		
		#setStatus
		if(setStatus): setStatus('Base Groups created')
	

	#Methods
	#------------------------------------------------------------------
	
	
	#createGroup
	def createGroups(self):
		
		
		#create groups
		pm.select(cl = True)
		geo_grp = pm.group( n = 'geo_grp')
		pm.select(cl = True)
		chars_grp = pm.group(n = 'chars_grp')
		pm.select(cl = True)
		props_grp = pm.group(n = 'props_grp')
		pm.select(cl = True)
		set_grp = pm.group(n = 'set_grp')
		pm.select(cl = True)
		
		lights_grp = pm.group(n = 'lights_grp')
		pm.select(cl = True)
		
		cameras_grp = pm.group(n = 'cameras_grp')
		pm.select(cl = True)
		
		temp_grp = pm.group(n = 'temp_grp')
		pm.select(cl = True)
		
		
		#Parent grps
		
		
		#geo_grp
		pm.parent(chars_grp, props_grp, set_grp, geo_grp)
		pm.select(cl = True)
		
		
		#print result
		if(self.verbose): print('Base Grps created')
	
	
	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------
	
	
	
	
	
	
	
	
	
	
	