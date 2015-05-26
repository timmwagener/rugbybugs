




#rbDynamicChainFromCurves Module
#----------------------------------------------------

'''
Description:
Module to create a standardized dynamic chain rig module from curves
Selection Order:
1. Low Resolution Curve for manual Spline IK
2. High Res Curve for dynamic hair system

ToDo:
-

'''



#Import
#----------------------------------------------------
import pymel.core as pm
import math





#RbDynamicChainFromCurves Class
#----------------------------------------------------

class RbDynamicChainFromCurves():
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#----------------------------------------------------
		
		#Debug and Ui
		self.verbose = True
		self.prefix = None
		self.progressbarWindow = None
		self.progressControl = None
		
		
		
		#Selection
		self.selectionList = None
		self.lowResCurveTrans = None
		self.highResCurveTrans = None
		
		
		#Curve coords
		self.lowResCurveCoordList = None
		self.highResCurveCoordList = None
		
		
		#IkSpline joint chain
		self.ikSplineJointsList = None
		self.ikSplineJointsGrp = None
		
		
		#IkDynamic joint chain
		self.ikDynamicJointsList = None
		self.ikDynamicJointsGrp = None
		
		
		#Bound joint chain
		self.boundJointsList = None
		self.boundJointsGrp = None
		
		
		#Manipulators
		self.manip_master = None
		self.manip_master_grp = None
		self.manipIkSplineList = None
		self.manipIkSplineGrpList = None
		self.manipIkSplineTopGrp = None
		
		
		#Manipulator Dynamic
		self.manip_dynamic = None
		self.manip_dynamic_grp = None
		
		
		#splineIk bound joints
		self.splineIkBoundJointsList = None
		self.splineIkBoundJointsGrpList = None
		self.splineIkBoundJointsTopGrp = None
		
		
		#Skincluster and spline ik (bound)
		self.bound_curve_skincluster = None
		self.bound_curve_spline_ik = None
		self.bound_curve_spline_ik_grp = None
	
		
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
		
		
		#bound joint constraints
		self.boundJointConstraintList = None
		self.orientConstraintWeight_reverse = None
		
		
		#Sorting Groups
		self.nodesGrp = None
		self.manipsGrp = None
		self.jointsGrp = None
	
	
	
	
	
	
	#Toplevel Methods
	#----------------------------------------------------
	
	
	
	#createDynamicChainFromCurves
	def createDynamicChainFromCurves(self, prefix = '', displayProgressbar = True):
		
		
		
		#get selection
		self.selectionList = pm.ls(sl = True, fl = True)
		
		
		#Tests
		#----------------------------------------------------
		
		#Check if two objects are selected
		if not(len(self.selectionList) == 2):
			if(self.verbose): print('Length of SelectionList wrong. Please select two objects')
			return None
			
		
		#get two selected objects 
		self.lowResCurveTrans = self.selectionList[0]
		self.highResCurveTrans = self.selectionList[1]
		
		#Check if objects are of type curve
		if not(pm.nodeType(self.lowResCurveTrans.getShape()) == 'nurbsCurve'):
			if(self.verbose): print('First Selection is of type: ' +pm.nodeType(self.lowResCurveTrans) +'. Should be of type nurbsCurve.')
			return None
			
		if not(pm.nodeType(self.highResCurveTrans.getShape()) == 'nurbsCurve'):
			if(self.verbose): print('Second Selection is of type: ' +pm.nodeType(self.highResCurveTrans) +'. Should be of type nurbsCurve.')
			return None
		
			
				
		

		
		
		
		#Create Chain Procedures
		#----------------------------------------------------
				
				
		
		#Set general variables
		#----------------------------------------------------
		
		#Create Progressbarwin if displayProgressbar == True
		if(displayProgressbar): self.createProgressbarWindow(progressbarSize = 15)
					
					
		#set instance prefix var
		self.setPrefix(prefix)
					
					
		pm.select(cl = True)
						
		
		
		
		
		
		
		#Rig
		#----------------------------------------------------
		
		
		#getCurveCoords
		self.getCurveCoords()
		if(self.verbose): print('Successfully aquired curve coords')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		
		#createSplineIkJointChain
		self.createSplineIkJointChain()
		if(self.verbose): print('Successfully created spline Ik joint chain')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createDynamicIkJointChain
		self.createDynamicIkJointChain()
		if(self.verbose): print('Successfully created dynamic Ik joint chain')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createBoundJointChain
		self.createBoundJointChain()
		if(self.verbose): print('Successfully created bound joint chain')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createManipulators
		self.createManipulators()
		if(self.verbose): print('Successfully created manipulators')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createManipulatorDynamic
		self.createManipulatorDynamic()
		if(self.verbose): print('Successfully created manipulator for dynamic attributes')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#addAttributesToManipulatorDynamic
		self.addAttributesToManipulatorDynamic()
		if(self.verbose): print('Successfully added attributes to manipulator dynamic')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createSplineCurveBoundJoints
		self.createSplineCurveBoundJoints()
		if(self.verbose): print('Successfully created spline curve bound joints')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createSkinclusterAndSplineIk
		self.createSkinclusterAndSplineIk()
		if(self.verbose): print('Successfully created skincluster and spline ik')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createHairSystemForDynamicCurve
		self.createHairSystemForDynamicCurve()
		if(self.verbose): print('Successfully created hairsystem for dynamic curve')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#connectManipDynamicToHairSystemAttributes
		self.connectManipDynamicToHairSystemAttributes()
		if(self.verbose): print('Successfully connected manip dynamic attributes to hair system')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createDynamicChainSplineIk
		self.createDynamicChainSplineIk()
		if(self.verbose): print('Successfully created dynamic chain spline Ik')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createManipulatorConstraints
		self.createManipulatorConstraints()
		if(self.verbose): print('Successfully created manipulator constraints')
		if(displayProgressbar): self.updateProgressbarWindow()
		
		
		#createBoundJointConstraintsAndConnectVisibility
		self.createBoundJointConstraintsAndConnectVisibility()
		if(self.verbose): print('Successfully created bound joint constraints and connected visibility')
		if(displayProgressbar): self.updateProgressbarWindow()
					
					
		

		
		
		
		
		#CleanUp
		#----------------------------------------------------
		

		
		#createGroupsAndSortContent
		self.createGroupsAndSortContent()
		if(self.verbose): print('Successfully created groups and sorted content')
		if(displayProgressbar): self.updateProgressbarWindow()
					
					
				
				
				
				
				
		#deleteProgressbar
		if(displayProgressbar): self.deleteProgressbarWindow()
				
		#SuccessMsg
		if(self.verbose): print('Successfully created dynamic joint chain module from curves')
		return None
				
				
				
				
				
				
		
	
	
	
	#Methods
	#----------------------------------------------------
	
	
	#getCurveCoords
	def getCurveCoords(self):
		pm.select(cl = True)
		
		
		#get lowResCurveCoordList
		self.lowResCurveCoordList = []
		for cv in self.lowResCurveTrans.cv[:]:
			self.lowResCurveCoordList.append(pm.pointPosition(cv, w = True))
			
		#rename
		pm.rename(self.lowResCurveTrans, self.prefix +'_splineIk_curve')
		
			
		#get highResCurveCoordList
		self.highResCurveCoordList = []
		for cv in self.highResCurveTrans.cv[:]:
			self.highResCurveCoordList.append(pm.pointPosition(cv, w = True))
			
		#rename
		pm.rename(self.highResCurveTrans, self.prefix +'_dynamic_splineIk_curve')
		
		pm.select(cl = True)
	
	
	
	#createSplineIkJointChain
	def createSplineIkJointChain(self):
		pm.select(cl = True)
		
		
		#Iterate highResCurveCoordList and append to ikSplineJointsList joint at each position
		self.ikSplineJointsList = []
		
		for index in range(0, len(self.highResCurveCoordList)):
			#create Joint
			
			#decide jointNames
			jointName = self.prefix + '_ik_spline_j_' + str(index + 1)
			if( index == 0 ): jointName = self.prefix + '_ik_spline_j_' + 'base'
			if( index + 1 == len(self.highResCurveCoordList) ): jointName = self.prefix + '_ik_spline_j_' + 'tip'
			
			joint = pm.joint(a = True, p= self.highResCurveCoordList[index] , co = True, n = jointName)
			self.ikSplineJointsList.append(joint)
			
			
		pm.select(cl = True)
		
		
		#Orient SplineIkJoints
		pm.joint(self.ikSplineJointsList[0], e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		pm.select(cl = True)
		
		
		#Create ikSplineJointsGrp and parent first ik spline joint
		self.ikSplineJointsGrp = pm.group(n = self.prefix + '_ik_spline_joints_grp')
		pm.select(cl = True)
		pm.parent(self.ikSplineJointsList[0] , self.ikSplineJointsGrp)
		pm.select(cl = True)
		
		
		
	#createDynamicIkJointChain
	def createDynamicIkJointChain(self):
		pm.select(cl = True)
		
		
		#Iterate highResCurveCoordList and append to ikDynamicJointsList joint at each position
		self.ikDynamicJointsList = []
		
		for index in range(0, len(self.highResCurveCoordList)):
			#create Joint
			
			#decide jointNames
			jointName = self.prefix + '_ik_dynamic_j_' + str(index + 1)
			if( index == 0 ): jointName = self.prefix + '_ik_dynamic_j_' + 'base'
			if( index + 1 == len(self.highResCurveCoordList) ): jointName = self.prefix + '_ik_dynamic_j_' + 'tip'
			
			joint = pm.joint(a = True, p= self.highResCurveCoordList[index] , co = True, n = jointName)
			self.ikDynamicJointsList.append(joint)
			
			
		pm.select(cl = True)
		
		
		#Orient DynamicIkJoints
		pm.joint(self.ikDynamicJointsList[0], e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		pm.select(cl = True)
		
		
		#Create ikDynamicJointsGrp and parent first ik dynamic joint
		self.ikDynamicJointsGrp = pm.group(n = self.prefix + '_ik_dynamic_joints_grp')
		pm.select(cl = True)
		pm.parent(self.ikDynamicJointsList[0] , self.ikDynamicJointsGrp)
		pm.select(cl = True)
		
		
		
		
	#createBoundJointChain
	def createBoundJointChain(self):
		pm.select(cl = True)
		
		
		#Iterate highResCurveCoordList and append to boundJointsList joint at each position
		self.boundJointsList = []
		
		for index in range(0, len(self.highResCurveCoordList)):
			#create Joint
			
			#decide jointNames
			jointName = self.prefix + '_bound_j_' + str(index + 1)
			if( index == 0 ): jointName = self.prefix + '_bound_j_' + 'base'
			if( index + 1 == len(self.highResCurveCoordList) ): jointName = self.prefix + '_bound_j_' + 'tip'
			
			joint = pm.joint(a = True, p= self.highResCurveCoordList[index] , co = True, n = jointName)
			self.boundJointsList.append(joint)
			
			
		pm.select(cl = True)
		
		
		#Orient boundJoints
		pm.joint(self.boundJointsList[0], e = True, sao = 'yup', oj='xyz', zso = True, ch = True)
		pm.select(cl = True)
		
		
		#Create boundJointsGrp and parent first bound joint
		self.boundJointsGrp = pm.group(n = self.prefix + '_bound_joints_grp')
		pm.select(cl = True)
		pm.parent(self.boundJointsList[0] , self.boundJointsGrp)
		pm.select(cl = True)
		
		
		
		
	
	#createManipulators
	def createManipulators(self):
		
		pm.select(cl = True)
		
		#manip_master
		#----------------------------------------------------
		
		#create manip master
		self.manip_master = pm.circle(r = 1.5, name = self.prefix +'_manip_master', ch = False, nr=(0, 1, 0))[0]
		pm.select(cl = True)
		
		#create and parent under grp
		self.manip_master_grp = pm.group(n = self.prefix + '_manip_master_grp')
		pm.select(cl = True)
		pm.parent(self.manip_master, self.manip_master_grp)
		pm.select(cl = True)
		#translate
		self.manip_master_grp.translate.set(self.highResCurveCoordList[0])
		pm.select(cl = True)
		
		
		
		
		
		
		#manip_ikSpline list
		#----------------------------------------------------
		
		#manipIkSplineList
		self.manipIkSplineList = []
		self.manipIkSplineGrpList = []
		
		
		#iterate through low curve points list and create manip ik spline
		for index in range(len(self.lowResCurveCoordList)):
			
			pm.select(cl = True)
			
			#manipName
			manipName = self.prefix + '_manip_ik_spline_' + str(index + 1)
			if( index == 0 ): manipName = self.prefix + '_manip_ik_spline_' + 'base'
			if( index + 1 == len(self.lowResCurveCoordList) ): manipName = self.prefix + '_manip_ik_spline_' + 'tip'
			
			#Create manip
			manip_ik_spline = pm.sphere(r = 1, ch = False, n = manipName)[0]
			pm.select(cl = True)
			
			#create manip grp
			manip_ik_spline_grp = pm.group(n = manipName + '_grp')
			pm.select(cl = True)
			pm.parent(manip_ik_spline, manip_ik_spline_grp)
			pm.select(cl = True)
			
			#translate grp
			manip_ik_spline_grp.translate.set(self.lowResCurveCoordList[index])
			pm.select(cl = True)
			
			
			#Append to lists
			self.manipIkSplineList.append(manip_ik_spline)
			self.manipIkSplineGrpList.append(manip_ik_spline_grp)
			pm.select(cl = True)
			
		
		
		#Create group for manip groups
		self.manipIkSplineTopGrp = pm.group(n = self.prefix +'_manip_ik_spline_top_grp')
		pm.select(cl = True)
		
		#parent all manips to top grp
		pm.parent(self.manipIkSplineGrpList, self.manipIkSplineTopGrp)
		pm.select(cl = True)
		
	

	
	#createManipulatorDynamic
	def createManipulatorDynamic(self):
		
		pm.select(cl = True)
		
		#createTextCurves
		nurbsText = self.prefix + '_ctrl'
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
			
			
		#create manip_dynamicGrp
		self.manip_dynamic = pm.group(n = self.prefix + '_manip_dynamic')
		pm.select(cl = True)
		
		#iterate through nurbsCurve list and parent shapes under manip ctrlCenter
		for nurbsCurveShape in textNurbsCurveList:
			pm.parent(nurbsCurveShape, self.manip_dynamic, r = True, s = True)
			
		pm.select(cl = True)
		
		#create manip_dynamic grp and translate correctly
		self.manip_dynamic_grp = pm.group(n = self.prefix + '_manip_dynamic_grp')
		pm.select(cl = True)
		pm.parent(self.manip_dynamic, self.manip_dynamic_grp)
		pm.select(cl = True)
		
		self.manip_dynamic_grp.translate.set(self.highResCurveCoordList[0])
		
		
		#delete remaining text transform nodes
		pm.delete(textTopGrp)
		pm.select(cl = True)
	
	
	
	
	#addAttributesToManipulatorDynamic
	def addAttributesToManipulatorDynamic(self):
		
		pm.select(cl = True)
		
		#Lock existing transform, rotate, scale and vis attrs
		#----------------------------------------------------
		pm.setAttr(self.manip_dynamic.translateX, lock = True)
		pm.setAttr(self.manip_dynamic.translateY, lock = True)
		pm.setAttr(self.manip_dynamic.translateZ, lock = True)
		
		pm.setAttr(self.manip_dynamic.rotateX, lock = True)
		pm.setAttr(self.manip_dynamic.rotateY, lock = True)
		pm.setAttr(self.manip_dynamic.rotateZ, lock = True)
		
		pm.setAttr(self.manip_dynamic.scaleX, lock = True)
		pm.setAttr(self.manip_dynamic.scaleY, lock = True)
		pm.setAttr(self.manip_dynamic.scaleZ, lock = True)
		
		pm.setAttr(self.manip_dynamic.visibility, lock = True)
		
		
		
		#Add Custom attributes to manip dynamic
		#----------------------------------------------------
		
		#Custom Divider
		pm.addAttr(self.manip_dynamic, ln = '_', at='enum', en = 'Custom', h = False, k = True, r = True)
		pm.setAttr(self.manip_dynamic._ , lock = True)
		
		
		#Dynamics
		pm.addAttr(self.manip_dynamic, ln = '__', at='enum', en = 'Dynamics', h = False, k = True, r = True)
		pm.setAttr(self.manip_dynamic.__ , lock = True)
		
		pm.addAttr(self.manip_dynamic, ln = 'simMethod', at='enum', en = 'Off:Static:Dynamic:All', h = False, k = True, r = True)
		pm.addAttr(self.manip_dynamic,ln = 'solverIterations', at='long', defaultValue= 4, h = False, k = True, r = True, minValue = 0)
		pm.addAttr(self.manip_dynamic,ln = 'gravity', at='float', defaultValue= 0.98, h = False, k = True, r = True)
		pm.addAttr(self.manip_dynamic,ln = 'stiffness', at='float', defaultValue= 0.2, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		pm.addAttr(self.manip_dynamic,ln = 'startCurveAttract', at='float', defaultValue= 0.1, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		pm.addAttr(self.manip_dynamic,ln = 'damp', at='float', defaultValue= 0.05, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		pm.addAttr(self.manip_dynamic,ln = 'drag', at='float', defaultValue= 0.05, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		
		pm.addAttr(self.manip_dynamic,ln = 'turbulenceIntensity', at='float', defaultValue= 0.0, h = False, k = True, r = True, minValue=0.0)
		pm.addAttr(self.manip_dynamic,ln = 'turbulenceFrequency', at='float', defaultValue= 1.0, h = False, k = True, r = True, minValue=0.0)
		pm.addAttr(self.manip_dynamic,ln = 'turbulenceSpeed', at='float', defaultValue= 1.0, h = False, k = True, r = True, minValue=0.0)
		
		
		
		#Weighting
		pm.addAttr(self.manip_dynamic, ln = '___', at='enum', en = 'Weighting', h = False, k = True, r = True)
		pm.setAttr(self.manip_dynamic.___ , lock = True)
		
		pm.addAttr(self.manip_dynamic,ln = 'manualDynamicBlend', at='float', defaultValue= 0.0, h = False, k = True, r = True, minValue=0.0, maxValue=1.0)
		
		
		
	
	
	
	
		
	#createSplineCurveBoundJoints
	def createSplineCurveBoundJoints(self):
		
		pm.select(cl = True)
		
		#Spline Ik Joint Lists
		self.splineIkBoundJointsList = []
		self.splineIkBoundJointsGrpList = []
		
		#Iterate lowresCurve Coords List and create joint for each
		for index in range(len(self.lowResCurveCoordList)):
			
			pm.select(cl = True)
			
			#jointName
			jointName = self.prefix + '_ik_spline_bound_j_' + str(index + 1)
			if( index == 0 ): jointName = self.prefix + '_ik_spline_bound_j_' + 'base'
			if( index + 1 == len(self.lowResCurveCoordList) ): jointName = self.prefix + '_ik_spline_bound_j_' + 'tip'
		
			#Create joint
			pm.select(cl = True)
			joint = pm.joint(a = True, p = (0,0,0) , co = True, n = jointName)
			pm.select(cl = True)
			
			#create joint_grp
			joint_grp = pm.group(n = jointName + '_grp')
			pm.select(cl = True)
			pm.parent(joint, joint_grp)
			pm.select(cl = True)
			#translate joint_grp
			joint_grp.translate.set(self.lowResCurveCoordList[index])
			pm.select(cl = True)
			
			
			#Append to splineIkBoundJointsList and splineIkBoundJointsGrpList
			self.splineIkBoundJointsList.append(joint)
			self.splineIkBoundJointsGrpList.append(joint_grp)
			pm.select(cl = True)
			
			
		
		#Create top grp
		self.splineIkBoundJointsTopGrp = pm.group(n = self.prefix + '_spline_ik_joints_top_grp')
		pm.select(cl = True)
		pm.parent(self.splineIkBoundJointsGrpList, self.splineIkBoundJointsTopGrp)
		pm.select(cl = True)
		
	
	
	
	#createSkinclusterAndSplineIk
	def createSkinclusterAndSplineIk(self):
		
		#Skincluster
		#----------------------------------------------------
		
		pm.select(cl = True)
	
		self.bound_curve_skincluster = pm.skinCluster( self.splineIkBoundJointsList , self.lowResCurveTrans ,tsb=True, n = self.prefix + '_bound_curve_skincluster', rui = False, ih = True)
		
		pm.select(cl = True)
		
		
		
		#Spline Ik
		#----------------------------------------------------
		
		pm.select( cl = True )
		
		#Create spline IK
		self.bound_curve_spline_ik = pm.ikHandle( sj= self.ikSplineJointsList[0] , ee= self.ikSplineJointsList[-1] , roc = True, n = self.prefix + '_ikSplineHandle_bound_curve', c = self.lowResCurveTrans, ccv = False, pcv = False, sol = 'ikSplineSolver' )[0]
		pm.select( cl = True )
		
		#Group Spline_ik
		self.bound_curve_spline_ik_grp = pm.group(self.bound_curve_spline_ik ,  n= self.prefix + '_ikSplineHandle_bound_curve_grp' )
		
		pm.select(cl = True)
	
	
	
	
	#createHairSystemForDynamicCurve
	def createHairSystemForDynamicCurve(self):
		
		#Select dynamicCurve
		pm.select(cl = True)
		pm.select(self.highResCurveTrans, r = True)
		
		#makeCurveDynamic
		pm.runtime.MakeCurvesDynamic()
		pm.select(cl = True)
		
		
		#get Hairsystem and Follicle
		#----------------------------------------------------
		futureListDynamicCurve = pm.listHistory(self.highResCurveTrans.getShape(), future = True, af = True)
		
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
	
	
	
	
	
	
	#connectManipDynamicToHairSystemAttributes
	def connectManipDynamicToHairSystemAttributes(self):
		
		pm.select(cl = True)
		
		#Connect manip dynamic attributes to hairSys
		pm.connectAttr(self.manip_dynamic.simMethod, self.dynamicHairsystem.simulationMethod, f = True)
		pm.connectAttr(self.manip_dynamic.solverIterations, self.dynamicHairsystem.iterations, f = True)
		pm.connectAttr(self.manip_dynamic.gravity, self.dynamicHairsystem.gravity, f = True)
		pm.connectAttr(self.manip_dynamic.stiffness, self.dynamicHairsystem.stiffness, f = True)
		pm.connectAttr(self.manip_dynamic.startCurveAttract, self.dynamicHairsystem.startCurveAttract, f = True)
		pm.connectAttr(self.manip_dynamic.damp, self.dynamicHairsystem.damp, f = True)
		pm.connectAttr(self.manip_dynamic.drag, self.dynamicHairsystem.drag, f = True)
		
		pm.connectAttr(self.manip_dynamic.turbulenceIntensity, self.dynamicHairsystem.turbulenceStrength, f = True)
		pm.connectAttr(self.manip_dynamic.turbulenceFrequency, self.dynamicHairsystem.turbulenceFrequency, f = True)
		pm.connectAttr(self.manip_dynamic.turbulenceSpeed, self.dynamicHairsystem.turbulenceSpeed, f = True)
		
		pm.select(cl = True)
	
	
	
	
	
	
	#createDynamicChainSplineIk
	def createDynamicChainSplineIk(self):
		
		pm.select( cl = True )
		
		#Create spline IK
		self.dynamicChain_spline_ik = pm.ikHandle( sj= self.ikDynamicJointsList[0] , ee= self.ikDynamicJointsList[-1] , roc = True, n = self.prefix + '_ikSplineHandle_dynamic_chain', c = self.dynamicOutputCurve, ccv = False, pcv = False, sol = 'ikSplineSolver' )[0]
		pm.select( cl = True )
		
		#Group Spline_ik
		self.dynamicChain_spline_ik_grp = pm.group(self.dynamicChain_spline_ik ,  n= self.prefix + '_ikSplineHandle_dynamic_chain_grp' )
		
		pm.select(cl = True)
		
		
	
	#createManipulatorConstraints
	def createManipulatorConstraints(self):
		
		pm.select(cl = True)
		
		#manipIkSplineGrpList
		for manipIkSplineGrp in self.manipIkSplineGrpList:
			pm.select(cl = True)
			pm.parentConstraint(self.manip_master, manipIkSplineGrp, mo = True)
			pm.scaleConstraint(self.manip_master, manipIkSplineGrp, mo = True)
			pm.select(cl = True)
			
		
		#splineIkBoundJointsGrpList
		for index in range(len(self.splineIkBoundJointsGrpList)):
			pm.select(cl = True)
			pm.parentConstraint(self.manipIkSplineList[index], self.splineIkBoundJointsGrpList[index], mo = True)
			pm.scaleConstraint(self.manipIkSplineList[index], self.splineIkBoundJointsGrpList[index], mo = True)
			pm.select(cl = True)
			
		
		#ikSplineJointsGrp
		pm.select(cl = True)
		pm.parentConstraint(self.manip_master, self.ikSplineJointsGrp, mo = True)
		pm.scaleConstraint(self.manip_master, self.ikSplineJointsGrp, mo = True)
		pm.select(cl = True)
		
		
		#ikDynamicJointsGrp
		pm.select(cl = True)
		pm.parentConstraint(self.manip_master, self.ikDynamicJointsGrp, mo = True)
		pm.scaleConstraint(self.manip_master, self.ikDynamicJointsGrp, mo = True)
		pm.select(cl = True)
		
		
		#boundJointsGrp
		pm.select(cl = True)
		pm.parentConstraint(self.manip_master, self.boundJointsGrp, mo = True)
		pm.scaleConstraint(self.manip_master, self.boundJointsGrp, mo = True)
		pm.select(cl = True)
		
		
		#dynamicHairsystemFollicleGrp
		pm.select(cl = True)
		pm.parentConstraint(self.manip_master, self.dynamicHairsystemFollicleGrp, mo = True)
		pm.scaleConstraint(self.manip_master, self.dynamicHairsystemFollicleGrp, mo = True)
		pm.select(cl = True)
		
		
		#manip_dynamic_grp
		pm.select(cl = True)
		pm.parentConstraint(self.manip_master, self.manip_dynamic_grp, mo = True)
		pm.scaleConstraint(self.manip_master, self.manip_dynamic_grp, mo = True)
		pm.select(cl = True)
		
		
		
		
	#createBoundJointConstraintsAndConnectVisibility
	def createBoundJointConstraintsAndConnectVisibility(self):
		
		pm.select(cl = True)
		
		#bound joint constraint list
		self.boundJointConstraintList = []
		
		#iterate bound joint list and create orient constraint for each
		for index in range(len(self.boundJointsList)):
			pm.select(cl = True)
			self.boundJointConstraintList.append(pm.orientConstraint(self.ikSplineJointsList[index], self.ikDynamicJointsList[index], self.boundJointsList[index], mo = True))
			pm.select(cl = True)
			
		
		#create reverse node
		self.orientConstraintWeight_reverse = pm.createNode('reverse')
		pm.select(cl = True)
		
		#connect to manip dynamic blend
		self.manip_dynamic.manualDynamicBlend >> self.orientConstraintWeight_reverse.inputX
		pm.select(cl = True)
			
		#Connect Constraints to manip_dynamic
		for index in range(len(self.boundJointConstraintList)):
			pm.select(cl = True)
			pm.connectAttr(self.orientConstraintWeight_reverse.outputX, self.boundJointConstraintList[index].name() +'.' +self.ikSplineJointsList[index].name() +'W0', f = True)
			pm.connectAttr(self.manip_dynamic.manualDynamicBlend, self.boundJointConstraintList[index].name() +'.' +self.ikDynamicJointsList[index].name() +'W1', f = True)
			pm.select(cl = True)
	
	
		
		
		#Visibility
		self.orientConstraintWeight_reverse.outputX >> self.manipIkSplineTopGrp.visibility
			
	
	
	
	
	
	
	
	
	
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
		pm.parent(self.dynamicChain_spline_ik_grp, self.bound_curve_spline_ik_grp, self.hairsystemNodesGrp, self.lowResCurveTrans, self.nodesGrp)
		pm.select(cl = True)
		
		#manipsGrp
		pm.parent(self.manip_dynamic_grp, self.manipIkSplineTopGrp, self.manip_master_grp, self.manipsGrp)
		pm.select(cl = True)
		
		#jointsGrp
		pm.parent(self.splineIkBoundJointsTopGrp, self.boundJointsGrp, self.ikSplineJointsGrp, self.ikDynamicJointsGrp, self.jointsGrp)
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
pm.select(cl = True)

#load new scene without saving
pm.mel.eval('file -f -new;')

#CREATE CURVES
pm.select(cl = True)
pm.playbackOptions(maxTime = 1000, e = True)

#Create lowRes Curve
lowResCurve =  pm.curve( p=[(-5.242, 10.576, 0), (-11.457, 11.245, 0), (-15.41, 3.723, 0), (-14.198, -1.95, 0)], ws = True, d = 2 )
pm.select(cl = True)
pm.rename(lowResCurve, 'lowResCurve')
pm.select(cl = True)

#Create highRes Curve
highResCurve =  pm.curve( p=[(-5.274, 10.64, 0), (-7.76, 10.703, 0), (-9.736, 10.448, 0), (-12.159, 9.269, 0), (-13.784, 7.07, 0), (-14.358, 5.094, 0), (-14.708, 2.321, 0), (-14.549, -0.00557, 0), (-14.198, -2.013, 0)], ws = True, d = 2 )
pm.select(cl = True)
pm.rename(highResCurve, 'highResCurve')
pm.select(cl = True)

pm.select([lowResCurve,highResCurve])
'''


'''
#CREATE CHAIN FROM CURVES

#Import 
from rugbyBugs.maya.rbRigging import rbDynamicChainFromCurves
doReload = True
if(doReload): reload(rbDynamicChainFromCurves)


#createInstance
rbDynamicChainFromCurvesInstance = rbDynamicChainFromCurves.RbDynamicChainFromCurves()
#create Rig
rbDynamicChainFromCurvesInstance.createDynamicChainFromCurves(prefix = 'Test')
'''
	
	
	