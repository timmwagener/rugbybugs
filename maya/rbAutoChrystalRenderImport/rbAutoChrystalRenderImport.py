



#rbAutoChrystalRenderImport module
#------------------------------------------------------------------
'''
Create renderlayer, vrops assign materials and create renderlayer overrides to automatically 
integrate the chrystal reference in the scene after it has been grouped.
'''




#Imports
#------------------------------------------------------------------
import pymel.core as pm






#RbAutoChrystalRenderImport class
#------------------------------------------------------------------
class RbAutoChrystalRenderImport():
	'''RbAutoChrystalRenderImport class'''
	
	#__init__
	def __init__(self, namespaceShader = '', namespaceChrystal = ''):
		'''Constructor: Create custom instance vars'''
		
		#verbose
		self.verbose = True
		
		#namespaceShader
		self.namespaceShader = namespaceShader
		#namespaceChrystal
		self.namespaceChrystal = namespaceChrystal
		
		#shaderNames
		self.shaderNamesList = ['inner_sss_main_mt', 
		'intermediary_diffuse_main_mt', 
		'intermediary_sss_main_mt', 
		'intermediary_sss_mask_main_mt',
		'intermediary_sss_mask_rockremainder_main_mt',
		'intermediary_sss_refractive_main_mt',
		'outerHull_diffuse_main_mt',
		'outerHull_refract_main_mt',
		'outerHull_refract_sss_baked_main_mt'
		]
		
		#chrystalSubgroupNamesList
		self.chrystalSubgroupNamesList = ['innerHull_grp',
		'outerHull_grp',
		'intermediary_grp',
		'innerChrystal_grp',
		'chrystal_meshlights_grp',
		'inner_chrystal_rockremainder_grp'
		]
		
		
		#Geo
		
		#groups
		self.chrystal_grp = None
		
		self.innerHull_grp = None
		self.outerHull_grp = None
		self.intermediary_grp = None
		self.innerChrystal_grp = None
		self.inner_chrystal_rockremainder_grp = None
		
		self.chrystal_meshlights_grp = None
		self.inner_chrystal_lights_grp = None
		self.chrystal_intermediary_lights_grp = None
		
		#meshlightsTransform
		self.inner_chrystal_light_a_1 = None
		self.inner_chrystal_light_a_2 = None
		self.inner_chrystal_light_b_1 = None
		self.inner_chrystal_light_b_2 = None
		self.inner_chrystal_light_center = None
		
		self.chrystal_intermediary_light_a_1 = None
		self.chrystal_intermediary_light_a_2 = None
		self.chrystal_intermediary_light_b_1 = None
		self.chrystal_intermediary_light_b_2 = None
		self.chrystal_intermediary_light_center = None
		
		
		#meshlightsShape
		self.inner_chrystal_light_a_shape = None
		self.inner_chrystal_light_b_shape = None
		self.inner_chrystal_light_center_shape = None
		
		self.chrystal_intermediary_light_a_shape = None
		self.chrystal_intermediary_light_b_shape = None
		self.chrystal_intermediary_light_center_shape = None
		
		
		#shader
		self.outerHull_refract_main_mt = None
		self.outerHull_refract_sss_baked_main_mt = None
		self.outerHull_diffuse_main_mt = None
		
		self.intermediary_diffuse_main_mt = None
		self.intermediary_sss_main_mt = None
		self.intermediary_sss_refractive_main_mt = None
		self.intermediary_sss_mask_main_mt = None
		self.intermediary_sss_mask_rockremainder_main_mt = None
		
		self.inner_sss_main_mt = None
		
		
		
		#vrops
		self.vrop_innerHull_grp = None
		self.vrop_outerHull_grp = None
		self.vrop_intermediary_grp = None
		self.vrop_innerChrystal_grp = None
		self.vrop_inner_chrystal_rockremainder_grp = None
		
		
		
		#renderLayer
		self.default_renderLayer = None
		
		self.chrystal_shader_outerHull_refract_rlyr = None
		self.chrystal_shader_outerHull_diffuse_rlyr = None
		
		self.chrystal_shader_intermediary_sss_refract_rlyr = None
		self.chrystal_shader_intermediary_sss_simple_rlyr = None
		self.chrystal_shader_intermediary_diffuse_rlyr = None
		self.chrystal_shader_intermediary_mask_rlyr = None
		
		self.chrystal_shader_inner_sss_rlyr = None
		
		self.chrystal_shader_datapasses_rlyr = None
		
	



	#Script Routine
	#------------------------------------------------------------------
	
	#doIt
	def doIt(self):
		'''Complete procedure to auto import chrystal in renderscene'''
		
		#Startup Check
		if(self.startupCheck()):
			if(self.verbose):print('Startup check successful. Starting chrystal auto setup procedure.')
			
			
			
			#Assign Objects
			try:
				self.assignObjects()
				if(self.verbose):print('Successfuly assigned objects')
			except:
				if(self.verbose):print('Error assigning objects')
				return False
			
			#createVRops
			try:
				self.createVRops()
				if(self.verbose):print('Successfuly created vrops')
			except:
				if(self.verbose):print('Error creating vrops')
				return False
			
			
			#createMeshlights
			try:
				self.createMeshlights()
				if(self.verbose):print('Successfuly created meshlights')
			except:
				if(self.verbose):print('Error creating meshlights')
				return False
				
				
			#adjustMeshlights
			try:
				self.adjustMeshlights()
				if(self.verbose):print('Successfuly adjusted meshlights')
			except:
				if(self.verbose):print('Error adjusting meshlights')
				return False
				
			
			#unlinkChrystalFromLights
			try:
				self.unlinkChrystalFromLights()
				if(self.verbose):print('Successfuly unlinked chrystal shading geo')
			except:
				if(self.verbose):print('Error unlinking chrystal shading geo')
				return False
			
			
			#createRLayer
			try:
				self.createRLayer()
				if(self.verbose):print('Successfuly created renderlayer')
			except:
				if(self.verbose):print('Error creating renderlayer')
				return False
				
				
			#assignShaderOnRLayer
			try:
				self.assignShaderOnRLayer()
				if(self.verbose):print('Successfuly assigned Shader on renderlayer')
			except:
				if(self.verbose):print('Error assigning Shader on renderlayer')
				return False
				
				
			#createOverridesOnRLayer
			try:
				self.createOverridesOnRLayer()
				if(self.verbose):print('Successfuly created overrides on renderlayer')
			except:
				if(self.verbose):print('Error creating overrides on renderlayer')
				return False
			
			
			
			
			
		else:
			if(self.verbose):print('Startup check was not successful.')
		
	
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	
	#startupCheck
	def startupCheck(self):
		'''Perform check to see if all requirements to run the script are fullfilled'''
		
		
		#Check namespaces attrs.
		if not(self.namespaceShader):
			if(self.verbose):print('Empty namespaces for shader. Please provide correct parameter.')
			return False
			
		#Check namespaces attrs.
		if not(self.namespaceChrystal):
			if(self.verbose):print('Empty namespaces for chrystal. Please provide correct parameter.')
			return False
		
		
		
		
		#check selection
		selectionList = pm.ls(sl = True, fl  = True)
		
		#check selectionList 
		if not(selectionList):
			if(self.verbose):print('Nothing selected.')
			return False
			
		#check selectionList == 1
		if not(len(selectionList) == 1):
			if(self.verbose):print('SelectionList has wrong length, please only select Chrystal_top_grp')
			return False
			
		
		#check shadernames in scene
		for shaderName in self.shaderNamesList:
			#if shdername in scene
			if not(self.namespaceShader +':' +shaderName in pm.ls(fl = True, mat = True)):
				if(self.verbose):print(self.namespaceShader +':' +shaderName +' not in scene')
				return False
				
		
		#check if chrystalTopGrp is type transform
		if not(pm.nodeType(selectionList[0]) == 'transform'):
			if(self.verbose):print('Selected chrystal top grp is not of type transform')
			return False
			
		#Check subGroupNames
		for chrystalSubgroupName in self.chrystalSubgroupNamesList:
			if not(chrystalSubgroupName in [x.name().split('|')[-1] for x in selectionList[0].getChildren()]):
				if(self.verbose):print(chrystalSubgroupName +' not in selectionList')
				return False
		
		
		#If successful return True
		return True
		
		
	
	#assignObjects
	def assignObjects(self):
		'''Assign pyNodes to instance vars'''
		
		
		#get selection
		selectionList = pm.ls(sl = True, fl = True)
		pm.select(cl = True)
		
		
		
		#Shader
		#------------------------------------------------------------------
		self.outerHull_refract_main_mt = pm.PyNode(self.namespaceShader +':' +'outerHull_refract_main_mt',)
		self.outerHull_refract_sss_baked_main_mt = pm.PyNode(self.namespaceShader +':' +'outerHull_refract_sss_baked_main_mt')
		self.outerHull_diffuse_main_mt = pm.PyNode(self.namespaceShader +':' +'outerHull_diffuse_main_mt')
		
		self.intermediary_diffuse_main_mt = pm.PyNode(self.namespaceShader +':' +'intermediary_diffuse_main_mt')
		self.intermediary_sss_main_mt = pm.PyNode(self.namespaceShader +':' +'intermediary_sss_main_mt')
		self.intermediary_sss_refractive_main_mt = pm.PyNode(self.namespaceShader +':' +'intermediary_sss_refractive_main_mt')
		self.intermediary_sss_mask_main_mt = pm.PyNode(self.namespaceShader +':' +'intermediary_sss_mask_main_mt')
		self.intermediary_sss_mask_rockremainder_main_mt = pm.PyNode(self.namespaceShader +':' +'intermediary_sss_mask_rockremainder_main_mt')
		
		self.inner_sss_main_mt = pm.PyNode(self.namespaceShader +':' +'inner_sss_main_mt')
		
		#statusMsg
		#if(self.verbose):print('Successfuly assigned shader')
		
		
		#Chrystal and subgroups
		#------------------------------------------------------------------
		self.chrystal_grp = selectionList[0]
		
		#Chrystal subgroups
		for chrystalSubgroup in self.chrystal_grp.getChildren():
			
			if(chrystalSubgroup.name().split('|')[-1] == 'innerHull_grp'):self.innerHull_grp = chrystalSubgroup
			if(chrystalSubgroup.name().split('|')[-1] == 'outerHull_grp'):self.outerHull_grp = chrystalSubgroup
			if(chrystalSubgroup.name().split('|')[-1] == 'intermediary_grp'):self.intermediary_grp = chrystalSubgroup
			if(chrystalSubgroup.name().split('|')[-1] == 'innerChrystal_grp'):self.innerChrystal_grp = chrystalSubgroup
			if(chrystalSubgroup.name().split('|')[-1] == 'inner_chrystal_rockremainder_grp'):self.inner_chrystal_rockremainder_grp = chrystalSubgroup
			if(chrystalSubgroup.name().split('|')[-1] == 'chrystal_meshlights_grp'):self.chrystal_meshlights_grp = chrystalSubgroup
		
		#statusMsg
		#if(self.verbose):print('Successfuly assigned chrystal subgroups')
		
		
		
		#Meshlight Subgroups
		#------------------------------------------------------------------
		for meshlightSubgroup in self.chrystal_meshlights_grp.getChildren():
			if(meshlightSubgroup.name().split('|')[-1] == 'inner_chrystal_lights_grp'):self.inner_chrystal_lights_grp = meshlightSubgroup
			if(meshlightSubgroup.name().split('|')[-1] == 'chrystal_intermediary_lights_grp'):self.chrystal_intermediary_lights_grp = meshlightSubgroup
		
		#statusMsg
		#if(self.verbose):print('Successfuly assigned meshlight subgroups')
		
		
		#Meshlights
		#------------------------------------------------------------------
		
		#inner_chrystal
		for meshlight in self.inner_chrystal_lights_grp.getChildren():
			if( meshlight.name() == self.namespaceChrystal +':' +'inner_chrystal_light_a_1'):self.inner_chrystal_light_a_1 = meshlight
			if(meshlight.name() == self.namespaceChrystal +':' +'inner_chrystal_light_a_2'):self.inner_chrystal_light_a_2 = meshlight
			
			if(meshlight.name() == self.namespaceChrystal +':' +'inner_chrystal_light_b_1'):self.inner_chrystal_light_b_1 = meshlight
			if(meshlight.name() == self.namespaceChrystal +':' +'inner_chrystal_light_b_2'):self.inner_chrystal_light_b_2 = meshlight
			
			if(meshlight.name() == self.namespaceChrystal +':' +'inner_chrystal_light_center'):self.inner_chrystal_light_center = meshlight
		
		
		
		#intermediary_chrystal
		for meshlight in self.chrystal_intermediary_lights_grp.getChildren():
			if(meshlight.name() == self.namespaceChrystal +':' +'chrystal_intermediary_light_a_1'):self.chrystal_intermediary_light_a_1 = meshlight
			if(meshlight.name() == self.namespaceChrystal +':' +'chrystal_intermediary_light_a_2'):self.chrystal_intermediary_light_a_2 = meshlight
			
			if(meshlight.name() == self.namespaceChrystal +':' +'chrystal_intermediary_light_b_1'):self.chrystal_intermediary_light_b_1 = meshlight
			if(meshlight.name() == self.namespaceChrystal +':' +'chrystal_intermediary_light_b_2'):self.chrystal_intermediary_light_b_2 = meshlight
			
			if(meshlight.name() == self.namespaceChrystal +':' +'chrystal_intermediary_light_center'):self.chrystal_intermediary_light_center = meshlight
		
		
		#statusMsg
		#if(self.verbose):print('Successfuly assigned meshlights')
		
	

	
	#createVRops
	def createVRops(self):
		'''Create and assign Vrops'''
		
		pm.select(cl = True)
		
		
		#create Vrops
		self.vrop_innerHull_grp = pm.createNode('VRayObjectProperties', n = 'vrop_cs_innerHull_grp');pm.select(cl = True)
		self.vrop_outerHull_grp = pm.createNode('VRayObjectProperties', n = 'vrop_cs_outerHull_grp');pm.select(cl = True)
		self.vrop_intermediary_grp = pm.createNode('VRayObjectProperties', n = 'vrop_cs_intermediary_grp');pm.select(cl = True)
		self.vrop_innerChrystal_grp = pm.createNode('VRayObjectProperties', n = 'vrop_cs_innerChrystal_grp');pm.select(cl = True)
		self.vrop_inner_chrystal_rockremainder_grp = pm.createNode('VRayObjectProperties', n = 'vrop_cs_inner_chrystal_rockremainder_grp');pm.select(cl = True)
		
		#statusMsg
		#if(self.verbose):print('Successfuly created vrops')
		
		
		#assign vrops
		self.vrop_innerHull_grp.addMembers([self.innerHull_grp]);pm.select(cl = True)
		self.vrop_outerHull_grp.addMembers([self.outerHull_grp]);pm.select(cl = True)
		self.vrop_intermediary_grp.addMembers([self.intermediary_grp]);pm.select(cl = True)
		self.vrop_innerChrystal_grp.addMembers([self.innerChrystal_grp]);pm.select(cl = True)
		self.vrop_inner_chrystal_rockremainder_grp.addMembers([self.inner_chrystal_rockremainder_grp]);pm.select(cl = True)
		
		
		#statusMsg
		#if(self.verbose):print('Successfuly assigned vrops')
		
		
	
	
	
	
	#createMeshlights
	def createMeshlights(self):
		'''Create and assign Vray Meshlights'''
		
		#inner_chrystal_lights
		self.inner_chrystal_light_a_shape = self.createVrayMeshlight(meshList = [self.inner_chrystal_light_a_1, self.inner_chrystal_light_a_2], name = 'inner_chrystal_light_a');pm.select(cl = True)
		self.inner_chrystal_light_b_shape = self.createVrayMeshlight(meshList = [self.inner_chrystal_light_b_1, self.inner_chrystal_light_b_2], name = 'inner_chrystal_light_b');pm.select(cl = True)
		self.inner_chrystal_light_center_shape = self.createVrayMeshlight(meshList = [self.inner_chrystal_light_center], name = 'inner_chrystal_light_center');pm.select(cl = True)
		
		#chrystal_intermediary_lights
		self.chrystal_intermediary_light_a_shape = self.createVrayMeshlight(meshList = [self.chrystal_intermediary_light_a_1, self.chrystal_intermediary_light_a_2], name = 'chrystal_intermediary_light_a');pm.select(cl = True)
		self.chrystal_intermediary_light_b_shape = self.createVrayMeshlight(meshList = [self.chrystal_intermediary_light_b_1, self.chrystal_intermediary_light_b_2], name = 'chrystal_intermediary_light_b');pm.select(cl = True)
		self.chrystal_intermediary_light_center_shape = self.createVrayMeshlight(meshList = [self.chrystal_intermediary_light_center], name = 'chrystal_intermediary_light_center');pm.select(cl = True)
		
		
		#statusMsg
		#if(self.verbose):print('Successfuly created vray meshlights')
		
	
	
	
	#adjustMeshlights
	def adjustMeshlights(self):
		'''Initially Adjust Meshlights'''
		
		pm.select(cl = True)
		
		#makeTextureConnection (connect animated ramp to meshlight texture)
		makeTextureConnection = True
		
		
		
		#inner_chrystal_light_a
		#------------------------------------------------------------------
		
		#meshlight settings
		self.inner_chrystal_light_a_shape.intensityMult.set(7)
		self.inner_chrystal_light_a_shape.shadows.set(0)
		self.inner_chrystal_light_a_shape.useTex.set(1)
		self.inner_chrystal_light_a_shape.invisible.set(1)
		self.inner_chrystal_light_a_shape.cacheTexResolution.set(512)
		
		
		#create innerChrystal light texture 
		inner_chrystal_light_a_noise, inner_chrystal_light_a_noise_ramp, inner_chrystal_light_a_noise_time = self.createMeshlightTexture()
		#connect meshlight texture
		inner_chrystal_light_a_noise_ramp.outColor >> self.inner_chrystal_light_a_shape.tex
		pm.select(cl = True)
		
		
		
		
		#inner_chrystal_light_b
		#------------------------------------------------------------------
		
		#meshlight settings
		self.inner_chrystal_light_b_shape.intensityMult.set(7)
		self.inner_chrystal_light_b_shape.shadows.set(0)
		self.inner_chrystal_light_b_shape.useTex.set(1)
		self.inner_chrystal_light_b_shape.invisible.set(1)
		self.inner_chrystal_light_b_shape.cacheTexResolution.set(512)
		
		
		#create innerChrystal light texture 
		inner_chrystal_light_b_noise, inner_chrystal_light_b_noise_ramp, inner_chrystal_light_b_noise_time = self.createMeshlightTexture()
		#connect meshlight texture
		inner_chrystal_light_b_noise_ramp.outColor >> self.inner_chrystal_light_b_shape.tex
		pm.select(cl = True)
		
		
		
		#inner_chrystal_light_center_shape
		#------------------------------------------------------------------
		
		#meshlight settings
		self.inner_chrystal_light_center_shape.intensityMult.set(14)
		self.inner_chrystal_light_center_shape.shadows.set(0)
		self.inner_chrystal_light_center_shape.useTex.set(1)
		self.inner_chrystal_light_center_shape.invisible.set(1)
		self.inner_chrystal_light_center_shape.cacheTexResolution.set(512)
		
		
		#create innerChrystal light texture 
		inner_chrystal_light_center_noise, inner_chrystal_light_center_noise_ramp, inner_chrystal_light_center_noise_time = self.createMeshlightTexture()
		#connect meshlight texture
		inner_chrystal_light_center_noise_ramp.outColor >> self.inner_chrystal_light_center_shape.tex
		pm.select(cl = True)
		
		
		
		
		
		
		#chrystal_intermediary_light_a_shape
		#------------------------------------------------------------------
		
		#meshlight settings
		self.chrystal_intermediary_light_a_shape.intensityMult.set(50)
		self.chrystal_intermediary_light_a_shape.shadows.set(0)
		self.chrystal_intermediary_light_a_shape.invisible.set(1)
		self.chrystal_intermediary_light_a_shape.cacheTexResolution.set(512)
		self.chrystal_intermediary_light_a_shape.lightColor.set(1.0,0.0,0.0)
		
		
		#if makeTextureConnection
		if not(makeTextureConnection):
			#useTex
			self.chrystal_intermediary_light_a_shape.useTex.set(1)
			#create innerChrystal light texture 
			chrystal_intermediary_light_a_noise, chrystal_intermediary_light_a_noise_ramp, chrystal_intermediary_light_a_noise_time = self.createMeshlightTexture()
			#connect meshlight texture
			chrystal_intermediary_light_a_noise_ramp.outColor >> self.chrystal_intermediary_light_a_shape.tex
		pm.select(cl = True)
		
		
		
		#chrystal_intermediary_light_b_shape
		#------------------------------------------------------------------
		
		#meshlight settings
		self.chrystal_intermediary_light_b_shape.intensityMult.set(50)
		self.chrystal_intermediary_light_b_shape.shadows.set(0)
		self.chrystal_intermediary_light_b_shape.invisible.set(1)
		self.chrystal_intermediary_light_b_shape.cacheTexResolution.set(512)
		self.chrystal_intermediary_light_b_shape.lightColor.set(1.0,0.0,0.0)
		
		
		#if makeTextureConnection
		if not(makeTextureConnection):
			#useTex
			self.chrystal_intermediary_light_b_shape.useTex.set(1)
			#create innerChrystal light texture 
			chrystal_intermediary_light_b_noise, chrystal_intermediary_light_b_noise_ramp, chrystal_intermediary_light_b_noise_time = self.createMeshlightTexture()
			#connect meshlight texture
			chrystal_intermediary_light_b_noise_ramp.outColor >> self.chrystal_intermediary_light_b_shape.tex
		pm.select(cl = True)
		
		
		
		#chrystal_intermediary_light_center_shape
		#------------------------------------------------------------------
		
		#meshlight settings
		self.chrystal_intermediary_light_center_shape.intensityMult.set(75)
		self.chrystal_intermediary_light_center_shape.shadows.set(0)
		self.chrystal_intermediary_light_center_shape.useTex.set(1)
		self.chrystal_intermediary_light_center_shape.invisible.set(1)
		self.chrystal_intermediary_light_center_shape.cacheTexResolution.set(512)
		
		
		#create innerChrystal light texture 
		chrystal_intermediary_light_center_noise, chrystal_intermediary_light_center_noise_ramp, chrystal_intermediary_light_center_noise_time = self.createMeshlightTexture()
		#connect meshlight texture
		chrystal_intermediary_light_center_noise_ramp.outColor >> self.chrystal_intermediary_light_center_shape.tex
		pm.select(cl = True)

		
		
	
	
	

	
	#unlinkChrystalFromLights
	def unlinkChrystalFromLights(self):
		'''Unlink chrystal shading geo from all lights in the scene'''
		
		pm.select(cl = True)
		
		#Break lightlinks
		#------------------------------------------------------------------
		
		#Get all scene lights as list by type
		standardMayaLightsList = pm.ls(fl = True, lights = True)
		vrayDomeLightsList = pm.ls(fl = True, type = 'VRayLightDomeShape')
		vrayRectLightsList = pm.ls(fl = True, type = 'VRayLightRectShape')
		vraySphereLightsList = pm.ls(fl = True, type = 'VRayLightSphereShape')
		vrayMeshLightsList = pm.ls(fl = True, type = 'VRayLightMeshLightLinking')
		
		#add them together
		sceneLightsList = standardMayaLightsList+vrayDomeLightsList+vraySphereLightsList+vrayRectLightsList+vrayMeshLightsList
		
		#Break lightlinks for all lights
		pm.lightlink( b = True, light = sceneLightsList, object=(self.chrystal_grp))
		pm.select(cl = True)
		
		
		#statusMsg
		#if(self.verbose):print('Successfuly broken lightLinks')
		
		
		#ReCreate lightlinks
		#------------------------------------------------------------------
		
		#intermediary
		#Get vrayLightMeshLightLinking for chrystal intermediary meshlights
		intermediary_lights_lightlink_nodeList = []
		intermediary_lights_lightlink_nodeList.append(self.getVrayMeshlightLightLink(self.chrystal_intermediary_light_a_shape))
		pm.select(cl = True)
		intermediary_lights_lightlink_nodeList.append(self.getVrayMeshlightLightLink(self.chrystal_intermediary_light_b_shape))
		pm.select(cl = True)
		intermediary_lights_lightlink_nodeList.append(self.getVrayMeshlightLightLink(self.chrystal_intermediary_light_center_shape))
		pm.select(cl = True)
		
		#recreate lightlinks
		pm.lightlink( m = True, light = intermediary_lights_lightlink_nodeList, object=(self.innerHull_grp, self.intermediary_grp, self.inner_chrystal_rockremainder_grp))
		pm.select(cl = True)
		
		#statusMsg
		#if(self.verbose):print('Successfuly recreated intermediary lightLinks')
		
		
		
		#innerChrystal
		#Get vrayLightMeshLightLinking for chrystal intermediary meshlights
		innerChrystal_lights_lightlink_nodeList = []
		innerChrystal_lights_lightlink_nodeList.append(self.getVrayMeshlightLightLink(self.inner_chrystal_light_a_shape))
		pm.select(cl = True)
		innerChrystal_lights_lightlink_nodeList.append(self.getVrayMeshlightLightLink(self.inner_chrystal_light_b_shape))
		pm.select(cl = True)
		innerChrystal_lights_lightlink_nodeList.append(self.getVrayMeshlightLightLink(self.inner_chrystal_light_center_shape))
		pm.select(cl = True)
		
		pm.lightlink( m = True, light = innerChrystal_lights_lightlink_nodeList, object=(self.innerChrystal_grp))
		pm.select(cl = True)
		
		#statusMsg
		#if(self.verbose):print('Successfuly recreated innerChrystal lightLinks')
		
		
		
		#statusMsg
		#if(self.verbose):print('Successfuly unlinked lights')
		
		pm.select(cl = True)
		
		
		
		
	
	
	
	
	#createRLayer
	def createRLayer(self):
		'''Create and assign renderlayer for chrystal shading asset'''
		
		pm.select(cl = True)
		
		#Create renderLayer
		#------------------------------------------------------------------
		
		#Default
		self.default_renderLayer = pm.nodetypes.RenderLayer.defaultRenderLayer();pm.select(cl = True)
		
		#outerHull
		self.chrystal_shader_outerHull_refract_rlyr = pm.createRenderLayer(e = True, n = 'cs_outerHull_refract_rlyr');pm.select(cl = True)
		self.chrystal_shader_outerHull_diffuse_rlyr = pm.createRenderLayer(e = True, n = 'cs_outerHull_diffuse_rlyr');pm.select(cl = True)
		
		#intermediate
		self.chrystal_shader_intermediary_sss_refract_rlyr = pm.createRenderLayer(e = True, n = 'cs_intermediary_sss_refract_rlyr');pm.select(cl = True)
		self.chrystal_shader_intermediary_sss_simple_rlyr = pm.createRenderLayer(e = True, n = 'cs_intermediary_sss_simple_rlyr');pm.select(cl = True)
		self.chrystal_shader_intermediary_diffuse_rlyr = pm.createRenderLayer(e = True, n = 'cs_intermediary_diffuse_rlyr');pm.select(cl = True)
		self.chrystal_shader_intermediary_mask_rlyr = pm.createRenderLayer(e = True, n = 'cs_intermediary_mask_rlyr');pm.select(cl = True)
		
		#inner
		self.chrystal_shader_inner_sss_rlyr = pm.createRenderLayer(e = True, n = 'cs_inner_sss_rlyr');pm.select(cl = True)
		
		#datapasses
		self.chrystal_shader_datapasses_rlyr = pm.createRenderLayer(e = True, n = 'cs_datapasses_rlyr');pm.select(cl = True)
		
		
		
		#statusMsg
		#if(self.verbose):print('Successfuly created renderLayer')
		
		
		#Assign membership for renderLayer
		#------------------------------------------------------------------
		pm.select(cl = True)
		
		#outerHull refract
		self.chrystal_shader_outerHull_refract_rlyr.addMembers([self.innerChrystal_grp, self.outerHull_grp],  noRecurse = True);pm.select(cl = True)
		#outerHull diffuse
		self.chrystal_shader_outerHull_diffuse_rlyr.addMembers([self.innerHull_grp, self.outerHull_grp, self.intermediary_grp , self.innerChrystal_grp, self.inner_chrystal_rockremainder_grp],  noRecurse = True);pm.select(cl = True)
		
		#intermediary sss refract
		self.chrystal_shader_intermediary_sss_refract_rlyr.addMembers([self.innerHull_grp, self.outerHull_grp, self.intermediary_grp , self.innerChrystal_grp, self.inner_chrystal_rockremainder_grp, self.chrystal_intermediary_lights_grp],  noRecurse = True);pm.select(cl = True)
		#intermediary sss simple
		self.chrystal_shader_intermediary_sss_simple_rlyr.addMembers([self.innerHull_grp, self.outerHull_grp, self.intermediary_grp , self.innerChrystal_grp, self.inner_chrystal_rockremainder_grp, self.chrystal_intermediary_lights_grp],  noRecurse = True);pm.select(cl = True)
		#intermediary diffuse
		self.chrystal_shader_intermediary_diffuse_rlyr.addMembers([self.innerHull_grp, self.outerHull_grp, self.intermediary_grp , self.innerChrystal_grp, self.inner_chrystal_rockremainder_grp],  noRecurse = True);pm.select(cl = True)
		#intermediary mask
		self.chrystal_shader_intermediary_mask_rlyr.addMembers([self.innerHull_grp, self.outerHull_grp, self.intermediary_grp , self.innerChrystal_grp, self.inner_chrystal_rockremainder_grp],  noRecurse = True);pm.select(cl = True)
		
		#inner sss
		self.chrystal_shader_inner_sss_rlyr.addMembers([self.innerHull_grp, self.outerHull_grp, self.intermediary_grp , self.innerChrystal_grp, self.inner_chrystal_rockremainder_grp, self.inner_chrystal_lights_grp],  noRecurse = True);pm.select(cl = True)
		
		#datapasses
		self.chrystal_shader_datapasses_rlyr.addMembers([self.innerHull_grp, self.outerHull_grp, self.intermediary_grp , self.innerChrystal_grp, self.inner_chrystal_rockremainder_grp],  noRecurse = True);pm.select(cl = True)
		
		pm.select(cl = True)

		
		#statusMsg
		#if(self.verbose):print('Successfuly assigned chrystal objects to renderLayer')
		
		
		
	
	
	
	#assignShaderOnRLayer
	def assignShaderOnRLayer(self):
		'''Assign shader on renderlayers'''
		
		pm.select(cl = True)
		
		
		#chrystal outerHull refract rlyr
		#------------------------------------------------------------------
		#outerHull
		self.shaderOverrideOnRLayer(rlayer = self.chrystal_shader_outerHull_refract_rlyr, shader = self.outerHull_refract_main_mt, geometryList = [self.outerHull_grp])
		#innerChrystal
		self.shaderOverrideOnRLayer(rlayer = self.chrystal_shader_outerHull_refract_rlyr, shader = self.outerHull_refract_sss_baked_main_mt, geometryList = [self.innerChrystal_grp])
		
		pm.select(cl = True)
		
		
		
		
		#chrystal outerHull diffuse rlyr
		#------------------------------------------------------------------
		#outerHull
		self.shaderOverrideOnRLayer(rlayer = self.chrystal_shader_outerHull_diffuse_rlyr, shader = self.outerHull_diffuse_main_mt, geometryList = [self.outerHull_grp])
		pm.select(cl = True)
		
		
		
		
		
		
		
		
		#chrystal intermediary sss refract rlyr
		#------------------------------------------------------------------
		#intermediary
		self.shaderOverrideOnRLayer(rlayer = self.chrystal_shader_intermediary_sss_refract_rlyr, shader = self.intermediary_sss_refractive_main_mt, geometryList = [self.intermediary_grp, self.innerHull_grp, self.inner_chrystal_rockremainder_grp])
		pm.select(cl = True)
		
		
		
		#chrystal intermediary sss simple rlyr
		#------------------------------------------------------------------
		#intermediary
		self.shaderOverrideOnRLayer(rlayer = self.chrystal_shader_intermediary_sss_simple_rlyr, shader = self.intermediary_sss_main_mt, geometryList = [self.intermediary_grp, self.innerHull_grp, self.inner_chrystal_rockremainder_grp])
		pm.select(cl = True)
		
		
		
		#chrystal intermediary diffuse rlyr
		#------------------------------------------------------------------
		#intermediary
		self.shaderOverrideOnRLayer(rlayer = self.chrystal_shader_intermediary_diffuse_rlyr, shader = self.intermediary_diffuse_main_mt, geometryList = [self.intermediary_grp, self.innerHull_grp, self.inner_chrystal_rockremainder_grp])
		pm.select(cl = True)
		
		
		
		#chrystal intermediary sss mask rlyr
		#------------------------------------------------------------------
		#intermediary
		self.shaderOverrideOnRLayer(rlayer = self.chrystal_shader_intermediary_mask_rlyr, shader = self.intermediary_sss_mask_main_mt, geometryList = [self.intermediary_grp])
		pm.select(cl = True)
		#rockremainder
		self.shaderOverrideOnRLayer(rlayer = self.chrystal_shader_intermediary_mask_rlyr, shader = self.intermediary_sss_mask_rockremainder_main_mt, geometryList = [self.inner_chrystal_rockremainder_grp, self.innerHull_grp])
		pm.select(cl = True)
		
		
		
		
		
		#chrystal inner sss rlyr
		#------------------------------------------------------------------
		#intermediary
		self.shaderOverrideOnRLayer(rlayer = self.chrystal_shader_inner_sss_rlyr, shader = self.inner_sss_main_mt, geometryList = [self.innerChrystal_grp])
		pm.select(cl = True)
		
		
		
		
		#statusMsg
		#if(self.verbose):print('Successfuly overriden shader on renderLayers')
		
		
		
	
	#createOverridesOnRLayer
	def createOverridesOnRLayer(self):
		'''Create overrides on renderlayer'''
		
		pm.select(cl = True)
		
		
		#chrystal_shader_outerHull_refract_rlyr
		#------------------------------------------------------------------
		
		#vrop overrides
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_innerChrystal_grp, rlayer = self.chrystal_shader_outerHull_refract_rlyr, alpha = 0)
		
		
		
		#chrystal_shader_outerHull_diffuse_rlyr
		#------------------------------------------------------------------
		
		#vrop overrides
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_innerHull_grp, rlayer = self.chrystal_shader_outerHull_diffuse_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_intermediary_grp, rlayer = self.chrystal_shader_outerHull_diffuse_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_innerChrystal_grp, rlayer = self.chrystal_shader_outerHull_diffuse_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_inner_chrystal_rockremainder_grp, rlayer = self.chrystal_shader_outerHull_diffuse_rlyr)
		
		
		
		
		#chrystal_shader_intermediary_sss_refract_rlyr
		#------------------------------------------------------------------
		
		#vrop overrides
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_outerHull_grp, rlayer = self.chrystal_shader_intermediary_sss_refract_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_innerChrystal_grp, rlayer = self.chrystal_shader_intermediary_sss_refract_rlyr)
		
		
		#additional overrides
		
		#set rlayer Current
		self.chrystal_shader_intermediary_sss_refract_rlyr.setCurrent();pm.select(cl = True)
		
		#overrides
		pm.editRenderLayerAdjustment(self.chrystal_intermediary_light_center.visibility);self.chrystal_intermediary_light_center.visibility.set(0);pm.select(cl = True)
		
		
		#setCurrent back to default
		pm.nodetypes.RenderLayer.defaultRenderLayer().setCurrent();pm.select(cl = True)
		
		
		
		
		
		#chrystal_shader_intermediary_sss_simple_rlyr
		#------------------------------------------------------------------
		
		#vrop overrides
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_outerHull_grp, rlayer = self.chrystal_shader_intermediary_sss_simple_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_innerChrystal_grp, rlayer = self.chrystal_shader_intermediary_sss_simple_rlyr)
		
		
		#additional overrides
		
		#set rlayer Current
		self.chrystal_shader_intermediary_sss_simple_rlyr.setCurrent();pm.select(cl = True)
		
		#overrides
		pm.editRenderLayerAdjustment(self.chrystal_intermediary_light_a_1.visibility);self.chrystal_intermediary_light_a_1.visibility.set(0);pm.select(cl = True)
		pm.editRenderLayerAdjustment(self.chrystal_intermediary_light_a_2.visibility);self.chrystal_intermediary_light_a_2.visibility.set(0);pm.select(cl = True)
		pm.editRenderLayerAdjustment(self.chrystal_intermediary_light_b_1.visibility);self.chrystal_intermediary_light_b_1.visibility.set(0);pm.select(cl = True)
		pm.editRenderLayerAdjustment(self.chrystal_intermediary_light_b_2.visibility);self.chrystal_intermediary_light_b_2.visibility.set(0);pm.select(cl = True)
		
		
		#setCurrent back to default
		pm.nodetypes.RenderLayer.defaultRenderLayer().setCurrent();pm.select(cl = True)
		
		
		
		
		#chrystal_shader_intermediary_diffuse_rlyr
		#------------------------------------------------------------------
		
		#vrop overrides
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_outerHull_grp, rlayer = self.chrystal_shader_intermediary_diffuse_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_innerChrystal_grp, rlayer = self.chrystal_shader_intermediary_diffuse_rlyr)
		
		
		
		#chrystal_shader_intermediary_mask_rlyr
		#------------------------------------------------------------------
		
		#vrop overrides
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_outerHull_grp, rlayer = self.chrystal_shader_intermediary_mask_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_innerChrystal_grp, rlayer = self.chrystal_shader_intermediary_mask_rlyr)
		
	
		
		
		
		#chrystal_shader_inner_sss_rlyr
		#------------------------------------------------------------------
		
		#vrop overrides
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_outerHull_grp, rlayer = self.chrystal_shader_inner_sss_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_intermediary_grp, rlayer = self.chrystal_shader_inner_sss_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_innerHull_grp, rlayer = self.chrystal_shader_inner_sss_rlyr)
		self.setVropMatteOverrideOnLayer(vrop = self.vrop_inner_chrystal_rockremainder_grp, rlayer = self.chrystal_shader_inner_sss_rlyr)
		
		
		#additional overrides
		
		#set rlayer Current
		self.chrystal_shader_inner_sss_rlyr.setCurrent();pm.select(cl = True)
		
		#overrides
		pm.editRenderLayerAdjustment(self.inner_chrystal_light_center.visibility);self.inner_chrystal_light_center.visibility.set(0);pm.select(cl = True)
		
		
		#setCurrent back to default
		pm.nodetypes.RenderLayer.defaultRenderLayer().setCurrent();pm.select(cl = True)
		
	
	
	
	
	
	
	
	#Shared methods
	#------------------------------------------------------------------
	
	#createVrayMeshlight
	def createVrayMeshlight(self, meshList = [], name = ''):
		'''Create a vray meshLight from the meshList objects with passed name and return the shape'''
		
		pm.select(cl = True)
		
		#Select passed meshList
		pm.select(meshList, r = True)
		
		#Create Vray Meshlight from selected objects
		pm.mel.eval("vray objectProperties add_single VRayLightMesh;")
		pm.select(cl = True)
		
		#get vraylightmesh by list connections
		vrayMeshLight = pm.listConnections(meshList[0], type = 'VRayLightMesh')[0]
		pm.rename(vrayMeshLight, name)
		pm.select(cl = True)
		
		return vrayMeshLight
		
	
	
	
	#createMeshlightTexture
	def createMeshlightTexture(self):
		'''Create animated texture for meshlights of chrystal'''
		
		
		pm.select(cl = True)
		
		
		#create noise
		inner_chrystal_sss_light_noise = pm.createNode('noise', name='inner_chrystal_light_noise')
		pm.select(cl = True)

		#AdjustNoise
		inner_chrystal_sss_light_noise.noiseType.set(0)
		inner_chrystal_sss_light_noise.frequency.set(1.3)
		inner_chrystal_sss_light_noise.colorOffset.set(0.5,0.5,0.5)
		pm.select(cl = True)

		#keyframe noise
		pm.setKeyframe( inner_chrystal_sss_light_noise , attribute='time', t=1, v = 0.0 )
		pm.setKeyframe( inner_chrystal_sss_light_noise , attribute='time', t=30, v = 0.3 )
		pm.select(cl = True)

		#get animCurveNoed by downstream Connection and set Inifinty behaviour for animCurve
		inner_chrystal_sss_light_noise_time = pm.listConnections(inner_chrystal_sss_light_noise.time, source = True)[0]

		inner_chrystal_sss_light_noise_time.preInfinity.set(4)
		inner_chrystal_sss_light_noise_time.postInfinity.set(4)
		pm.select(cl = True)

		#create place2Dtexture
		inner_chrystal_sss_light_noise_placement = pm.createNode('place2dTexture', name='inner_chrystal_light_noise_place2dTexture')
		pm.select(cl = True)

		#create ramp
		inner_chrystal_sss_light_noise_ramp = pm.createNode('ramp', name='inner_chrystal_sss_light_noise_ramp')
		pm.select(cl = True)

		#adjust ramp
		inner_chrystal_sss_light_noise_ramp.interpolation.set(4)

		inner_chrystal_sss_light_noise_ramp.colorEntryList[2].color.set(1.0, 0.3, 0.3)
		inner_chrystal_sss_light_noise_ramp.colorEntryList[2].position.set(1.0)

		inner_chrystal_sss_light_noise_ramp.colorEntryList[1].color.set(1.0, 0.0, 0.0)
		inner_chrystal_sss_light_noise_ramp.colorEntryList[1].position.set(0.8)


		inner_chrystal_sss_light_noise_ramp.colorEntryList[0].color.set(0.0, 0.0, 0.0)
		inner_chrystal_sss_light_noise_ramp.colorEntryList[0].position.set(0.79)
		pm.select(cl = True)

		#Connect noise and ramp
		inner_chrystal_sss_light_noise.outColor.outColorR >> inner_chrystal_sss_light_noise_ramp.uvCoord.vCoord

		#Connect place2dTexture to noise
		inner_chrystal_sss_light_noise_placement.outUV >> inner_chrystal_sss_light_noise.uvCoord
		inner_chrystal_sss_light_noise_placement.outUvFilterSize >> inner_chrystal_sss_light_noise.uvFilterSize
		pm.select(cl = True)
		
		
		return [inner_chrystal_sss_light_noise, inner_chrystal_sss_light_noise_ramp, inner_chrystal_sss_light_noise_time]

		
		
	
	
	#shaderOverrideOnRLayer
	def shaderOverrideOnRLayer(self, rlayer = None, shader = None, geometryList = None):
		'''Assign passed shader on passed RLayer to passed geometry'''
		
		pm.select(cl = True)
		
		#set rlyr
		rlayer.setCurrent()
		
		#get shadingGroup
		shaderSG = shader.listConnections(t='shadingEngine', et = True)[0];pm.select(cl = True)
		#assign
		pm.sets(shaderSG, e = True, fe = geometryList);pm.select(cl = True)
		
		
		#reset rlyr
		pm.nodetypes.RenderLayer.defaultRenderLayer().setCurrent();pm.select(cl = True)
		
		
	
	
	
	#getVrayMeshlightLightLink
	def getVrayMeshlightLightLink(self, vrayMeshLight):
		'''Accept vrayMeshLight as Param and traverse the connections to return corresponding lightlink node'''
		
		pm.select(cl = True)
		
		#get list of all connections of type transform for vray meshlight
		lightConnectionsList = vrayMeshLight.listConnections(t='transform', et = True)
		pm.select(cl = True)
		
		#iterate over lightconnectionsList and check children, return if child is of type vrayLightLink
		for obj in lightConnectionsList:
			try:
				if(len(obj.getChildren()) == 1 and pm.nodeType(obj.getChildren()[0]) == 'VRayLightMeshLightLinking'):return obj.getChildren()[0]
			except:
				pass
		
		
	
	#setVropMatteOverrideOnLayer
	def setVropMatteOverrideOnLayer(self, vrop = None, rlayer = None, alpha = -1):
		'''Set Vrop to matte for a specific renderlayer'''
		
		pm.select(cl = True)
		
		#set rlayer Current
		rlayer.setCurrent();pm.select(cl = True)
		
		#vrop overrides
		pm.editRenderLayerAdjustment(vrop.matteSurface, layer = rlayer);vrop.matteSurface.set(1);pm.select(cl = True)
		pm.editRenderLayerAdjustment(vrop.alphaContribution, layer = rlayer);vrop.alphaContribution.set(alpha);pm.select(cl = True)
		pm.editRenderLayerAdjustment(vrop.noGIOnOtherMattes, layer = rlayer);vrop.noGIOnOtherMattes.set(0);pm.select(cl = True)
		
		#setCurrent back to default
		pm.nodetypes.RenderLayer.defaultRenderLayer().setCurrent();pm.select(cl = True)
		

		

		
		
#Execute autoChrystalRenderImport
#------------------------------------------------------------------	
'''
import pymel.core as pm

#reopen file without saving
pm.openFile('Q:\\Production\\_Rnd\Rnd.timm\\autoChrystalRenderImport\\3d\\autoChrystalRenderImportTest_v0001_tw.mb', force = 1)

#deselect all
pm.select(cl = True)

#select chrystal_shading_grp
pm.select('chrystal_shading_grp')

#import module
from rugbyBugs.maya.rbAutoChrystalRenderImport import rbAutoChrystalRenderImport

#Reload if true
doReload = True
if(doReload): reload(rbAutoChrystalRenderImport)


#Create Instance
rbAutoChrystalRenderImportInstance = rbAutoChrystalRenderImport.RbAutoChrystalRenderImport(namespaceShader = 'chrystal_shader', namespaceChrystal = '_ball1')
rbAutoChrystalRenderImportInstance.doIt()
''' 
		
		
		
		
