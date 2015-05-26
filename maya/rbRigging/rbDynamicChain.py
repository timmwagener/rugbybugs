




#rbDynamicChain Module
#----------------------------------------------------

'''
Description:
Module to create a standardized dynamic chain rig module

ToDo:
-

'''



#Import
#----------------------------------------------------
import pymel.core as pm
import math





#RbDynamicChain Class
#----------------------------------------------------

class RbDynamicChain():
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#----------------------------------------------------
		
		#Debug and Ui
		self.verbose = True
		self.prefix = None
		self.jointCount = None
		self.progressbarWindow = None
		self.progressControl = None
		
		
		#Locators and Annotations
		self.dynamic_chain_locator_base = None
		self.dynamic_chain_locator_tip = None
		
		self.annotation_dynamic_chain_locator_base = None
		self.annotation_dynamic_chain_locator_tip = None
		
		
		#JointPositionList and FinalTransformMatrix
		self.jointPositionList = None
		self.locatorDistance = None
		self.finalTransformMatrix = None
		
		
		#ManipMaster
		self.manip_master = None
		self.manip_master_grp = None
		
		#ManipCtrlCenter
		self.manip_CtrlCenter = None
		self.manip_CtrlCenter_grp = None
		
		
		
		
		
		
		#IK Dynamic
		#---------------------
		
		#IkDynamicJoints
		self.ikDynamicJointsList = None
		self.ikDynamicJointsGrp = None
		
		
		#IkDynamicCurve
		self.spline_ik_dynamic_curve = None
		
		
		#HairSystemDynamicCurve
		self.dynamicHairsystem = None
		self.dynamicHairsystemFollicle = None
		self.dynamicHairsystemFollicleGrp = None
		self.dynamicOutputCurve = None
		self.dynamicOutputCurveGrp = None
		self.hairsystemNodesGrp = None
		
		
		#SplineIk
		self.dynamicChain_spline_ik = None
		self.dynamicChain_spline_ik_grp = None
		
		
		
		
		
		
		#IK Animated
		#---------------------
		
		#IkAnimatedJoints
		self.ikAnimatedJointsList = None
		self.ikAnimatedJointsGrp = None
		
		
		#manipIkAnimated and Pole Vector
		self.manipIkAnimated = None
		self.manipIkAnimatedGrp = None
		self.manipIkAnimatedPoleVector = None
		self.manipIkAnimatedPoleVectorGrp = None
		
		
		#ikRpHandleAnimated
		self.ikHandleAnimated = None
		self.ikHandleAnimatedGrp = None
		
		
		
		
		
		
		#FK Animated
		#---------------------
		
		#FkAnimatedJoints
		self.fkAnimatedJointsList = None
		self.fkAnimatedJointsGrp = None
		
		#FkAnimatedManips
		self.fkAnimatedManipsList = None
		self.fkAnimatedManipsGrp = None
		
		
		
		
		#Complete Swing
		#---------------------
		
		#CompleteSwingJoints
		self.completeSwingJointsList = None
		self.completeSwingJointsGrp = None
		
		#CompleteSwingManip
		self.completeSwingManip = None
		self.completeSwingManipAimGrp = None
		self.completeSwingManipGrp = None
		
		
		
		
		#Bound Joints
		#---------------------
		
		#BoundJoints
		self.boundJointsList = None
		self.boundJointsGrp = None
		
		
		#OrientConstraints
		self.boundJointsOrientConstraintList = None
		
		
		
		
		#Sorting Groups
		#---------------------
		self.nodesGrp = None
		self.manipsGrp = None
		self.jointsGrp = None
		
		
	
	
	
	#Toplevel Methods
	#----------------------------------------------------
	
	#createDynamicChainLocators
	def createDynamicChainLocators(self, prefix = ''):
		
		#set instance prefix var
		self.setPrefix(prefix)
		
		pm.select(cl = True)
		
		#Create Space locators and translate
		self.dynamic_chain_locator_base = pm.spaceLocator(n = self.prefix + '_dynamic_chain_locator_base')
		self.dynamic_chain_locator_base.translate.set(0, 0, 0)
		pm.select(cl = True)
		
		self.dynamic_chain_locator_tip = pm.spaceLocator(n = self.prefix + '_dynamic_chain_locator_tip')
		self.dynamic_chain_locator_tip.translate.set(0, 10, 0)
		pm.select(cl = True)
		
		
		
		#Create Annotations and rename
		self.annotation_dynamic_chain_locator_base = pm.annotate( self.dynamic_chain_locator_base, tx = self.prefix +'_dynamic_chain_base' )
		pm.rename(self.annotation_dynamic_chain_locator_base.getParent().name(), self.prefix + '_dynamic_chain_base_annotation')
		
		self.annotation_dynamic_chain_locator_tip = pm.annotate( self.dynamic_chain_locator_tip, tx = self.prefix +'_dynamic_chain_tip' )
		pm.rename(self.annotation_dynamic_chain_locator_tip.getParent().name(), self.prefix + '_dynamic_chain_tip_annotation')
		
		pm.select(cl = True)
		
		#Parent constrain annotation transforms
		pm.parentConstraint(self.dynamic_chain_locator_base, self.annotation_dynamic_chain_locator_base.getParent(), mo = False)
		pm.parentConstraint(self.dynamic_chain_locator_tip, self.annotation_dynamic_chain_locator_tip.getParent(), mo = False)
		
	
	
	
	#createDynamicChain
	def createDynamicChain(self, prefix = '', jointCount = 5, displayProgressbar = True):
		
		#Check if Variables != None
		if(self.dynamic_chain_locator_base and self.dynamic_chain_locator_tip):
			
			#Check if locators exist in scene
			if(pm.objExists(self.dynamic_chain_locator_base) and pm.objExists(self.dynamic_chain_locator_tip)):
			
				#Check if jointCount > 2
				if(jointCount > 2):
				
				
				
				
					#Create Progressbarwin if displayProgressbar == True
					if(displayProgressbar): self.createProgressbarWindow(progressbarSize = 28)
						
					#setJointCount
					self.setJointCount(jointCount)
					
					#set instance prefix var
					self.setPrefix(prefix)
					
					
						
					#Create dynamicChain
					#----------------------------------------------------
						
					#getJointPositionListAndFinalTransformMatrix
					self.getJointPositionListAndFinalTransformMatrix()
					if(self.verbose): print('Successfully aquired joint positions and final transform matrix')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					#createManipMaster
					self.createManipMaster()
					if(self.verbose): print('Successfully created Master manip')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					#createManipCtrlCenter
					self.createManipCtrlCenter()
					if(self.verbose): print('Successfully created Manip Ctrl Center')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					#addAttributesManipCtrlCenter
					self.addAttributesManipCtrlCenter()
					if(self.verbose): print('Successfully added Attributes to Manip Ctrl Center')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					
					#IK Dynamic
					#---------------------
					
					#createIkDynamicJoints
					self.createIkDynamicJoints()
					if(self.verbose): print('Successfully created dynamic ik joint chain')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createIkDynamicCurve
					self.createIkDynamicCurve()
					if(self.verbose): print('Successfully created dynamic curve')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createHairSystemForDynamicCurve
					self.createHairSystemForDynamicCurve()
					if(self.verbose): print('Successfully created hairsystem for dynamic curve')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#connectDynamicAttributesManipCtrlCenter
					self.connectDynamicAttributesManipCtrlCenter()
					if(self.verbose): print('Successfully connected dynamic Attributes of Manip Ctrl Center to hair sys')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createSplineIk
					self.createSplineIk()
					if(self.verbose): print('Successfully created spline Ik for dynamic chain')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#constrainCtrlCenterAndFollicle
					self.constrainCtrlCenterAndFollicle()
					if(self.verbose): print('Successfully constrained manip ctrl center and hairSys follicle')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					
					
					
					#IK Animated
					#---------------------
					
					#createIkAnimatedJoints
					self.createIkAnimatedJoints()
					if(self.verbose): print('Successfully created animated ik joint chain')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createManipIkAnimatedAndPoleVector
					self.createManipIkAnimatedAndPoleVector()
					if(self.verbose): print('Successfully created Manip Ik Animated and Pole Vector')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createIkRpHandleAnimated
					self.createIkRpHandleAnimated()
					if(self.verbose): print('Successfully created Ik Rp Handle Animated')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createIkAnimatedSystemConstraints
					self.createIkAnimatedSystemConstraints()
					if(self.verbose): print('Successfully created all Ik Animated system constraints')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					
					
					
					
					
					
					
					#FK Animated
					#---------------------
					
					#createFkAnimatedJoints
					self.createFkAnimatedJoints()
					if(self.verbose): print('Successfully created animated fk joint chain')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createFkAnimatedManips
					self.createFkAnimatedManips()
					if(self.verbose): print('Successfully created animated fk manips')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createFkAnimatedSystemConstraints
					self.createFkAnimatedSystemConstraints()
					if(self.verbose): print('Successfully created animated fk system constraints')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					
					
					
					
					
					#Complete Swing
					#---------------------
					
					#createCompleteSwingJoints
					self.createCompleteSwingJoints()
					if(self.verbose): print('Successfully created complete swing joints')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createCompleteSwingManip
					self.createCompleteSwingManip()
					if(self.verbose): print('Successfully created complete swing manip')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createCompleteSwingSystemConstraints
					self.createCompleteSwingSystemConstraints()
					if(self.verbose): print('Successfully created complete swing system constraints')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					
					
					
					
					
					
					
					#Bound Joints
					#---------------------
					
					#createBoundJoints
					self.createBoundJoints()
					if(self.verbose): print('Successfully created bound joints')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#constrainBoundJoints
					self.constrainBoundJoints()
					if(self.verbose): print('Successfully constrained bound joints')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#connectManipCtrlToOrientConstraintWeights
					self.connectManipCtrlToOrientConstraintWeights()
					if(self.verbose): print('Successfully connected ManipCtrl to orientConstraint weights')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					
					
					
					
					
					
					#Apply final transform matrix
					#---------------------
					
					#applyFinalTransformMatrix
					self.applyFinalTransformMatrix()
					if(self.verbose): print('Successfully applied final transform matrix')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					
					
					
					
					#CleanUp and Grouping
					#---------------------
					
					#lockAttributes
					self.lockAttributes()
					if(self.verbose): print('Successfully locked attributes')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#connectVisibilityAttributes
					self.connectVisibilityAttributes()
					if(self.verbose): print('Successfully connected visibility attributes')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#deleteLocatorsAndAnnotations
					self.deleteLocatorsAndAnnotations()
					if(self.verbose): print('Successfully deleted Locators and Annotations')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					#createGroupsAndSortContent
					self.createGroupsAndSortContent()
					if(self.verbose): print('Successfully created groups and sorted content')
					if(displayProgressbar): self.updateProgressbarWindow()
					
					
					
					
					
						
						
						
					#deleteProgressbar
					if(displayProgressbar): self.deleteProgressbarWindow()
						
					#SuccessMsg
					if(self.verbose): print('Successfully created dynamic joint chain')
					return None
					
				
				
				
				else:
					if(self.verbose): print('Please select a joint count larger than two (minimum is 3)')
					return None	
				
			else:
				if(self.verbose): print('Locators seem to be missing in scene, please recreate them')
				return None
			
		else:
			if(self.verbose): print('No Locators created')
			return None
	
	
	
	#Methods
	#----------------------------------------------------
	
	
	
	
	#GENERAL
	#----------------------------------------------------
	
	
	
	
	#getJointPositionListAndFinalTransformMatrix
	def getJointPositionListAndFinalTransformMatrix(self):
		
		pm.select(cl = True)
		
		#jointPositionList
		#----------------------------------------------------
		
		#Query worldspace of locators
		loc_base_worldcoord = pm.xform(self.dynamic_chain_locator_base, ws = True, q = True, t = True)
		loc_tip_worldcoord = pm.xform(self.dynamic_chain_locator_tip, ws = True, q = True, t = True)
		
		#getDistance
		self.locatorDistance = self.getDistance(loc_base_worldcoord, loc_tip_worldcoord)
		
		#Reset and append joint positions to jointPositionList
		self.jointPositionList = []
		
		for index in range(0, self.jointCount + 1):
			jointCoordinate = [0, (self.locatorDistance / self.jointCount) * index, 0]
			self.jointPositionList.append(jointCoordinate)
			
		
		
		#FinalTransformMatrix
		#----------------------------------------------------		
		
		pm.select(cl = True)
		
		#createTempMatrixJoints
		
		#matrix_j_base
		matrix_j_base = pm.joint(a = True, p= loc_base_worldcoord , co = True, n = self.prefix + '_matrix_j_base')
		
		#matrix_j_tip
		matrix_j_tip = pm.joint(a = True, p= loc_tip_worldcoord , co = True, n = self.prefix + '_matrix_j_tip')
		
		pm.select(cl = True)
		
		#Orient matrix joints
		pm.joint(matrix_j_base, e = True, sao = 'xup', oj='yxz', zso = True, ch = True)
		pm.select(cl = True)
		
		#get TransformMatrix
		self.finalTransformMatrix = pm.xform(matrix_j_base, q = True, ws = True, matrix = True)
		
		#deleteMAtrixJoints
		pm.delete(matrix_j_base)
		pm.select(cl = True)
		
	

	#createManipMaster
	def createManipMaster(self):
		
		pm.select(cl = True)
		
		#Create Manip_spine_master
		self.manip_master = pm.circle(r = 3, name = self.prefix + '_manip_master', ch = False, nr=(0, 1, 0))[0]
		
		pm.select(cl = True)
		
		#Group
		self.manip_master_grp = pm.group(self.manip_master,  n= self.prefix + '_manip_master_grp' )
		
		pm.select(cl = True)
		
		
		
	#createManipCtrlCenter
	def createManipCtrlCenter(self):
		
		pm.select(cl = True)
		
		#createTextCurves
		nurbsText = self.prefix + '_Ctrl'
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
			
			
		#create manipCtrlGrp
		self.manip_CtrlCenter = pm.group(n = self.prefix + '_manip_ctrl_center')
		pm.select(cl = True)
		
		#iterate through nurbsCurve list and parent shapes under manip ctrlCenter
		for nurbsCurveShape in textNurbsCurveList:
			pm.parent(nurbsCurveShape, self.manip_CtrlCenter, r = True, s = True)
			
		pm.select(cl = True)
		
		#create manip_ctrlCenter grp and translate correctly
		self.manip_CtrlCenter_grp = pm.group(n = self.prefix + '_manip_ctrl_center_grp')
		pm.select(cl = True)
		pm.parent(self.manip_CtrlCenter, self.manip_CtrlCenter_grp)
		pm.select(cl = True)
		
		self.manip_CtrlCenter_grp.translate.set(self.jointPositionList[-1][0], self.jointPositionList[-1][1] + 2, self.jointPositionList[-1][2])
		
		
		#delete remaining text transform nodes
		pm.delete(textTopGrp)
		pm.select(cl = True)
		
		
		
	
	#addAttributesManipCtrlCenter
	def addAttributesManipCtrlCenter(self):
		
		pm.select(cl = True)
		
		#Lock existing transform, rotate, scale and vis attrs
		#----------------------------------------------------
		pm.setAttr(self.manip_CtrlCenter.translateX, lock = True)
		pm.setAttr(self.manip_CtrlCenter.translateY, lock = True)
		pm.setAttr(self.manip_CtrlCenter.translateZ, lock = True)
		
		pm.setAttr(self.manip_CtrlCenter.rotateX, lock = True)
		pm.setAttr(self.manip_CtrlCenter.rotateY, lock = True)
		pm.setAttr(self.manip_CtrlCenter.rotateZ, lock = True)
		
		pm.setAttr(self.manip_CtrlCenter.scaleX, lock = True)
		pm.setAttr(self.manip_CtrlCenter.scaleY, lock = True)
		pm.setAttr(self.manip_CtrlCenter.scaleZ, lock = True)
		
		pm.setAttr(self.manip_CtrlCenter.visibility, lock = True)
		
		
		
		#Add Custom attributes to manip ctrl center
		#----------------------------------------------------
		#Custom Divider
		pm.addAttr(self.manip_CtrlCenter, ln = '_', at='enum', en = 'Custom', h = False, k = True, r = True)
		pm.setAttr(self.manip_CtrlCenter._ , lock = True)
		
		
		#Dynamics
		pm.addAttr(self.manip_CtrlCenter, ln = '__', at='enum', en = 'Dynamics', h = False, k = True, r = True)
		pm.setAttr(self.manip_CtrlCenter.__ , lock = True)
		
		pm.addAttr(self.manip_CtrlCenter, ln = 'simMethod', at='enum', en = 'Off:Static:Dynamic:All', h = False, k = True, r = True)
		pm.addAttr(self.manip_CtrlCenter,ln = 'solverIterations', at='long', defaultValue= 4, h = False, k = True, r = True, minValue = 0)
		pm.addAttr(self.manip_CtrlCenter,ln = 'gravity', at='float', defaultValue= 0.98, h = False, k = True, r = True)
		pm.addAttr(self.manip_CtrlCenter,ln = 'stiffness', at='float', defaultValue= 0.2, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		pm.addAttr(self.manip_CtrlCenter,ln = 'startCurveAttract', at='float', defaultValue= 0.1, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		pm.addAttr(self.manip_CtrlCenter,ln = 'damp', at='float', defaultValue= 0.05, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		pm.addAttr(self.manip_CtrlCenter,ln = 'drag', at='float', defaultValue= 0.05, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		
		pm.addAttr(self.manip_CtrlCenter,ln = 'turbulenceIntensity', at='float', defaultValue= 0.0, h = False, k = True, r = True, minValue=0.0)
		pm.addAttr(self.manip_CtrlCenter,ln = 'turbulenceFrequency', at='float', defaultValue= 1.0, h = False, k = True, r = True, minValue=0.0)
		pm.addAttr(self.manip_CtrlCenter,ln = 'turbulenceSpeed', at='float', defaultValue= 1.0, h = False, k = True, r = True, minValue=0.0)
		
		
		#Weighting
		pm.addAttr(self.manip_CtrlCenter, ln = '___', at='enum', en = 'Weighting', h = False, k = True, r = True)
		pm.setAttr(self.manip_CtrlCenter.___ , lock = True)
		
		pm.addAttr(self.manip_CtrlCenter,ln = 'weightDynamicChain', at='float', defaultValue= 0.0, h = False, k = True, r = True, minValue=0.0)
		pm.addAttr(self.manip_CtrlCenter,ln = 'weightIkChain', at='float', defaultValue= 1.0, h = False, k = True, r = True, minValue=0.0)
		pm.addAttr(self.manip_CtrlCenter,ln = 'weightFkChain', at='float', defaultValue= 0.0, h = False, k = True, r = True, minValue=0.0)
		pm.addAttr(self.manip_CtrlCenter,ln = 'weightCompleteSwingChain', at='float', defaultValue= 0.0, h = False, k = True, r = True, minValue=0.0)
		
		
		
		#Visibility
		pm.addAttr(self.manip_CtrlCenter, ln = '____', at='enum', en = 'Visibility', h = False, k = True, r = True)
		pm.setAttr(self.manip_CtrlCenter.____ , lock = True)
		
		pm.addAttr(self.manip_CtrlCenter, ln = 'ikManipsVis', at='enum', en = 'Off:On', h = False, k = True, r = True)
		pm.addAttr(self.manip_CtrlCenter, ln = 'fkManipsVis', at='enum', en = 'Off:On', h = False, k = True, r = True)
		pm.addAttr(self.manip_CtrlCenter, ln = 'completeSwingManipsVis', at='enum', en = 'Off:On', h = False, k = True, r = True)
	

	
	
	
	
	
	
	#IK DYNAMICS
	#----------------------------------------------------
	
		
	
	#createIkDynamicJoints
	def createIkDynamicJoints(self):
		
		pm.select(cl = True)
		
		#Iterate jointPositionList and append to ikDynamicJointsList joint at each position
		self.ikDynamicJointsList = []
		
		for index in range(0, len(self.jointPositionList)):
			#create Joint
			
			#decide jointNames
			jointName = self.prefix + '_ik_dynamic_j_' + str(index + 1)
			if( index == 0 ): jointName = self.prefix + '_ik_dynamic_j_' + 'base'
			if( index + 1 == len(self.jointPositionList) ): jointName = self.prefix + '_ik_dynamic_j_' + 'tip'
			
			joint = pm.joint(a = True, p= self.jointPositionList[index] , co = True, n = jointName)
			self.ikDynamicJointsList.append(joint)
			
			
		pm.select(cl = True)
		
		
		#Create ikDynamicJointsGrp and parent first ik dynamic joint
		self.ikDynamicJointsGrp = pm.group(n = self.prefix + '_ik_dynamic_joints_grp')
		pm.select(cl = True)
		pm.parent(self.ikDynamicJointsList[0] , self.ikDynamicJointsGrp)
		pm.select(cl = True)
		
		
	
	
	#createIkDynamicCurve
	def createIkDynamicCurve(self):
		
		pm.select(cl = True)
		
		#Create dynamic spline ik curve
		self.spline_ik_dynamic_curve = pm.curve( p = self.jointPositionList, ws = True, d = 2, n = self.prefix + '_spline_ik_dynamic_curve')
		
		pm.select(cl = True)
		
		
	
	#createHairSystemForDynamicCurve
	def createHairSystemForDynamicCurve(self):
		
		#Select dynamicCurve
		pm.select(cl = True)
		pm.select(self.spline_ik_dynamic_curve, r = True)
		
		#makeCurveDynamic
		pm.runtime.MakeCurvesDynamic()
		pm.select(cl = True)
		
		
		#get Hairsystem and Follicle
		#----------------------------------------------------
		futureListDynamicCurve = pm.listHistory(self.spline_ik_dynamic_curve.getShape(), future = True, af = True)
		
		#Iterate futureList and get Hairsystem and follicle
		for node in futureListDynamicCurve:
			
			#HairSys
			if(pm.nodeType(node) == 'hairSystem'): 
				self.dynamicHairsystem = node
				pm.rename(self.dynamicHairsystem.getParent(), self.prefix + '_dynamic_hair_system')
			
			#Follicle
			if(pm.nodeType(node) == 'follicle'):
				#follicle
				self.dynamicHairsystemFollicle = node
				pm.rename(self.dynamicHairsystemFollicle.getParent(), self.prefix + '_dynamic_hair_system_follicle')
				
				#follicle_grp
				self.dynamicHairsystemFollicleGrp = self.dynamicHairsystemFollicle.getParent().getParent()
				pm.rename(self.dynamicHairsystemFollicleGrp, self.prefix + '_dynamic_hair_system_follicle_grp')
				
		
		pm.select(cl = True)
		
		#get dynamicOutputCurve
		#----------------------------------------------------
		connectionsList = pm.listConnections(self.dynamicHairsystemFollicle.outCurve, d = True)
		
		#dynamicOutputCurve
		self.dynamicOutputCurve = connectionsList[0]
		pm.rename(self.dynamicOutputCurve, self.prefix + '_dynamic_output_curve')
		pm.select(cl = True)
		
		#dynamicOutputCurveGrp
		self.dynamicOutputCurveGrp = self.dynamicOutputCurve.getParent()
		pm.rename(self.dynamicOutputCurveGrp, self.prefix + '_dynamic_output_curve_grp')
		pm.select(cl = True)
		
		
		#group hairSystem nodes
		#----------------------------------------------------
		self.hairsystemNodesGrp = pm.group(n = self.prefix + '_hairSys_nodes_grp')
		pm.select(cl = True)
		
		#parent
		pm.parent(self.dynamicOutputCurveGrp, self.dynamicHairsystem.getParent(), self.dynamicHairsystemFollicleGrp, self.hairsystemNodesGrp)
		pm.select(cl = True)
		
		
		
		#Initial hairSys and follicle adjustments
		#----------------------------------------------------
		
		#Set Follicle point lock attr to lock base
		pm.setAttr(self.dynamicHairsystemFollicle.pointLock, 1)
		
		
		
	
	
	#connectDynamicAttributesManipCtrlCenter
	def connectDynamicAttributesManipCtrlCenter(self):
		
		pm.select(cl = True)
		
		#Connect manip ctrl center dynamic attributes to hairSys
		pm.connectAttr(self.manip_CtrlCenter.simMethod, self.dynamicHairsystem.simulationMethod, f = True)
		pm.connectAttr(self.manip_CtrlCenter.solverIterations, self.dynamicHairsystem.iterations, f = True)
		pm.connectAttr(self.manip_CtrlCenter.gravity, self.dynamicHairsystem.gravity, f = True)
		pm.connectAttr(self.manip_CtrlCenter.stiffness, self.dynamicHairsystem.stiffness, f = True)
		pm.connectAttr(self.manip_CtrlCenter.startCurveAttract, self.dynamicHairsystem.startCurveAttract, f = True)
		pm.connectAttr(self.manip_CtrlCenter.damp, self.dynamicHairsystem.damp, f = True)
		pm.connectAttr(self.manip_CtrlCenter.drag, self.dynamicHairsystem.drag, f = True)
		
		pm.connectAttr(self.manip_CtrlCenter.turbulenceIntensity, self.dynamicHairsystem.turbulenceStrength, f = True)
		pm.connectAttr(self.manip_CtrlCenter.turbulenceFrequency, self.dynamicHairsystem.turbulenceFrequency, f = True)
		pm.connectAttr(self.manip_CtrlCenter.turbulenceSpeed, self.dynamicHairsystem.turbulenceSpeed, f = True)
		
		pm.select(cl = True)
		
		
	

	#createSplineIk
	def createSplineIk(self):
		
		pm.select( cl = True )
		
		#Create spline IK
		self.dynamicChain_spline_ik = pm.ikHandle( sj= self.ikDynamicJointsList[0] , ee= self.ikDynamicJointsList[-1] , roc = True, n = self.prefix + '_ikSplineHandle_dynamic_chain', c = self.dynamicOutputCurve, ccv = False, pcv = False, sol = 'ikSplineSolver' )[0]
		pm.select( cl = True )
		
		#Group Spline_ik
		self.dynamicChain_spline_ik_grp = pm.group(self.dynamicChain_spline_ik ,  n= self.prefix + '_ikSplineHandle_dynamic_chain_grp' )
		
		pm.select(cl = True)
		
		
	#constrainCtrlCenterAndFollicle
	def constrainCtrlCenterAndFollicle(self):
		
		pm.select(cl = True)
		
		#ctrlCenterManipGrp
		pm.scaleConstraint( self.manip_master, self.manip_CtrlCenter_grp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.manip_CtrlCenter_grp,  mo = True ) 
		pm.select(cl = True )
		
		#dynamicJointsGrp
		pm.scaleConstraint( self.manip_master, self.ikDynamicJointsGrp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.ikDynamicJointsGrp,  mo = True ) 
		pm.select(cl = True )
		
		#hairSysFollicleGrp
		pm.scaleConstraint( self.manip_master, self.dynamicHairsystemFollicleGrp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.dynamicHairsystemFollicleGrp,  mo = True ) 
		pm.select(cl = True )
		
		
	

	
	
	
	
	
	
	#IK ANIMATED
	#----------------------------------------------------
	
	#createIkAnimatedJoints
	def createIkAnimatedJoints(self):
		
		pm.select(cl = True)
		
		#Iterate jointPositionList and append to ikAnimatedJointsList joint at each position
		self.ikAnimatedJointsList = []
		
		for index in range(0, len(self.jointPositionList)):
			#create Joint
			
			#decide jointNames
			jointName = self.prefix + '_ik_animated_j_' + str(index + 1)
			if( index == 0 ): jointName = self.prefix + '_ik_animated_j_' + 'base'
			if( index + 1 == len(self.jointPositionList) ): jointName = self.prefix + '_ik_animated_j_' + 'tip'
			
			joint = pm.joint(a = True, p= self.jointPositionList[index] , co = True, n = jointName)
			#setJointPreferredAngle for correct ikHandle bending
			pm.setAttr(joint.preferredAngleX, -1.0)
			self.ikAnimatedJointsList.append(joint)
			
			
		pm.select(cl = True)
		
		
		#Create ikAnimatedJointsGrp and parent first ik animated joint
		self.ikAnimatedJointsGrp = pm.group(n = self.prefix + '_ik_animated_joints_grp')
		pm.select(cl = True)
		pm.parent(self.ikAnimatedJointsList[0] , self.ikAnimatedJointsGrp)
		pm.select(cl = True)

	
	
	
	#createManipIkAnimatedAndPoleVector
	def createManipIkAnimatedAndPoleVector(self):
		
		pm.select(cl = True)
		
		#manipIkAnimated
		#----------------------------------------------------
		
		#create manipIkAnimated
		self.manipIkAnimated = pm.sphere(r = 1, n = self.prefix + '_manip_ik_animated', ch = False)[0]
		pm.select(cl = True)
		
		
		#grp ik animated
		self.manipIkAnimatedGrp = pm.group(n = self.prefix + '_manip_ik_animated_grp')
		pm.select(cl = True)
		pm.parent(self.manipIkAnimated, self.manipIkAnimatedGrp)
		pm.select(cl = True)
		
		#Move grp to appropiate place
		self.manipIkAnimatedGrp.translate.set(self.jointPositionList[-1])
		pm.select(cl = True)
		
		
		
		#poleVector
		#----------------------------------------------------
		
		#create poleVector
		self.manipIkAnimatedPoleVector = pm.spaceLocator(n = self.prefix + '_ik_animated_poleVector')
		pm.select(cl = True)
		
		#grp poleVector and translate
		self.manipIkAnimatedPoleVectorGrp = pm.group(n = self.prefix + '_ik_animated_poleVector_grp')
		pm.select(cl = True)
		pm.parent(self.manipIkAnimatedPoleVector, self.manipIkAnimatedPoleVectorGrp)
		pm.select(cl = True)
		
		#poleVectorGrp Translation
		zAxisDistance = 3
		self.manipIkAnimatedPoleVectorGrp.translate.set(0, self.locatorDistance * 0.5, zAxisDistance)
		pm.select(cl = True)
		
		
		
		
	#createIkRpHandleAnimated
	def createIkRpHandleAnimated(self):
		
		pm.select(cl = True)
		
		#create ik handle
		self.ikHandleAnimated = pm.ikHandle( sj= self.ikAnimatedJointsList[0] , ee= self.ikAnimatedJointsList[-1] , n = self.prefix +'_ik_rp_Handle_animated' , sol = 'ikRPsolver' )[0]
		pm.select(cl = True)
		
		#Group ik solver
		self.ikHandleAnimatedGrp = pm.group(n = self.prefix + '_ik_rp_Handle_animated_grp')
		pm.select(cl = True)
		pm.parent(self.ikHandleAnimated, self.ikHandleAnimatedGrp)
		pm.select(cl = True)
		
		
		
	#createIkAnimatedSystemConstraints
	def createIkAnimatedSystemConstraints(self):
		
		pm.select(cl = True)
		
		#ikRpHandleGrp
		pm.poleVectorConstraint(self.manipIkAnimatedPoleVector, self.ikHandleAnimated)
		pm.scaleConstraint( self.manipIkAnimated, self.ikHandleAnimatedGrp,  mo = True ) 
		pm.parentConstraint( self.manipIkAnimated, self.ikHandleAnimatedGrp,  mo = True )
		pm.select(cl = True)
		
		#poleVectorGrp
		pm.scaleConstraint( self.manip_master, self.manipIkAnimatedPoleVectorGrp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.manipIkAnimatedPoleVectorGrp,  mo = True )
		pm.select(cl = True)
		
		#manipIkAnimatedGrp
		pm.scaleConstraint( self.manip_master, self.manipIkAnimatedGrp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.manipIkAnimatedGrp,  mo = True )
		pm.select(cl = True)
		
		#ikAnimatedJointsGrp
		pm.scaleConstraint( self.manip_master, self.ikAnimatedJointsGrp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.ikAnimatedJointsGrp,  mo = True )
		pm.select(cl = True)
		
	





	
	#FK ANIMATED
	#----------------------------------------------------
	
	#createFkAnimatedJoints
	def createFkAnimatedJoints(self):
		
		pm.select(cl = True)
		
		#Iterate jointPositionList and append to fkAnimatedJointsList joint at each position
		self.fkAnimatedJointsList = []
		
		for index in range(0, len(self.jointPositionList)):
			#create Joint
			
			#decide jointNames
			jointName = self.prefix + '_fk_animated_j_' + str(index + 1)
			if( index == 0 ): jointName = self.prefix + '_fk_animated_j_' + 'base'
			if( index + 1 == len(self.jointPositionList) ): jointName = self.prefix + '_fk_animated_j_' + 'tip'
			
			joint = pm.joint(a = True, p= self.jointPositionList[index] , co = True, n = jointName)
			self.fkAnimatedJointsList.append(joint)
			
			
		pm.select(cl = True)
		
		
		#Create fkAnimatedJointsGrp and parent first fk animated joint
		self.fkAnimatedJointsGrp = pm.group(n = self.prefix + '_fk_animated_joints_grp')
		pm.select(cl = True)
		pm.parent(self.fkAnimatedJointsList[0] , self.fkAnimatedJointsGrp)
		pm.select(cl = True)
		
		
		
	#createFkAnimatedManips
	def createFkAnimatedManips(self):
		
		pm.select(cl = True)
		
		#iterate through len(jointPosList) - 1 and append to fkAnimatedMaipsLisz
		self.fkAnimatedManipsList = []
		
		for index in range(0, len(self.jointPositionList) - 1):
			
			#decide manipNames
			manipName = self.prefix + '_fk_animated_manip_' + str(index + 1)
			if( index == 0 ): manipName = self.prefix + '_fk_animated_manip_' + 'base'
			
			#createManip
			manip = self.createFkManip(name = manipName)
			self.fkAnimatedManipsList.append(manip)
			pm.select(cl = True)
			
			#createManipGrp
			manipGrp = pm.group(n = manipName + '_grp')
			pm.select(cl = True)
			
			#parent manip under manipGrp
			pm.parent(manip, manipGrp)
			pm.select(cl = True)
			
			#translateManipGrp to correct position
			manipGrp.translate.set(self.jointPositionList[index])
			pm.select(cl = True)
			
			
		
		
		#create fkANimatedManipsGrp
		self.fkAnimatedManipsGrp = pm.group(n = self.prefix + '_fk_animated_manips_grp')
		pm.select(cl = True)
		
		#iterate fkManipsList and group each manip under grp
		for fkAnimatedManip in self.fkAnimatedManipsList:
			pm.parent(fkAnimatedManip.getParent(), self.fkAnimatedManipsGrp)
			pm.select(cl = True)
			
			
			
			
	#createFkAnimatedSystemConstraints
	def createFkAnimatedSystemConstraints(self):
		
		pm.select(cl = True)
		
		#FkManips
		
		#iterate fkManipsList
		for index in range(0, len(self.fkAnimatedManipsList) - 1):
			
			#constrain
			pm.scaleConstraint( self.fkAnimatedManipsList[index], self.fkAnimatedManipsList[index + 1].getParent(),  mo = True ) 
			pm.parentConstraint( self.fkAnimatedManipsList[index], self.fkAnimatedManipsList[index + 1].getParent(),  mo = True ) 
			pm.select(cl = True)
			
			
		
		#FkManipBase
		pm.scaleConstraint( self.manip_master, self.fkAnimatedManipsList[0].getParent(),  mo = True ) 
		pm.parentConstraint( self.manip_master, self.fkAnimatedManipsList[0].getParent(),  mo = True ) 
		pm.select(cl = True)
		
		
		#FkAnimatedJointsGrp
		pm.scaleConstraint( self.manip_master, self.fkAnimatedJointsGrp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.fkAnimatedJointsGrp,  mo = True ) 
		pm.select(cl = True)
		
		
		#Orientconstrain all fkAnimatedJoints
		for index in range(0, len(self.fkAnimatedManipsList)):
			pm.orientConstraint( self.fkAnimatedManipsList[index], self.fkAnimatedJointsList[index],  mo = True )
			pm.select(cl = True)
	
	
	
	
	
	
	
	
	
	#COMPLETE SWING
	#----------------------------------------------------
	
	#createCompleteSwingJoints
	def createCompleteSwingJoints(self):
		
		pm.select(cl = True)
		
		#Iterate jointPositionList and append to completeSwingJointsList joint at each position
		self.completeSwingJointsList = []
		
		for index in range(0, len(self.jointPositionList)):
			#create Joint
			
			#decide jointNames
			jointName = self.prefix + '_complete_swing_j_' + str(index + 1)
			if( index == 0 ): jointName = self.prefix + '_complete_swing_j_' + 'base'
			if( index + 1 == len(self.jointPositionList) ): jointName = self.prefix + '_complete_swing_j_' + 'tip'
			
			joint = pm.joint(a = True, p= self.jointPositionList[index] , co = True, n = jointName)
			self.completeSwingJointsList.append(joint)
			
			
		pm.select(cl = True)
		
		
		#Create completeSwingJointsGrp and parent first complete swing joint
		self.completeSwingJointsGrp = pm.group(n = self.prefix + '_complete_swing_joints_grp')
		pm.select(cl = True)
		pm.parent(self.completeSwingJointsList[0] , self.completeSwingJointsGrp)
		pm.select(cl = True)
	
	
	
	
	#createCompleteSwingManip
	def createCompleteSwingManip(self):
		
		pm.select(cl = True)
		
		#create CompleteSwingManip
		self.completeSwingManip = pm.curve( p=[(-1, 1, 0), (-1, 3, 0), (-2, 3, 0), (0, 5, 0),(2, 3, 0),(1, 3, 0),(1, 1, 0), (-1, 1, 0)], ws = True, d = 1, name = self.prefix + '_complete_swing_manip' )
		pm.select(cl = True)
		
		#completeSwingManipAimGrp
		self.completeSwingManipAimGrp = pm.group( n = self.prefix + '_complete_swing_manip_aim_grp')
		pm.select(cl = True)
		pm.parent(self.completeSwingManip, self.completeSwingManipAimGrp)
		pm.select(cl = True)
		
		#completeSwingManipGrp
		self.completeSwingManipGrp = pm.group( n = self.prefix + '_complete_swing_manip_grp')
		pm.select(cl = True)
		pm.parent(self.completeSwingManipAimGrp, self.completeSwingManipGrp)
		pm.select(cl = True)
		
		
	
	
	#createCompleteSwingSystemConstraints
	def createCompleteSwingSystemConstraints(self):
		
		pm.select(cl = True)
		
		#completeSwingJointsGrp
		pm.scaleConstraint( self.manip_master, self.completeSwingJointsGrp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.completeSwingJointsGrp,  mo = True ) 
		pm.select(cl = True)
		
		
		#completeSwingManipGrp
		pm.scaleConstraint( self.manip_master, self.completeSwingManipGrp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.completeSwingManipGrp,  mo = True ) 
		pm.select(cl = True)
		
		
		#completeSwingManipAimGrp
		pm.aimConstraint( self.ikDynamicJointsList[-1], self.completeSwingManipAimGrp, aim = (0.0,1.0,0.0), u = (1.0,0.0,0.0), wut = 'objectrotation', wuo = self.manip_master, wu = (1.0,0.0,0.0),  mo = True ) 
		pm.select(cl = True)
		
		
		#completeSwingJointsList[0]
		pm.orientConstraint( self.completeSwingManipAimGrp, self.completeSwingJointsList[0],  mo = True ) 
		pm.select(cl = True)
	
	
	
	
	
	
	
	
	#BOUND JOINTS
	#----------------------------------------------------
	
	#createBoundJoints
	def createBoundJoints(self):
		
		pm.select(cl = True)
		
		#Iterate jointPositionList and append to boundJointsList joint at each position
		self.boundJointsList = []
		
		for index in range(0, len(self.jointPositionList)):
			#create Joint
			
			#decide jointNames
			jointName = self.prefix + '_bound_j_' + str(index + 1)
			if( index == 0 ): jointName = self.prefix + '_bound_j_' + 'base'
			if( index + 1 == len(self.jointPositionList) ): jointName = self.prefix + '_bound_j_' + 'tip'
			
			joint = pm.joint(a = True, p= self.jointPositionList[index] , co = True, n = jointName)
			self.boundJointsList.append(joint)
			
			
		pm.select(cl = True)
		
		
		#Create boundJointsGrp and parent first bound joint
		self.boundJointsGrp = pm.group(n = self.prefix + '_bound_joints_grp')
		pm.select(cl = True)
		pm.parent(self.boundJointsList[0] , self.boundJointsGrp)
		pm.select(cl = True)
		
		
		
		
	#constrainBoundJoints
	def constrainBoundJoints(self):
		
		pm.select(cl = True)
		
		self.boundJointsOrientConstraintList = []
		
		#iterate len(boundJointsList) - 1 and orient constrain each joints
		for index in range(0, len(self.boundJointsList) - 1):
			orientConstraint = pm.orientConstraint( self.ikDynamicJointsList[index], self.ikAnimatedJointsList[index], self.fkAnimatedJointsList[index], self.completeSwingJointsList[index], self.boundJointsList[index],  mo = True )
			self.boundJointsOrientConstraintList.append(orientConstraint)
			pm.select(cl = True)
			
			
			
		#constrain bound joints grp to master manip
		pm.scaleConstraint( self.manip_master, self.boundJointsGrp,  mo = True ) 
		pm.parentConstraint( self.manip_master, self.boundJointsGrp,  mo = True ) 
		pm.select(cl = True)
		
	
	
	
	
	#connectManipCtrlToOrientConstraintWeights
	def connectManipCtrlToOrientConstraintWeights(self):
		
		pm.select(cl = True)
		
		#iterate boundJointsOrientConstraintList and make connections to manipCtrl for each constraint
		for index in range(0, len(self.boundJointsOrientConstraintList)):
			
			pm.connectAttr(self.manip_CtrlCenter.weightDynamicChain, self.boundJointsOrientConstraintList[index] +'.' +self.ikDynamicJointsList[index].name() +'W0', f = True)
			pm.connectAttr(self.manip_CtrlCenter.weightIkChain, self.boundJointsOrientConstraintList[index] +'.' +self.ikAnimatedJointsList[index].name() +'W1', f = True)
			pm.connectAttr(self.manip_CtrlCenter.weightFkChain, self.boundJointsOrientConstraintList[index] +'.' +self.fkAnimatedJointsList[index].name() +'W2', f = True)
			pm.connectAttr(self.manip_CtrlCenter.weightCompleteSwingChain, self.boundJointsOrientConstraintList[index] +'.' +self.completeSwingJointsList[index].name() +'W3', f = True)
			pm.select(cl = True)
	
	
	
	
	
	
	
	
	
	#APPLY FINAL TRANSFORM MATRIX
	#----------------------------------------------------
	
	#applyFinalTransformMatrix
	def applyFinalTransformMatrix(self):
		
		pm.select(cl = True)
		pm.xform(self.manip_master_grp, ws = True, matrix = self.finalTransformMatrix)
		pm.select(cl = True)
	
	
	
	
	
	
	
	
	#CLEANUP AND GROUPING
	#----------------------------------------------------
	
	#lockAttributes
	def lockAttributes(self):
		pm.select(cl = True)
		
		#fkAnimatedManips
		for fkAnimatedManip in self.fkAnimatedManipsList:
			
			#translate
			pm.setAttr(fkAnimatedManip.translateX , lock = True)
			pm.setAttr(fkAnimatedManip.translateY , lock = True)
			pm.setAttr(fkAnimatedManip.translateZ , lock = True)
			
			#scale
			pm.setAttr(fkAnimatedManip.scaleX , lock = True)
			pm.setAttr(fkAnimatedManip.scaleY , lock = True)
			pm.setAttr(fkAnimatedManip.scaleZ , lock = True)
			
		pm.select(cl = True)	
		
		
		
		#completeSwingManip
		
		#translate
		pm.setAttr(self.completeSwingManip.translateX , lock = True)
		pm.setAttr(self.completeSwingManip.translateY , lock = True)
		pm.setAttr(self.completeSwingManip.translateZ , lock = True)
		
		#rotate
		pm.setAttr(self.completeSwingManip.rotateX , lock = True)
		pm.setAttr(self.completeSwingManip.rotateY , lock = True)
		pm.setAttr(self.completeSwingManip.rotateZ , lock = True)
		
		#scale
		pm.setAttr(self.completeSwingManip.scaleX , lock = True)
		pm.setAttr(self.completeSwingManip.scaleY , lock = True)
		pm.setAttr(self.completeSwingManip.scaleZ , lock = True)
		
		pm.select(cl = True)
		
		
		
		#manipIkAnimatedPoleVector
		
		#scale
		pm.setAttr(self.manipIkAnimatedPoleVector.scaleX , lock = True)
		pm.setAttr(self.manipIkAnimatedPoleVector.scaleY , lock = True)
		pm.setAttr(self.manipIkAnimatedPoleVector.scaleZ , lock = True)
		
		pm.select(cl = True)
		
	



	#connectVisibilityAttributes
	def connectVisibilityAttributes(self):
		
		pm.select(cl = True)
		
		#fkAnimatedManips
		for fkAnimatedManip in self.fkAnimatedManipsList:
			pm.connectAttr(self.manip_CtrlCenter.fkManipsVis, fkAnimatedManip.visibility ,f = True)
			pm.select(cl = True)
			
		
		#poleVectorVis
		pm.connectAttr(self.manip_CtrlCenter.ikManipsVis, self.manipIkAnimatedPoleVector.visibility ,f = True)
		pm.select(cl = True)
		
		
		#ikManipVis
		pm.connectAttr(self.manip_CtrlCenter.ikManipsVis, self.manipIkAnimated.visibility ,f = True)
		pm.select(cl = True)
		
		
		
		#completeSwingManipVis
		pm.connectAttr(self.manip_CtrlCenter.completeSwingManipsVis, self.completeSwingManip.visibility ,f = True)
		pm.select(cl = True)
		
	
	
	
	
	
	#deleteLocatorsAndAnnotations
	def deleteLocatorsAndAnnotations(self):
		
		pm.select(cl = True)
		
		#delete Locators
		pm.delete(self.dynamic_chain_locator_base, self.dynamic_chain_locator_tip)
		pm.select(cl = True)
		
		#delete annotations
		pm.delete(self.annotation_dynamic_chain_locator_base.getParent(), self.annotation_dynamic_chain_locator_tip.getParent())
		pm.select(cl = True)
		
	
	
	
	#createGroupsAndSortContent
	def createGroupsAndSortContent(self):
		
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
		pm.parent(self.ikHandleAnimatedGrp, self.dynamicChain_spline_ik_grp, self.hairsystemNodesGrp, self.nodesGrp)
		pm.select(cl = True)
		
		#manipsGrp
		pm.parent(self.completeSwingManipGrp, self.fkAnimatedManipsGrp, self.manipIkAnimatedPoleVectorGrp, self.manipIkAnimatedGrp, self.manip_CtrlCenter_grp, self.manip_master_grp, self.manipsGrp)
		pm.select(cl = True)
		
		#jointsGrp
		pm.parent(self.ikDynamicJointsGrp, self.ikAnimatedJointsGrp, self.fkAnimatedJointsGrp, self.completeSwingJointsGrp, self.boundJointsGrp, self.jointsGrp)
		pm.select(cl = True)
		
	
	
	
	
	
	
	
	#Shared Methods
	#----------------------------------------------------
	
	
	#setPrefix
	def setPrefix(self, prefix):
		self.prefix = prefix
		
		
	#setJointCount
	def setJointCount(self, jointCount):
		self.jointCount = jointCount
		
		
	

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
		
		
		
	#createFkManip
	def createFkManip(self, name = '_defaultName'):
		
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
import rbDynamicChain

#Reload if true
doReload = True
if(doReload): reload(rbDynamicChain)

#Create Instance if it doesnt exist
rbDynamicChainInstance = rbDynamicChain.RbDynamicChain()

#createLocators
rbDynamicChainInstance.createDynamicChainLocators(prefix = 'Test')
'''

'''
#CREATE CHAIN

#createLocators
rbDynamicChainInstance.createDynamicChain(prefix = 'Test')
'''
	
	
	