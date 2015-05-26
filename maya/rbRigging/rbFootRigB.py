




#rbFootRigB Module
#----------------------------------------------------

'''
Description:
Module to create a standardized foot rig module

ToDo:
-

'''



#Import
#----------------------------------------------------
import pymel.core as pm
import maya.cmds as cmds
import math





#RbFootRigB Class
#----------------------------------------------------

class RbFootRigB():
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#----------------------------------------------------
		
		#Debug and Ui
		self.verbose = True
		self.prefix = None
		self.progressbarWindow = None
		self.progressControl = None
		
		
		#Locators and Annotations
		self.leg_locator_base = None
		self.leg_locator_knee = None
		self.leg_locator_tip = None
		self.leg_locator_poleVector = None
		self.foot_locator = None
		
		self.annotation_leg_locator_base = None
		self.annotation_leg_locator_knee = None
		self.annotation_leg_locator_tip = None
		self.annotation_leg_locator_poleVector = None
		self.annotation_foot_locator = None
		
		
		#locator world coords
		self.leg_locator_base_worldCoords = None
		self.leg_locator_knee_worldCoords = None
		self.leg_locator_tip_worldCoords = None
		self.leg_locator_poleVector_worldCoords = None
		self.foot_locator_worldCoords = None
		
		self.facingXPlus = True
		
		
		
		
		
		
		#Leg Ik
		#----------------------------------------------------
		
		#leg ik joint chain
		self.leg_ik_j_base = None
		self.leg_ik_j_knee = None
		self.leg_ik_j_tip = None
		
		self.leg_ik_j_grp = None
		
		
		
		#leg ik handle
		self.leg_ik_handle = None
		self.leg_ik_handle_grp = None
		
		
		
		#leg ik manips and aim group
		self.manip_leg_base = None
		self.manip_leg_base_grp = None
		
		self.manip_leg_ik = None
		self.manip_leg_ik_grp = None
		self.manip_leg_ik_point_grp = None
		
		self.manip_leg_complete = None
		self.manip_leg_complete_grp = None
		
		self.manip_aim_indicator = None
		self.manip_aim_indicator_grp = None
		self.manip_aim_indicator_aim_grp = None
		
		
		
		#poleVectorLocator and Linking Curve
		self.leg_ik_pole_vector_locator = None
		self.leg_ik_pole_vector_locator_grp = None
		
		self.leg_ik_pole_vector_locator_linking_curve_locator = None
		self.pole_vector_linking_curve = None
		self.pole_vector_linking_curve_grp = None
		
		
		
		
		
		
		#Foot Spline Ik
		#----------------------------------------------------
		
		
		#Foot Ik Manips
		self.manip_foot_ik_base = None
		self.manip_foot_ik_base_grp = None
		
		self.manip_foot_ik_tip = None
		self.manip_foot_ik_tip_grp = None
		self.manip_foot_ik_tip_point_grp = None
		
		
		
		#Curve Bound Joints
		self.curve_bound_j_base = None
		self.curve_bound_j_base_grp = None
		
		self.curve_bound_j_tip = None
		self.curve_bound_j_tip_grp = None
		
		
		#Foot Ik Bound Joint Chain
		self.footIkJointsPositionList = None
		
		self.foot_ik_bound_j_base = None
		self.foot_ik_bound_j_2 = None
		self.foot_ik_bound_j_3 = None
		self.foot_ik_bound_j_4 = None
		self.foot_ik_bound_j_5 = None
		self.foot_ik_bound_j_6 = None
		self.foot_ik_bound_j_tip = None
		
		self.foot_ik_bound_j_grp = None
		
		
		#Foot Ik Tip Joint Chain
		self.foot_ik_tip_j_base = None
		self.foot_ik_tip_j_2 = None
		self.foot_ik_tip_j_3 = None
		self.foot_ik_tip_j_4 = None
		self.foot_ik_tip_j_5 = None
		self.foot_ik_tip_j_6 = None
		self.foot_ik_tip_j_tip = None
		
		self.foot_ik_tip_j_grp = None
		
		
		#Foot Ik base Joint Chain
		self.foot_ik_base_j_base = None
		self.foot_ik_base_j_2 = None
		self.foot_ik_base_j_3 = None
		self.foot_ik_base_j_4 = None
		self.foot_ik_base_j_5 = None
		self.foot_ik_base_j_6 = None
		self.foot_ik_base_j_tip = None
		
		self.foot_ik_base_j_grp = None
		
		
		#foot spline ik curve and skincluster
		self.foot_splineIk_curve = None
		self.foot_splineIk_curve_grp = None
		self.foot_splineIk_skincluster = None
		
		
		#foot splineIk tip and base
		self.foot_spline_ik_tip = None
		self.foot_spline_ik_tip_grp = None
		
		self.foot_spline_ik_base = None
		self.foot_spline_ik_base_grp = None
		
		
		#foot ik bound joint orient constraints
		self.foot_ik_bound_j_2_orientCon = None
		self.foot_ik_bound_j_3_orientCon = None
		self.foot_ik_bound_j_4_orientCon = None
		self.foot_ik_bound_j_5_orientCon = None
		self.foot_ik_bound_j_6_orientCon = None
		
		
		#foot ik stretchyness
		self.splineIk_curve_info = None
		self.normalize_world_space = None
		self.normalize_distance = None
		self.normalized_distance_greater_one = None
		self.blend_stretchyness = None
		self.multiply_stretch_factor = None
		self.add_offset = None
		
		
		
		
		
		
		#CleanUp
		#----------------------------------------------------
		
		#Sorting Groups
		#---------------------
		self.nodesGrp = None
		self.manipsGrp = None
		self.jointsGrp = None
		
		
	
	
	
	#Toplevel Methods
	#----------------------------------------------------
	
	
	
	#Create Locators
	#----------------------------------------------------
	
	#createFootRigBLocators
	def createFootRigBLocators(self, prefix = ''):
		
		#set instance prefix var
		self.setPrefix(prefix)
		
		pm.select(cl = True)
		
		
		
		
		#Create Space locators and translate
		self.leg_locator_base = pm.spaceLocator(n = self.prefix + '_leg_locator_base')
		self.leg_locator_base.translate.set(0, 0, 0)
		pm.select(cl = True)
		
		self.leg_locator_knee = pm.spaceLocator(n = self.prefix + '_leg_locator_knee')
		self.leg_locator_knee.translate.set(4, 2, 0)
		pm.select(cl = True)
		
		self.leg_locator_tip = pm.spaceLocator(n = self.prefix + '_leg_locator_tip')
		self.leg_locator_tip.translate.set(8, -2, 0)
		pm.select(cl = True)
		
		self.leg_locator_poleVector = pm.spaceLocator(n = self.prefix + '_leg_locator_poleVector')
		self.leg_locator_poleVector.translate.set(4, 4, 0)
		pm.select(cl = True)
		
		self.foot_locator = pm.spaceLocator(n = self.prefix + '_foot_locator')
		self.foot_locator.translate.set(12, -2, 0)
		pm.select(cl = True)
		
		
		
		
		
		
		#Create Annotations and rename
		self.annotation_leg_locator_base = pm.annotate( self.leg_locator_base, tx = self.prefix +'_leg_locator_base' )
		pm.rename(self.annotation_leg_locator_base.getParent().name(), self.prefix + '_leg_locator_base_annotation')
		
		self.annotation_leg_locator_knee = pm.annotate( self.leg_locator_knee, tx = self.prefix +'_leg_locator_knee' )
		pm.rename(self.annotation_leg_locator_knee.getParent().name(), self.prefix + '_leg_locator_knee_annotation')
		
		self.annotation_leg_locator_tip = pm.annotate( self.leg_locator_tip, tx = self.prefix +'_leg_locator_tip' )
		pm.rename(self.annotation_leg_locator_tip.getParent().name(), self.prefix + '_leg_locator_tip_annotation')
		
		self.annotation_leg_locator_poleVector = pm.annotate( self.leg_locator_poleVector, tx = self.prefix +'_leg_locator_poleVector' )
		pm.rename(self.annotation_leg_locator_poleVector.getParent().name(), self.prefix + '_leg_locator_poleVector_annotation')
		
		self.annotation_foot_locator = pm.annotate( self.foot_locator, tx = self.prefix +'_foot_locator' )
		pm.rename(self.annotation_foot_locator.getParent().name(), self.prefix + '_foot_locator_annotation')
		
		
		pm.select(cl = True)
		
		
		
		
		
		#Parent constrain annotation transforms
		pm.parentConstraint(self.leg_locator_base, self.annotation_leg_locator_base.getParent(), mo = False)
		pm.parentConstraint(self.leg_locator_knee, self.annotation_leg_locator_knee.getParent(), mo = False)
		pm.parentConstraint(self.leg_locator_tip, self.annotation_leg_locator_tip.getParent(), mo = False)
		pm.parentConstraint(self.leg_locator_poleVector, self.annotation_leg_locator_poleVector.getParent(), mo = False)
		pm.parentConstraint(self.foot_locator, self.annotation_foot_locator.getParent(), mo = False)
		
		pm.select(cl = True)
		
	
	
	
	
	
	#Create Rig
	#----------------------------------------------------
	
	#createFootRigB
	def createFootRigB(self, prefix = '', displayProgressbar = True):
		
		
		#Check if Variables != None
		if(self.leg_locator_base and self.leg_locator_knee and self.leg_locator_tip and self.leg_locator_poleVector and self.foot_locator):
			
			#Check if locators exist in scene
			if(pm.objExists(self.leg_locator_base) and pm.objExists(self.leg_locator_knee) and pm.objExists(self.leg_locator_tip) and pm.objExists(self.leg_locator_poleVector) and pm.objExists(self.foot_locator)):
			
				
				
				
				#Create Progressbarwin if displayProgressbar == True
				if(displayProgressbar): self.createProgressbarWindow(progressbarSize = 19)
						
				
				#set instance prefix var
				self.setPrefix(prefix)
				
		
				pm.select(cl = True)
						
						
				#Create FootRigB
				#----------------------------------------------------
				
				
				
				
				#Leg Ik
				#----------------------------------------------------
				
				#createLocatorWorldCoordsAndSetFacingXPlus
				self.createLocatorWorldCoordsAndSetFacingXPlus()
				if(self.verbose): print('Successfully created locator world coords and facing direction')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createIkLegJoints
				self.createIkLegJoints()
				if(self.verbose): print('Successfully created IK leg joints')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createIkHandleLeg
				self.createIkHandleLeg()
				if(self.verbose): print('Successfully created IK handle leg')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createLegManipulatorsAndAimGroup
				self.createLegManipulatorsAndAimGroup()
				if(self.verbose): print('Successfully created leg manipulators and aim group')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createPoleVectorLocatorAndLinkingCurve
				self.createPoleVectorLocatorAndLinkingCurve()
				if(self.verbose): print('Successfully created pole vector locator and linking curve')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createManipulatorAndIkHandleConstraints
				self.createManipulatorAndIkHandleConstraints()
				if(self.verbose): print('Successfully created Manipulator and IK Handle Constraints')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				
				
				
				
				
				#Foot Spline Ik
				#----------------------------------------------------
				
				#createFootIkManipulators
				self.createFootIkManipulators()
				if(self.verbose): print('Successfully created Foot Ik Manipulators')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createCurveBoundJoints
				self.createCurveBoundJoints()
				if(self.verbose): print('Successfully created Curve Bound Joints')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFootIkBoundJointChain
				self.createFootIkBoundJointChain()
				if(self.verbose): print('Successfully created Bound Joint Chain')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFootIkTipJointChain
				self.createFootIkTipJointChain()
				if(self.verbose): print('Successfully created Tip Joint Chain')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFootIkBaseJointChain
				self.createFootIkBaseJointChain()
				if(self.verbose): print('Successfully created Base Joint Chain')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFootIkSplineCurveAndBindIt
				self.createFootIkSplineCurveAndBindIt()
				if(self.verbose): print('Successfully created foot ik spline curve and skincluster')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFootIkSplineIkTipAndBase
				self.createFootIkSplineIkTipAndBase()
				if(self.verbose): print('Successfully created foot ik spline ik for tip and base')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFootIkManipulatorConstraints
				self.createFootIkManipulatorConstraints()
				if(self.verbose): print('Successfully created foot ik manipulator constraints')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFootIkBoundJointsConstraints
				self.createFootIkBoundJointsConstraints()
				if(self.verbose): print('Successfully created foot ik bound joints constraints')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				#createFootIkStretchyness
				self.createFootIkStretchyness()
				if(self.verbose): print('Successfully created foot ik stretchyness')
				if(displayProgressbar): self.updateProgressbarWindow()
				
				
				
				
				
				
				
				#CleanUp
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
				if(self.verbose): print('Successfully created FootRigB')
				return None
					
				
				
				
				
				
			else:
				if(self.verbose): print('Locators seem to be missing in scene, please recreate them')
				return None
			
		else:
			if(self.verbose): print('No Locators created')
			return None
	
	
	
	
	
	
	
	
	#Methods
	#----------------------------------------------------
	
	
	#createLocatorWorldCoordsAndSetFacingXPlus
	def createLocatorWorldCoordsAndSetFacingXPlus(self):
		
		
		pm.select(cl = True)
		
		#create worldCoords
		self.leg_locator_base_worldCoords = pm.xform(self.leg_locator_base, ws = True, q = True, t = True)
		self.leg_locator_knee_worldCoords = pm.xform(self.leg_locator_knee, ws = True, q = True, t = True)
		self.leg_locator_tip_worldCoords = pm.xform(self.leg_locator_tip, ws = True, q = True, t = True)
		self.leg_locator_poleVector_worldCoords = pm.xform(self.leg_locator_poleVector, ws = True, q = True, t = True)
		self.foot_locator_worldCoords = pm.xform(self.foot_locator, ws = True, q = True, t = True)
		
		pm.select(cl = True)
		
		#set facingXPlus
		if(self.leg_locator_base_worldCoords[0] > self.foot_locator_worldCoords[0]): self.facingXPlus = False
		pm.select(cl = True)
	
	
	
	
	
	
	
	
	
	
	
	#Leg Ik
	#----------------------------------------------------
	
	

	#createIkLegJoints
	def createIkLegJoints(self):
		
		#Create Joints
		
		#leg_ik_j_base
		pm.select(cl = True)
		self.leg_ik_j_base = pm.joint(a = True, p= self.leg_locator_base_worldCoords , co = True, n = self.prefix +'_leg_ik_j_base')
		pm.select(cl = True)
		
		#leg_ik_j_knee
		pm.select(cl = True)
		self.leg_ik_j_knee = pm.joint(a = True, p= self.leg_locator_knee_worldCoords , co = True, n = self.prefix +'_leg_ik_j_knee')
		pm.select(cl = True)
		
		#leg_ik_j_tip
		pm.select(cl = True)
		self.leg_ik_j_tip = pm.joint(a = True, p= self.leg_locator_tip_worldCoords , co = True, n = self.prefix +'_leg_ik_j_tip')
		pm.select(cl = True)
		
		
		
		#Parent ik joints
		
		pm.parent(self.leg_ik_j_knee, self.leg_ik_j_base)
		pm.parent(self.leg_ik_j_tip, self.leg_ik_j_knee)
		pm.select(cl = True)
		
		#Orient ik joints
		pm.joint(self.leg_ik_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		
		
		
		#Group ik joints
		self.leg_ik_j_grp = pm.group(n = self.prefix + '_leg_ik_j_grp')
		pm.select(cl = True)
		#parent joint chain
		pm.parent(self.leg_ik_j_base, self.leg_ik_j_grp)
		pm.select(cl = True)
	
	
	
	
	#createIkHandleLeg
	def createIkHandleLeg(self):
		
		#create ik handle
		self.leg_ik_handle = pm.ikHandle( sj= self.leg_ik_j_base , ee= self.leg_ik_j_tip , n = self.prefix +'_ik_rp_Handle_leg' , sol = 'ikRPsolver' )[0]
		pm.select(cl = True)
		
		#ik handle grp
		self.leg_ik_handle_grp = pm.group(self.leg_ik_handle, n = self.prefix + '_leg_ik_handle_grp')
		pm.select(cl = True)
		
		
		
	
	#createLegManipulatorsAndAimGroup
	def createLegManipulatorsAndAimGroup(self):
		
		pm.select(cl = True)
		
		
		#manip_leg_base
		#----------------------------------------------------
		
		#create manip
		self.manip_leg_base = pm.circle(r = 2, name = self.prefix +'_manip_leg_base', ch = False, nr=(1, 0, 0))[0]
		pm.select(cl = True)
		
		#create and parent under grp
		self.manip_leg_base_grp = pm.group(n = self.prefix + '_manip_leg_base_grp')
		pm.select(cl = True)
		pm.parent(self.manip_leg_base, self.manip_leg_base_grp)
		pm.select(cl = True)
		#translate
		self.manip_leg_base_grp.translate.set(self.leg_locator_base_worldCoords)
		pm.select(cl = True)
		
		
		
		
		#manip_leg_ik
		#----------------------------------------------------
		
		#create manip
		self.manip_leg_ik = pm.circle(r = 2, name = self.prefix +'_manip_leg_ik', ch = False, nr=(1, 0, 0))[0]
		pm.select(cl = True)
		
		#create parentScale and point grps
		self.manip_leg_ik_grp = pm.group(n = self.prefix + '_manip_leg_ik_grp')
		pm.select(cl = True)
		self.manip_leg_ik_point_grp = pm.group(n = self.prefix + '_manip_leg_ik_point_grp')
		pm.select(cl = True)
		
		#parent grps and manip
		pm.parent(self.manip_leg_ik_point_grp, self.manip_leg_ik_grp)
		pm.select(cl = True)
		pm.parent(self.manip_leg_ik, self.manip_leg_ik_point_grp)
		pm.select(cl = True)
		
		#translate
		self.manip_leg_ik_grp.translate.set(self.leg_locator_tip_worldCoords)
		pm.select(cl = True)
		
		
		
		
		#manip_leg_complete
		#----------------------------------------------------
		
		#create manip
		self.manip_leg_complete = pm.circle(r = 2, name = self.prefix +'_manip_leg_complete', ch = False, nr=(0, 1, 0))[0]
		pm.select(cl = True)
		
		#create and parent under grp
		self.manip_leg_complete_grp = pm.group(n = self.prefix + '_manip_leg_complete_grp')
		pm.select(cl = True)
		pm.parent(self.manip_leg_complete, self.manip_leg_complete_grp)
		pm.select(cl = True)
		#translate
		self.manip_leg_complete_grp.translate.set(self.foot_locator_worldCoords)
		pm.select(cl = True)
		
		
		
		
		#manip_aim_indicator
		#----------------------------------------------------
	
		#create manip_aim_indicator point list
		if(self.facingXPlus): manip_aim_indicator_PointsList = [(0,0,-1), (2,0,-1), (2,0,-2), (4, 0, 0), (2, 0, 2), (2, 0, 1), (0, 0, 1), (0,0,-1)]
		else: manip_aim_indicator_PointsList = [(0,0,-1), (-2,0,-1), (-2,0,-2), (-4, 0, 0), (-2, 0, 2), (-2, 0, 1), (0, 0, 1), (0,0,-1)]
		
		#create manip_aim_indicator
		self.manip_aim_indicator = pm.curve( p = manip_aim_indicator_PointsList, ws = True, d = 1 , n = self.prefix + '_manip_aim_indicator')
		pm.select(cl = True)
		
		#create manip aim indicator grp
		self.manip_aim_indicator_grp = pm.group(n = self.prefix + '_manip_aim_indicator_grp')
		pm.select(cl = True)
		
		#create manip aim indicator aim grp
		self.manip_aim_indicator_aim_grp = pm.group(n = self.prefix + '_manip_aim_indicator_aim_grp')
		pm.select(cl = True)
		
		#parent groups and manip
		pm.parent(self.manip_aim_indicator_aim_grp, self.manip_aim_indicator_grp)
		pm.parent(self.manip_aim_indicator, self.manip_aim_indicator_aim_grp)
		
		#translate aim group
		self.manip_aim_indicator_grp.translate.set(self.leg_locator_base_worldCoords)
		pm.select(cl = True)
		
		
		
		
		
	#createPoleVectorLocatorAndLinkingCurve
	def createPoleVectorLocatorAndLinkingCurve(self):
	
		pm.select(cl = True)
		
		#PoleVector
		#----------------------------------------------------
		
		#Create leg ik pole vector loc
		self.leg_ik_pole_vector_locator = pm.spaceLocator(n = self.prefix +'_leg_ik_pole_vector_locator')
		pm.select(cl = True)
		
		#Group leg ik pole vec
		self.leg_ik_pole_vector_locator_grp = pm.group(self.leg_ik_pole_vector_locator, n = self.prefix + '_leg_ik_pole_vector_locator_grp')
		pm.select(cl = True)
		
		#Translate leg_ik_pole_vector_locator_grp
		self.leg_ik_pole_vector_locator_grp.translate.set(self.leg_locator_poleVector_worldCoords)
		
		
		
		#LinkingCurve
		#----------------------------------------------------
		
		#Create linking curve loc
		self.leg_ik_pole_vector_locator_linking_curve_locator = pm.spaceLocator(n = self.prefix +'_leg_ik_pole_vector_locator_linking_curve_locator')
		pm.select(cl = True)
		
		#point con linking curve loc to leg ik j base
		pm.pointConstraint(self.leg_ik_j_base, self.leg_ik_pole_vector_locator_linking_curve_locator , mo = False)
		
		
		#Create Pole vector Linking Curve
		self.pole_vector_linking_curve = pm.curve(p = [self.leg_locator_base_worldCoords , self.leg_locator_poleVector_worldCoords], d = 1, n = self.prefix +'_pole_vector_linking_curve')
		pm.select(cl = True)
		
		#make curve not selectable
		pm.setAttr(self.pole_vector_linking_curve.getShape().overrideEnabled, 1)
		pm.setAttr(self.pole_vector_linking_curve.getShape().overrideDisplayType, 2)
		pm.select(cl = True)
		
		#Connect loc world space coords to curve points
		self.leg_ik_pole_vector_locator_linking_curve_locator.getShape().worldPosition[0] >> self.pole_vector_linking_curve.getShape().controlPoints[0]
		self.leg_ik_pole_vector_locator.getShape().worldPosition[0] >> self.pole_vector_linking_curve.getShape().controlPoints[1]
		pm.select(cl = True)
		
		#Create grp
		self.pole_vector_linking_curve_grp = pm.group( n = self.prefix +'_pole_vector_linking_curve_grp')
		pm.select(cl = True)
		
		#parent objects in group
		pm.parent(self.leg_ik_pole_vector_locator_linking_curve_locator, self.pole_vector_linking_curve ,self.pole_vector_linking_curve_grp)
		pm.select(cl = True)
		
		
		
	#createManipulatorAndIkHandleConstraints
	def createManipulatorAndIkHandleConstraints(self):
		
		pm.select(cl = True)
		
		
		#manip_aim indicator aim grp
		pm.aimConstraint(self.manip_leg_complete, self.manip_aim_indicator_aim_grp, aim = (1,0,0), u = (0,1,0), wut = 'objectrotation' , wu = (0,1,0) ,mo = True)
		pm.select(cl = True)
		
		
		#manip_leg_ik
		pm.parentConstraint(self.manip_aim_indicator, self.manip_leg_ik_grp, mo = True)
		pm.scaleConstraint(self.manip_aim_indicator, self.manip_leg_ik_grp, mo = True)
		
		pm.pointConstraint(self.manip_leg_complete, self.manip_leg_ik_point_grp, mo = True)
		pm.select(cl = True)
		
		
		#poleVector
		pm.parentConstraint(self.manip_aim_indicator, self.leg_ik_pole_vector_locator_grp, mo = True)
		pm.scaleConstraint(self.manip_aim_indicator, self.leg_ik_pole_vector_locator_grp, mo = True)
		pm.select(cl = True)
		
		
		#poleVectorConstraint
		pm.poleVectorConstraint(self.leg_ik_pole_vector_locator, self.leg_ik_handle)
		pm.select(cl = True)
		
		
		#IkHandle
		pm.parentConstraint(self.manip_leg_ik, self.leg_ik_handle_grp, mo = True)
		pm.scaleConstraint(self.manip_leg_ik, self.leg_ik_handle_grp, mo = True)
		pm.select(cl = True)
		
		
		#ik_j_tip
		pm.orientConstraint(self.manip_leg_ik, self.leg_ik_j_tip, mo = True)
		pm.select(cl = True)
		
		
		#ik_j_grp
		pm.parentConstraint(self.manip_leg_base, self.leg_ik_j_grp, mo = True)
		pm.scaleConstraint(self.manip_leg_base, self.leg_ik_j_grp, mo = True)
		pm.select(cl = True)
		
		
		
		
	
	
	
	
	
	
	#Foot Spline Ik
	#----------------------------------------------------
		
		
	#createFootIkManipulators
	def createFootIkManipulators(self):
		
		pm.select(cl = True)
		
		#manip_foot_ik_pointsList
		manip_foot_ik_pointsList = [(0,0,1), (0,2,0), (0,0,-1), (0, 0, 1)]
		
		
		
		#manip_foot_ik_base
		#----------------------------------------------------
		
		#create manip_foot_ik_base
		self.manip_foot_ik_base = pm.curve( p = manip_foot_ik_pointsList, ws = True, d = 1 , n = self.prefix + '_manip_foot_ik_base')
		pm.select(cl = True)
		
		#foot_ik_base_grp
		self.manip_foot_ik_base_grp = pm.group(n = self.prefix + '_manip_foot_ik_base_grp')
		pm.select(cl = True)
		
		#parent manip and translate grp
		pm.parent(self.manip_foot_ik_base, self.manip_foot_ik_base_grp)
		pm.select(cl = True)
		self.manip_foot_ik_base_grp.translate.set(self.leg_locator_tip_worldCoords)
		pm.select(cl = True)
		
		
		
		
		#manip_foot_ik_tip
		#----------------------------------------------------
		
		#create manip_foot_ik_tip
		self.manip_foot_ik_tip = pm.curve( p = manip_foot_ik_pointsList, ws = True, d = 1 , n = self.prefix + '_manip_foot_ik_tip')
		pm.select(cl = True)
		
		#Custom Divider
		pm.addAttr(self.manip_foot_ik_tip, ln = '_', at='enum', en = 'Custom', h = False, k = True, r = True)
		pm.setAttr(self.manip_foot_ik_tip._ , lock = True)
		
		pm.addAttr(self.manip_foot_ik_tip,ln = 'stretchy', at='float', defaultValue= 0.0, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		pm.addAttr(self.manip_foot_ik_tip,ln = 'stretchyOffset', at='float', defaultValue= 0.0, h = False, k = True, r = True)
		pm.addAttr(self.manip_foot_ik_tip,ln = 'worldScale', at='float', defaultValue= 1.0, h = False, k = True, r = True)
		
		
		
		#foot_ik_tip_grp
		self.manip_foot_ik_tip_grp = pm.group(n = self.prefix + '_manip_foot_ik_tip_grp')
		pm.select(cl = True)
		
		#foot_ik_tip_point_grp
		self.manip_foot_ik_tip_point_grp = pm.group(n = self.prefix + '_manip_foot_ik_tip_point_grp')
		pm.select(cl = True)
		
		#parent manips and translate grp
		pm.parent(self.manip_foot_ik_tip_point_grp, self.manip_foot_ik_tip_grp)
		pm.select(cl = True)
		pm.parent(self.manip_foot_ik_tip, self.manip_foot_ik_tip_point_grp)
		pm.select(cl = True)
		self.manip_foot_ik_tip_grp.translate.set(self.foot_locator_worldCoords)
		pm.select(cl = True)
		
	
	
	
	
	#createCurveBoundJoints
	def createCurveBoundJoints(self):
		
		pm.select(cl = True)
		
		
		#curve_bound_j_base
		pm.select(cl = True)
		self.curve_bound_j_base = pm.joint(a = True, p= (0,0,0),  co = True, n = self.prefix +'_curve_bound_j_base')
		pm.select(cl = True)
		
		#group
		self.curve_bound_j_base_grp = pm.group(self.curve_bound_j_base, n = self.prefix + '_curve_bound_j_base_grp')
		pm.select(cl = True)
		
		#translate
		self.curve_bound_j_base_grp.translate.set(self.leg_locator_tip_worldCoords)
		pm.select(cl = True)
		
		
		
		#curve_bound_j_tip
		pm.select(cl = True)
		self.curve_bound_j_tip = pm.joint(a = True, p= (0,0,0),  co = True, n = self.prefix +'_curve_bound_j_tip')
		pm.select(cl = True)
		
		#group
		self.curve_bound_j_tip_grp = pm.group(self.curve_bound_j_tip, n = self.prefix + '_curve_bound_j_tip_grp')
		pm.select(cl = True)
		
		#translate
		self.curve_bound_j_tip_grp.translate.set(self.foot_locator_worldCoords)
		pm.select(cl = True)
	
	
	
	
	#createFootIkBoundJointChain
	def createFootIkBoundJointChain(self):
		
		pm.select(cl = True)
		
		#getFootIkPositionList(self, vectorA, vectorB, divisions)
		self.footIkJointsPositionList = self.getFootIkPositionList(self.leg_locator_tip_worldCoords, self.foot_locator_worldCoords, 6)
		
		
		#Create Joints
		
		#foot_ik_bound_j_base
		pm.select(cl = True)
		self.foot_ik_bound_j_base = pm.joint(a = True, p= self.footIkJointsPositionList[0] , co = True, n = self.prefix +'_foot_ik_bound_j_base')
		
		
		#foot_ik_bound_j_2
		self.foot_ik_bound_j_2 = pm.joint(a = True, p= self.footIkJointsPositionList[1] , co = True, n = self.prefix +'_foot_ik_bound_j_2')
		
		
		#foot_ik_bound_j_3
		self.foot_ik_bound_j_3 = pm.joint(a = True, p= self.footIkJointsPositionList[2] , co = True, n = self.prefix +'_foot_ik_bound_j_3')
		
		
		#foot_ik_bound_j_4
		self.foot_ik_bound_j_4 = pm.joint(a = True, p= self.footIkJointsPositionList[3] , co = True, n = self.prefix +'_foot_ik_bound_j_4')
		
		
		#foot_ik_bound_j_5
		self.foot_ik_bound_j_5 = pm.joint(a = True, p= self.footIkJointsPositionList[4] , co = True, n = self.prefix +'_foot_ik_bound_j_5')
		
		
		#foot_ik_bound_j_6
		self.foot_ik_bound_j_6 = pm.joint(a = True, p= self.footIkJointsPositionList[5] , co = True, n = self.prefix +'_foot_ik_bound_j_6')
		
		
		#foot_ik_bound_j_tip
		self.foot_ik_bound_j_tip = pm.joint(a = True, p= self.footIkJointsPositionList[6] , co = True, n = self.prefix +'_foot_ik_bound_j_tip')
		pm.select(cl = True)
		
		
		
		
		
		#Orient ik joints
		pm.joint(self.foot_ik_bound_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		
		
		
		#Group ik joints
		self.foot_ik_bound_j_grp = pm.group(n = self.prefix + '_foot_ik_bound_j_grp')
		pm.select(cl = True)
		#parent joint chain
		pm.parent(self.foot_ik_bound_j_base, self.foot_ik_bound_j_grp)
		pm.select(cl = True)
		
		
		
	#createFootIkTipJointChain
	def createFootIkTipJointChain(self):
		
		pm.select(cl = True)
		
		
		#Create Joints
		
		#foot_ik_tip_j_base
		pm.select(cl = True)
		self.foot_ik_tip_j_base = pm.joint(a = True, p= self.footIkJointsPositionList[0] , co = True, n = self.prefix +'_foot_ik_tip_j_base')
		
		
		#foot_ik_tip_j_2
		self.foot_ik_tip_j_2 = pm.joint(a = True, p= self.footIkJointsPositionList[1] , co = True, n = self.prefix +'_foot_ik_tip_j_2')
		
		
		#foot_ik_tip_j_3
		self.foot_ik_tip_j_3 = pm.joint(a = True, p= self.footIkJointsPositionList[2] , co = True, n = self.prefix +'_foot_ik_tip_j_3')
		
		
		#foot_ik_tip_j_4
		self.foot_ik_tip_j_4 = pm.joint(a = True, p= self.footIkJointsPositionList[3] , co = True, n = self.prefix +'_foot_ik_tip_j_4')
		
		
		#foot_ik_tip_j_5
		self.foot_ik_tip_j_5 = pm.joint(a = True, p= self.footIkJointsPositionList[4] , co = True, n = self.prefix +'_foot_ik_tip_j_5')
		
		
		#foot_ik_tip_j_6
		self.foot_ik_tip_j_6 = pm.joint(a = True, p= self.footIkJointsPositionList[5] , co = True, n = self.prefix +'_foot_ik_tip_j_6')
		
		
		#foot_ik_tip_j_tip
		self.foot_ik_tip_j_tip = pm.joint(a = True, p= self.footIkJointsPositionList[6] , co = True, n = self.prefix +'_foot_ik_tip_j_tip')
		pm.select(cl = True)
		
		
		
		
		
		#Orient ik joints
		pm.joint(self.foot_ik_tip_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		
		
		
		#Group ik joints
		self.foot_ik_tip_j_grp = pm.group(n = self.prefix + '_foot_ik_tip_j_grp')
		pm.select(cl = True)
		#parent joint chain
		pm.parent(self.foot_ik_tip_j_base, self.foot_ik_tip_j_grp)
		pm.select(cl = True)
		
		
		
	#createFootIkBaseJointChain
	def createFootIkBaseJointChain(self):
		
		pm.select(cl = True)
		
		
		#Create Joints
		
		#foot_ik_base_j_base
		pm.select(cl = True)
		self.foot_ik_base_j_base = pm.joint(a = True, p= self.footIkJointsPositionList[0] , co = True, n = self.prefix +'_foot_ik_base_j_base')
		
		
		#foot_ik_base_j_2
		self.foot_ik_base_j_2 = pm.joint(a = True, p= self.footIkJointsPositionList[1] , co = True, n = self.prefix +'_foot_ik_base_j_2')
		
		
		#foot_ik_base_j_3
		self.foot_ik_base_j_3 = pm.joint(a = True, p= self.footIkJointsPositionList[2] , co = True, n = self.prefix +'_foot_ik_base_j_3')
		
		
		#foot_ik_base_j_4
		self.foot_ik_base_j_4 = pm.joint(a = True, p= self.footIkJointsPositionList[3] , co = True, n = self.prefix +'_foot_ik_base_j_4')
		
		
		#foot_ik_base_j_5
		self.foot_ik_base_j_5 = pm.joint(a = True, p= self.footIkJointsPositionList[4] , co = True, n = self.prefix +'_foot_ik_base_j_5')
		
		
		#foot_ik_base_j_6
		self.foot_ik_base_j_6 = pm.joint(a = True, p= self.footIkJointsPositionList[5] , co = True, n = self.prefix +'_foot_ik_base_j_6')
		
		
		#foot_ik_base_j_tip
		self.foot_ik_base_j_tip = pm.joint(a = True, p= self.footIkJointsPositionList[6] , co = True, n = self.prefix +'_foot_ik_base_j_tip')
		pm.select(cl = True)
		
		
		
		
		
		#Orient ik joints
		pm.joint(self.foot_ik_base_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		
		
		
		#Group ik joints
		self.foot_ik_base_j_grp = pm.group(n = self.prefix + '_foot_ik_base_j_grp')
		pm.select(cl = True)
		#parent joint chain
		pm.parent(self.foot_ik_base_j_base, self.foot_ik_base_j_grp)
		pm.select(cl = True)
		
		
		
		
	#createFootIkSplineCurveAndBindIt
	def createFootIkSplineCurveAndBindIt(self):
		
		pm.select(cl = True)
		
		#create foot_splineIk_curve
		self.foot_splineIk_curve = pm.curve( p = self.footIkJointsPositionList, ws = True, d = 2 , n = self.prefix + '_foot_splineIk_curve')
		pm.select(cl = True)
		
		#create foot_splineIk_curve_grp
		self.foot_splineIk_curve_grp = pm.group(n = self.prefix + '_foot_splineIk_curve_grp')
		pm.select(cl = True)
		#parent
		pm.parent(self.foot_splineIk_curve, self.foot_splineIk_curve_grp)
		pm.select(cl = True)
		
		
		#smoothbind splineIk curve to curve bound joints
		self.foot_splineIk_skincluster = pm.skinCluster( self.curve_bound_j_base , self.curve_bound_j_tip , self.foot_splineIk_curve , tsb=True, n = self.prefix + '_splineIk_skincluster', rui = False, ih = True)
		pm.select(cl = True)
	
	
	
	
	#createFootIkSplineIkTipAndBase
	def createFootIkSplineIkTipAndBase(self):
		
		pm.select(cl = True)
		
		#foot_spline_ik_tip
		#----------------------------------------------------
		self.foot_spline_ik_tip = pm.ikHandle( sj= self.foot_ik_tip_j_base , ee= self.foot_ik_tip_j_tip , roc = True, n = self.prefix + '_ik_spline_handle_tip', c = self.foot_splineIk_curve, ccv = False, pcv = False, sol = 'ikSplineSolver')[0]
		pm.select(cl = True)
		
		#set splineIk twist attributes
		pm.setAttr(self.foot_spline_ik_tip.dTwistControlEnable, 1)
		pm.setAttr(self.foot_spline_ik_tip.dWorldUpType, 3)
		pm.setAttr(self.foot_spline_ik_tip.dWorldUpAxis, 0)
		pm.setAttr(self.foot_spline_ik_tip.dWorldUpVectorX, 0)
		pm.setAttr(self.foot_spline_ik_tip.dWorldUpVectorY, 1)
		pm.setAttr(self.foot_spline_ik_tip.dWorldUpVectorZ, 0)
		
		pm.connectAttr(self.manip_foot_ik_tip.worldMatrix[0], self.foot_spline_ik_tip.dWorldUpMatrix, f = True)
		pm.select(cl = True)
		
		#Group Spline_ik
		self.foot_spline_ik_tip_grp = pm.group(self.foot_spline_ik_tip ,  n= self.prefix + '_foot_spline_ik_tip_grp' )
		pm.select(cl = True)
		
		
		
		
		#foot_spline_ik_base
		#----------------------------------------------------
		self.foot_spline_ik_base = pm.ikHandle( sj= self.foot_ik_base_j_base , ee= self.foot_ik_base_j_tip , roc = True, n = self.prefix + '_ik_spline_handle_base', c = self.foot_splineIk_curve, ccv = False, pcv = False, sol = 'ikSplineSolver')[0]
		pm.select(cl = True)
		
		#set splineIk twist attributes
		pm.setAttr(self.foot_spline_ik_base.dTwistControlEnable, 1)
		pm.setAttr(self.foot_spline_ik_base.dWorldUpType, 3)
		pm.setAttr(self.foot_spline_ik_base.dWorldUpAxis, 0)
		pm.setAttr(self.foot_spline_ik_base.dWorldUpVectorX, 0)
		pm.setAttr(self.foot_spline_ik_base.dWorldUpVectorY, 1)
		pm.setAttr(self.foot_spline_ik_base.dWorldUpVectorZ, 0)
		
		pm.connectAttr(self.manip_foot_ik_base.worldMatrix[0], self.foot_spline_ik_base.dWorldUpMatrix, f = True)
		pm.select(cl = True)
		
		#Group Spline_ik
		self.foot_spline_ik_base_grp = pm.group(self.foot_spline_ik_base ,  n= self.prefix + '_foot_spline_ik_base_grp' )
		pm.select(cl = True)
		
		
		
	#createFootIkManipulatorConstraints
	def createFootIkManipulatorConstraints(self):
		
		pm.select(cl = True)
		
		#manip foot spline ik base
		pm.parentConstraint(self.leg_ik_j_tip, self.manip_foot_ik_base_grp, mo = True)
		pm.scaleConstraint(self.leg_ik_j_tip, self.manip_foot_ik_base_grp, mo = True)
		pm.select(cl = True)
		
		#manip foot spline ik tip
		pm.parentConstraint(self.manip_aim_indicator, self.manip_foot_ik_tip_grp, mo = True)
		pm.scaleConstraint(self.manip_aim_indicator, self.manip_foot_ik_tip_grp, mo = True)
		
		pm.pointConstraint(self.manip_leg_complete, self.manip_foot_ik_tip_point_grp, mo = True)
		pm.select(cl = True)
		
		
		#curve_bound_j_base_grp
		pm.parentConstraint(self.manip_foot_ik_base, self.curve_bound_j_base_grp, mo = True)
		pm.scaleConstraint(self.manip_foot_ik_base, self.curve_bound_j_base_grp, mo = True)
		pm.select(cl = True)
		
		#curve_bound_j_tip_grp
		pm.parentConstraint(self.manip_foot_ik_tip, self.curve_bound_j_tip_grp, mo = True)
		pm.scaleConstraint(self.manip_foot_ik_tip, self.curve_bound_j_tip_grp, mo = True)
		pm.select(cl = True)
		
		
		#foot_ik_bound_j_grp
		pm.parentConstraint(self.manip_foot_ik_base, self.foot_ik_bound_j_grp, mo = True)
		pm.scaleConstraint(self.manip_foot_ik_base, self.foot_ik_bound_j_grp, mo = True)
		pm.select(cl = True)
		
		#foot_ik_tip_j_grp
		pm.parentConstraint(self.manip_foot_ik_base, self.foot_ik_tip_j_grp, mo = True)
		pm.scaleConstraint(self.manip_foot_ik_base, self.foot_ik_tip_j_grp, mo = True)
		pm.select(cl = True)
		
		#foot_ik_base_j_grp
		pm.parentConstraint(self.manip_foot_ik_base, self.foot_ik_base_j_grp, mo = True)
		pm.scaleConstraint(self.manip_foot_ik_base, self.foot_ik_base_j_grp, mo = True)
		pm.select(cl = True)
		
		
		
		
	#createFootIkBoundJointsConstraints
	def createFootIkBoundJointsConstraints(self):
		
		pm.select(cl = True)
		
		
		#Create Constratints
		#----------------------------------------------------
		
		#foot_ik_bound_j_base
		pm.orientConstraint(self.foot_ik_base_j_base, self.foot_ik_bound_j_base, mo = True)
		pm.select(cl = True)
		
		#foot_ik_bound_j_2_orientCon
		self.foot_ik_bound_j_2_orientCon = pm.orientConstraint(self.foot_ik_base_j_2, self.foot_ik_tip_j_2, self.foot_ik_bound_j_2, mo = True)
		pm.select(cl = True)
		
		#foot_ik_bound_j_3_orientCon
		self.foot_ik_bound_j_3_orientCon = pm.orientConstraint(self.foot_ik_base_j_3, self.foot_ik_tip_j_3, self.foot_ik_bound_j_3, mo = True)
		pm.select(cl = True)
		
		#foot_ik_bound_j_4_orientCon
		self.foot_ik_bound_j_4_orientCon = pm.orientConstraint(self.foot_ik_base_j_4, self.foot_ik_tip_j_4, self.foot_ik_bound_j_4, mo = True)
		pm.select(cl = True)
		
		#foot_ik_bound_j_5_orientCon
		self.foot_ik_bound_j_5_orientCon = pm.orientConstraint(self.foot_ik_base_j_5, self.foot_ik_tip_j_5, self.foot_ik_bound_j_5, mo = True)
		pm.select(cl = True)
		
		#foot_ik_bound_j_6_orientCon
		self.foot_ik_bound_j_6_orientCon = pm.orientConstraint(self.foot_ik_base_j_6, self.foot_ik_tip_j_6, self.foot_ik_bound_j_6, mo = True)
		pm.select(cl = True)
		
		#foot_ik_bound_j_tip
		pm.orientConstraint(self.foot_ik_tip_j_tip, self.foot_ik_bound_j_tip, mo = True)
		pm.select(cl = True)
		
		
		
		#Adjust weights
		#----------------------------------------------------
		
		#foot_ik_bound_j_2_orientCon
		pm.setAttr(self.foot_ik_bound_j_2_orientCon.name() +'.' + self.foot_ik_tip_j_2.name() + 'W1' , 0.33)
		
		#foot_ik_bound_j_3_orientCon
		pm.setAttr(self.foot_ik_bound_j_3_orientCon.name() +'.' + self.foot_ik_tip_j_3.name() + 'W1' , 0.66)
		
		#foot_ik_bound_j_5_orientCon
		pm.setAttr(self.foot_ik_bound_j_5_orientCon.name() +'.' + self.foot_ik_base_j_5.name() + 'W0' , 0.66)
		
		#foot_ik_bound_j_6_orientCon
		pm.setAttr(self.foot_ik_bound_j_6_orientCon.name() +'.' + self.foot_ik_base_j_6.name() + 'W0' , 0.33)
		
		pm.select(cl = True)
		
	
	
	
	
	#createFootIkStretchyness
	def createFootIkStretchyness(self):
		
		pm.select(cl = True)
		
		
		#Create Stretchyness
		#----------------------------------------------------
		
		
		#createArcLen Node
		self.splineIk_curve_info = pm.PyNode(cmds.arclen(self.foot_splineIk_curve.name(), ch = True))
		pm.select(cl = True)
		
		
		#Normalize Worldspace
		self.normalize_world_space = pm.nodetypes.MultiplyDivide(n = self.prefix +'_normalize_world_space')
		pm.setAttr(self.normalize_world_space.operation , 2)
		self.splineIk_curve_info.arcLength >> self.normalize_world_space.input1X
		self.manip_foot_ik_tip.worldScale >> self.normalize_world_space.input2X
		pm.select(cl = True)
		
		
		#Normalize Distance
		self.normalize_distance = pm.nodetypes.MultiplyDivide(n = self.prefix +'_normalize_distance')
		pm.setAttr(self.normalize_distance.operation , 2)
		self.normalize_world_space.outputX >> self.normalize_distance.input1X
		
		#Set Normalize Distance to arcLength
		pm.setAttr(self.normalize_distance.input2X , pm.getAttr(self.splineIk_curve_info.arcLength))
		
		
		#Create condition node to check wether or not normalized distance is greater one
		self.normalized_distance_greater_one = pm.nodetypes.Condition(n = self.prefix +'_normalized_distance_greater_one')
		pm.setAttr(self.normalized_distance_greater_one.operation, 2)
		self.normalize_distance.outputX >> self.normalized_distance_greater_one.firstTerm
		self.normalize_distance.outputX >> self.normalized_distance_greater_one.colorIfTrueR
		pm.setAttr(self.normalized_distance_greater_one.secondTerm , 1)
		pm.setAttr(self.normalized_distance_greater_one.colorIfFalseR , 1)
		
		#Create Blend colors node to blend stretchyness
		self.blend_stretchyness = pm.nodetypes.BlendColors(n = self.prefix +'_blend_stretchyness')
		self.manip_foot_ik_tip.stretchy >> self.blend_stretchyness.blender
		self.normalized_distance_greater_one.outColorR >> self.blend_stretchyness.color1R
		pm.setAttr(self.blend_stretchyness.color2R, 1)
		
		
		
		#Multiply output of Blendnode with joints translate x value
		self.multiply_stretch_factor = pm.nodetypes.MultiplyDivide(n = self.prefix +'_multiply_stretch_factor')
		pm.setAttr(self.multiply_stretch_factor.operation , 1)
		self.blend_stretchyness.outputR >> self.multiply_stretch_factor.input1X
		pm.setAttr(self.multiply_stretch_factor.input2X , pm.getAttr(self.foot_ik_bound_j_2.tx))
		
		
		#Create Add Offset node
		self.add_offset = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_add_offset')
		self.manip_foot_ik_tip.stretchyOffset >> self.add_offset.input1D[0]
		self.multiply_stretch_factor.outputX >> self.add_offset.input1D[1]
		
		
		
		#Connect Joints
		#----------------------------------------------------
		
		
		#spline_ik_bound_joints
		self.add_offset.output1D >> self.foot_ik_bound_j_2.translateX
		self.add_offset.output1D >> self.foot_ik_bound_j_3.translateX
		self.add_offset.output1D >> self.foot_ik_bound_j_4.translateX
		self.add_offset.output1D >> self.foot_ik_bound_j_5.translateX
		self.add_offset.output1D >> self.foot_ik_bound_j_6.translateX
		self.add_offset.output1D >> self.foot_ik_bound_j_tip.translateX
		
		#spline_ik_base_joints
		self.add_offset.output1D >> self.foot_ik_base_j_2.translateX
		self.add_offset.output1D >> self.foot_ik_base_j_3.translateX
		self.add_offset.output1D >> self.foot_ik_base_j_4.translateX
		self.add_offset.output1D >> self.foot_ik_base_j_5.translateX
		self.add_offset.output1D >> self.foot_ik_base_j_6.translateX
		self.add_offset.output1D >> self.foot_ik_base_j_tip.translateX
		
		#spline_ik_tip_joints
		self.add_offset.output1D >> self.foot_ik_tip_j_2.translateX
		self.add_offset.output1D >> self.foot_ik_tip_j_3.translateX
		self.add_offset.output1D >> self.foot_ik_tip_j_4.translateX
		self.add_offset.output1D >> self.foot_ik_tip_j_5.translateX
		self.add_offset.output1D >> self.foot_ik_tip_j_6.translateX
		self.add_offset.output1D >> self.foot_ik_tip_j_tip.translateX
		
		
		pm.select(cl = True)
		
	




	
	
	#CleanUp
	#----------------------------------------------------
	
	
	#setVisibilityAndLockAttrs
	def setVisibilityAndLockAttrs(self):
		pm.select(cl = True)
		
		#manip_leg_base
		pm.setAttr(self.manip_leg_base.scaleX, lock = True)
		pm.setAttr(self.manip_leg_base.scaleY, lock = True)
		pm.setAttr(self.manip_leg_base.scaleZ, lock = True)
		
		pm.setAttr(self.manip_leg_base.visibility, lock = True)
		
		
		#manip_aim_indicator
		pm.setAttr(self.manip_aim_indicator.translateX, lock = True)
		pm.setAttr(self.manip_aim_indicator.translateY, lock = True)
		pm.setAttr(self.manip_aim_indicator.translateZ, lock = True)
		
		pm.setAttr(self.manip_aim_indicator.rotateX, lock = True)
		pm.setAttr(self.manip_aim_indicator.rotateY, lock = True)
		pm.setAttr(self.manip_aim_indicator.rotateZ, lock = True)
		
		pm.setAttr(self.manip_aim_indicator.scaleX, lock = True)
		pm.setAttr(self.manip_aim_indicator.scaleY, lock = True)
		pm.setAttr(self.manip_aim_indicator.scaleZ, lock = True)
		
		pm.setAttr(self.manip_aim_indicator.visibility, lock = True)
		
		
		#leg_ik_pole_vector_locator
		pm.setAttr(self.leg_ik_pole_vector_locator.scaleX, lock = True)
		pm.setAttr(self.leg_ik_pole_vector_locator.scaleY, lock = True)
		pm.setAttr(self.leg_ik_pole_vector_locator.scaleZ, lock = True)
		
		pm.setAttr(self.leg_ik_pole_vector_locator.visibility, lock = True)
		
		
		#manip_leg_ik
		pm.setAttr(self.manip_leg_ik.scaleX, lock = True)
		pm.setAttr(self.manip_leg_ik.scaleY, lock = True)
		pm.setAttr(self.manip_leg_ik.scaleZ, lock = True)
		
		pm.setAttr(self.manip_leg_ik.visibility, lock = True)
		
		
		#manip_foot_ik_tip
		pm.setAttr(self.manip_foot_ik_tip.visibility, lock = True)
		
		
		#manip_leg_complete
		pm.setAttr(self.manip_leg_complete.scaleX, lock = True)
		pm.setAttr(self.manip_leg_complete.scaleY, lock = True)
		pm.setAttr(self.manip_leg_complete.scaleZ, lock = True)
		
		pm.setAttr(self.manip_leg_complete.visibility, lock = True)
		
		
		#Set manip_foot_ik_base_grp visibility
		pm.setAttr(self.manip_foot_ik_base_grp.visibility, 0)
		
		
	
	
	
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
		pm.parent( self.foot_spline_ik_base_grp ,self.foot_spline_ik_tip_grp, self.foot_splineIk_curve_grp, self.leg_ik_handle_grp, self.nodesGrp)
		pm.select(cl = True)
		
		#manipsGrp
		pm.parent( self.pole_vector_linking_curve_grp, self.manip_foot_ik_tip_grp , self.manip_foot_ik_base_grp, self.leg_ik_pole_vector_locator_grp , self.manip_aim_indicator_grp , self.manip_leg_complete_grp, self.manip_leg_ik_grp, self.manip_leg_base_grp, self.manipsGrp)
		pm.select(cl = True)
		
		#jointsGrp
		pm.parent( self.foot_ik_tip_j_grp , self.foot_ik_base_j_grp, self.foot_ik_bound_j_grp , self.curve_bound_j_tip_grp, self.curve_bound_j_base_grp, self.leg_ik_j_grp, self.jointsGrp)
		pm.select(cl = True)
	
	
	#deletePositionLocatorsAndAnnotations
	def deletePositionLocatorsAndAnnotations(self):
		
		pm.select(cl = True)
		
		#delete Locators
		pm.delete(self.leg_locator_base, self.leg_locator_knee, self.leg_locator_tip, self.leg_locator_poleVector, self.foot_locator)
		pm.select(cl = True)
		
		#delete annotations
		pm.delete(self.annotation_foot_locator.getParent(), self.annotation_leg_locator_poleVector.getParent(), self.annotation_leg_locator_base.getParent(), self.annotation_leg_locator_knee.getParent(), self.annotation_leg_locator_tip.getParent())
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
		
	
	
	
	#getFootIkPositionList
	def getFootIkPositionList(self, vectorA, vectorB, divisions):
		
		#get vector AB
		vectorAB = [vectorB[0] - vectorA[0], vectorB[1] - vectorA[1], vectorB[2] - vectorA[2]]
		
		#get single vectorPart
		vectorMultiplier = 1.0 / divisions
		vectorPart = [vectorAB[0] * vectorMultiplier, vectorAB[1] * vectorMultiplier, vectorAB[2] * vectorMultiplier]
		
		#create positionList
		positionList = [vectorA]
		
		for index in range(1, divisions):
			
			#create vectorPartIndex
			vectorPartIndex = [vectorPart[0] * index, vectorPart[1] * index, vectorPart[2] * index]
			
			#positionVector
			positionVector = [vectorA[0] + vectorPartIndex[0], vectorA[1] + vectorPartIndex[1] , vectorA[2] + vectorPartIndex[2]]
			
			#append positionVector
			positionList.append(positionVector)
			
		
		#append last position to positionList
		positionList.append(vectorB)
		
		
		return positionList
		
		
		
	
	
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
		
	
	
		
#Execute Temp
#----------------------------------------------------

'''
#CREATE LOCATORS
import rbFootRigB

#Reload if true
doReload = True
if(doReload): reload(rbFootRigB)

#Create Instance if it doesnt exist
rbFootRigBInstance = rbFootRigB.RbFootRigB()

#createLocators
rbFootRigBInstance.createFootRigBLocators(prefix = 'Test')
'''

'''
#CREATE RIG

#createLocators
rbFootRigBInstance.createFootRigB(prefix = 'Test')
'''
	
	
	