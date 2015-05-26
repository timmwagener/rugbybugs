




#rbCreateShadowPass Module
#------------------------------------------------------------------

'''
Description:
Creates a Shadow Pass VrayRenderElement according to our pipeline standards
'''

'''
ToDo:

'''




#Imports
#------------------------------------------------------------------
import pymel.core as pm
import maya.OpenMaya as openMaya







#RbCreateShadowPass class
#------------------------------------------------------------------

class RbCreateShadowPass():
	
	#Constructor / Main Procedure
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		
		
	
	#Top Level Methods
	#------------------------------------------------------------------
	
	#createShadowPass
	def createShadowPass(self, setStatusFunction = False):
		
		
		
		#Check if Vray Loaded, else set Status and return
		if not(self.vrayLoaded(setStatusFunction)): return None
		
		
		
		#rawShadowRE
		attrName = 'vray_name_rawshadow'
		attrValue = 'rbRawShadow'
		if not(self.REWithAttrAndValueExists(attrName, attrValue)): self.createRawShadowRE()
		
		#shadowRE
		attrName = 'vray_name_shadow'
		attrValue = 'rbShadow'
		if not(self.REWithAttrAndValueExists(attrName, attrValue)): self.createShadowRE()
		
		
		
		
		#setStatus
		if(setStatusFunction): setStatusFunction('Shadow pass created successfully')
	
	
	
	
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	
	#createRawShadowRE
	def createRawShadowRE(self):
		
		#create raw shadow RE
		rawShadowRE = self.createRenderElement('rawShadowChannel')
		pm.rename(rawShadowRE, 'rbRawShadow')
		
		#SetAttrs on rawShadowRE
		pm.setAttr(rawShadowRE.vray_name_rawshadow, 'rbRawShadow')
		
		#verbose
		if(self.verbose): print('Raw Shadow RE created')
		
		
		
	#createShadowRE
	def createShadowRE(self):
		
		#create shadow RE
		shadowRE = self.createRenderElement('shadowChannel')
		pm.rename(shadowRE, 'rbShadow')
		
		#SetAttrs on shadowRE
		pm.setAttr(shadowRE.vray_name_shadow, 'rbShadow')
		
		#verbose
		if(self.verbose): print('Shadow RE created')
		
		
	
	
	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------
	
	
	#REWithAttrAndValueExists
	def REWithAttrAndValueExists(self, attrName, attrValue):
		
		#List all nodes of Type VRayRenderElement
		REList = pm.ls(fl = True, typ = 'VRayRenderElement')
		
		#if list < 1 return False (no RE in scene, ready to create)
		if not(REList): return False
		
		#if list larger check if REName in list of RElements
		for RE in REList:
			#check if RE has attr of attrName and if return True
			try:
				if(pm.getAttr(RE.name() +'.' +attrName) == attrValue): return True
			except:
				pass
		
		#Else False (ready to create)
		return False
	
	
	
	#createRenderElement
	def createRenderElement(self, renderElementName):
		
		#clear Selection
		pm.select(cl = True)
		
		#build MEL Cmd
		createRElementMELCmd = 'vrayAddRenderElement ' +renderElementName +';'
		
		#Execute
		pm.mel.eval(createRElementMELCmd)
		
		#return created RenderElementNode
		renderElement = pm.ls(sl = True, fl = True)[0]
		pm.select(cl = True)
		
		return renderElement
		
	
	#createRamp
	def createRamp(self, rampDirection = 1):
		
		#rampDirection 1 = u, 0 = v
		
		#clear selection
		pm.select(cl = True)
		#createRamp
		ramp = pm.createNode('ramp')
		pm.setAttr(ramp.name() +'.type' , rampDirection)
		pm.select(cl = True)
		#createUVCoords
		place2dTexture = pm.createNode('place2dTexture')
		pm.rename(place2dTexture, 'rbSTMapPlace2dTextureNode')
		pm.select(cl = True)
		#connections
		place2dTexture.outUV >> ramp.uvCoord
		place2dTexture.outUvFilterSize >> ramp.uvFilterSize
		pm.select(cl = True)
		
		return ramp
		
		
	#vrayLoaded
	def vrayLoaded(self, setStatusFunction = False):
		#Get list of all loaded plugIns
		plugInList = pm.pluginInfo( query=True, listPlugins=True )
		
		#Return true if loaded else setStatus and return false
		if('vrayformaya' in plugInList): return True
		
		if(setStatusFunction): setStatusFunction('Vray for Maya Plugin not loaded')
		return False
	
	
	
	
	