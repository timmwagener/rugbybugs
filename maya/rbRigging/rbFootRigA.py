




#rbFootRigA Module
#------------------------------------------------------------------

'''
Description:
Creates a standardized rugby bugs foot rig type A
'''

'''
ToDo:

'''




#Imports
#------------------------------------------------------------------
import math
import pymel.core as pm





#RbFootRigA class
#------------------------------------------------------------------

class RbFootRigA():
	
	#Constructor
	def __init__(self):
		
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		self.prefix = None
		
		#progress bar win
		#---------------------------------------
		self.displayProgress = True
		self.progressbarwin = None
		self.progressControl = None
		
		
		
		#position locators
		#---------------------------------------
		
		
		self.spine_locator_base = None
		self.spine_locator_tip = None
		self.leg_locator_base = None
		self.knee_locator = None
		self.poleVector_locator = None
		
		self.annotation_spine_locator_base = None
		self.annotation_spine_locator_tip = None
		self.annotation_leg_locator_base = None
		self.annotation_knee_locator = None
		self.annotation_poleVector_locator = None
		
		self.leg_base_worldcoord = None
		self.knee_worldcoord = None
		self.poleVector_worldcoord = None
		self.leg_tip_worldcoord = None
		
		
		#Leg Ik joints
		#---------------------------------------
		self.leg_ik_j_base = None
		self.leg_ik_j_knee = None
		self.leg_ik_j_tip = None
		
		self.leg_ik_joints_grp = None
		
		
		#Pole Vector Locator
		#---------------------------------------
		self.poleVectorLocator = None
		self.poleVectorLocatorGrp = None
		
		
		#Ik Leg manipulators
		#---------------------------------------
		self.legMasterManipulator = None
		self.legMasterManipulatorGrp = None
		
		self.legBaseManipulator = None
		self.legBaseManipulatorGrp = None
		
		self.legTipManipulator = None
		self.legTipManipulatorGrp = None
		
		
		
		#Leg IK
		#---------------------------------------
		self.leg_ik = None
		self.leg_ik_grp = None
		
		
		#Leg Distance Measurement Node
		#---------------------------------------
		self.leg_distance_measure_loc_base = None
		self.leg_distance_measure_loc_base_grp = None
		
		self.leg_distance_measure_loc_tip = None
		self.leg_distance_measure_loc_tip_grp = None
		
		self.leg_distance_measure_node = None
		
		self.leg_distance_measure_nodes_grp = None
		
		
		#Leg Stretchy nodes
		#---------------------------------------
		self.leg_mul_div_correct_parentspace_scale = None
		self.leg_mul_div_normalize_distance = None
		self.leg_con_distance_greater_one = None
		self.leg_blend_col_stretchy_blend = None
		
		self.multiply_translate_leg_ik_j_knee =None
		self.multiply_translate_leg_ik_j_tip =None
		
		
		self.add_offset_leg_ik_j_knee = None
		self.add_offset_leg_ik_j_tip = None
		
		
		#Hand parent joint
		#---------------------------------------
		self.handParentJoint = None
		self.handParentJointGrp = None
		
		
		
		
		
		
		#Spline Curve
		#---------------------------------------
		self.spline_ik_curve = None
		
		self.cv_1_world_coord = None
		self.cv_2_world_coord = None
		self.cv_3_world_coord = None
		self.cv_4_world_coord = None
		self.cv_5_world_coord = None
		self.cv_6_world_coord = None
		
		
		
		#Bound joints
		#---------------------------------------
		self.bound_j_base = None
		self.bound_j_1 = None
		self.bound_j_2 = None
		self.bound_j_3 = None
		self.bound_j_tip = None
		self.bound_j_aim_tip = None
		
		self.bound_joints_grp = None
		
		
		
		#Spline Ik joints
		#---------------------------------------
		self.spline_ik_j_base = None
		self.spline_ik_j_1 = None
		self.spline_ik_j_2 = None
		self.spline_ik_j_3 = None
		self.spline_ik_j_tip = None
		self.spline_ik_j_aim_tip = None
		
		self.spline_ik_joints_grp = None
		
		
		
		#ctrl joints
		#---------------------------------------
		self.ctrl_j_base = None
		self.ctrl_j_tip = None
		
		self.ctrl_j_base_grp = None
		self.ctrl_j_tip_grp = None
		
		
		
		#Manips
		#---------------------------------------
		self.manip_spine_base = None
		self.manip_spine_base_grp = None
		
		self.manip_spine_tip = None
		self.manip_spine_tip_grp = None
		
		self.manip_spine_master = None
		self.manip_spine_master_grp = None
		
		
		#Spline IK
		#---------------------------------------
		self.spline_ik = None
		self.spline_ik_grp = None
		
		
		#Skincluster
		#---------------------------------------
		self.spine_skincluster = None
		
		
		#Aim locators
		#---------------------------------------
		self.aim_loc_j_base = None
		self.aim_loc_j_base_twist_grp = None
		self.aim_loc_j_base_parent_grp = None
		
		self.aim_loc_j_1 = None
		self.aim_loc_j_1_twist_grp = None
		self.aim_loc_j_1_parent_grp = None
		
		self.aim_loc_j_2 = None
		self.aim_loc_j_2_twist_grp = None
		self.aim_loc_j_2_parent_grp = None
		
		self.aim_loc_j_3 = None
		self.aim_loc_j_3_twist_grp = None
		self.aim_loc_j_3_parent_grp = None
		
		self.aim_loc_j_tip = None
		self.aim_loc_j_tip_twist_grp = None
		self.aim_loc_j_tip_parent_grp = None
		
		self.all_aim_locators_grp = None
		
		
		
		#Aim locator twist
		#---------------------------------------
		self.average_aim_loc_j_2 = None
		self.average_aim_loc_j_1 = None
		self.average_aim_loc_j_3 = None
		
		self.multiplyByNegativeOneTwistBase = None
		self.multiplyByNegativeOneTwistTip = None
		
		
		
		#Distance Measurement Node
		#---------------------------------------
		self.distance_measure_loc_base = None
		self.distance_measure_loc_base_grp = None
		
		self.distance_measure_loc_tip = None
		self.distance_measure_loc_tip_grp = None
		
		self.distance_measure_node = None
		
		self.distance_measure_nodes_grp = None
		
		
		
		#Stretchy nodes
		#---------------------------------------
		self.mul_div_correct_parentspace_scale = None
		self.mul_div_normalize_distance = None
		self.con_distance_greater_one = None
		self.blend_col_stretchy_blend = None
		
		self.multiply_translate_spline_ik_j_1 =None
		self.multiply_translate_spline_ik_j_2 =None
		self.multiply_translate_spline_ik_j_3 =None
		self.multiply_translate_spline_ik_j_tip =None
		
		self.add_offset_spline_ik_j_1 = None
		self.add_offset_spline_ik_j_2 = None
		self.add_offset_spline_ik_j_3 = None
		self.add_offset_spline_ik_j_tip = None
		
		
		#Rig node groups
		#---------------------------------------
		self.spine_rig_nodes_grp = None
		self.spine_rig_manips_grp = None
		self.spine_rig_joints_grp = None


	
	
	
	
	
	#Toplevel Methods
	#------------------------------------------------------------------
	
	
	#createPositionLocators
	def createPositionLocators(self, prefix = ''):
		
		#set prefix
		self.prefix = prefix
		
		#create Position Locators
		self.createPosLocators()
		
		
	
	#createFootRigA
	def createFootRigA(self, prefix = ''):
		
		#test if posLoc exist, and if so, start footRig procedure
		if(self.spine_locator_base and self.spine_locator_tip and self.leg_locator_base and self.knee_locator and self.poleVector_locator):
			if(pm.objExists(self.spine_locator_base.name()) and pm.objExists(self.spine_locator_tip.name()) and pm.objExists(self.leg_locator_base.name()) and pm.objExists(self.knee_locator.name()) and pm.objExists(self.poleVector_locator.name())):
				
				
			
			
				#createProgressWindow if true
				if(self.displayProgress): self.createProgressbarWindow(progressbarsize = 27)
				
				
				#footRigA procedure
				#---------------------------------------
				
				#set prefix
				self.prefix = prefix
				
				
				
				
				#Ik leg
				#---------------------------------------
				
				#createLegIkJoints
				self.createLegIkJoints()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created leg Ik joints')
				
				#createPoleVectorLocator
				self.createPoleVectorLocator()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created pole vector locator')
				
				#createLegManipulators
				self.createLegManipulators()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created leg manipulators')
				
				#createIkHandleLeg
				self.createIkHandleLeg()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created Ik Handle for leg')
				
				#constrainLegManipulatorsAndIkHandle
				self.constrainLegManipulatorsAndIkHandle()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully constrained leg manipulators and Ik Handle')
				
				#createLegDistanceMeasureNodes
				self.createLegDistanceMeasureNodes()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created leg Distance Measure Nodes')
				
				#createLegStretchyness
				self.createLegStretchyness()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created leg stretchyness')
				
				#createAndConstrainHandParentJoint
				self.createAndConstrainHandParentJoint()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created and constrained Hand Parent Joint')
				
				
				
				
				
				#Spine Ik Hand
				#---------------------------------------
				
				#createSplineIkCurve
				self.createSplineIkCurve()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created Spline IK curve')
				
				#createBoundJoints
				self.createBoundJoints()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created Bound joints')
				
				#createSplineIkJoints
				self.createSplineIkJoints()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created Spline Ik joints')
				
				#createControlJoints
				self.createControlJoints()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created Control joints')
				
				#createSpineManipulators
				self.createSpineManipulators()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created Spine Manipulators')
				
				#createSplineIk
				self.createSplineIk()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created Spline Ik')
				
				#createSpineSkincluster
				self.createSpineSkincluster()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created Spine skincluster')
				
				#createAimLocators
				self.createAimLocators()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created Aim Locators')
				
				#constrainManipulators
				self.constrainManipulators()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully constrained Manipulators')
				
				#constrainControlJoints
				self.constrainControlJoints()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully constrained control joints')
				
				#constrainBoundJoints
				self.constrainBoundJoints()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully constrained bound joints')
				
				#constrainAimLocators
				self.constrainAimLocators()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully constrained aim locators')
				
				#constrainIkJointGrp
				self.constrainIkJointGrp()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully constrained IK joint grps')
				
				#createAimLocatorTwist
				self.createAimLocatorTwist()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created aim locator twist')
				
				#createDistanceMeasureNode
				self.createDistanceMeasureNode()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created distance measure node')
				
				#createStretchyness
				self.createStretchyness()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully created stretchyness')
				
				
				
				
				
				
				#Shared Methods
				#---------------------------------------
				
				#groupNodes
				self.groupNodes()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully grouped %s Rig Nodes' % (self.prefix))
				
				#deleteLocatorsAndAnnotations
				self.deleteLocatorsAndAnnotations()
				if(self.displayProgress): self.updateProgressbarWindow()
				if(self.verbose): print('Successfully Deleted Locators and Annotations')
				
				
				
				
				#deleteProgressWindow if true
				if(self.displayProgress): self.deleteProgressbarWindow()
	
		
			
			else:
				if(self.verbose): print('Error creating footRigA, some locators seem to be missing. Please recreate locators')
			
		else:
			if(self.verbose): print('Error creating footRigA, no position locators')
	
	
	
	
	
	
	
	
	
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	
	
	
	#Ik leg
	#---------------------------------------
	
	
	
	#createLegIkJoints
	def createLegIkJoints(self):
		
		pm.select(cl = True)
		
		#Query posLocators worldspace
		self.leg_base_worldcoord = pm.xform(self.leg_locator_base, ws = True, q = True, t = True)
		self.knee_worldcoord = pm.xform(self.knee_locator, ws = True, q = True, t = True)
		self.poleVector_worldcoord = pm.xform(self.poleVector_locator, ws = True, q = True, t = True)
		self.leg_tip_worldcoord = pm.xform(self.spine_locator_base, ws = True, q = True, t = True)
		
		
		
		
		
		#Create leg ik joints at worldcoord positions
		#----------------------------------------------------
		
		#leg_ik_j_base
		pm.select(cl = True)
		self.leg_ik_j_base = pm.joint(a = True, p= self.leg_base_worldcoord , co = True, n = self.prefix + '_leg_ik_j_base')
		
		#leg_ik_j_knee
		self.leg_ik_j_knee = pm.joint(a = True, p= self.knee_worldcoord , co = True, n = self.prefix + '_leg_ik_j_knee')
		
		#leg_ik_j_tip
		self.leg_ik_j_tip = pm.joint(a = True, p= self.leg_tip_worldcoord , co = True, n = self.prefix + '_leg_ik_j_tip')
		pm.select(cl = True)
		
		
		
		#Orient ik joints
		pm.joint(self.leg_ik_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		pm.select(cl = True)
		
		
		#create leg_ik_joints_grp and translate to leg base worldcoord
		self.leg_ik_joints_grp = pm.group(n = self.prefix + '_leg_ik_joints_grp')
		self.leg_ik_joints_grp.translate.set(self.leg_base_worldcoord)
		
		pm.select(cl = True)
		
		#Add joint chain to grp
		pm.parent(self.leg_ik_j_base, self.leg_ik_joints_grp)
		
		pm.select(cl = True)
		
		
		
	#createPoleVectorLocator
	def createPoleVectorLocator(self):
		
		pm.select(cl = True)
		
		
		#create Pole Vector Loc
		self.poleVectorLocator = pm.spaceLocator(n = self.prefix + '_poleVector_loc') 
		
		#poleVectorLoc grp
		self.poleVectorLocatorGrp = pm.group(self.poleVectorLocator ,  n= self.prefix + '_poleVector_loc_grp' )
		
		
		#Move and orient poleVectorLoc grp
		self.poleVectorLocatorGrp.translate.set(self.poleVector_worldcoord)
		
		pm.select(cl = True)
		
		
		
	
	#createLegManipulators
	def createLegManipulators(self):
		
		
		#legMasterManipulator
		#-------------------------------------
		#Create self.legMasterManipulator
		self.legMasterManipulator = pm.circle(r = 2, name = self.prefix + '_leg_master_manip', ch = False, nr=(1, 0, 0))
		
		#Add Custom attributes
		pm.addAttr(self.legMasterManipulator, ln = '_', at='enum', en = 'Custom', h = False, k = True, r = True)
		pm.setAttr(self.legMasterManipulator[0] +'._', lock = True)
		pm.addAttr(self.legMasterManipulator,ln = 'worldSpace', at='float', defaultValue= 1, h = False, k = True, r = True)
		
		#Group
		self.legMasterManipulatorGrp = pm.group(self.legMasterManipulator,  n= self.prefix + '_leg_master_manip_grp' )
		
		#Translate and orient group to right position
		self.legMasterManipulatorGrp.translate.set(self.leg_base_worldcoord)
		
		pm.select(cl = True)
		
		
		
		#legBaseManipulator
		#-------------------------------------
		#Create legBaseManipulator
		self.legBaseManipulator = pm.circle(r = 5, name = self.prefix + '_leg_base_manip', ch = False, nr=(1, 0, 0))
		
		#Group
		self.legBaseManipulatorGrp = pm.group(self.legBaseManipulator,  n= self.prefix + '_leg_base_manip_grp' )
		
		#Translate and orient group to right position
		self.legBaseManipulatorGrp.translate.set(self.leg_base_worldcoord)
		
		pm.select(cl = True)
		
		
		
		
		#legTipManipulator
		#-------------------------------------
		#Create legTipManipulator
		self.legTipManipulator = pm.circle(r = 5, name = self.prefix + '_leg_tip_manip', ch = False, nr=(0, 1, 0))
		
		#Add Custom attributes
		pm.addAttr(self.legTipManipulator, ln = '_', at='enum', en = 'Custom', h = False, k = True, r = True)
		pm.setAttr(self.legTipManipulator[0] +'._', lock = True)
		pm.addAttr(self.legTipManipulator,ln = 'legStretchy', at='float', defaultValue= 0, h = False, k = True, r = True, minValue=0.0, maxValue=1)
		pm.addAttr(self.legTipManipulator,ln = 'legStretchyOffset', at='float', defaultValue= 0, h = False, k = True, r = True)
		
		#Group
		self.legTipManipulatorGrp = pm.group(self.legTipManipulator,  n= self.prefix + '_leg_tip_manip_grp' )
		
		#Translate and orient group to right position
		self.legTipManipulatorGrp.translate.set(self.leg_tip_worldcoord)
		
		pm.select(cl = True)
		
		
	
	
	
	#createIkHandleLeg
	def createIkHandleLeg(self):
		
		
		pm.select(cl = True)
		
		#create ik handle
		self.leg_ik = pm.ikHandle( sj= self.leg_ik_j_base , ee= self.leg_ik_j_tip , n = self.prefix +'_ik_rp_Handle_leg' , sol = 'ikRPsolver' )[0]
		
		#Group ik solver
		self.leg_ik_grp = pm.group(self.leg_ik, n = self.prefix + '_leg_ik_grp')
		
		pm.select(cl = True)
		
		
		
	#constrainLegManipulatorsAndIkHandle
	def constrainLegManipulatorsAndIkHandle(self):
		
		pm.select(cl = True)
		
		#manip_base to manip Master
		#pm.scaleConstraint( self.legMasterManipulator , self.legBaseManipulatorGrp , mo = True) 
		#pm.parentConstraint( self.legMasterManipulator , self.legBaseManipulatorGrp , mo = True)
		
		pm.select(cl = True)
		
		#manip_tip to manip Master
		pm.scaleConstraint( self.legMasterManipulator , self.legTipManipulatorGrp , mo = True) 
		pm.parentConstraint( self.legMasterManipulator , self.legTipManipulatorGrp , mo = True) 
		
		pm.select(cl = True)
		
		#poleVectorGrp to manip Master
		pm.scaleConstraint( self.legMasterManipulator , self.poleVectorLocatorGrp , mo = True) 
		pm.parentConstraint( self.legMasterManipulator , self.poleVectorLocatorGrp , mo = True)
		
		pm.select(cl = True)
		
		
		
		
		#ikHandle to manip leg tip
		pm.pointConstraint( self.legTipManipulator , self.leg_ik , mo = True)
		
		pm.select(cl = True)
		
		#ikHandle to poleVector
		pm.poleVectorConstraint( self.poleVectorLocator , self.leg_ik )
		
		pm.select(cl = True)
		
		#leg ik joints grp to base manip
		pm.scaleConstraint( self.legBaseManipulator , self.leg_ik_joints_grp , mo = True) 
		pm.parentConstraint( self.legBaseManipulator , self.leg_ik_joints_grp , mo = True)
		
		pm.select(cl = True)
		
	


	#createLegDistanceMeasureNodes
	def createLegDistanceMeasureNodes(self):
		
		pm.select(cl = True)
		
		#Create locators as start point (base)
		self.leg_distance_measure_loc_base = pm.spaceLocator(n = self.prefix + '_leg_distance_measure_loc_base') 
		#Group  locator
		self.leg_distance_measure_loc_base_grp = pm.group(self.leg_distance_measure_loc_base ,  n= self.prefix + '_leg_distance_measure_loc_base_grp' )
		#Point constrain grp to ik_j_base
		pm.pointConstraint( self.leg_ik_j_base, self.leg_distance_measure_loc_base_grp , mo = False) 
		
		
		
		pm.select(cl = True)
		
		#Create locators as end point (tip)
		self.leg_distance_measure_loc_tip = pm.spaceLocator(n = self.prefix + '_leg_distance_measure_loc_tip') 
		#Group  locator
		self.leg_distance_measure_loc_tip_grp = pm.group(self.leg_distance_measure_loc_tip ,  n= self.prefix +'_leg_distance_measure_loc_tip_grp' )
		#Point constrain grp to self.legTipManipulator
		pm.pointConstraint( self.legTipManipulator, self.leg_distance_measure_loc_tip_grp, mo = False)
		
		
		
		pm.select(cl = True)
		
		#Create Distance Dimension Node 
		pm.select(self.leg_distance_measure_loc_base, self.leg_distance_measure_loc_tip)
		self.leg_distance_measure_node = pm.distanceDimension()
		
		pm.select(cl = True)
		
		#Group all three nodes
		self.leg_distance_measure_nodes_grp = pm.group(self.leg_distance_measure_loc_base_grp,  self.leg_distance_measure_loc_tip_grp, self.leg_distance_measure_node ,  n= self.prefix +'_leg_ik_distance_measure_grp' )
		
		pm.select(cl = True)
		
		
	
		
		
	#createLegStretchyness
	def createLegStretchyness(self):
		
		
		pm.select(cl = True)
		
		
		#Correct Parentspace scale
		self.leg_mul_div_correct_parentspace_scale = pm.nodetypes.MultiplyDivide(name = self.prefix + '_leg_mul_div_correct_parentspace_scale')
		pm.setAttr(self.leg_mul_div_correct_parentspace_scale.name()+'.operation' , 2)
		self.leg_distance_measure_node.distance >> self.leg_mul_div_correct_parentspace_scale.input1X
		self.legMasterManipulator[0].worldSpace >> self.leg_mul_div_correct_parentspace_scale.input2X
		
		
		#Normalize Distance
		self.leg_mul_div_normalize_distance = pm.nodetypes.MultiplyDivide(name = self.prefix +'_leg_mul_div_normalize_distance')
		pm.setAttr(self.leg_mul_div_normalize_distance.name()+'.operation' , 2)
		self.leg_mul_div_correct_parentspace_scale.outputX >> self.leg_mul_div_normalize_distance.input1X
		pm.setAttr(self.leg_mul_div_normalize_distance.name() +'.input2X', (pm.getAttr(self.leg_ik_j_knee.translateX) + pm.getAttr(self.leg_ik_j_tip.translateX)))
		
		#Create Condition Node
		self.leg_con_distance_greater_one = pm.nodetypes.Condition(n = self.prefix +'_leg_con_distance_greater_one')
		pm.setAttr(self.leg_con_distance_greater_one.name() +'.operation', 2)
		self.leg_mul_div_normalize_distance.outputX >> self.leg_con_distance_greater_one.firstTerm
		self.leg_mul_div_normalize_distance.outputX >> self.leg_con_distance_greater_one.colorIfTrueR
		pm.setAttr(self.leg_con_distance_greater_one.name() +'.secondTerm' , 1)
		pm.setAttr(self.leg_con_distance_greater_one.name() +'.colorIfFalseR' , 1)
		
		#Create Blend colors node to blend stretchyness
		self.leg_blend_col_stretchy_blend = pm.nodetypes.BlendColors(n = self.prefix +'_leg_blend_col_stretchy_blend')
		self.legTipManipulator[0].legStretchy >> self.leg_blend_col_stretchy_blend.blender
		self.leg_con_distance_greater_one.outColorR >> self.leg_blend_col_stretchy_blend.color1R
		pm.setAttr(self.leg_blend_col_stretchy_blend.name() + '.color2R', 1)
		
		pm.select(cl = True)
		
		
		
		
		#create multiply translate nodes
		#------------------------------------------
		
		#multiply_translate_leg_ik_j_knee
		self.multiply_translate_leg_ik_j_knee = pm.nodetypes.MultiplyDivide(n = self.prefix + '_multiply_translate_leg_ik_j_knee')
		self.leg_blend_col_stretchy_blend.outputR >> self.multiply_translate_leg_ik_j_knee.input1X
		pm.setAttr(self.multiply_translate_leg_ik_j_knee.input2X , pm.getAttr(self.leg_ik_j_knee.translateX))
		
		
		#multiply_translate_leg_ik_j_tip
		self.multiply_translate_leg_ik_j_tip = pm.nodetypes.MultiplyDivide(n = self.prefix + '_multiply_translate_leg_ik_j_tip')
		self.leg_blend_col_stretchy_blend.outputR >> self.multiply_translate_leg_ik_j_tip.input1X
		pm.setAttr(self.multiply_translate_leg_ik_j_tip.input2X , pm.getAttr(self.leg_ik_j_tip.translateX))
		
		
		pm.select(cl = True)
		
		
		
		#create add offset nodes
		#------------------------------------------
		
		#add_offset_leg_ik_j_knee
		self.add_offset_leg_ik_j_knee = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_offset_leg_ik_j_knee')
		self.legTipManipulator[0].legStretchyOffset >> self.add_offset_leg_ik_j_knee.input1D[0]
		self.multiply_translate_leg_ik_j_knee.outputX >> self.add_offset_leg_ik_j_knee.input1D[1]
		
		
		#add_offset_leg_ik_j_tip
		self.add_offset_leg_ik_j_tip = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_offset_leg_ik_j_tip')
		self.legTipManipulator[0].legStretchyOffset >> self.add_offset_leg_ik_j_tip.input1D[0]
		self.multiply_translate_leg_ik_j_tip.outputX >> self.add_offset_leg_ik_j_tip.input1D[1]
		
		
		
		
		#Connect joints
		#------------------------------------------
		
		self.add_offset_leg_ik_j_knee.output1D >> self.leg_ik_j_knee.translateX
		self.add_offset_leg_ik_j_tip.output1D >> self.leg_ik_j_tip.translateX
		
		
		pm.select(cl = True)
		
		
		
	#createAndConstrainHandParentJoint
	def createAndConstrainHandParentJoint(self):
		
		#Create handParent Joint and Grp
		#--------------------------------------------------------
		
		pm.select(cl = True)
		
		#handParentJoint
		self.handParentJoint = pm.joint(a = True, p= (0,0,0) , co = True, n = self.prefix + '_hand_parent_joint')
		pm.select(cl = True)
		
		
		#create handParentJointGrp and translate to leg_tip_worldcoord
		self.handParentJointGrp = pm.group(self.handParentJoint, n = self.prefix + '_hand_parent_joint_grp')
		self.handParentJointGrp.translate.set(self.leg_tip_worldcoord)
		
		pm.select(cl = True)
		
		
		#Constrain handParent Joint Grp
		#--------------------------------------------------------
		
		#handParentJointGrp to self.legTipManipulator
		pm.scaleConstraint( self.legTipManipulator, self.handParentJointGrp , mo = True)
		pm.orientConstraint( self.legTipManipulator, self.handParentJointGrp , mo = False)
		
		#handParentJointGrp to self.leg_ik_j_tip
		pm.pointConstraint( self.leg_ik_j_tip, self.handParentJointGrp , mo = True)
		
		
	
	
	#Spine Ik Hand
	#---------------------------------------
	
	#createSplineIkCurve
	def createSplineIkCurve(self):
		
		pm.select(cl = True)
		
		#Query posLocators worldspace
		loc_base_worldcoord = pm.xform(self.spine_locator_base, ws = True, q = True, t = True)
		loc_tip_worldcoord = pm.xform(self.spine_locator_tip, ws = True, q = True, t = True)
		
		
		#calculate spline curve cv positions
		distanceVector = self.getDistance(loc_base_worldcoord, loc_tip_worldcoord, vector = True)
		distance = self.getDistance(loc_base_worldcoord, loc_tip_worldcoord)
		
		
		self.cv_1_world_coord = loc_base_worldcoord
		self.cv_2_world_coord = self.addVectors(loc_base_worldcoord, self.multiplyVector(distanceVector, ((1.0/4.0)*1.0)))
		self.cv_3_world_coord = self.addVectors(loc_base_worldcoord, self.multiplyVector(distanceVector, ((1.0/4.0)*2.0)))
		self.cv_4_world_coord = self.addVectors(loc_base_worldcoord, self.multiplyVector(distanceVector, ((1.0/4.0)*3.0)))
		self.cv_5_world_coord = self.addVectors(loc_base_worldcoord, self.multiplyVector(distanceVector, ((1.0/4.0)*4.0)))
		self.cv_6_world_coord = self.addVectors(loc_base_worldcoord, self.multiplyVector(distanceVector, ((1.0/4.0)*5.0)))
		
		#Create spline ik curve
		pm.select(cl = True)
		self.spline_ik_curve = pm.curve( p=[ self.cv_1_world_coord, self.cv_2_world_coord, self.cv_3_world_coord, self.cv_4_world_coord, self.cv_5_world_coord, self.cv_6_world_coord], ws = True, d = 5, n = self.prefix + '_spline_ik_curve')
		pm.select(cl = True)
	
	
	
	
	#Create Bound Joints	
	def createBoundJoints(self):
		
		#Create Joints at spline ik curve cv positions
		#----------------------------------------------------
		
		#bound_j_base
		pm.select(cl = True)
		self.bound_j_base = pm.joint(a = True, p= self.cv_1_world_coord , co = True, n = self.prefix + '_bound_j_base')
		pm.select(cl = True)
		
		#bound_j_1
		pm.select(cl = True)
		self.bound_j_1 = pm.joint(a = True, p= self.cv_2_world_coord , co = True, n = self.prefix + '_bound_j_1')
		pm.select(cl = True)
		
		#bound_j_2
		pm.select(cl = True)
		self.bound_j_2 = pm.joint(a = True, p= self.cv_3_world_coord , co = True, n =self.prefix + '_bound_j_2')
		pm.select(cl = True)
		
		#bound_j_3
		pm.select(cl = True)
		self.bound_j_3 = pm.joint(a = True, p= self.cv_4_world_coord , co = True, n = self.prefix + '_bound_j_3')
		pm.select(cl = True)
		
		#bound_j_tip
		pm.select(cl = True)
		self.bound_j_tip = pm.joint(a = True, p= self.cv_5_world_coord , co = True, n = self.prefix + '_bound_j_tip')
		pm.select(cl = True)
		
		#bound_j_aim_tip
		pm.select(cl = True)
		self.bound_j_aim_tip = pm.joint(a = True, p= self.cv_6_world_coord , co = True, n = self.prefix + '_bound_j_aim_tip')
		pm.select(cl = True)
		
		
		#create joint chain, orient joints, unparent joints
		#----------------------------------------------------
		
		pm.parent(self.bound_j_1, self.bound_j_base)
		pm.parent(self.bound_j_2, self.bound_j_1)
		pm.parent(self.bound_j_3, self.bound_j_2)
		pm.parent(self.bound_j_tip, self.bound_j_3)
		pm.parent(self.bound_j_aim_tip, self.bound_j_tip)
		pm.select(cl = True)
		
		#Orient ik joints
		pm.joint(self.bound_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		pm.select(cl = True)
		
		#unparent each joint
		pm.parent(self.bound_j_1, w = True)
		pm.parent(self.bound_j_2, w = True)
		pm.parent(self.bound_j_3, w = True)
		pm.parent(self.bound_j_tip, w = True)
		pm.parent(self.bound_j_aim_tip, w = True)
		pm.select(cl = True)
		
		
		#Create and orient Grp and put joints under it
		#----------------------------------------------------
		
		#Create group
		pm.select(cl = True)
		self.bound_joints_grp = pm.group( n= self.prefix + '_bound_joints_grp' ) 
		pm.select(cl = True)
		
		#Move and rotate grp to correct position
		self.bound_joints_grp.translate.set(self.cv_1_world_coord)
		self.bound_joints_grp.rotate.set(pm.joint(self.bound_j_base, q = True, o = True))
		
		#Parent Joints under group
		pm.select(cl = True)
		pm.parent(self.bound_j_base, self.bound_joints_grp)
		pm.parent(self.bound_j_1, self.bound_joints_grp)
		pm.parent(self.bound_j_2, self.bound_joints_grp)
		pm.parent(self.bound_j_3, self.bound_joints_grp)
		pm.parent(self.bound_j_tip, self.bound_joints_grp)
		pm.parent(self.bound_j_aim_tip, self.bound_joints_grp)
		pm.select(cl = True)
	
		
		
	
	#Create Spline IK Joint Chain
	def createSplineIkJoints(self):
		
		#Create Joint chain at spline ik curve cv positions
		#----------------------------------------------------
		
		pm.select(cl = True)
		
		#bound_j_base
		self.spline_ik_j_base = pm.joint(a = True, p= self.cv_1_world_coord , co = True, n = self.prefix + '_spline_ik_j_base', rad = 0.5)
		
		#bound_j_1
		self.spline_ik_j_1 = pm.joint(a = True, p= self.cv_2_world_coord , co = True, n = self.prefix + '_spline_ik_j_1', rad = 0.5)
		
		
		#bound_j_2
		self.spline_ik_j_2 = pm.joint(a = True, p= self.cv_3_world_coord , co = True, n = self.prefix + '_spline_ik_j_2', rad = 0.5)
		
		#bound_j_3
		self.spline_ik_j_3 = pm.joint(a = True, p= self.cv_4_world_coord , co = True, n = self.prefix + '_spline_ik_j_3', rad = 0.5)
		
		
		#bound_j_tip
		self.spline_ik_j_tip = pm.joint(a = True, p= self.cv_5_world_coord , co = True, n = self.prefix + '_spline_ik_j_tip', rad = 0.5)
		
		
		#bound_j_aim_tip
		self.spline_ik_j_aim_tip = pm.joint(a = True, p= self.cv_6_world_coord , co = True, n = self.prefix + '_spline_ik_j_aim_tip', rad = 0.5)
		
		pm.select(cl = True)
		
		
		#Orient spline ik sjoint chain
		#----------------------------------------------------
		
		#Orient ik joints
		pm.joint(self.spline_ik_j_base, e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		pm.select(cl = True)
		
		
		#Group joint chain under spline ik joints grp
		#----------------------------------------------------
		
		#Deselect everything
		pm.select(cl = True)
		
		#Create group
		self.spline_ik_joints_grp = pm.group( n= self.prefix + '_spline_ik_joints_grp' ) 
		
		#Move and orient grp to correct position
		self.spline_ik_joints_grp.translate.set(self.cv_1_world_coord)
		self.spline_ik_joints_grp.rotate.set(pm.joint(self.spline_ik_j_base, q = True, o = True))
		
		#Parent Joints under group
		pm.parent(self.spline_ik_j_base, self.spline_ik_joints_grp)
		pm.select(cl = True)
		
	
	
	
	
	#Create ctrl_joints
	def createControlJoints(self):
		
		
		pm.select(cl = True)
		
		#ctrl_j_base
		self.ctrl_j_base = pm.joint(a = True, p= (0,0,0), co = True, n = self.prefix + '_ctrl_j_base', rad = 1.5)
		
		#group ctrl_j_base
		self.ctrl_j_base_grp = pm.group( self.ctrl_j_base, n= self.prefix + '_ctrl_j_base_grp' )
		
		#Move and orient grp to correct position
		self.ctrl_j_base_grp.translate.set(self.cv_1_world_coord)
		self.ctrl_j_base_grp.rotate.set(self.spline_ik_joints_grp.rotate.get())
		
		pm.select(cl = True)
		
		#ctrl_j_tip
		self.ctrl_j_tip = pm.joint(a = True, p= (0,0,0) , co = True, n = self.prefix + '_ctrl_j_tip', rad = 1.5)
		
		#group ctrl_j_tip
		self.ctrl_j_tip_grp = pm.group( self.ctrl_j_tip, n= self.prefix + '_ctrl_j_tip_grp' ) 
		
		#Move and orient grp to correct position
		self.ctrl_j_tip_grp.translate.set(self.cv_5_world_coord)
		self.ctrl_j_tip_grp.rotate.set(self.spline_ik_joints_grp.rotate.get())
		
		pm.select(cl = True)
		
		
		
	#Create Spine manipulators
	def createSpineManipulators(self):
		
		#Manip spine base
		#-------------------------------------
		#Create Manip_spine_base
		self.manip_spine_base = self.createCubeManipulator(self.prefix + '_manip_spine_base')
		
		#Group
		self.manip_spine_base_grp = pm.group(self.manip_spine_base,  n = self.prefix + '_manip_spine_base_grp' )
		
		#Translate and orient group to right position
		self.manip_spine_base_grp.translate.set(self.cv_1_world_coord)
		self.manip_spine_base_grp.rotate.set(self.ctrl_j_base_grp.rotate.get())
		
		#If tip is left from base on X Axis then set grp rotation back to zer0 on Y Axis
		if(self.cv_1_world_coord[0] > self.cv_5_world_coord[0]): self.manip_spine_base_grp.rotateY.set(0)
		
		#Set Manip_spine_base rotation order
		pm.xform(self.manip_spine_base , roo = 'zxy')
		
		pm.select(cl = True)
		
		
		
		#Manip spine tip
		#-------------------------------------
		#Create Manip_spine_tip
		self.manip_spine_tip = self.createCubeManipulator(self.prefix + '_manip_spine_tip')
		
		#Add Custom attributes
		pm.addAttr(self.manip_spine_tip, ln = '_', at='enum', en = 'Custom', h = False, k = True, r = True)
		pm.setAttr(self.manip_spine_tip._ , lock = True)
		pm.addAttr(self.manip_spine_tip,ln = 'handStretchy', at='float', defaultValue= 0, h = False, k = True, r = True, minValue=0.0, maxValue=1)
		pm.addAttr(self.manip_spine_tip,ln = 'handStretchyOffset', at='float', defaultValue= 0, h = False, k = True, r = True)
		
		
		#Group
		self.manip_spine_tip_grp = pm.group(self.manip_spine_tip,  n = self.prefix + '_manip_spine_tip_grp' )
		
		#Translate and orient group to right position
		self.manip_spine_tip_grp.translate.set(self.cv_5_world_coord)
		self.manip_spine_tip_grp.rotate.set(self.ctrl_j_tip_grp.rotate.get())
		
		#If tip is left from base on X Axis then set grp rotation back to zer0 on Y Axis
		if(self.cv_1_world_coord[0] > self.cv_5_world_coord[0]): self.manip_spine_tip_grp.rotateY.set(0)
		
		#Set Manip_spine_tip rotation order
		pm.xform(self.manip_spine_tip , roo = 'zxy')
		
		pm.select(cl = True)
		
		
		
		#Manip spine master
		#-------------------------------------
		#Create Manip_spine_master
		self.manip_spine_master = pm.circle(r = 5, name = self.prefix + '_manip_spine_master', ch = False, nr=(1, 0, 0))
		
		#Group
		self.manip_spine_master_grp = pm.group(self.manip_spine_master,  n= self.prefix + '_manip_spine_master_grp' )
		
		#Translate and orient group to right position
		self.manip_spine_master_grp.translate.set(self.cv_1_world_coord)
		self.manip_spine_master_grp.rotate.set(self.ctrl_j_base_grp.rotate.get())
		
		#If tip is left from base on X Axis then set grp rotation back to zer0 on Y Axis
		if(self.cv_1_world_coord[0] > self.cv_5_world_coord[0]): self.manip_spine_master_grp.rotateY.set(0)
		
		#Set Manip_spine_master rotation order
		pm.xform(self.manip_spine_master , roo = 'zxy')
		
		pm.select(cl = True)
		
		
		
	#Create Spline IK
	def createSplineIk(self):
		
		pm.select(cl = True)
		
		#Create spline IK
		self.spline_ik = pm.ikHandle( sj= self.spline_ik_j_base , ee= self.spline_ik_j_aim_tip , roc = True, n = self.prefix + '_ikHandle_spine', c = self.spline_ik_curve, ccv = False, pcv = False, sol = 'ikSplineSolver' )[0]
		
		#Group Spline_ik
		self.spline_ik_grp = pm.group(self.spline_ik ,  n= self.prefix + '_spline_ik_grp' )
	
		pm.select(cl = True)
		
		
	#Create Spine skincluster
	def createSpineSkincluster(self):
		
		pm.select(cl = True)
	
		self.spine_skincluster = pm.skinCluster( self.ctrl_j_base , self.ctrl_j_tip , self.spline_ik_curve ,tsb=True, n = self.prefix + '_spine_skincluster', rui = False, ih = True)
		
		pm.select(cl = True)
		
		
	
	
	#Create Aim locators and groups
	def createAimLocators(self):
		
		#Aim locator bound_j_base
		#--------------------------------------------------
		self.aim_loc_j_base = pm.spaceLocator(n = self.prefix + '_aim_loc_j_base') 
		
		#Group  Twist
		self.aim_loc_j_base_twist_grp = pm.group(self.aim_loc_j_base ,  n= self.prefix + '_aim_loc_j_base_twist_grp' )
		
		#Group  Parent
		self.aim_loc_j_base_parent_grp = pm.group(self.aim_loc_j_base_twist_grp  ,  n= self.prefix + '_aim_loc_j_base_parent_grp' )
		
		#Move and orient group to correct position
		self.aim_loc_j_base_parent_grp.translate.set(self.cv_1_world_coord)
		self.aim_loc_j_base_parent_grp.rotate.set(self.ctrl_j_base_grp.rotate.get())
		
		#Move locator 3 units in z
		self.aim_loc_j_base.translateY.set(3)
		
		pm.select(cl = True)
		
		
		#Aim locator bound_j_1
		#--------------------------------------------------
		self.aim_loc_j_1 = pm.spaceLocator(n = self.prefix + '_aim_loc_j_1') 
		
		#Group  Twist
		self.aim_loc_j_1_twist_grp = pm.group(self.aim_loc_j_1 ,  n= self.prefix + '_aim_loc_j_1_twist_grp' )
		
		#Group  Parent
		self.aim_loc_j_1_parent_grp = pm.group(self.aim_loc_j_1_twist_grp  ,  n= self.prefix + '_aim_loc_j_1_parent_grp' )
		
		#Move and orient group to correct position
		self.aim_loc_j_1_parent_grp.translate.set(self.cv_2_world_coord)
		self.aim_loc_j_1_parent_grp.rotate.set(self.ctrl_j_base_grp.rotate.get())
		
		#Move locator 3 units in z
		self.aim_loc_j_1.translateY.set(3)
		
		pm.select(cl = True)
		
		
		#Aim locator bound_j_2
		#--------------------------------------------------
		self.aim_loc_j_2 = pm.spaceLocator(n = self.prefix + '_aim_loc_j_2') 
		
		#Group  Twist
		self.aim_loc_j_2_twist_grp = pm.group(self.aim_loc_j_2 ,  n= self.prefix + '_aim_loc_j_2_twist_grp' )
		
		#Group  Parent
		self.aim_loc_j_2_parent_grp = pm.group(self.aim_loc_j_2_twist_grp  ,  n= self.prefix + '_aim_loc_j_2_parent_grp' )
		
		#Move and orient group to correct position
		self.aim_loc_j_2_parent_grp.translate.set(self.cv_3_world_coord)
		self.aim_loc_j_2_parent_grp.rotate.set(self.ctrl_j_base_grp.rotate.get())
		
		#Move locator 3 units in z
		self.aim_loc_j_2.translateY.set(3)
		
		pm.select(cl = True)
		
		
		#Aim locator bound_j_3
		#--------------------------------------------------
		self.aim_loc_j_3 = pm.spaceLocator(n = self.prefix + '_aim_loc_j_3') 
		
		#Group  Twist
		self.aim_loc_j_3_twist_grp = pm.group(self.aim_loc_j_3 ,  n= self.prefix + '_aim_loc_j_3_twist_grp' )
		
		#Group  Parent
		self.aim_loc_j_3_parent_grp = pm.group(self.aim_loc_j_3_twist_grp  ,  n= self.prefix + '_aim_loc_j_3_parent_grp' )
		
		#Move and orient group to correct position
		self.aim_loc_j_3_parent_grp.translate.set(self.cv_4_world_coord)
		self.aim_loc_j_3_parent_grp.rotate.set(self.ctrl_j_base_grp.rotate.get())
		
		#Move locator 3 units in z
		self.aim_loc_j_3.translateY.set(3)
		
		pm.select(cl = True)
		
		
		#Aim locator bound_j_tip
		#--------------------------------------------------
		self.aim_loc_j_tip = pm.spaceLocator(n = self.prefix + '_aim_loc_j_tip') 
		
		#Group  Twist
		self.aim_loc_j_tip_twist_grp = pm.group(self.aim_loc_j_tip ,  n= self.prefix + '_aim_loc_j_tip_twist_grp' )
		
		#Group  Parent
		self.aim_loc_j_tip_parent_grp = pm.group(self.aim_loc_j_tip_twist_grp  ,  n= self.prefix + '_aim_loc_j_tip_parent_grp' )
		
		#Move and orient group to correct position
		self.aim_loc_j_tip_parent_grp.translate.set(self.cv_5_world_coord)
		self.aim_loc_j_tip_parent_grp.rotate.set(self.ctrl_j_base_grp.rotate.get())
		
		#Move locator 3 units in z
		self.aim_loc_j_tip.translateY.set(3)
		
		pm.select(cl = True)
		
		
		
		
		#Group all locators parent grps
		#--------------------------------------------------
		self.all_aim_locators_grp = pm.group(self.aim_loc_j_base_parent_grp, self.aim_loc_j_1_parent_grp, self.aim_loc_j_2_parent_grp, self.aim_loc_j_3_parent_grp, self.aim_loc_j_tip_parent_grp ,  n= self.prefix + '_aim_locators_grp' )
		pm.select(cl = True)
		
		
		
		
	#Constrain manipulators
	def constrainManipulators(self):
		
		pm.select(cl = True)
		
		#manip_base to manip Master
		pm.scaleConstraint( self.manip_spine_master, self.manip_spine_base_grp , mo = True) 
		pm.parentConstraint( self.manip_spine_master, self.manip_spine_base_grp , mo = True) 
		
		#manip_tip to manip Master
		pm.scaleConstraint( self.manip_spine_master, self.manip_spine_tip_grp , mo = True) 
		pm.parentConstraint( self.manip_spine_master, self.manip_spine_tip_grp , mo = True) 
		
		#manip Master Grp to handParentJoint
		pm.scaleConstraint( self.handParentJoint, self.manip_spine_master_grp , mo = True) 
		pm.parentConstraint( self.handParentJoint, self.manip_spine_master_grp , mo = True)
		
		
		pm.select(cl = True)
	
	
	
	#Constrain control joints grps
	def constrainControlJoints(self):
		
		pm.select(cl = True)
		
		#ctrl_joint_base Group to manipSpineBase
		pm.scaleConstraint( self.manip_spine_base, self.ctrl_j_base_grp , mo = True) 
		pm.parentConstraint( self.manip_spine_base, self.ctrl_j_base_grp , mo = True)
		
		#ctrl_joint_tip Group to manipSpineTip
		pm.scaleConstraint( self.manip_spine_tip, self.ctrl_j_tip_grp, mo = True) 
		pm.parentConstraint( self.manip_spine_tip, self.ctrl_j_tip_grp, mo = True)
		
		pm.select(cl = True)
	
	
	
	
	#Constrain bound joints
	def constrainBoundJoints(self):
		
		#constrain bound_j_base
		pm.scaleConstraint( self.spline_ik_j_base, self.bound_j_base , mo = True) 
		pm.pointConstraint( self.spline_ik_j_base, self.bound_j_base , mo = True)
		pm.aimConstraint( self.aim_loc_j_base, self.bound_j_base , mo = True, aim = (0,1,0), u = (1,0,0), wut = 'object', wuo = self.bound_j_1)
		
		#constrain bound_j_1
		pm.scaleConstraint( self.spline_ik_j_1, self.bound_j_1 , mo = True) 
		pm.pointConstraint( self.spline_ik_j_1, self.bound_j_1 , mo = True)
		pm.aimConstraint( self.aim_loc_j_1, self.bound_j_1, mo = True, aim = (0,1,0), u = (1,0,0), wut = 'object', wuo = self.bound_j_2)
		
		#constrain bound_j_2
		pm.scaleConstraint( self.spline_ik_j_2, self.bound_j_2 , mo = True) 
		pm.pointConstraint( self.spline_ik_j_2, self.bound_j_2 , mo = True)
		pm.aimConstraint( self.aim_loc_j_2, self.bound_j_2, mo = True, aim = (0,1,0), u = (1,0,0), wut = 'object', wuo = self.bound_j_3)
		
		#constrain bound_j_3
		pm.scaleConstraint( self.spline_ik_j_3, self.bound_j_3 , mo = True) 
		pm.pointConstraint( self.spline_ik_j_3, self.bound_j_3, mo = True)
		pm.aimConstraint( self.aim_loc_j_3, self.bound_j_3, mo = True, aim = (0,1,0), u = (1,0,0), wut = 'object', wuo = self.bound_j_tip)
		
		#constrain bound_j_tip
		pm.scaleConstraint( self.spline_ik_j_tip, self.bound_j_tip , mo = True) 
		pm.pointConstraint( self.spline_ik_j_tip, self.bound_j_tip , mo = True)
		pm.aimConstraint( self.aim_loc_j_tip, self.bound_j_tip , mo = True, aim = (0,1,0), u = (1,0,0), wut = 'object', wuo = self.bound_j_aim_tip)
		
		#constrain bound_j_aim_tip
		pm.scaleConstraint( self.spline_ik_j_aim_tip, self.bound_j_aim_tip,  mo = True) 
		pm.pointConstraint( self.spline_ik_j_aim_tip, self.bound_j_aim_tip, mo = True)
		
		
		
	#Constrain Aim locator groups
	def constrainAimLocators(self):
		
		#aim_locator_j_base_parent_grp
		pm.scaleConstraint( self.spline_ik_j_base, self.aim_loc_j_base_parent_grp , mo = True) 
		pm.parentConstraint( self.spline_ik_j_base, self.aim_loc_j_base_parent_grp, mo = True) 
		
		#aim_locator_j_1_parent_grp
		pm.scaleConstraint( self.spline_ik_j_1, self.aim_loc_j_1_parent_grp , mo = True) 
		pm.parentConstraint( self.spline_ik_j_1, self.aim_loc_j_1_parent_grp, mo = True)
		
		#aim_locator_j_2_parent_grp
		pm.scaleConstraint( self.spline_ik_j_2, self.aim_loc_j_2_parent_grp , mo = True) 
		pm.parentConstraint( self.spline_ik_j_2, self.aim_loc_j_2_parent_grp , mo = True)
		
		#aim_locator_j_3_parent_grp
		pm.scaleConstraint( self.spline_ik_j_3, self.aim_loc_j_3_parent_grp , mo = True) 
		pm.parentConstraint( self.spline_ik_j_3, self.aim_loc_j_3_parent_grp , mo = True)
		
		#aim_locator_j_tip_parent_grp
		pm.scaleConstraint( self.spline_ik_j_tip, self.aim_loc_j_tip_parent_grp , mo = True) 
		pm.parentConstraint( self.spline_ik_j_tip, self.aim_loc_j_tip_parent_grp , mo = True)
		
		
		
	#constrainIkJointGrp
	def constrainIkJointGrp(self):
		
		#aim_locator_j_base_parent_grp
		pm.scaleConstraint( self.manip_spine_master, self.spline_ik_joints_grp , mo = True) 
		pm.parentConstraint( self.manip_spine_master, self.spline_ik_joints_grp, mo = True) 
		
		
	#Create Aim locator twist
	def createAimLocatorTwist(self):
		
		pm.select(cl = True)
		
		
		#twist base tip
		#--------------------------------------------
		
		#If tip < than base in worldPos wire twist grps with negative x rotation
		if(self.cv_1_world_coord[0] > self.cv_5_world_coord[0]):
			
			#create multiplyByNegativeOneTwistBase
			self.multiplyByNegativeOneTwistBase = pm.nodetypes.MultiplyDivide(name = self.prefix + '_multiplyByNegativeOneTwistBase')
			self.manip_spine_base.rotateX >> self.multiplyByNegativeOneTwistBase.input1X
			pm.setAttr(self.multiplyByNegativeOneTwistBase.input2X, -1.0)
			
			#create multiplyByNegativeOneTwistTip
			self.multiplyByNegativeOneTwistTip = pm.nodetypes.MultiplyDivide(name = self.prefix + '_multiplyByNegativeOneTwistTip')
			self.manip_spine_tip.rotateX >> self.multiplyByNegativeOneTwistTip.input1X
			pm.setAttr(self.multiplyByNegativeOneTwistTip.input2X, -1.0)
			
			#conncect twist negative multipliers for base and tip
			self.multiplyByNegativeOneTwistBase.outputX >> self.aim_loc_j_base_twist_grp.rotateX
			self.multiplyByNegativeOneTwistTip.outputX >> self.aim_loc_j_tip_twist_grp.rotateX
		
		
		else:
			#conncect twist groups for base and tip
			self.manip_spine_base.rotateX >> self.aim_loc_j_base_twist_grp.rotateX
			self.manip_spine_tip.rotateX >> self.aim_loc_j_tip_twist_grp.rotateX
		
		pm.select(cl = True)
		
		
		
		#aim_loc_j_2_twist_grp
		#--------------------------------------------
		
		#If tip < than base in worldPos wire twist grps with negative x rotation
		if(self.cv_1_world_coord[0] > self.cv_5_world_coord[0]):
			
			#Create Middle aim loc twist (aim_loc_j_2)
			self.average_aim_loc_j_2 = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_average_aim_loc_j_2')
			pm.setAttr(self.average_aim_loc_j_2.name() +'.operation', 3)
			self.multiplyByNegativeOneTwistBase.outputX >> self.average_aim_loc_j_2.input1D[0]
			self.multiplyByNegativeOneTwistTip.outputX >> self.average_aim_loc_j_2.input1D[1]
			self.average_aim_loc_j_2.output1D >> self.aim_loc_j_2_twist_grp.rotateX
		
		else:
			#Create Middle aim loc twist (aim_loc_j_2)
			self.average_aim_loc_j_2 = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_average_aim_loc_j_2')
			pm.setAttr(self.average_aim_loc_j_2.name() +'.operation', 3)
			self.manip_spine_base.rotateX >> self.average_aim_loc_j_2.input1D[0]
			self.manip_spine_tip.rotateX >> self.average_aim_loc_j_2.input1D[1]
			self.average_aim_loc_j_2.output1D >> self.aim_loc_j_2_twist_grp.rotateX
		
		pm.select(cl = True)
		
		
		
		
		#aim_loc_j_1_twist_grp
		#--------------------------------------------
		
		#If tip < than base in worldPos wire twist grps with negative x rotation
		if(self.cv_1_world_coord[0] > self.cv_5_world_coord[0]):
			#Create aim loc twist for aim_loc_j_1
			self.average_aim_loc_j_1 = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_average_aim_loc_j_1')
			pm.setAttr(self.average_aim_loc_j_1.name() +'.operation', 3)
			self.multiplyByNegativeOneTwistBase.outputX >> self.average_aim_loc_j_1.input1D[0]
			self.aim_loc_j_2_twist_grp.rotateX >> self.average_aim_loc_j_1.input1D[1]
			self.average_aim_loc_j_1.output1D >> self.aim_loc_j_1_twist_grp.rotateX
		
		else:
			#Create aim loc twist for aim_loc_j_1
			self.average_aim_loc_j_1 = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_average_aim_loc_j_1')
			pm.setAttr(self.average_aim_loc_j_1.name() +'.operation', 3)
			self.manip_spine_base.rotateX >> self.average_aim_loc_j_1.input1D[0]
			self.aim_loc_j_2_twist_grp.rotateX >> self.average_aim_loc_j_1.input1D[1]
			self.average_aim_loc_j_1.output1D >> self.aim_loc_j_1_twist_grp.rotateX
		
		pm.select(cl = True)
		
		
		
		
		#aim_loc_j_3_twist_grp
		#--------------------------------------------
		
		#If tip < than base in worldPos wire twist grps with negative x rotation
		if(self.cv_1_world_coord[0] > self.cv_5_world_coord[0]):
			#Create aim loc twist for aim_loc_j_3
			self.average_aim_loc_j_3 = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_average_aim_loc_j_3')
			pm.setAttr(self.average_aim_loc_j_3.name() +'.operation', 3)
			self.multiplyByNegativeOneTwistTip.outputX >> self.average_aim_loc_j_3.input1D[0]
			self.aim_loc_j_2_twist_grp.rotateX >> self.average_aim_loc_j_3.input1D[1]
			self.average_aim_loc_j_3.output1D >> self.aim_loc_j_3_twist_grp.rotateX
		
		else:
			#Create aim loc twist for aim_loc_j_3
			self.average_aim_loc_j_3 = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_average_aim_loc_j_3')
			pm.setAttr(self.average_aim_loc_j_3.name() +'.operation', 3)
			self.manip_spine_tip.rotateX >> self.average_aim_loc_j_3.input1D[0]
			self.aim_loc_j_2_twist_grp.rotateX >> self.average_aim_loc_j_3.input1D[1]
			self.average_aim_loc_j_3.output1D >> self.aim_loc_j_3_twist_grp.rotateX
		
		pm.select(cl = True)
	
	
	
	
	
	#Create Distance Measure Node
	def createDistanceMeasureNode(self):
		
		pm.select(cl = True)
		
		#Create locators as start point (base)
		self.distance_measure_loc_base = pm.spaceLocator(n = self.prefix + '_distance_measure_loc_base') 
		#Group  locator
		self.distance_measure_loc_base_grp = pm.group(self.distance_measure_loc_base ,  n= self.prefix + '_distance_measure_loc_base_grp' )
		#Point constrain grp to spine_manip_base
		pm.pointConstraint( self.manip_spine_base, self.distance_measure_loc_base_grp , mo = False) 
		
		pm.select(cl = True)
		
		#Create locators as end point (tip)
		self.distance_measure_loc_tip = pm.spaceLocator(n = self.prefix + '_distance_measure_loc_tip') 
		#Group  locator
		self.distance_measure_loc_tip_grp = pm.group(self.distance_measure_loc_tip ,  n= self.prefix +'_distance_measure_loc_tip_grp' )
		#Point constrain grp to spine_manip_tip
		pm.pointConstraint( self.manip_spine_tip, self.distance_measure_loc_tip_grp, mo = False)
		
		pm.select(cl = True)
		
		#Create Distance Dimension Node 
		pm.select(self.distance_measure_loc_base, self.distance_measure_loc_tip)
		self.distance_measure_node = pm.distanceDimension()
		
		pm.select(cl = True)
		
		#Group all three nodes
		self.distance_measure_nodes_grp = pm.group(self.distance_measure_loc_base_grp,  self.distance_measure_loc_tip_grp, self.distance_measure_node ,  n= self.prefix +'_spine_distance_measure_grp' )
		
		pm.select(cl = True)
	
	
	
	
	
	#Create stretchyness
	def createStretchyness(self):
		
		#Correct Parentspace scale
		self.mul_div_correct_parentspace_scale = pm.nodetypes.MultiplyDivide(name = self.prefix + '_mul_div_correct_parentspace_scale')
		pm.setAttr(self.mul_div_correct_parentspace_scale.name()+'.operation' , 2)
		self.distance_measure_node.distance >> self.mul_div_correct_parentspace_scale.input1X
		self.legMasterManipulator[0].worldSpace >> self.mul_div_correct_parentspace_scale.input2X
		
		#Normalize Distance
		self.mul_div_normalize_distance = pm.nodetypes.MultiplyDivide(name = self.prefix +'_mul_div_normalize_distance')
		pm.setAttr(self.mul_div_normalize_distance.name()+'.operation' , 2)
		self.mul_div_correct_parentspace_scale.outputX >> self.mul_div_normalize_distance.input1X
		pm.setAttr(self.mul_div_normalize_distance.name() +'.input2X', pm.getAttr(self.distance_measure_node.name() +'.distance'))
		
		#Create Condition Node
		self.con_distance_greater_one = pm.nodetypes.Condition(n = self.prefix +'_con_distance_greater_one')
		pm.setAttr(self.con_distance_greater_one.name() +'.operation', 2)
		self.mul_div_normalize_distance.outputX >> self.con_distance_greater_one.firstTerm
		self.mul_div_normalize_distance.outputX >> self.con_distance_greater_one.colorIfTrueR
		pm.setAttr(self.con_distance_greater_one.name() +'.secondTerm' , 1)
		pm.setAttr(self.con_distance_greater_one.name() +'.colorIfFalseR' , 1)
		
		#Create Blend colors node to blend stretchyness
		self.blend_col_stretchy_blend = pm.nodetypes.BlendColors(n = self.prefix +'_blend_col_stretchy_blend')
		self.manip_spine_tip.handStretchy >> self.blend_col_stretchy_blend.blender
		self.con_distance_greater_one.outColorR >> self.blend_col_stretchy_blend.color1R
		pm.setAttr(self.blend_col_stretchy_blend.name() + '.color2R', 1)
		
		pm.select(cl = True)
		
		
		#create multiply translate nodes
		#------------------------------------------
		
		#multiply_translate_spline_ik_j_1
		self.multiply_translate_spline_ik_j_1 = pm.nodetypes.MultiplyDivide(n = self.prefix + '_multiply_translate_spline_ik_j_1')
		self.blend_col_stretchy_blend.outputR >> self.multiply_translate_spline_ik_j_1.input1X
		pm.setAttr(self.multiply_translate_spline_ik_j_1.input2X , pm.getAttr(self.spline_ik_j_1.translateX))
		
		
		#multiply_translate_spline_ik_j_2
		self.multiply_translate_spline_ik_j_2 = pm.nodetypes.MultiplyDivide(n = self.prefix + '_multiply_translate_spline_ik_j_2')
		self.blend_col_stretchy_blend.outputR >> self.multiply_translate_spline_ik_j_2.input1X
		pm.setAttr(self.multiply_translate_spline_ik_j_2.input2X , pm.getAttr(self.spline_ik_j_2.translateX))
		
		#multiply_translate_spline_ik_j_3
		self.multiply_translate_spline_ik_j_3 = pm.nodetypes.MultiplyDivide(n = self.prefix + '_multiply_translate_spline_ik_j_3')
		self.blend_col_stretchy_blend.outputR >> self.multiply_translate_spline_ik_j_3.input1X
		pm.setAttr(self.multiply_translate_spline_ik_j_3.input2X , pm.getAttr(self.spline_ik_j_3.translateX))
		
		#multiply_translate_spline_ik_j_tip
		self.multiply_translate_spline_ik_j_tip = pm.nodetypes.MultiplyDivide(n = self.prefix + '_multiply_translate_spline_ik_j_tip')
		self.blend_col_stretchy_blend.outputR >> self.multiply_translate_spline_ik_j_tip.input1X
		pm.setAttr(self.multiply_translate_spline_ik_j_tip.input2X , pm.getAttr(self.spline_ik_j_tip.translateX))
		
		
		
		#create add offset nodes
		#------------------------------------------
		
		#add_offset_spline_ik_j_1
		self.add_offset_spline_ik_j_1 = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_offset_spline_ik_j_1')
		self.manip_spine_tip.handStretchyOffset >> self.add_offset_spline_ik_j_1.input1D[0]
		self.multiply_translate_spline_ik_j_1.outputX >> self.add_offset_spline_ik_j_1.input1D[1]
		
		
		#add_offset_spline_ik_j_2
		self.add_offset_spline_ik_j_2 = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_offset_spline_ik_j_2')
		self.manip_spine_tip.handStretchyOffset >> self.add_offset_spline_ik_j_2.input1D[0]
		self.multiply_translate_spline_ik_j_2.outputX >> self.add_offset_spline_ik_j_2.input1D[1]
		
		#add_offset_spline_ik_j_3
		self.add_offset_spline_ik_j_3 = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_offset_spline_ik_j_3')
		self.manip_spine_tip.handStretchyOffset >> self.add_offset_spline_ik_j_3.input1D[0]
		self.multiply_translate_spline_ik_j_3.outputX >> self.add_offset_spline_ik_j_3.input1D[1]
		
		#add_offset_spline_ik_j_tip
		self.add_offset_spline_ik_j_tip = pm.nodetypes.PlusMinusAverage(n = self.prefix +'_offset_spline_ik_j_tip')
		self.manip_spine_tip.handStretchyOffset >> self.add_offset_spline_ik_j_tip.input1D[0]
		self.multiply_translate_spline_ik_j_tip.outputX >> self.add_offset_spline_ik_j_tip.input1D[1]
		
		
		
		
		#Connect joints
		#------------------------------------------
		
		self.add_offset_spline_ik_j_1.output1D >> self.spline_ik_j_1.translateX
		self.add_offset_spline_ik_j_2.output1D >> self.spline_ik_j_2.translateX
		self.add_offset_spline_ik_j_3.output1D >> self.spline_ik_j_3.translateX
		self.add_offset_spline_ik_j_tip.output1D >> self.spline_ik_j_tip.translateX
		
		pm.select(cl = True)
		
	
	
	
	
	#Group Spine Rig Nodes
	def groupNodes(self):
		
		pm.select(cl = True)
		
		#spine_rig_nodes_grp
		self.spine_rig_nodes_grp = pm.group(self.leg_distance_measure_nodes_grp, self.leg_ik_grp, self.spline_ik_curve, self.spline_ik_grp,self.all_aim_locators_grp, self.distance_measure_nodes_grp , n = self.prefix + '_spine_rig_nodes_grp')
		
		#spine_rig_manips_grp
		self.spine_rig_manips_grp = pm.group(self.legTipManipulatorGrp, self.legBaseManipulatorGrp, self.legMasterManipulatorGrp, self.poleVectorLocatorGrp,  self.manip_spine_base_grp,self.manip_spine_tip_grp,self.manip_spine_master_grp, n =  self.prefix + '_spine_rig_manips_grp')
		
		#spine_rig_joints_grp
		self.spine_rig_joints_grp = pm.group(self.handParentJointGrp, self.leg_ik_joints_grp, self.bound_joints_grp , self.spline_ik_joints_grp,self.ctrl_j_base_grp, self.ctrl_j_tip_grp , n = self.prefix + '_spine_rig_joints_grp')
	
		pm.select(cl = True)
	
	
	
	
	#Delete Construction locators and annotations
	def deleteLocatorsAndAnnotations(self):
		
		try:
			#delete pos Locs
			pm.delete(self.leg_locator_base, self.knee_locator, self.poleVector_locator, self.spine_locator_base, self.spine_locator_tip)
			#delete pos locs annotations
			pm.delete(self.annotation_leg_locator_base.getParent(),self.annotation_knee_locator.getParent(),self.annotation_poleVector_locator.getParent(),self.annotation_spine_locator_base.getParent(), self.annotation_spine_locator_tip.getParent())
		except:
			pass
	
	
	
	#createPosLocators
	def createPosLocators(self):
		
		try:
			#deselect all
			pm.select(cl = True)
			
			#Create Space locators and translate
			self.leg_locator_base = pm.spaceLocator(n = self.prefix + '_leg_locator_base')
			self.leg_locator_base.translate.set(0, 0, 0)
			pm.select(cl = True)
			
			self.knee_locator = pm.spaceLocator(n = self.prefix + '_knee_locator')
			self.knee_locator.translate.set(4, 1, 0)
			pm.select(cl = True)
			
			self.poleVector_locator = pm.spaceLocator(n = self.prefix + '_poleVector_locator')
			self.poleVector_locator.translate.set(4, 4, 0)
			pm.select(cl = True)
			
			self.spine_locator_base = pm.spaceLocator(n = self.prefix + '_spine_locator_base')
			self.spine_locator_base.translate.set(8, -2, 0)
			pm.select(cl = True)
			
			self.spine_locator_tip = pm.spaceLocator(n = self.prefix + '_spine_locator_tip')
			self.spine_locator_tip.translate.set(10, -2, 0)
			pm.select(cl = True)
			
			
			
			#Create Annotations and rename
			self.annotation_leg_locator_base = pm.annotate( self.leg_locator_base, tx= self.prefix + '_leg_base' )
			pm.rename(self.annotation_leg_locator_base.getParent().name(), self.prefix + '_leg_base_annotation')
			
			self.annotation_knee_locator = pm.annotate( self.knee_locator, tx= self.prefix + '_knee' )
			pm.rename(self.annotation_knee_locator.getParent().name(), self.prefix + '_knee_annotation')
			
			self.annotation_poleVector_locator = pm.annotate( self.poleVector_locator , tx= self.prefix + '_poleVector' )
			pm.rename(self.annotation_poleVector_locator.getParent().name(), self.prefix + '_poleVector_annotation')
			
			self.annotation_spine_locator_base = pm.annotate( self.spine_locator_base, tx= self.prefix + '_spine_base' )
			pm.rename(self.annotation_spine_locator_base.getParent().name(), self.prefix + '_spine_base_annotation')
			
			self.annotation_spine_locator_tip = pm.annotate( self.spine_locator_tip, tx= self.prefix + '_spine_tip' )
			pm.rename(self.annotation_spine_locator_tip.getParent().name(), self.prefix + '_spine_tip_annotation')
			
			
			
			#Parent constrain annotation transforms
			pm.parentConstraint(self.leg_locator_base, self.annotation_leg_locator_base.getParent(), mo = False)
			pm.parentConstraint(self.knee_locator, self.annotation_knee_locator.getParent(), mo = False)
			pm.parentConstraint(self.poleVector_locator, self.annotation_poleVector_locator.getParent(), mo = False)
			pm.parentConstraint(self.spine_locator_base, self.annotation_spine_locator_base.getParent(), mo = False)
			pm.parentConstraint(self.spine_locator_tip, self.annotation_spine_locator_tip.getParent(), mo = False)
			
			pm.select(cl = True)
			
			if(self.verbose): print('Successfully created position locators')
		
		
		
		except:
			pm.select(cl = True)
			if(self.verbose): print('Error creating position locators')

	
	
	
	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------
	
	
	#getDistance (worldPos delivered as list [x, y,z])
	def getDistance(self, worldPosA, worldPosB, vector = False):
		
		#subtract vectors (B +(-A))
		distanceVector = [worldPosB[0] + (-1 * worldPosA[0]), worldPosB[1] + (-1 * worldPosA[1]), worldPosB[2] + (-1 * worldPosA[2])]
		
		if(vector): return distanceVector
		
		#get scalar representation (distance)
		distance = math.sqrt(math.pow(distanceVector[0], 2) + math.pow(distanceVector[1], 2) + math.pow(distanceVector[2], 2))
		
		return distance
		
	
	#addVectors (vectors given as list [x,y,z])
	def addVectors(self, vectorA, vectorB):
		
		return [vectorA[0] + vectorB[0], vectorA[1] + vectorB[1], vectorA[2] + vectorB[2]]
		
	
	#multiplyVector
	def multiplyVector(self, vector, factor):
		
		return [vector[0] * factor, vector[1] * factor, vector[2] * factor]
		
	
	
	
	#Create Cube Manips
	def createCubeManipulator(self, manipulator_name):
		
		pm.select(cl = True)
		
		curve_rectangle_down = pm.curve( p=[(-1, -1, -1), (-1, -1, 1), (1, -1, 1), (1, -1, -1),(-1, -1, -1)], ws = True, d = 1 )

		curve_rectangle_up = pm.curve( p=[(-1, 1, -1), (-1, 1, 1), (1, 1, 1), (1, 1, -1),(-1, 1, -1)], ws = True, d = 1 )

		curve_1 = pm.curve( p=[(-1, -1, -1),(-1, 1, -1)], ws = True, d = 1 )

		curve_2 = pm.curve( p=[(1, -1, -1),(1, 1, -1)], ws = True, d = 1 )

		curve_3 = pm.curve( p=[(1, -1, 1),(1, 1, 1)], ws = True, d = 1 )

		curve_4 = pm.curve( p=[(-1, -1, 1),(-1, 1, 1)], ws = True, d = 1 )
		
		
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
		
	
	
	
	#createProgressbarWindow
	def createProgressbarWindow(self, progressbarsize = 1):
		try:
			pm.select(cl = True)
			self.progressbarwin = pm.window(title = 'Progress', resizeToFitChildren = True)
			pm.columnLayout()
			self.progressControl = pm.progressBar(maxValue = progressbarsize, width = 300)
			pm.showWindow(self.progressbarwin)
			
		except:
			if(self.verbose): print('Error creating progress bar')
		
		
	#deleteProgressbarWindow
	def deleteProgressbarWindow(self):
		try:
			pm.deleteUI(self.progressbarwin, window = True)
		except:
			if(self.verbose): print('Error deleting progress bar')
		
	
	#updateProgressBarWindow
	def updateProgressbarWindow(self, updateSteps = 1):
		try:
			pm.progressBar(self.progressControl, edit=True, step = updateSteps)
		except:
			if(self.verbose): print('Error updating progress bar')
	
#Execute TMP
#------------------------------------------------------------------
'''
TMP
'''
	
	
