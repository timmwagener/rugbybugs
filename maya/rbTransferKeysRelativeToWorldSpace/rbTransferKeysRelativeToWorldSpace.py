




#rbTransferKeysRelativeToWorldSpace Module
#------------------------------------------------------------------

'''
Description:
Transfers animation from an object in relative space (object with parent transforms) to an object in world space
'''

'''
ToDo:

'''




#Imports
#------------------------------------------------------------------
import pymel.core as pm
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim






#RbTransferKeysRelativeToWorldSpace class
#------------------------------------------------------------------

class RbTransferKeysRelativeToWorldSpace():
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		
		


	
	
	#TopLevel Methods
	#------------------------------------------------------------------
	
	
	#transferKeysRelativeToWorldSpace
	def transferKeysRelativeToWorldSpace(self, bake = False):
		
		#getSelection
		selectedObjectsList = self.getSelection()
		
		#Check if len(selection) == 2, if false print msg and return
		if not(len(selectedObjectsList) == 2):
			if(self.verbose): print('Please select two objects to copy keys')
			return None
		
		#else continue execution
		else:
			
			try:
				
				#getMasterObject
				masterObject = selectedObjectsList[0]
				
				#getTargetObject
				targetObject = selectedObjectsList[1]
				
				
				#check if both objects are of type transform
				if not(pm.nodeType(masterObject) == 'transform'):
					if(self.verbose): print('Master object is not of type transform')
					return None
					
					
				if not(pm.nodeType(targetObject) == 'transform'):
					if(self.verbose): print('Target object is not of type transform')
					return None
				
				
				
				#check if masterObject has animation
				if not(self.getAnimCurveNodeList(masterObject)):
					if(self.verbose): print('Master object has no animation')
					return None
					
				
				
				
				#getAnimCurveNodeList
				animCurveNodeList = self.getAnimCurveNodeList(masterObject)
				if(self.verbose): print('AnimCurve Node List of Master: ' + str(animCurveNodeList))
				
				
				
				#getCurrentAnimationRange
				self.currentAnimationTime = pm.currentTime(q = True)
				
				self.currentAnimationStart = pm.playbackOptions(ast = True, q = True)
				self.currentAnimationEnd = pm.playbackOptions(aet = True, q = True)
				
				self.currentAnimationRangeStart = pm.playbackOptions(minTime = True, q = True)
				self.currentAnimationRangeEnd = pm.playbackOptions(maxTime = True, q = True)
				
				#Get new animation range
				animationStartEndList = self.getAnimationRange(animCurveNodeList)
				self.animationStart = animationStartEndList[0]
				self.animationEnd = animationStartEndList[1]
				
				#setTempNewAnimationRange
				self.setAnimationRange(self.animationStart, self.animationEnd, self.animationStart, self.animationEnd)
				
				
				
				#getKeyList for masterObject
				self.keyList = self.getKeyList(animCurveNodeList)
				if(self.verbose): print('KeyList of Master: ' + str(self.keyList))
				
				#getKeyableAttrList
				self.keyableAttrList = pm.listAttr(targetObject, k = True)
				if(self.verbose): print('Keyable Attr List of Target: ' + str(self.keyableAttrList))
				
				
				
				#if bake == True
				if(bake == True):
					#iterate keyList and set time to key time
					for key in range(0, self.keyList[-1] + 1):
						
						
						pm.select(cl = True)
						
						#set current time to key time
						pm.currentTime(key)
						
						#getTransformMatrixForMaster in Ws
						masterTransformMatrix = pm.xform(masterObject, matrix = True, q = True, ws = True)
						
						#setMasterTransformMatrixOnTarget
						pm.xform(targetObject, matrix = masterTransformMatrix)
						
						#keyframeAllChannelsOnTargetObj
						for channel in self.keyableAttrList:
							pm.setKeyframe(targetObject, at = channel)
				
				
				#else
				else:
					#iterate keyList and set time to key time
					for key in self.keyList:
						
						
						pm.select(cl = True)
						
						#set current time to key time
						pm.currentTime(key)
						
						#getTransformMatrixForMaster in Ws
						masterTransformMatrix = pm.xform(masterObject, matrix = True, q = True, ws = True)
						
						#setMasterTransformMatrixOnTarget
						pm.xform(targetObject, matrix = masterTransformMatrix)
						
						#keyframeAllChannelsOnTargetObj
						for channel in self.keyableAttrList:
							pm.setKeyframe(targetObject, at = channel)
				
				
				
				
				#setAnimationRange back to old
				self.setAnimationRange(self.currentAnimationStart, self.currentAnimationEnd, self.currentAnimationRangeStart, self.currentAnimationRangeEnd)
				
				#set Current time back to old
				pm.currentTime(self.currentAnimationTime)
				
			
			
			except:
				if(self.verbose): print('Error copying keys')
				return None
			
			
		
		#Print Success Msg
		if(self.verbose): print('Successfully transferred keys')
		return None
	
	
	#Methods
	#------------------------------------------------------------------
	
	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------
	
	
	#getSelection
	def getSelection(self):
		
		return pm.ls(sl = True, fl = True)
	
	
	
	
	
	#getAnimCurveNodeList
	def getAnimCurveNodeList(self, object):
		
		pm.select(cl = True)
		
		#get all connections to object
		connectionsList = pm.listConnections(object)
		
		#Check if connectionsList is empty
		if not(connectionsList):
			if(self.verbose): print('Object hast no input coonections')
			return connectionsList
			
		#get animCurveList
		animCurveList = []
		
		#iterate through connectionList and append animcurve nodes
		for node in connectionsList:
			if(pm.nodeType(node) == 'animCurveTU' or pm.nodeType(node) == 'animCurveTL' or pm.nodeType(node) == 'animCurveTA'): animCurveList.append(node)
			
			
		return animCurveList
		
	
	
	
	
	#getAnimationRange
	def getAnimationRange(self, curveAnimNodeList):
		
		#Set initial end and start values from first curveAnimNode
		animationStart = curveAnimNodeList[0].getTime(0)
		animationEnd = curveAnimNodeList[0].getTime(curveAnimNodeList[0].numKeys() - 1)
		
		
		#iterate through curveAnimNodeList and check lowest and highest key times
		for curveAnimNode in curveAnimNodeList:
			
			#check lowest key time value
			if(curveAnimNode.getTime(0) < animationStart): animationStart = curveAnimNode.getTime(0)
			
			#check highest key time value
			if(curveAnimNode.getTime(curveAnimNode.numKeys() - 1) > animationEnd): animationEnd = curveAnimNode.getTime(curveAnimNode.numKeys() - 1)
			
			
		
		return [animationStart, animationEnd]
		
		
	
	
	
	
	#setAnimationRange
	def setAnimationRange(self, startTime, endTime, startRange, endRange):
		
		#setStartTime
		pm.playbackOptions(ast = startTime, e = True)
		pm.playbackOptions(minTime = startRange, e = True)
		
		#setEndTime
		pm.playbackOptions(aet = endTime, e = True)
		pm.playbackOptions(maxTime = endRange, e = True)
		
		
	
	
	
	
	#getKeyList
	def getKeyList(self, curveAnimNodeList):
		
		pm.select(cl = True)
		
		keyList = []
		
		
		#iterate curveAnimNodeList and append all keys time to keyList
		for curveAnimNode in curveAnimNodeList:
			
			
			#get curveAnimMObject 
			curveAnimObject = OpenMaya.MObject()
			
			
			#select current curveAnimNode
			pm.select(cl = True)
			pm.select(curveAnimNode)
			
			#getSelectionList API
			selectionList = OpenMaya.MSelectionList()
			#set selectionList to active selection
			OpenMaya.MGlobal.getActiveSelectionList(selectionList)
			#selectionList iterator
			itSelectionList = OpenMaya.MItSelectionList(selectionList)
			
			pm.select(cl = True)
			
			#traverse selectionList and assign curve anim mobject
			while not(itSelectionList.isDone()):
				
				itSelectionList.getDependNode(curveAnimObject)
				
				itSelectionList.next()
			
			
			#create curveAnim fnSet
			fnCurveAnimObject = OpenMayaAnim.MFnAnimCurve(curveAnimObject)
			
			#iterate
			for index in range(0, fnCurveAnimObject.numKeys()):
				
				#Get time object for index and append to list
				timeObject = fnCurveAnimObject.time(index)
				keyList.append(timeObject.value())
			
			
				
		#remove duplicates and return
		return sorted(list(set(keyList)))
	
	
	
	
	
	
#Execute TMP
#------------------------------------------------------------------
'''
import rbTransferKeysRelativeToWorldSpace
doReload = True
if(doReload): reload(rbTransferKeysRelativeToWorldSpace)
rbTransferKeysRelativeToWorldSpace.RbTransferKeysRelativeToWorldSpace().transferKeysRelativeToWorldSpace()
'''
	
	
