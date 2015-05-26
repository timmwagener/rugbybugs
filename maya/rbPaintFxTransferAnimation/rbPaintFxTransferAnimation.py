




#rbPaintFxTransferAnimation Module
#------------------------------------------------------------------

'''
Description:
Transferes animation from the alembic cached geo to the hair setup geo by either connecting to the alembic node 
or by auto creating blendshapes (UV independent)
'''

'''
ToDo:

'''




#Imports
#------------------------------------------------------------------
import pymel.core as pm







#RbPaintFxTransferAnimation class
#------------------------------------------------------------------

class RbPaintFxTransferAnimation():
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		
		


	
	
	#TopLevel Methods
	#------------------------------------------------------------------
	
	
	#connectToAlembicCache
	def connectToAlembicCache(self, namespace = ''):
		
		#get SelectionList
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		pm.select(cl = True)
		
		#check if objects are selected
		if not(selectionList):
			if(self.verbose): print('No objects selected, please select at least one object.')
			return None
			
		#Check if namespace is valid
		if not(namespace in self.getNamespaces()):
			if(self.verbose): print('Picked namespace does not exists anymore. Please refresh namespace list')
			return None
		
		
		
		
		#Connect to alembic node
		
		
		#Iterate through selectionList and connect same object plus namespace to alembic cache node if possible
		for masterTrans in selectionList:
			
			#getShape
			masterShape = masterTrans.getShape()
			
			#check if masterShape inMesh Attr connected to Alembic
			if not(pm.nodeType(pm.listConnections(masterShape.inMesh, s = True)[0]) == 'AlembicNode'):
				if(self.verbose): print(masterTrans.name() +' inMesh Attribute not connected to Alembic node. Continuing...')
				continue
				
			#Check if namespace + masterTrans object exists
			if not(pm.objExists(namespace +':' +masterTrans.name().split(':')[-1])):
				if(self.verbose): print(namespace +':' +masterTrans.name().split(':')[-1] +' does not exist. Continuing...')
				continue
				
			
			#Connect Object to Alembic Node
			connectioSourceAttr = pm.listConnections(masterShape.inMesh, s = True, p = True)[0]
			connectionDestinationAttr = namespace +':'  +masterShape.name().split(':')[-1] +'.inMesh'
			pm.connectAttr(connectioSourceAttr, connectionDestinationAttr,f = True)
		
		
		
		#Success Msg
		if(self.verbose): print('Successfully connected PaintFx Hair Geo to Alembic Cache')
		
		
		
		
	#transferAnimationByBlendshapes
	def transferAnimationByBlendshapes(self, namespace = '' ):
		
		#get SelectionList
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		pm.select(cl = True)
		
		#check if objects are selected
		if not(selectionList):
			if(self.verbose): print('No objects selected, please select at least one object.')
			return None
			
		#Check if namespace is valid
		if not(namespace in self.getNamespaces()):
			if(self.verbose): print('Picked namespace does not exists anymore. Please refresh namespace list')
			return None
			
			
		
		#Transfer Animation by blendshapes
		
		#Iterate through selectionList and create blendshape deformer for equal base and target objects
		for masterTrans in selectionList:
			
			#getShape
			masterShape = masterTrans.getShape()
			
			'''
			#SKIP ALEMBIC CONNECTION CHECK - NOT NECCESSARY FOR BLENDSHAPES 
			
			#check if masterShape inMesh Attr connected to Alembic
			if not(pm.nodeType(pm.listConnections(masterShape.inMesh, s = True)[0]) == 'AlembicNode'):
				if(self.verbose): print(masterTrans.name() +' inMesh Attribute not connected to Alembic node. Continuing...')
				continue
			'''
				
			#Check if namespace + masterTrans object exists
			if not(pm.objExists(namespace +':' +masterTrans.name().split(':')[-1])):
				if(self.verbose): print(namespace +':' +masterTrans.name().split(':')[-1] +' does not exist. Continuing...')
				continue
				
				
			#create blendshape
			targetName = namespace +':' +masterTrans.name().split(':')[-1]
			blendshapeDeformer = pm.blendShape(masterTrans.name(), targetName, foc = True)
			pm.select(cl = True)
			pm.blendShape(blendshapeDeformer, edit = True, w = (0, 1.0))
			pm.select(cl = True)
		
		
		#Success Msg
		if(self.verbose): print('Successfully connected PaintFx Hair Geo to Alembic Cache Geo by blendshapes.')
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------
	
	
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
		
		return namespacesList
		
		
	
	
	
		
		
		
		

		
		
		
#Test Execution
#------------------------------------------------------------------







	
	
