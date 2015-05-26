




#rbChrystalGuiFunctionality Module
#------------------------------------------------------------------

'''
Functionality for chrystal gui
'''

'''
ToDo:

'''


#Imports
#------------------------------------------------------------------
import pymel.core as pm









#RbChrystalGuiFunctionality class
#------------------------------------------------------------------
class RbChrystalGuiFunctionality:
	
	
	#Constructor
	#------------------------------------------------------------------
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		
		self.verbose = True
		
		#piecesCount
		self.piecesCount = 51
	
	
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	
	
	
	
	
	
	
	#SELECTION
	#------------------------------------------------------------------
	
	#selectAllPieceManipulators
	def selectAllPieceManipulators(self, namespaceString):
		
		pm.select(cl = True)
		
		#check if namespace is root
		if(namespaceString == 'root'): namespaceString = ''
		
		#select manips
		for index in range(self.piecesCount):
			try:
				pm.select(namespaceString +':' +'manip_piece_' +str(index), add = True)
			except:
				if(self.verbose): print('Error selecting ' +namespaceString +':' +'manip_piece_' +str(index))
				
	
	
	#selectPieceManipulator
	def selectPieceManipulator(self, namespaceString, index, additiveMode):
		
		#check if namespace is root
		if(namespaceString == 'root'): namespaceString = ''
		
		#try selection, else print error
		try:
			
			if(additiveMode):pm.select(namespaceString +':' +'manip_piece_' +str(index), add = True)
			else:
				pm.select(cl = True)
				pm.select(namespaceString +':' +'manip_piece_' +str(index), r = True)
		except:
			if(self.verbose): print('Error selecting ' +namespaceString +':' +'manip_piece_' +str(index))
			
	




	
	
	#ZERO SELECTION
	#------------------------------------------------------------------
	
	#zeroSelectedManipulators
	def zeroSelectedManipulators(self):
		
		
		#get selectionList
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		
		#check if something is selected
		if not(selectionList):
			if(self.verbose): print('Empty Selection')
			return None
			
		pm.select(cl = True)
		
		#iterate selectionList and set translate, rotate and scale to 0 if manip check successfull
		for transformNode in selectionList:
			
			try:
				transformNode.translate.set(0,0,0)
				transformNode.rotate.set(0,0,0)
				transformNode.scale.set(1,1,1)
				
				if(self.verbose): print('Successfully reset ' +transformNode.name())
			except:
				if(self.verbose): print('Error zeroing transform node ' +transformNode.name())
	
	
		#Redo selection
		pm.select(selectionList, r = True)
	
	
	
	
	
	
	
	#PARENTSPACE
	#------------------------------------------------------------------
	
	
	#switchParentspace
	def switchParentspace(self, weightChrystal = 1, weightWorld = 0, weightWildcard1 = 0 , weightWildcard2 = 0 , weightWildcard3 = 0 , weightWildcard4 = 0):
		
		#get selectionList
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		
		pm.select(cl = True)
		
		#check if something is selected
		if not(selectionList):
			if(self.verbose): print('Empty Selection')
			return None
			
		
		#Iterate selectionList and set parentConstraint weights
		for transformNode in selectionList:
			
			try:
				
				#Get transform matrix of transformNode in ws
				transformMatrixWs = pm.xform(transformNode, q = True, m = True, ws = True)
				
				
				#get ParentConstraint
				try:
					parentspaceConstraint = pm.listRelatives(transformNode.getParent().getParent(), typ = 'parentConstraint')[0]
				except:
					if(self.verbose): print('Parentspace Constraint not found for object ' +transformNode.name() +'. Continuing...')
					continue
				
				
				#Set Weightvalues
				pm.setAttr(parentspaceConstraint.chrystal_master_jW0, weightChrystal)
				pm.setAttr(parentspaceConstraint.world_parent_dummy_locW1, weightWorld)
				pm.setAttr(parentspaceConstraint.manip_wildcard_1W2 , weightWildcard1)
				pm.setAttr(parentspaceConstraint.manip_wildcard_2W3 , weightWildcard2)
				pm.setAttr(parentspaceConstraint.manip_wildcard_3W4 , weightWildcard3)
				pm.setAttr(parentspaceConstraint.manip_wildcard_4W5 , weightWildcard4)
				
				#set transformation back
				pm.xform(transformNode, m = transformMatrixWs, ws = True)
				
				#Verbose
				if(self.verbose): print('Succesfully switched parentspaces for node: ' +transformNode.name())
				
				
			except:
				if(self.verbose): print('Error settings weights for selected node: ' +transformNode.name())
	
		
		#Redo selection
		pm.select(selectionList, r = True)
	
	
	
	
	#selectSpecialManipulator
	def selectSpecialManipulator(self, namespaceString, manipName):
		
		pm.select(cl = True)
		
		#check if namespace is root
		if(namespaceString == 'root'): namespaceString = ''
		
		#try selection, else print error
		try:
			pm.select(namespaceString +':' +manipName , r = True)
		except:
			if(self.verbose): print('Error selecting ' +namespaceString +':' +manipName)
			
			
	
	
	
	
	#keyframeParentspaceForSelectedManipulators
	def keyframeParentspaceForSelectedManipulators(self):
		
		#get selectionList
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		
		pm.select(cl = True)
		
		#check if something is selected
		if not(selectionList):
			if(self.verbose): print('Empty Selection')
			return None
			
		
		#Iterate selectionList and set parentConstraint weights
		for transformNode in selectionList:
			
			try:
				#get ParentConstraint
				try:
					parentspaceConstraint = pm.listRelatives(transformNode.getParent().getParent(), typ = 'parentConstraint')[0]
				except:
					if(self.verbose): print('Parentspace Constraint not found for object ' +transformNode.name() +'. Continuing...')
					continue
				
				
				#keyframe
				pm.setKeyframe(parentspaceConstraint, at = 'chrystal_master_jW0', t = pm.currentTime())
				pm.setKeyframe(parentspaceConstraint, at = 'world_parent_dummy_locW1', t = pm.currentTime())
				pm.setKeyframe(parentspaceConstraint, at = 'manip_wildcard_1W2', t = pm.currentTime())
				pm.setKeyframe(parentspaceConstraint, at = 'manip_wildcard_2W3', t = pm.currentTime())
				pm.setKeyframe(parentspaceConstraint, at = 'manip_wildcard_3W4', t = pm.currentTime())
				pm.setKeyframe(parentspaceConstraint, at = 'manip_wildcard_4W5', t = pm.currentTime())
				
				#Verbose
				if(self.verbose): print('Succesfully keyframed weighting for node: ' +transformNode.name())
				
				
			except:
				if(self.verbose): print('Error keyframing weights for selected node: ' +transformNode.name())
	
		
		#Redo selection
		pm.select(selectionList, r = True)
		
	
	
	#selectParentConstraintForSelectedManipulators
	def selectParentConstraintForSelectedManipulators(self):
		
		#get selectionList
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		
		pm.select(cl = True)
		
		#check if something is selected
		if not(selectionList):
			if(self.verbose): print('Empty Selection')
			return None
			
		
		#Iterate selectionList and select parent constraints
		for transformNode in selectionList:
			
			try:
				
				#get ParentConstraint
				try:
					parentspaceConstraint = pm.listRelatives(transformNode.getParent().getParent(), typ = 'parentConstraint')[0]
				except:
					if(self.verbose): print('Parentspace Constraint not found for object ' +transformNode.name() +'. Continuing...')
					continue
				
				
				pm.select(parentspaceConstraint, add = True)
				
				#Verbose
				if(self.verbose): print('Succesfully selected parent constraint for node: ' +transformNode.name())
				
				
			except:
				if(self.verbose): print('Error selecting parent constraint for selected node: ' +transformNode.name())
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	#VISIBILITY
	#------------------------------------------------------------------
	
	
	
	#togglePieceVisibility
	def togglePieceVisibility(self, namespaceString):
		
		
		
		#check if namespace is root
		if(namespaceString == 'root'): namespaceString = ''
		
		#check if namespace is root
		if not(namespaceString):
			if(self.verbose): print('Please select namespace different from root')
			return None
		
		
		
		#get selectionList
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		
		#check if something is selected
		if not(selectionList):
			if(self.verbose): print('Empty Selection')
			return None
		
		
		
		
		#iterate selectionList
		for transformNode in selectionList:
			
			#check if object is piece manip
			
			#check parent
			#get ParentConstraint
			try:
				parentspaceConstraint = pm.listRelatives(transformNode.getParent().getParent(), typ = 'parentConstraint')[0]
			except:
				if(self.verbose): print('Parentspace Constraint not found for object ' +transformNode.name() +'. Continuing...')
				continue
			
				
			#check for name
			if not(transformNode.name().split(':')[-1].split('_')[0] +'_'  +transformNode.name().split(':')[-1].split('_')[1] == 'manip_piece'):
				if(self.verbose): print('Name of selected transform node ' +transformNode.name() +' does not match manipulator name for pieces. Continuing...')
				continue
				
			
			
			#If succesfully managed checks execute viz toggle
			#get index of selected manip
			manipPieceIndex = transformNode.name().split(':')[-1].split('_')[-1]
			
			#grpList
			grpList = ['innerHull_grp', 'outerHull_grp', 'intermediary_grp']
			
			#Iterate grpList
			for groupName in grpList:
			
				try:
				
					#Check if topGrp exists
					if not(pm.objExists(namespaceString +':' +groupName)):
						if(self.verbose): print('Object ' +namespaceString +':' +groupName +' does not exists. Continuing')
						continue
					
					#get piecesTopGrp
					piecesTopGrp = pm.PyNode(namespaceString +':' +groupName)
					
					#get piece_grp and toggle viz
					for pieceGrp in piecesTopGrp.getChildren():
						if(pieceGrp.name().split(':')[-1] == 'piece_' +manipPieceIndex):self.toggleVisibility(pieceGrp)
					
					#success msg
					if(self.verbose): print('Succesfully toggled visibility for piece_' +manipPieceIndex +' in ' +namespaceString +':' +groupName +'. Continuing...')
					
				except:
					if(self.verbose): print('Error toggling visibility for piece_' +manipPieceIndex +'in ' +namespaceString +':' +groupName +'. Continuing...')
			
			
			
	
	
	
	#unhideAllPieces
	def unhideAllPieces(self, namespaceString):
		
		#check if namespace is root
		if(namespaceString == 'root'): namespaceString = ''
		
		#check if namespace is root
		if not(namespaceString):
			if(self.verbose): print('Please select namespace different from root')
			return None
		
		#grpList
		grpList = ['innerHull_grp', 'outerHull_grp', 'intermediary_grp']
		
		#Iterate grpLIst and unhide pieces
		for groupName in grpList:
			
			try:
				
				#Check if topGrp exists
				if not(pm.objExists(namespaceString +':' +groupName)):
					if(self.verbose): print('Object ' +namespaceString +':' +groupName +' does not exists. Continuing')
					continue
				
				#get piecesTopGrp
				piecesTopGrp = pm.PyNode(namespaceString +':' +groupName)
				
				#get piece_grp and unhide it
				for pieceGrp in piecesTopGrp.getChildren():
					pieceGrp.visibility.set(True)
				
				#success msg
				if(self.verbose): print('Succesfully unhid all pieces in ' +piecesTopGrp.name() +'. Continuing...')
				
			except:
				if(self.verbose): print('Error unhiding pieces in ' +namespaceString +':' +groupName +'. Continuing...')
				
			
		
	
	
	
	
	
	
	
	
	
	
	
	#SMOOTH MESH PREVIEW
	#------------------------------------------------------------------
	
	#toggleSmoothMeshPreviewForSelected
	def toggleSmoothMeshPreviewForSelected(self, namespaceString):
		
		#check if namespace is root
		if(namespaceString == 'root'): namespaceString = ''
		
		#check if namespace is root
		if not(namespaceString):
			if(self.verbose): print('Please select namespace different from root')
			return None
		
		
		
		#get selectionList
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		
		#check if something is selected
		if not(selectionList):
			if(self.verbose): print('Empty Selection')
			return None
		
		
		
		
		#iterate selectionList
		for transformNode in selectionList:
			
			#check if object is piece manip
			
			#check parent
			#get ParentConstraint
			try:
				parentspaceConstraint = pm.listRelatives(transformNode.getParent().getParent(), typ = 'parentConstraint')[0]
			except:
				if(self.verbose): print('Parentspace Constraint not found for object ' +transformNode.name() +'. Continuing...')
				continue
			
				
			#check for name
			if not(transformNode.name().split(':')[-1].split('_')[0] +'_'  +transformNode.name().split(':')[-1].split('_')[1] == 'manip_piece'):
				if(self.verbose): print('Name of selected transform node ' +transformNode.name() +' does not match manipulator name for pieces. Continuing...')
				continue
				
			
			
			#If succesfully managed checks execute viz toggle
			#get index of selected manip
			manipPieceIndex = transformNode.name().split(':')[-1].split('_')[-1]
			
			#grpList
			grpList = ['intermediary_grp']
			
			#Iterate grpList
			for groupName in grpList:
			
				try:
				
					#Check if topGrp exists
					if not(pm.objExists(namespaceString +':' +groupName)):
						if(self.verbose): print('Object ' +namespaceString +':' +groupName +' does not exists. Continuing')
						continue
					
					#get piecesTopGrp
					piecesTopGrp = pm.PyNode(namespaceString +':' +groupName)
					
					#iterate children of piecesTopGrp
					for pieceGrp in piecesTopGrp.getChildren():
						
						#if name of child matches index get execute smooth mesh toggle
						if(pieceGrp.name().split(':')[-1] == 'piece_' +manipPieceIndex):
							
							#iterate list of transform children
							for pieceGrpChild in pm.listRelatives(pieceGrp, typ = 'transform'):
								#toggleSmoothMeshPreview
								self.toggleSmoothMeshPreview(pieceGrpChild)
							
						
					
					#success msg
					if(self.verbose): print('Succesfully toggled smooth mesh preview for piece_' +manipPieceIndex +' in ' +namespaceString +':' +groupName +'. Continuing...')
					
				except:
					if(self.verbose): print('Error toggling smooth mesh preview for piece_' +manipPieceIndex +'in ' +namespaceString +':' +groupName +'. Continuing...')
	
		
	
	
	#unsmoothAll
	def unsmoothAll(self, namespaceString):
		
		#check if namespace is root
		if(namespaceString == 'root'): namespaceString = ''
		
		#check if namespace is root
		if not(namespaceString):
			if(self.verbose): print('Please select namespace different from root')
			return None
		
		
		#grpList
		grpList = ['intermediary_grp']
			
		#Iterate grpList
		for groupName in grpList:
			try:
				#Check if topGrp exists
				if not(pm.objExists(namespaceString +':' +groupName)):
					if(self.verbose): print('Object ' +namespaceString +':' +groupName +' does not exists. Continuing')
					continue
					
				#get piecesTopGrp
				piecesTopGrp = pm.PyNode(namespaceString +':' +groupName)
					
				#iterate children of piecesTopGrp
				for pieceGrp in piecesTopGrp.getChildren():
						
					#iterate list of transform children
					for pieceGrpChild in pm.listRelatives(pieceGrp, typ = 'transform'):
						#switchOffSmoothMeshPreview
						self.switchOffSmoothMeshPreview(pieceGrpChild)
							
						
					
				#success msg
				if(self.verbose): print('Succesfully switched off smooth mesh preview for objects in ' +namespaceString +':' +groupName +'. Continuing...')
					
			except:
				if(self.verbose): print('Error switching off smooth mesh preview for objects in ' +namespaceString +':' +groupName +'. Continuing...')
	
	
	
	
	
	
	
	
	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------	
	
	#toggleVisibility
	def toggleVisibility(self, node):
		
		#Check node status and toggle vis value
		if(node.visibility.get()): node.visibility.set(False)
		else: node.visibility.set(True)
	
	
	
	#toggleSmoothMeshPreview
	def toggleSmoothMeshPreview(self, node):
		
		#if node smooth mesh preview is on then turn off
		if(node.displaySmoothMesh.get() != 0): node.displaySmoothMesh.set(0)
		
		#else
		else:
			#setSmoothmesh Attrs.
			node.displaySmoothMesh.set(2)
			node.smoothLevel.set(2)
			node.smoothUVs.set(1)
			#Smooth borders 0 = Do not smooth, 1 = Smooth internal, 2 = Smooth All
			node.keepMapBorders.set(1)
			node.keepBorder.set(1)
	
	
	#switchOffSmoothMeshPreview
	def switchOffSmoothMeshPreview(self, node):
		node.displaySmoothMesh.set(0)
	
	
	#toggleGroupsVisibility
	def toggleGroupsVisibility(self, namespaceString, grpList):
		
		#check if namespace is root
		if(namespaceString == 'root'): namespaceString = ''
		
		
		#Iterate innerChrystalGrpsList and check if all objects exists
		for groupName in grpList:
			
			#check if innerChrystal Objects exist
			if not(pm.objExists(namespaceString +':' +groupName)):
				if(self.verbose): print('Object ' +namespaceString +':' +groupName +' does not exists. Break...')
				return None
		

		#Iterate again and toggle visibility
		for groupName in grpList:
			
			#else toggle visibility
			self.toggleVisibility(pm.PyNode(namespaceString +':' +groupName))
			pm.select(cl = True)
	
	
	
	#getNamespaces
	def getNamespaces(self):
		
		namespacesList = []
		
		#Check if current namespace is root else set to scene root
		if not(pm.namespaceInfo(isRootNamespace = True)):
			
			#store current namespace
			currentNamespace = pm.namespaceInfo(currentNamespace = True)
			#Set to rootnamespace
			pm.namespace(setNamespace = ':')
			#Query namespaceList
			namespacesList = pm.namespaceInfo(listOnlyNamespaces = True, r = True)
			#Set back to old namespace
			pm.namespace(setNamespace = currentNamespace)
		
		#If namespace is root namespace
		else:
			#Query namespaceList
			namespacesList = pm.namespaceInfo(listOnlyNamespaces = True, r = False)
			
		#Rebuild namespaceList without UI and shared
		namespacesListTmp = []
		
		for namespaceItem in namespacesList:
			if not(namespaceItem == 'UI' or namespaceItem == 'shared'): namespacesListTmp.append(namespaceItem)
		
		namespacesList = namespacesListTmp
		
		#append root
		namespacesList.append('root')
		
		return namespacesList
	
	
