




#rbCreateFrameBufferContributions Module
#------------------------------------------------------------------

'''
Description:
Creates Framebuffer Contributions (Refl., Refr., Spec. etc.) VrayRenderElements according to our pipeline standards
'''

'''
ToDo:

'''




#Imports
#------------------------------------------------------------------
import pymel.core as pm
import maya.OpenMaya as openMaya







#RbCreateFrameBufferContributions class
#------------------------------------------------------------------

class RbCreateFrameBufferContributions():
	
	#Constructor / Main Procedure
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		
		
	
	#Top Level Methods
	#------------------------------------------------------------------
	
	#createFrameBufferContributions
	def createFrameBufferContributions(self, setStatusFunction = False):
		
		
		
		#Check if Vray Loaded, else set Status and return
		if not(self.vrayLoaded(setStatusFunction)): return None
		
		
		
		
		#diffuseRE
		attrName = 'vray_name_rawdiffuse'
		attrValue = 'rbDiffuse'
		if not(self.REWithAttrAndValueExists(attrName, attrValue)): self.createDiffuseRE()
		
		
		#reflectionRE
		attrName = 'vray_name_reflect'
		attrValue = 'rbReflection'
		if not(self.REWithAttrAndValueExists(attrName, attrValue)): self.createReflectionRE()
		
		
		#refractionRE
		attrName = 'vray_name_refract'
		attrValue = 'rbRefraction'
		if not(self.REWithAttrAndValueExists(attrName, attrValue)): self.createRefractionRE()
		
		
		#specularRE
		attrName = 'vray_name_specular'
		attrValue = 'rbSpecular'
		if not(self.REWithAttrAndValueExists(attrName, attrValue)): self.createSpecularRE()
		
		
		#SubsurfaceRE
		attrName = 'vray_name_sss'
		attrValue = 'rbSubsurface'
		if not(self.REWithAttrAndValueExists(attrName, attrValue)): self.createSubsurfaceRE()
		
		
		
		#setStatus
		if(setStatusFunction): setStatusFunction('Frame Buffer Contribution REs created successfully')
	
	
	
	
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	
	
	#Frame Buffer Contribution REs
	#------------------------------------------------------------------
	
	#createDiffuseRE
	def createDiffuseRE(self):
		
		#create diffuse RE
		diffuseRE = self.createRenderElement('diffuseChannel')
		pm.rename(diffuseRE, 'rbDiffuse')
		
		#SetAttrs on diffuseRE
		pm.setAttr(diffuseRE.vray_name_rawdiffuse, 'rbDiffuse')
		
		#verbose
		if(self.verbose): print('Diffuse RE created')
		
		
	
	#createReflectionRE
	def createReflectionRE(self):
		
		#create reflection RE
		reflectionRE = self.createRenderElement('reflectChannel')
		pm.rename(reflectionRE, 'rbReflection')
		
		#SetAttrs on reflectionRE
		pm.setAttr(reflectionRE.vray_name_reflect, 'rbReflection')
		
		#verbose
		if(self.verbose): print('Reflection RE created')
		
		
	
	#createRefractionRE
	def createRefractionRE(self):
		
		#create refractionRE
		refractionRE = self.createRenderElement('refractChannel')
		pm.rename(refractionRE, 'rbRefraction')
		
		#SetAttrs on refractionRE
		pm.setAttr(refractionRE.vray_name_refract, 'rbRefraction')
		
		#verbose
		if(self.verbose): print('Refraction RE created')
		
		
	
	#createSpecularRE
	def createSpecularRE(self):
		
		#create specularRE
		specularRE = self.createRenderElement('specularChannel')
		pm.rename(specularRE, 'rbSpecular')
		
		#SetAttrs on specularRE
		pm.setAttr(specularRE.vray_name_specular, 'rbSpecular')
		
		#verbose
		if(self.verbose): print('Specular RE created')
		
		
	
	#createSubsurfaceRE
	def createSubsurfaceRE(self):
		
		#create subsurfaceRE
		subsurfaceRE = self.createRenderElement('FastSSS2Channel')
		pm.rename(subsurfaceRE, 'rbSubsurface')
		
		#SetAttrs on subsurfaceRE
		pm.setAttr(subsurfaceRE.vray_name_sss, 'rbSubsurface')
		
		#verbose
		if(self.verbose): print('SSS RE created')
		
		
		
	
	
	
	
	
	
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
		
	
	
	#vrayLoaded
	def vrayLoaded(self, setStatusFunction = False):
		#Get list of all loaded plugIns
		plugInList = pm.pluginInfo( query=True, listPlugins=True )
		
		#Return true if loaded else setStatus and return false
		if('vrayformaya' in plugInList): return True
		
		if(setStatusFunction): setStatusFunction('Vray for Maya Plugin not loaded')
		return False
	
	
	
	
	