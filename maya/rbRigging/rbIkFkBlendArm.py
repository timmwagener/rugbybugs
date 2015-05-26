




#rbIkFkBlendArm Module
#----------------------------------------------------

'''
Description:
Module to create a standardized arm rig module

ToDo:
-

'''



#Import
#----------------------------------------------------
import pymel.core as pm
import math





#RbIkFkBlendArm Class
#----------------------------------------------------

class RbIkFkBlendArm():
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#----------------------------------------------------
		
		#Debug and Ui
		self.verbose = True
		self.prefix = None
		self.progressbarWindow = None
		self.progressControl = None
		
		
		
		#Locators and annotations
		self.locator_base = None
		self.locator_middle = None
		self.locator_tip = None
		self.locator_poleVector = None
		
		self.locator_base_annotation = None
		self.locator_middle_annotation = None
		self.locator_tip_annotation = None
		self.locator_poleVector_annotation = None
		
		
		#locator world coords
		self.locator_base_worldCoords = None
		self.locator_middle_worldCoords = None
		self.locator_tip_worldCoords = None
		self.locator_poleVector_worldCoords = None
		
		
		
		
		#IkFkBlendArm Nodes
		#----------------------------------------------------
		
		
		#ik joint chain
		self.ik_j_base = None
		self.ik_j_middle = None
		self.ik_j_tip = None
		
		self.ik_j_grp = None
		
		
		#fk joint chain
		self.fk_j_base = None
		self.fk_j_middle = None
		self.fk_j_tip = None
		
		self.fk_j_grp = None
		
		
		#bound joint chain
		self.bound_j_base = None
		self.bound_j_middle = None
		self.bound_j_tip = None
		
		self.bound_j_grp = None
		
		
		#ik manipulators and linking curve
		self.manip_ik_base = None
		self.manip_ik_base_grp = None
		
		self.manip_ik_tip = None
		self.manip_ik_tip_grp = None
		
		self.manip_ik_poleVector = None
		self.manip_ik_poleVector_grp = None
		
		self.ik_poleVector_linkingCurve_loc = None
		self.ik_poleVector_linkingCurve = None
		self.ik_poleVector_linkingCurve_grp = None
		
		
		#fk manipulators
		self.manip_fk_base = None
		self.manip_fk_base_grp = None
		
		self.manip_fk_middle = None
		self.manip_fk_middle_parent_grp = None
		self.manip_fk_middle_point_grp = None
		
		
		#general manipulators
		self.manip_master = None
		self.manip_master_grp = None
		
		self.manip_ik_fk_switch = None
		self.manip_ik_fk_switch_grp = None
		
		
		#ikHandle
		self.ikHandle = None
		self.ikHandle_grp = None
		
		
		#Ik distance measure
		self.ik_distance_measure_loc_base = None
		self.ik_distance_measure_loc_tip = None
		self.ik_distance_measure_node = None
		self.ik_distance_measure_nodes_grp = None
		
	
		#bound joint orientConstraints
		self.bound_j_base_orientConstraint = None
		self.bound_j_middle_orientConstraint = None
		
		
		#connectIkFkSwitch
		self.manip_ik_fk_switch_reverse = None
		
		
		
		
		#CleanUp
		#----------------------------------------------------
		
		#Sorting Groups
		#---------------------
		self.nodesGrp = None
		self.manipsGrp = None
		self.jointsGrp = None
	
	
	
	
	#Toplevel Methods
	#----------------------------------------------------
	
	#createIkFkBlendArmLocators
	def createIkFkBlendArmLocators(self, prefix = ''):
		
		#set instance prefix var
		self.setPrefix(prefix)
		
		pm.select(cl = True)
		
		#Create Space locators and translate
		self.locator_base = pm.spaceLocator(n = self.prefix + '_locator_base')
		self.locator_base.translate.set(0, 0, 0)
		pm.select(cl = True)
		
		self.locator_middle = pm.spaceLocator(n = self.prefix + '_locator_middle')
		self.locator_middle.translate.set(4, 1, 0)
		pm.select(cl = True)
		
		self.locator_tip = pm.spaceLocator(n = self.prefix + '_locator_tip')
		self.locator_tip.translate.set(8, -1, 0)
		pm.select(cl = True)
		
		self.locator_poleVector = pm.spaceLocator(n = self.prefix + '_locator_poleVector')
		self.locator_poleVector.translate.set(4, 3, 0)
		pm.select(cl = True)
		
		
		
		#Create Annotations and rename
		self.locator_base_annotation = pm.annotate( self.locator_base, tx = self.prefix +'_locator_base' )
		pm.rename(self.locator_base_annotation.getParent().name(), self.prefix + '_locator_base_annotation')
		pm.select(cl = True)
		
		self.locator_middle_annotation = pm.annotate( self.locator_middle, tx = self.prefix +'_locator_middle' )
		pm.rename(self.locator_middle_annotation.getParent().name(), self.prefix + '_locator_middle_annotation')
		pm.select(cl = True)
		
		self.locator_tip_annotation = pm.annotate( self.locator_tip, tx = self.prefix +'_locator_tip' )
		pm.rename(self.locator_tip_annotation.getParent().name(), self.prefix + '_locator_tip_annotation')
		pm.select(cl = True)
		
		self.locator_poleVector_annotation = pm.annotate( self.locator_poleVector, tx = self.prefix +'_locator_poleVector' )
		pm.rename(self.locator_poleVector_annotation.getParent().name(), self.prefix + '_locator_poleVector_annotation')
		pm.select(cl = True)
		
		
		
		#Parent constrain annotation transforms
		pm.parentConstraint(self.locator_base, self.locator_base_annotation.getParent(), mo = False)
		pm.parentConstraint(self.locator_middle, self.locator_middle_annotation.getParent(), mo = False)
		pm.parentConstraint(self.locator_tip, self.locator_tip_annotation.getParent(), mo = False)
		pm.parentConstraint(self.locator_poleVector, self.locator_poleVector_annotation.getParent(), mo = False)
		pm.select(cl = True)
		
		
	
	
	
	
	
	
	
	
	#createIkFkBlendArm
	def createIkFkBlendArm(self, prefix = '', displayProgressbar = True):
		
		#Check if Variables != None
		if(self.locator_base and self.locator_middle and self.locator_tip and self.locator_poleVector):
			
			#Check if locators exist in scene
			if(pm.objExists(self.locator_base) and pm.objExists(self.locator_middle) and pm.objExists(self.locator_tip) and pm.objExists(self.locator_poleVector)):
			
				
				
				
				
				
				#Create Progressbarwin if displayProgressbar == True
				if(displayProgressbar): self.createProgressbarWindow(progressbarSize = 17)
				
				#set instance prefix var
				self.setPrefix(prefix)
				
				
				
				#Create Ik Fk Blend Arm
				#----------------------------------------------------
				
				#setLocatorWorldCoords
				self.setLocatorWorldCoords()
				if(self.verbose): print('Successfully set Locator world coords')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createIkJointChain
				self.createIkJointChain()
				if(self.verbose): print('Successfully created ik joint chain')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFkJointChain
				self.createFkJointChain()
				if(self.verbose): print('Successfully created fk joint chain')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createBoundJointChain
				self.createBoundJointChain()
				if(self.verbose): print('Successfully created bound joint chain')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createIkManipulators
				self.createIkManipulators()
				if(self.verbose): print('Successfully created Ik manipulators')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFkManipulators
				self.createFkManipulators()
				if(self.verbose): print('Successfully created Fk manipulators')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createGeneralManipulators
				self.createGeneralManipulators()
				if(self.verbose): print('Successfully created general manipulators')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createIkHandle
				self.createIkHandle()
				if(self.verbose): print('Successfully created Ik Handle')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createManipulatorAndIkConstraints
				self.createManipulatorAndIkConstraints()
				if(self.verbose): print('Successfully created manipulator and Ik Handle constraints')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createIkDistanceMeasureGrp
				self.createIkDistanceMeasureGrp()
				if(self.verbose): print('Successfully created ik distance measure group')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createStretchynessIk
				self.createStretchynessIk()
				if(self.verbose): print('Successfully created stretchyness for ik joints')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createStretchynessFk
				self.createStretchynessFk()
				if(self.verbose): print('Successfully created stretchyness for fk joints')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createBoundJointOrientConstraints
				self.createBoundJointOrientConstraints()
				if(self.verbose): print('Successfully created bound joint constraints')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#connectIkFkSwitchManip
				self.connectIkFkSwitchManip()
				if(self.verbose): print('Successfully connected ik fk switch manip')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				
				
				
				
				
				
				
				#CleanUp and Sort
				#----------------------------------------------------
				
				#setVisibilityAndLockAttrs
				self.setVisibilityAndLockAttrs()
				if(self.verbose): print('Successfully set visibility and locked attrs')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createSortingGroups
				self.createSortingGroups()
				if(self.verbose): print('Successfully sorted into groups')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#deletePositionLocatorsAndAnnotations
				self.deletePositionLocatorsAndAnnotations()
				if(self.verbose): print('Successfully deleted position locators and annotations')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				
				
				
				
				
				
				#deleteProgressbar
				if(displayProgressbar): self.deleteProgressbarWindow()
				
				#SuccessMsg
				if(self.verbose): print('Successfully created Ik Fk Blend Arm')
				return None
				
				
				
				
				
				
			else:
				if(self.verbose): print('Locators seem to be missing in scene, please recreate them')
				return None
			
		else:
			if(self.verbose): print('No Locators created')
			return None
	
	
	
	
	
	
	
	
	
	
	
	#Methods
	#----------------------------------------------------
	
	#setLocatorWorldCoords
	def setLocatorWorldCoords(self):
		
		pm.select(cl = True)
		
		self.locator_base_worldCoords = pm.xform(self.locator_base, ws = True, q = True, t = True)
		self.locator_middle_worldCoords = pm.xform(self.locator_middle, ws = True, q = True, t = True)
		self.locator_tip_worldCoords = pm.xform(self.locator_tip, ws = True, q = True, t = True)
		self.locator_poleVector_worldCoords = pm.xform(self.locator_poleVector, ws = True, q = True, t = True)
		
		pm.select(cl = True)
		
		
		
		
	
	#createIkJointChain
	def createIkJointChain(self):
		
		pm.select(cl = True)
		
		#Create Joints
		
		#ik_j_base
		pm.select(cl = True)
		self.ik_j_base = pm.joint(a = True, p= self.locator_base_worldCoords , co = True, n = self.prefix +'_ik_j_base')
		pm.select(cl = True)
		
		#ik_j_middle
		pm.select(cl = True)
		self.ik_j_middle = pm.joint(a = True, p= self.locator_middle_worldCoords , co = True, n = self.prefix +'_ik_j_middle')
		pm.select(cl = True)
		
		#ik_j_tip
		pm.select(cl = True)
		self.ik_j_tip = pm.joint(a = True, p= self.locator_tip_worldCoords , co = True, n = self.prefix +'_ik_j_tip')
		pm.select(cl = True)
		
		
		
		#Parent ik joints
		
		pm.parent(self.ik_j_middle, self.ik_j_base)
		pm.parent(self.ik_j_tip, self.ik_j_middle)
		pm.select(cl = True)
		
		#Orient ik joints
		pm.joint(self.ik_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		
		
		
		#Group ik joints
		self.ik_j_grp = pm.group(n = self.prefix + '_ik_j_grp')
		pm.select(cl = True)
		#parent joint chain
		pm.parent(self.ik_j_base, self.ik_j_grp)
		pm.select(cl = True)
		
		
		
		
	#createFkJointChain
	def createFkJointChain(self):
		
		pm.select(cl = True)
		
		#Create Joints
		
		#fk_j_base
		pm.select(cl = True)
		self.fk_j_base = pm.joint(a = True, p= self.locator_base_worldCoords , co = True, n = self.prefix +'_fk_j_base')
		pm.select(cl = True)
		
		#fk_j_middle
		pm.select(cl = True)
		self.fk_j_middle = pm.joint(a = True, p= self.locator_middle_worldCoords , co = True, n = self.prefix +'_fk_j_middle')
		pm.select(cl = True)
		
		#fk_j_tip
		pm.select(cl = True)
		self.fk_j_tip = pm.joint(a = True, p= self.locator_tip_worldCoords , co = True, n = self.prefix +'_fk_j_tip')
		pm.select(cl = True)
		
		
		
		#Parent fk joints
		
		pm.parent(self.fk_j_middle, self.fk_j_base)
		pm.parent(self.fk_j_tip, self.fk_j_middle)
		pm.select(cl = True)
		
		#Orient fk joints
		pm.joint(self.fk_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		
		
		
		#Group fk joints
		self.fk_j_grp = pm.group(n = self.prefix + '_fk_j_grp')
		pm.select(cl = True)
		#parent joint chain
		pm.parent(self.fk_j_base, self.fk_j_grp)
		pm.select(cl = True)
		
		
		
		
		
	#createBoundJointChain
	def createBoundJointChain(self):
		
		pm.select(cl = True)
		
		#Create Joints
		
		#bound_j_base
		pm.select(cl = True)
		self.bound_j_base = pm.joint(a = True, p= self.locator_base_worldCoords , co = True, n = self.prefix +'_bound_j_base')
		pm.select(cl = True)
		
		#bound_j_middle
		pm.select(cl = True)
		self.bound_j_middle = pm.joint(a = True, p= self.locator_middle_worldCoords , co = True, n = self.prefix +'_bound_j_middle')
		pm.select(cl = True)
		
		#bound_j_tip
		pm.select(cl = True)
		self.bound_j_tip = pm.joint(a = True, p= self.locator_tip_worldCoords , co = True, n = self.prefix +'_bound_j_tip')
		pm.select(cl = True)
		
		
		
		#Parent bound joints
		
		pm.parent(self.bound_j_middle, self.bound_j_base)
		pm.parent(self.bound_j_tip, self.bound_j_middle)
		pm.select(cl = True)
		
		#Orient bound joints
		pm.joint(self.bound_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		
		
		
		#Group bound joints
		self.bound_j_grp = pm.group(n = self.prefix + '_bound_j_grp')
		pm.select(cl = True)
		#parent joint chain
		pm.parent(self.bound_j_base, self.bound_j_grp)
		pm.select(cl = True)
	
	
	
	
	
	
	
	#createIkManipulators
	def createIkManipulators(self):
		pm.select(cl = True)
		
		#manip_ik_base
		#----------------------------------------------------
		
		#create manip
		self.manip_ik_base = pm.circle(r = 1, name = self.prefix +'_manip_ik_base', ch = False, nr=(0, 1, 0))[0]
		pm.select(cl = True)
		
		#create and parent under grp
		self.manip_ik_base_grp = pm.group(n = self.prefix + '_manip_ik_base_grp')
		pm.select(cl = True)
		pm.parent(self.manip_ik_base, self.manip_ik_base_grp)
		pm.select(cl = True)
		#translate
		self.manip_ik_base_grp.translate.set(self.locator_base_worldCoords)
		pm.select(cl = True)
		
		#set Visibilty off
		pm.setAttr(self.manip_ik_base_grp.visibility, 0)
		pm.select(cl = True)
		
		
		
		
		#manip_ik_tip
		#----------------------------------------------------
		
		#create manip
		self.manip_ik_tip = pm.circle(r = 1, name = self.prefix +'_manip_ik_tip', ch = False, nr=(0, 1, 0))[0]
		pm.select(cl = True)
		
		#Custom Attrs
		pm.addAttr(self.manip_ik_tip, ln = '_', at='enum', en = 'Custom', h = False, k = True, r = True)
		pm.setAttr(self.manip_ik_tip._ , lock = True)
		
		pm.addAttr(self.manip_ik_tip ,ln = 'stretchy', at='float', defaultValue= 0.0, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		pm.addAttr(self.manip_ik_tip ,ln = 'stretchyOffset', at='float', defaultValue= 0.0, h = False, k = True, r = True )
		pm.addAttr(self.manip_ik_tip ,ln = 'worldScale', at='float', defaultValue= 1.0, h = False, k = True, r = True )
		
		#create and parent under grp
		self.manip_ik_tip_grp = pm.group(n = self.prefix + '_manip_ik_tip_grp')
		pm.select(cl = True)
		pm.parent(self.manip_ik_tip, self.manip_ik_tip_grp)
		pm.select(cl = True)
		#translate
		self.manip_ik_tip_grp.translate.set(self.locator_tip_worldCoords)
		pm.select(cl = True)
	
		
		
		
		
		
		#manip_ik_poleVector
		#----------------------------------------------------
		
		
		#Create leg ik pole vector loc
		self.manip_ik_poleVector = pm.spaceLocator(n = self.prefix +'_manip_ik_poleVector')
		pm.select(cl = True)
		
		#Group leg ik pole vec
		self.manip_ik_poleVector_grp = pm.group(self.manip_ik_poleVector, n = self.prefix + '_manip_ik_poleVector_grp')
		pm.select(cl = True)
		
		#Translate leg_ik_pole_vector_locator_grp
		self.manip_ik_poleVector_grp.translate.set(self.locator_poleVector_worldCoords)
		pm.select(cl = True)
		
		
		
		
		
		#LinkingCurve
		#----------------------------------------------------
		
		#Create linking curve loc
		self.ik_poleVector_linkingCurve_loc = pm.spaceLocator(n = self.prefix +'_ik_poleVector_linkingCurve_loc')
		pm.select(cl = True)
		
		#point con linking curve loc to bound j base
		pm.pointConstraint(self.bound_j_base, self.ik_poleVector_linkingCurve_loc , mo = False)
		pm.select(cl = True)
		
		#Create Pole vector Linking Curve
		self.ik_poleVector_linkingCurve = pm.curve(p = [self.locator_base_worldCoords , self.locator_poleVector_worldCoords], d = 1, n = self.prefix +'_ik_poleVector_linkingCurve')
		pm.select(cl = True)
		
		#make curve not selectable
		pm.setAttr(self.ik_poleVector_linkingCurve.getShape().overrideEnabled, 1)
		pm.setAttr(self.ik_poleVector_linkingCurve.getShape().overrideDisplayType, 2)
		pm.select(cl = True)
		
		#Connect loc world space coords to curve points
		self.manip_ik_poleVector.getShape().worldPosition[0] >> self.ik_poleVector_linkingCurve.getShape().controlPoints[0]
		self.ik_poleVector_linkingCurve_loc.getShape().worldPosition[0] >> self.ik_poleVector_linkingCurve.getShape().controlPoints[1]
		pm.select(cl = True)
		
		#Create grp
		self.ik_poleVector_linkingCurve_grp = pm.group( n = self.prefix +'_ik_poleVector_linkingCurve_grp')
		pm.select(cl = True)
		
		#parent objects in group
		pm.parent(self.ik_poleVector_linkingCurve_loc, self.ik_poleVector_linkingCurve ,self.ik_poleVector_linkingCurve_grp)
		pm.select(cl = True)
		
		#set linking curve base loc visibility
		pm.setAttr(self.ik_poleVector_linkingCurve_loc.visibility, 0)
		pm.select(cl = True)
	
	
	
	
	
	#createFkManipulators
	def createFkManipulators(self):
		
		pm.select(cl = True)
		
		#manip_fk_base
		#----------------------------------------------------
		
		#create manip
		self.manip_fk_base = pm.circle(r = 1, name = self.prefix +'_manip_fk_base', ch = False, nr=(0, 1, 0))[0]
		pm.select(cl = True)
		
		#Custom Attrs
		pm.addAttr(self.manip_fk_base, ln = '_', at='enum', en = 'Custom', h = False, k = True, r = True)
		pm.setAttr(self.manip_fk_base._ , lock = True)
		
		pm.addAttr(self.manip_fk_base ,ln = 'stretchyMultiplier', at='float', defaultValue= 1.0, h = False, k = True, r = True)
		
		#create and parent under grp
		self.manip_fk_base_grp = pm.group(n = self.prefix + '_manip_fk_base_grp')
		pm.select(cl = True)
		pm.parent(self.manip_fk_base, self.manip_fk_base_grp)
		pm.select(cl = True)
		
		#perform scaling on every second cv
		pm.xform(self.manip_fk_base.cv[::2], a = False, s = (0.3, 1, 0.3))
		pm.select(cl = True)
		
		#translate by transform matrix
		bound_j_base_transformMatrix = pm.xform(self.bound_j_base, q = True, ws = True, matrix = True)
		pm.xform(self.manip_fk_base_grp, ws = True, matrix = bound_j_base_transformMatrix)
		pm.select(cl = True)
		
		
		
		#manip_fk_middle
		#----------------------------------------------------
		
		#create middle
		self.manip_fk_middle = pm.circle(r = 1, name = self.prefix +'_manip_fk_middle', ch = False, nr=(0, 1, 0))[0]
		pm.select(cl = True)
		
		#perform scaling on every second cv
		pm.xform(self.manip_fk_middle.cv[::2], a = False, s = (0.3, 1, 0.3))
		pm.select(cl = True)
		
		#create and parent under grp
		self.manip_fk_middle_point_grp = pm.group(n = self.prefix + '_manip_fk_middle_point_grp')
		pm.select(cl = True)
		pm.parent(self.manip_fk_middle, self.manip_fk_middle_point_grp)
		pm.select(cl = True)
		
		#create and parent under grp
		self.manip_fk_middle_parent_grp = pm.group(n = self.prefix + '_manip_fk_middle_parent_grp')
		pm.select(cl = True)
		pm.parent(self.manip_fk_middle_point_grp, self.manip_fk_middle_parent_grp)
		pm.select(cl = True)
		
		
		#translate by transform matrix
		bound_j_middle_transformMatrix = pm.xform(self.bound_j_middle, q = True, ws = True, matrix = True)
		pm.xform(self.manip_fk_middle_parent_grp, ws = True, matrix = bound_j_middle_transformMatrix)
		pm.select(cl = True)
		
	
	
	
	
	
	#createGeneralManipulators
	def createGeneralManipulators(self):
		pm.select(cl = True)
		
		
		#manip_master
		#----------------------------------------------------
		
		#create manip
		self.manip_master = pm.circle(r = 1.5, name = self.prefix +'_manip_master', ch = False, nr=(0, 1, 0))[0]
		pm.select(cl = True)
		
		#create and parent under grp
		self.manip_master_grp = pm.group(n = self.prefix + '_manip_master_grp')
		pm.select(cl = True)
		pm.parent(self.manip_master, self.manip_master_grp)
		pm.select(cl = True)
		#translate
		self.manip_master_grp.translate.set(self.locator_base_worldCoords)
		pm.select(cl = True)
		
		
		
		
		#manip_ik_fk_switch
		#----------------------------------------------------
		
		pm.select(cl = True)
		
		#createTextCurves
		nurbsText = self.prefix + '_Ik_Fk_Switch'
		textCurvesReturnList = pm.textCurves(f = 'arial' , t = nurbsText, ch = True )
		
		textTopGrp = textCurvesReturnList[0]
		makeTextCurvesNode = textCurvesReturnList[1]
		
		pm.select(cl = True)
		
		#get future history of makeTextCurvesNode
		textHistoryList = pm.listHistory(makeTextCurvesNode, future = True, af = True)
		
		#get list of transforms and NurbsCurve nodes connected to makeTextCurvesNode
		textTransformList = []
		textNurbsCurveList = []
		for node in textHistoryList:
			if(pm.nodeType(node) == 'transform'): textTransformList.append(node)
			if(pm.nodeType(node) == 'nurbsCurve'): textNurbsCurveList.append(node)
			
		pm.select(cl = True)
		
		#delete makeTextCurvesNode
		pm.delete(makeTextCurvesNode)
		pm.select(cl = True)
		
		#iterate through transformList, move pivot to ws (0,0,0) and freeze all
		for transformNode in textTransformList:
			pm.xform(transformNode, ws = True, piv = (0,0,0))
			pm.makeIdentity(transformNode, a = True)
			
			
		#create manip_ik_fk_switch
		self.manip_ik_fk_switch = pm.group(n = self.prefix + '_manip_ik_fk_switch')
		pm.select(cl = True)
		
		#Custom Attrs
		pm.addAttr(self.manip_ik_fk_switch, ln = '_', at='enum', en = 'Custom', h = False, k = True, r = True)
		pm.setAttr(self.manip_ik_fk_switch._ , lock = True)
		
		pm.addAttr(self.manip_ik_fk_switch ,ln = 'ikFkBlend', at='float', defaultValue= 0.0, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		pm.select(cl = True)
		
		#iterate through nurbsCurve list and parent shapes under manip_ik_fk_switch
		for nurbsCurveShape in textNurbsCurveList:
			pm.parent(nurbsCurveShape, self.manip_ik_fk_switch, r = True, s = True)
			
		pm.select(cl = True)
		
		#create manip_ik_fk_switch grp and translate correctly
		self.manip_ik_fk_switch_grp = pm.group(n = self.prefix + '_manip_ik_fk_switch_grp')
		pm.select(cl = True)
		pm.parent(self.manip_ik_fk_switch, self.manip_ik_fk_switch_grp)
		pm.select(cl = True)
		
		self.manip_ik_fk_switch_grp.translate.set(self.locator_tip_worldCoords)
		
		
		#delete remaining text transform nodes
		pm.delete(textTopGrp)
		pm.select(cl = True)
		
		
		
		
		
	#createIkHandle
	def createIkHandle(self):
		pm.select(cl = True)
		
		#create ik handle
		self.ikHandle = pm.ikHandle( sj= self.ik_j_base , ee= self.ik_j_tip , n = self.prefix +'_ik_Handle' , sol = 'ikRPsolver' )[0]
		pm.select(cl = True)
		
		#Group ik solver
		self.ikHandle_grp = pm.group(n = self.prefix + '_ik_Handle_grp')
		pm.select(cl = True)
		pm.parent(self.ikHandle, self.ikHandle_grp)
		pm.select(cl = True)
		
		
		
		
	#createManipulatorAndIkConstraints
	def createManipulatorAndIkConstraints(self):
		pm.select(cl = True)
		
		
		#Manips
		#----------------------------------------------------
		
		#manip_ik_base
		pm.scaleConstraint( self.manip_master, self.manip_ik_base_grp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.manip_ik_base_grp,  mo = True )
		pm.select(cl = True)
		
		#manip_ik_tip
		pm.scaleConstraint( self.manip_master, self.manip_ik_tip_grp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.manip_ik_tip_grp,  mo = True )
		pm.select(cl = True)
		
		#manip_ik_poleVector
		pm.scaleConstraint( self.manip_master, self.manip_ik_poleVector_grp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.manip_ik_poleVector_grp,  mo = True )
		pm.select(cl = True)
		
		#manip_fk_base
		pm.scaleConstraint( self.manip_master, self.manip_fk_base_grp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.manip_fk_base_grp,  mo = True )
		pm.select(cl = True)
		
		#manip_fk_middle_parent_grp
		pm.scaleConstraint( self.manip_fk_base, self.manip_fk_middle_parent_grp,  mo = True ) 
		pm.parentConstraint( self.manip_fk_base, self.manip_fk_middle_parent_grp,  mo = True )
		pm.select(cl = True)
		
		#manip_fk_middle_point_grp 
		pm.pointConstraint( self.fk_j_middle, self.manip_fk_middle_point_grp,  mo = True )
		pm.select(cl = True)
		
		#manip_ik_fk_switch
		pm.scaleConstraint( self.bound_j_tip, self.manip_ik_fk_switch_grp,  mo = True ) 
		pm.parentConstraint( self.bound_j_tip, self.manip_ik_fk_switch_grp,  mo = True )
		pm.select(cl = True)
		
		
		
		
		#ikHandle
		#----------------------------------------------------
		
		#ikHandle_grp
		pm.scaleConstraint( self.manip_ik_tip, self.ikHandle_grp,  mo = True ) 
		pm.parentConstraint( self.manip_ik_tip, self.ikHandle_grp,  mo = True )
		pm.select(cl = True)
		
		#ikHandle
		pm.poleVectorConstraint( self.manip_ik_poleVector, self.ikHandle)
		pm.select(cl = True)
		
		
		
		
		
		
		
		#Joints
		#----------------------------------------------------
		
		#ik_j_grp
		pm.scaleConstraint( self.manip_ik_base, self.ik_j_grp,  mo = True ) 
		pm.parentConstraint( self.manip_ik_base, self.ik_j_grp,  mo = True )
		pm.select(cl = True)
		
		#fk_j_grp
		pm.scaleConstraint( self.manip_master, self.fk_j_grp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.fk_j_grp,  mo = True )
		pm.select(cl = True)
		
		#bound_j_grp
		pm.scaleConstraint( self.manip_master, self.bound_j_grp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.bound_j_grp,  mo = True )
		pm.select(cl = True)
		
		
		#fk_j_base
		pm.orientConstraint( self.manip_fk_base, self.fk_j_base,  mo = True ) 
		pm.select(cl = True)
		
		#fk_j_middle
		pm.orientConstraint( self.manip_fk_middle, self.fk_j_middle,  mo = True ) 
		pm.select(cl = True)
		
	




	#createIkDistanceMeasureGrp
	def createIkDistanceMeasureGrp(self):
		pm.select(cl = True)
		
		
		#Create locators as start point (base)
		self.ik_distance_measure_loc_base = pm.spaceLocator(n = self.prefix + '_ik_distance_measure_loc_base') 
		#Point constrain to bound_j_base
		pm.pointConstraint( self.bound_j_base, self.ik_distance_measure_loc_base , mo = False) 
		
		pm.select(cl = True)
		
		#Create locators as end point (base)
		self.ik_distance_measure_loc_tip = pm.spaceLocator(n = self.prefix + '_ik_distance_measure_loc_tip') 
		#Point constrain to bound_j_base
		pm.pointConstraint( self.manip_ik_tip, self.ik_distance_measure_loc_tip , mo = False) 
		
		pm.select(cl = True)
		
		#Create Distance Dimension Node 
		pm.select(self.ik_distance_measure_loc_base, self.ik_distance_measure_loc_tip)
		self.ik_distance_measure_node = pm.distanceDimension()
		
		pm.select(cl = True)
		
		#Group all three nodes
		self.ik_distance_measure_nodes_grp = pm.group( self.ik_distance_measure_loc_base,  self.ik_distance_measure_loc_tip , self.ik_distance_measure_node ,  n= self.prefix +'_ik_distance_measure_nodes_grp' )
		
		pm.select(cl = True)
	
	
	
	#createStretchynessIk
	def createStretchynessIk(self):
		pm.select(cl = True)
	
		
		#Normalize Worldspace
		self.normalize_world_space = pm.nodetypes.MultiplyDivide(n = self.prefix +'_normalize_world_space')
		pm.setAttr(self.normalize_world_space.operation , 2)
		self.ik_distance_measure_node.distance >> self.normalize_world_space.input1X
		self.manip_ik_tip.worldScale >> self.normalize_world_space.input2X
		pm.select(cl = True)
		
		
		#Normalize Distance
		self.normalize_distance = pm.nodetypes.MultiplyDivide(n = self.prefix +'_normalize_distance')
		pm.setAttr(self.normalize_distance.operation , 2)
		self.normalize_world_space.outputX >> self.normalize_distance.input1X
		
		#Set Normalize Distance to length of all middle  and tip joints transX added up
		standardJointDistance = pm.getAttr(self.bound_j_middle.tx) + pm.getAttr(self.bound_j_tip.tx)
		pm.setAttr(self.normalize_distance.input2X , standardJointDistance)
		
		
		#Create condition node to check wether or not normalized distance is greater one
		self.normalized_distance_greater_one = pm.nodetypes.Condition(n = self.prefix +'_normalized_distance_greater_one')
		pm.setAttr(self.normalized_distance_greater_one.operation, 2)
		self.normalize_distance.outputX >> self.normalized_distance_greater_one.firstTerm
		self.normalize_distance.outputX >> self.normalized_distance_greater_one.colorIfTrueR
		pm.setAttr(self.normalized_distance_greater_one.secondTerm , 1)
		pm.setAttr(self.normalized_distance_greater_one.colorIfFalseR , 1)
		
		#Create Blend colors node to blend stretchyness
		self.blend_stretchyness = pm.nodetypes.BlendColors(n = self.prefix +'_blend_stretchyness')
		self.manip_ik_tip.stretchy >> self.blend_stretchyness.blender
		self.normalized_distance_greater_one.outColorR >> self.blend_stretchyness.color1R
		pm.setAttr(self.blend_stretchyness.color2R, 1)
		
		
		
		#Multiply output of Blendnode with joints translate x value
		
		#ik_j_middle
		self.multiply_stretch_factor_ik_j_middle = pm.nodetypes.MultiplyDivide(n = self.prefix +'_multiply_stretch_factor_ik_j_middle')
		pm.setAttr(self.multiply_stretch_factor_ik_j_middle.operation , 1)
		self.blend_stretchyness.outputR >> self.multiply_stretch_factor_ik_j_middle.input1X
		pm.setAttr(self.multiply_stretch_factor_ik_j_middle.input2X , pm.getAttr(self.ik_j_middle.tx))
		
		#ik_j_tip
		self.multiply_stretch_factor_ik_j_tip = pm.nodetypes.MultiplyDivide(n = self.prefix +'_multiply_stretch_factor_ik_j_tip')
		pm.setAttr(self.multiply_stretch_factor_ik_j_tip.operation , 1)
		self.blend_stretchyness.outputR >> self.multiply_stretch_factor_ik_j_tip.input1X
		pm.setAttr(self.multiply_stretch_factor_ik_j_tip.input2X , pm.getAttr(self.ik_j_tip.tx))
		
		
		#Create Add Offset node
		
		#ik_j_middle
		self.add_offset_ik_j_middle = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_add_offset_ik_j_middle')
		self.manip_ik_tip.stretchyOffset >> self.add_offset_ik_j_middle.input1D[0]
		self.multiply_stretch_factor_ik_j_middle.outputX >> self.add_offset_ik_j_middle.input1D[1]
		
		#ik_j_tip
		self.add_offset_ik_j_tip = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_add_offset_ik_j_tip')
		self.manip_ik_tip.stretchyOffset >> self.add_offset_ik_j_tip.input1D[0]
		self.multiply_stretch_factor_ik_j_tip.outputX >> self.add_offset_ik_j_tip.input1D[1]
		
		
		#Connect Joints
		#----------------------------------------------------
	
		#ik_j_middle
		self.add_offset_ik_j_middle.output1D >> self.ik_j_middle.translateX
		#ik_j_tip
		self.add_offset_ik_j_tip.output1D >> self.ik_j_tip.translateX
		pm.select(cl = True)
		
	
	
	
	#createStretchynessFk
	def createStretchynessFk(self):
		pm.select(cl = True)
		
		#Multiply stretchy attr of fk_manip_base with joints translate x value
		
		#fk_j_middle
		self.multiply_stretch_factor_fk_j_middle = pm.nodetypes.MultiplyDivide(n = self.prefix +'_multiply_stretch_factor_fk_j_middle')
		pm.setAttr(self.multiply_stretch_factor_fk_j_middle.operation , 1)
		self.manip_fk_base.stretchyMultiplier >> self.multiply_stretch_factor_fk_j_middle.input1X
		pm.setAttr(self.multiply_stretch_factor_fk_j_middle.input2X , pm.getAttr(self.fk_j_middle.tx))
		
		#fk_j_tip
		self.multiply_stretch_factor_fk_j_tip = pm.nodetypes.MultiplyDivide(n = self.prefix +'_multiply_stretch_factor_fk_j_tip')
		pm.setAttr(self.multiply_stretch_factor_fk_j_tip.operation , 1)
		self.manip_fk_base.stretchyMultiplier >> self.multiply_stretch_factor_fk_j_tip.input1X
		pm.setAttr(self.multiply_stretch_factor_fk_j_tip.input2X , pm.getAttr(self.fk_j_tip.tx))
		
		
		#Connect Joints
		#----------------------------------------------------
	
		#fk_j_middle
		self.multiply_stretch_factor_fk_j_middle.outputX >> self.fk_j_middle.translateX
		#fk_j_tip
		self.multiply_stretch_factor_fk_j_tip.outputX >> self.fk_j_tip.translateX
		
		pm.select(cl = True)
		
		
		
		
		
		
	#createBoundJointOrientConstraints
	def createBoundJointOrientConstraints(self):
		pm.select(cl = True)
		
		#orient constraints
		#----------------------------------------------------
		
		#bound_j_base
		self.bound_j_base_orientConstraint = pm.orientConstraint( self.ik_j_base, self.fk_j_base, self.bound_j_base,  mo = True )
		pm.select(cl = True)
		
		#bound_j_middle
		self.bound_j_middle_orientConstraint = pm.orientConstraint( self.ik_j_middle, self.fk_j_middle, self.bound_j_middle,  mo = True )
		pm.select(cl = True)
		
		
		
		
		
		
	
	
	
	
	#connectIkFkSwitchManip
	def connectIkFkSwitchManip(self):
		pm.select(cl = True)
		
		
		#Connect orient constraints
		#----------------------------------------------------
		
		#reverse Node
		self.manip_ik_fk_switch_reverse = pm.createNode('reverse')
		pm.select(cl = True)
		
		#Connect reverse node
		self.manip_ik_fk_switch.ikFkBlend >> self.manip_ik_fk_switch_reverse.inputX
		
		
		#connect orientConstraints FK
		pm.connectAttr(self.manip_ik_fk_switch.ikFkBlend, self.bound_j_base_orientConstraint +'.' +self.fk_j_base.name() +'W1', f = True)
		pm.connectAttr(self.manip_ik_fk_switch.ikFkBlend, self.bound_j_middle_orientConstraint +'.' +self.fk_j_middle.name() +'W1', f = True)
		pm.select(cl = True)
		
		#connect orientConstraints IK
		pm.connectAttr(self.manip_ik_fk_switch_reverse.outputX , self.bound_j_base_orientConstraint +'.' +self.ik_j_base.name() +'W0', f = True)
		pm.connectAttr(self.manip_ik_fk_switch_reverse.outputX , self.bound_j_middle_orientConstraint +'.' +self.ik_j_middle.name() +'W0', f = True)
		pm.select(cl = True)
	
		
		
		
		#Create Stretchy blend
		#----------------------------------------------------
		
		#Create Blend colors node to blend stretchyness
		
		#bound_j_middle
		self.blend_stretchyness_bound_j_middle = pm.nodetypes.BlendColors(n = self.prefix +'_blend_stretchyness_bound_j_middle')
		self.manip_ik_fk_switch_reverse.outputX >> self.blend_stretchyness_bound_j_middle.blender
		self.ik_j_middle.translateX >> self.blend_stretchyness_bound_j_middle.color1R
		self.fk_j_middle.translateX >> self.blend_stretchyness_bound_j_middle.color2R
		pm.select(cl = True)
		
		#bound_j_tip
		self.blend_stretchyness_bound_j_tip = pm.nodetypes.BlendColors(n = self.prefix +'_blend_stretchyness_bound_j_tip')
		self.manip_ik_fk_switch_reverse.outputX >> self.blend_stretchyness_bound_j_tip.blender
		self.ik_j_tip.translateX >> self.blend_stretchyness_bound_j_tip.color1R
		self.fk_j_tip.translateX >> self.blend_stretchyness_bound_j_tip.color2R
		pm.select(cl = True)
		
		#Connect stretchy blendnodes to bound joints translateX
		self.blend_stretchyness_bound_j_middle.outputR >> self.bound_j_middle.translateX
		self.blend_stretchyness_bound_j_tip.outputR >> self.bound_j_tip.translateX
		pm.select(cl = True)
		
		
		
		
		#Connect visibility
		#----------------------------------------------------
		
		#ik manips
		self.manip_ik_fk_switch_reverse.outputX >> self.manip_ik_poleVector_grp.visibility
		self.manip_ik_fk_switch_reverse.outputX >> self.manip_ik_tip_grp.visibility
		self.manip_ik_fk_switch_reverse.outputX >> self.ik_poleVector_linkingCurve_grp.visibility
		
		#fk manips
		self.manip_ik_fk_switch.ikFkBlend >> self.manip_fk_base_grp.visibility
		self.manip_ik_fk_switch.ikFkBlend >> self.manip_fk_middle_parent_grp.visibility
		pm.select(cl = True)
		
	
	
	
	
	
	
	
	
	
	
	
	
	#CleanUp
	#----------------------------------------------------
	
	
	#setVisibilityAndLockAttrs
	def setVisibilityAndLockAttrs(self):
		pm.select(cl = True)
		
		#manip_ik_fk_switch
		pm.setAttr(self.manip_ik_fk_switch.translateX, lock = True)
		pm.setAttr(self.manip_ik_fk_switch.translateY, lock = True)
		pm.setAttr(self.manip_ik_fk_switch.translateZ, lock = True)
		
		pm.setAttr(self.manip_ik_fk_switch.rotateX, lock = True)
		pm.setAttr(self.manip_ik_fk_switch.rotateY, lock = True)
		pm.setAttr(self.manip_ik_fk_switch.rotateZ, lock = True)
		
		pm.setAttr(self.manip_ik_fk_switch.scaleX, lock = True)
		pm.setAttr(self.manip_ik_fk_switch.scaleY, lock = True)
		pm.setAttr(self.manip_ik_fk_switch.scaleZ, lock = True)
		
		pm.setAttr(self.manip_ik_fk_switch.visibility, lock = True)
		
		
		#self.manip_ik_poleVector
		pm.setAttr(self.manip_ik_poleVector.scaleX, lock = True)
		pm.setAttr(self.manip_ik_poleVector.scaleY, lock = True)
		pm.setAttr(self.manip_ik_poleVector.scaleZ, lock = True)
		
		pm.setAttr(self.manip_ik_poleVector.visibility, lock = True)
		
		
		#self.manip_fk_base
		pm.setAttr(self.manip_fk_base.translateX, lock = True)
		pm.setAttr(self.manip_fk_base.translateY, lock = True)
		pm.setAttr(self.manip_fk_base.translateZ, lock = True)
		
		pm.setAttr(self.manip_fk_base.scaleX, lock = True)
		pm.setAttr(self.manip_fk_base.scaleY, lock = True)
		pm.setAttr(self.manip_fk_base.scaleZ, lock = True)
		
		pm.setAttr(self.manip_fk_base.visibility, lock = True)
		
		
		#self.manip_fk_middle
		pm.setAttr(self.manip_fk_middle.translateX, lock = True)
		pm.setAttr(self.manip_fk_middle.translateY, lock = True)
		pm.setAttr(self.manip_fk_middle.translateZ, lock = True)
		
		pm.setAttr(self.manip_fk_middle.scaleX, lock = True)
		pm.setAttr(self.manip_fk_middle.scaleY, lock = True)
		pm.setAttr(self.manip_fk_middle.scaleZ, lock = True)
		
		pm.setAttr(self.manip_fk_middle.visibility, lock = True)
		
		
		#self.manip_ik_tip
		pm.setAttr(self.manip_ik_tip.scaleX, lock = True)
		pm.setAttr(self.manip_ik_tip.scaleY, lock = True)
		pm.setAttr(self.manip_ik_tip.scaleZ, lock = True)
		
		pm.setAttr(self.manip_ik_tip.visibility, lock = True)
		
		pm.select(cl = True)
		
		
		
	
	
	
	#createSortingGroups
	def createSortingGroups(self):
		
		pm.select(cl = True)
		
		
		
		#create nodesGrp
		self.nodesGrp = pm.group(n = self.prefix + '_nodes_grp')
		pm.select(cl = True)
		
		#create manipsGrp
		self.manipsGrp = pm.group(n = self.prefix + '_manips_grp')
		pm.select(cl = True)
		
		#create jointsGrp
		self.jointsGrp = pm.group(n = self.prefix + '_joints_grp')
		pm.select(cl = True)
		
		
		#Parent
		
		#nodesGrp
		pm.parent( self.ik_distance_measure_nodes_grp, self.ikHandle_grp, self.nodesGrp)
		pm.select(cl = True)
		
		#manipsGrp
		pm.parent( self.manip_ik_fk_switch_grp, self.manip_master_grp, self.manip_fk_middle_parent_grp, self.manip_fk_base_grp, self.manip_ik_poleVector_grp, self.manip_ik_tip_grp, self.manip_ik_base_grp, self.ik_poleVector_linkingCurve_grp, self.manipsGrp)
		pm.select(cl = True)
		
		#jointsGrp
		pm.parent( self.ik_j_grp, self.fk_j_grp, self.bound_j_grp, self.jointsGrp)
		pm.select(cl = True)
	
	
	
	
	#deletePositionLocatorsAndAnnotations
	def deletePositionLocatorsAndAnnotations(self):
		
		pm.select(cl = True)
		
		#delete Locators
		pm.delete(self.locator_base, self.locator_middle, self.locator_tip, self.locator_poleVector)
		pm.select(cl = True)
		
		#delete annotations
		pm.delete(self.locator_base_annotation.getParent(), self.locator_middle_annotation.getParent(), self.locator_tip_annotation.getParent(), self.locator_poleVector_annotation.getParent())
		pm.select(cl = True)
	
	
	
	
	
	#Shared Methods
	#----------------------------------------------------
	
	
	#setPrefix
	def setPrefix(self, prefix):
		self.prefix = prefix
		
		
	
		
	
	
	
	#createProgressbarWindow
	def createProgressbarWindow(self, progressbarSize = 1):
		
		pm.select(cl = True)
		
		#Create ProgressbarUi Window
		self.progressbarWindow = pm.window(title = 'Progress', resizeToFitChildren = True)
		pm.columnLayout()
		self.progressControl = pm.progressBar(maxValue = progressbarSize, width = 300)
		pm.showWindow(self.progressbarWindow)
		
		pm.select(cl = True)
		
	
	#updateProgressbarWindow
	def updateProgressbarWindow(self):
		
		#Update Progressbar
		pm.progressBar(self.progressControl, edit=True, step=1)
		
		
	#deleteProgressbarWindow
	def deleteProgressbarWindow(self):
		
		#Delete Progressbar
		pm.deleteUI(self.progressbarWindow, window = True)
		
	
	
	
	
	
	
	
	
	
	
	#getDistance
	def getDistance(self, vectorA, vectorB):
		
		
		#get vector between A and B
		vectorAB = [vectorB[0] - vectorA[0], vectorB[1] - vectorA[1], vectorB[2] - vectorA[2]]
		
		#return distance
		return math.sqrt(math.pow(vectorAB[0], 2) + math.pow(vectorAB[1], 2) + math.pow(vectorAB[2], 2))
		
	

	
	#Create Cube Manips
	def createCubeManipulator(self, manipulator_name):
		
		curve_rectangle_down = pm.curve( p=[(-2, -1, -2), (-2, -1, 2), (2, -1, 2), (2, -1, -2),(-2, -1, -2)], ws = True, d = 1 )

		curve_rectangle_up = pm.curve( p=[(-2, 1, -2), (-2, 1, 2), (2, 1, 2), (2, 1, -2),(-2, 1, -2)], ws = True, d = 1 )

		curve_1 = pm.curve( p=[(-2, -1, -2),(-2, 1, -2)], ws = True, d = 1 )

		curve_2 = pm.curve( p=[(2, -1, -2),(2, 1, -2)], ws = True, d = 1 )

		curve_3 = pm.curve( p=[(2, -1, 2),(2, 1, 2)], ws = True, d = 1 )

		curve_4 = pm.curve( p=[(-2, -1, 2),(-2, 1, 2)], ws = True, d = 1 )
		
		
		#Create Manipulator shape
		manipulator = pm.group(  n= manipulator_name )
		
		#Parent all shapes
		pm.parent(curve_rectangle_down.getShape(),manipulator, r = True, s = True)
		pm.delete(curve_rectangle_down)
		
		pm.parent(curve_rectangle_up.getShape(),manipulator, r = True, s = True)
		pm.delete(curve_rectangle_up)
		
		pm.parent(curve_1.getShape(),manipulator, r = True, s = True)
		pm.delete(curve_1)
		
		pm.parent(curve_2.getShape(),manipulator, r = True, s = True)
		pm.delete(curve_2)
		
		pm.parent(curve_3.getShape(),manipulator, r = True, s = True)
		pm.delete(curve_3)
		
		pm.parent(curve_4.getShape(),manipulator, r = True, s = True)
		pm.delete(curve_4)
		
		pm.select(cl = True)
		
		pm.xform(manipulator, ws=True, piv=(0, 0, 0) )
		
		#Return manipulator
		return manipulator
		
		
		
	#createArrowManip
	def createArrowManip(self, name = '_defaultName'):
		
		pm.select(cl = True)
		
		#create arrow curve
		arrowCurve =  pm.curve( p=[(-1, 0, 1), (-1, 0, 3), (-2, 0, 3), (0, 0, 5),(2, 0, 3),(1, 0, 3),(1, 0, 1),(-1, 0, 1)], ws = True, d = 1 )
		pm.select(cl = True)
		
		#manipGrp
		manipGrp = pm.group()
		pm.select(cl = True)
		
		#parent shape
		pm.parent(arrowCurve.getShape() , manipGrp, r = True, s = True)
		pm.select(cl = True)
		
		#rename grp
		pm.rename(manipGrp, name)
		
		#deleteRemaining Transforms
		pm.delete(arrowCurve)
		
		return manipGrp
	
		

		
		
		
		
		
		
		
#Execute Temp
#----------------------------------------------------

'''
#CREATE LOCATORS
from rugbyBugs.maya.rbRigging import rbIkFkBlendArm

#Reload if true
doReload = True
if(doReload): reload(rbIkFkBlendArm)

#Create Instance if it doesnt exist
rbIkFkBlendArmInstance = rbIkFkBlendArm.RbIkFkBlendArm()

#createLocators
rbIkFkBlendArmInstance.createIkFkBlendArmLocators(prefix = 'Test')
'''

'''
#CREATE CHAIN

#createLocators
rbIkFkBlendArmInstance.createIkFkBlendArm(prefix = 'Test')
'''
	
	
	