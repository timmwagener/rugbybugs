




#rugbyBugsMayaInterface Module
#------------------------------------------------------------------

'''
Interface for all Rugby Bugs Maya Tools
'''

'''
ToDo:

'''


#Imports
#------------------------------------------------------------------
from PyQt4 import QtGui, QtCore, uic
import sys, os
import functools
import maya.OpenMayaUI as openMayaUi
import sip
import pymel.core as pm



#Reload boolean
doReload = True

from lib import MayaFunctionality
if(doReload): reload(MayaFunctionality)

#grouping
from rugbyBugs.maya.rbGrouping import rbGrouping
if(doReload): reload(rbGrouping)

#dataPasses
from rugbyBugs.maya.rbCreateUpdateRenderElements import rbCreateDataPasses
if(doReload): reload(rbCreateDataPasses)

#Light Render Elements
from rugbyBugs.maya.rbCreateUpdateRenderElements import rbCreateUpdateLightRenderElements
if(doReload): reload(rbCreateUpdateLightRenderElements)

#Frame Buffer Contributions
from rugbyBugs.maya.rbCreateUpdateRenderElements import rbCreateFrameBufferContributions
if(doReload): reload(rbCreateFrameBufferContributions)

#MultiMatte Render Elements
from rugbyBugs.maya.rbCreateUpdateRenderElements import rbCreateUpdateMmRenderElements
if(doReload): reload(rbCreateUpdateMmRenderElements)

#Shadow Pass Render Elements
from rugbyBugs.maya.rbCreateUpdateRenderElements import rbCreateShadowPass
if(doReload): reload(rbCreateShadowPass)

#VRay Render Settings
from rugbyBugs.maya.rbSetVrayRenderGlobals import rbSetVrayRenderGlobals
if(doReload): reload(rbSetVrayRenderGlobals)

#rbRigging
from rugbyBugs.maya.rbRigging import rbRigging
if(doReload): reload(rbRigging)

#rbTransferKeysRelativeToWorldSpace
from rugbyBugs.maya.rbTransferKeysRelativeToWorldSpace import rbTransferKeysRelativeToWorldSpace
if(doReload): reload(rbTransferKeysRelativeToWorldSpace)

#rbBakeAnimation
from rugbyBugs.maya.rbBakeAnimation import rbBakeAnimation
if(doReload): reload(rbBakeAnimation)

#rbPaintFxTransferAnimation
from rugbyBugs.maya.rbPaintFxTransferAnimation import rbPaintFxTransferAnimation
if(doReload): reload(rbPaintFxTransferAnimation)

#rbApplyPresetToSelection
from rugbyBugs.maya.rbApplyPresetToSelection import rbApplyPresetToSelection
if(doReload): reload(rbApplyPresetToSelection)

#rbAutoShaderAssignmentAndGrouping
from rugbyBugs.maya.rbAutoShaderAssignmentAndGrouping import rbAutoShaderAssignmentAndGrouping
if(doReload): reload(rbAutoShaderAssignmentAndGrouping)






#Get Maya QMAinWindow as Parent
#------------------------------------------------------------------
def getMayaQMainWindow():
	ptr = openMayaUi.MQtUtil.mainWindow()
	return sip.wrapinstance(long(ptr), QtCore.QObject)



	
#Get ui file classes
#------------------------------------------------------------------
#Add path of ressource_rc.py
ressourceFilePath = os.path.join(os.path.dirname(__file__), 'media')
sys.path.append(ressourceFilePath)
uiFilePath = os.path.join(os.path.dirname(__file__), 'media\\rugbyBugsMayaInterfaceUi.ui')
uiClassesList = uic.loadUiType(uiFilePath)





#RugbyBugsMayaInterface class
#------------------------------------------------------------------
class RugbyBugsMayaInterface(uiClassesList[0], uiClassesList[1]):
	
	
	#Constructor
	#------------------------------------------------------------------	
	def __init__(self, parent = getMayaQMainWindow()):
		super(RugbyBugsMayaInterface, self).__init__(parent)
		
		
		#Instance Vars
		#------------------------------------------------------------------
		
		#Feature Instances
		#--------------------------------
		
		
		#Lighting and Shading
		self.groupingFunctions = rbGrouping.RbGrouping()
		self.dataPassFunctions = rbCreateDataPasses.RbCreateDataPasses()
		self.LightRenderElementsFunctions = rbCreateUpdateLightRenderElements.RbCreateUpdateLightRenderElements()
		self.frameBufferContributionFunctions = rbCreateFrameBufferContributions.RbCreateFrameBufferContributions()
		self.mMRenderElementsFunctions = rbCreateUpdateMmRenderElements.RbCreateUpdateMmRenderElements()
		self.shadowPassFunctions = rbCreateShadowPass.RbCreateShadowPass()
		self.vrayRenderSettingsFunctions = rbSetVrayRenderGlobals.RbSetVrayRenderGlobals()
		
		#Rigging
		self.rbRiggingInstance = rbRigging.RbRigging()
		
		#Animation
		self.rbTransferKeysRelativeToWorldSpaceInstance = rbTransferKeysRelativeToWorldSpace.RbTransferKeysRelativeToWorldSpace()
		self.rbBakeAnimationInstance = rbBakeAnimation.RbBakeAnimation()
		
		#PaintFxHair
		self.rbPaintFxTransferAnimationInstance = rbPaintFxTransferAnimation.RbPaintFxTransferAnimation()
		
		self.rbApplyPresetToSelectionInstance = rbApplyPresetToSelection.RbApplyPresetToSelection()
		
		
		#Alembic Import
		self.rbAutoShaderAssignmentAndGroupingInstance = rbAutoShaderAssignmentAndGrouping.RbAutoShaderAssignmentAndGrouping()
		
		
		
		
		
		#Dockability
		self.dockIt = True
		self.dockArea = 'left'
		self.version = 0.1
		self.label = 'RugbyBugs Maya Toolset Alpha'
		
		
		#Startup Routine
		#------------------------------------------------------------------
		
		#setupUi
		self.setupUi(self)
		
		#ConnectUi
		self.connectUi()
		
		#makeDockable
		if(self.dockIt):
			windowWidth = self.geometry().width()
			MayaFunctionality.makeDockable(self, self.dockArea, windowWidth, self.label + ' ' + str(self.version))
			
		
		#Set paintFx hair namespaces Combobox
		#self.refreshNamespacesComboboxPaintFxHair()
		
			
		#show Ui
		self.show()
		
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	#connectUi
	def connectUi(self):
		
		
		
		#Lighting & RenderElements
		#------------------------------------------------------------------
		
		
		#btnCreateBaseGroups
		self.btnCreateBaseGroups.clicked.connect(functools.partial(self.groupingFunctions.createBaseGroups, self.setStatus))
		
		
		#btnVraySetRenderGlobals
		self.btnVraySetRenderGlobals.clicked.connect(functools.partial(self.vrayRenderSettingsFunctions.setVrayRenderSettings, self.setStatus))
		#btnVraySetRenderGlobalsLinear
		self.btnVraySetRenderGlobalsLinear.clicked.connect(functools.partial(self.vrayRenderSettingsFunctions.setVrayRenderSettingsLinear,  self.setStatus))
		
		
		#btnCreateUpdateRenderElements
		self.btnCreateUpdateLightRenderElements.clicked.connect(functools.partial(self.LightRenderElementsFunctions.createUpdateLightRenderElements,  self.setStatus))
		#btnCreateAdditionalFramebufferContributions
		self.btnCreateAdditionalFramebufferContributions.clicked.connect(functools.partial(self.frameBufferContributionFunctions.createFrameBufferContributions,  self.setStatus))
		#btnCreateUpdateMmRenderElements
		self.btnCreateUpdateMmRenderElements.clicked.connect(functools.partial(self.mMRenderElementsFunctions.createUpdateMultiMatteElements,  self.setStatus))
		#btnCreateDataPasses
		self.btnCreateDataPasses.clicked.connect(functools.partial(self.dataPassFunctions.createDataPasses,  self.setStatus))
		#btnCreateShadowRenderElements
		self.btnCreateShadowRenderElements.clicked.connect(functools.partial(self.shadowPassFunctions.createShadowPass,  self.setStatus))
		
		
		
		
		
		
		
		#Rigging
		#------------------------------------------------------------------
		
		#btnCreateFootRigALocators
		self.btnCreateFootRigALocators.clicked.connect(functools.partial(self.createFootRigAPosLocators))
		#btnCreateFootRigA
		self.btnCreateFootRigA.clicked.connect(functools.partial(self.createFootRigA))
		
		
		#btnCreateFootRigBLocators
		self.btnCreateFootRigBLocators.clicked.connect(functools.partial(self.createFootRigBPosLocators))
		#btnCreateFootRigB
		self.btnCreateFootRigB.clicked.connect(functools.partial(self.createFootRigB))
		
		
		#btnCreateDynamicChainLocators
		self.btnCreateDynamicChainLocators.clicked.connect(functools.partial(self.createDynamicChainPosLocators))
		#btnCreateDynamicChain
		self.btnCreateDynamicChain.clicked.connect(functools.partial(self.createDynamicChain))
		
		
		#btnCreateIkFkBlendArmLocators
		self.btnCreateIkFkBlendArmLocators.clicked.connect(functools.partial(self.createIkFkBlendArmLocators))
		#btnCreateIkFkBlendArm
		self.btnCreateIkFkBlendArm.clicked.connect(functools.partial(self.createIkFkBlendArm))
		
		
		#btnCreateDynamicChainFromCurves
		self.btnCreateDynamicChainFromCurves.clicked.connect(functools.partial(self.createDynamicChainFromCurves))
		
		
		
		
		
		
		
		#Animation
		#------------------------------------------------------------------
		
		#btnTransferKeyframes
		self.btnTransferKeyframes.clicked.connect(functools.partial(self.rbTransferKeysRelativeToWorldSpaceInstance.transferKeysRelativeToWorldSpace))
		
		#btnBakeKeyframes
		self.btnBakeKeyframes.clicked.connect(functools.partial(self.rbTransferKeysRelativeToWorldSpaceInstance.transferKeysRelativeToWorldSpace, bake = True))
		
		
		
		#btnSetCurrentAnimRange
		self.btnSetCurrentAnimRange.clicked.connect(functools.partial(self.setAnimationRange))
		
		#btnBakeTransformOnly
		self.btnBakeTransformOnly.clicked.connect(functools.partial(self.bakeAnimationTransformOnly))
		
		#btnBake
		self.btnBake.clicked.connect(functools.partial(self.bakeAnimation))
		
		
		
		#PaintFx Hair
		#------------------------------------------------------------------
		
		#btnRefreshNamespacesPaintFxHair
		self.btnRefreshNamespacesPaintFxHair.clicked.connect(functools.partial(self.refreshNamespacesComboboxPaintFxHair))
		
		#btnTransferPaintFxHairAlembic
		self.btnTransferPaintFxHairAlembic.clicked.connect(functools.partial(self.connectToAlembicCache))
		
		#btnTransferPaintFxHairBlendshapes
		self.btnTransferPaintFxHairBlendshapes.clicked.connect(functools.partial(self.transferAnimationByBlendshapes))
		
		
		
		
		#btnPrintPresets
		self.btnPrintPresets.clicked.connect(functools.partial(self.rbApplyPresetToSelectionInstance.printAvailablePresets))
		
		#btnApplyPreset
		self.btnApplyPreset.clicked.connect(functools.partial(self.applyPresetToSelection))
		
		
		
		
		
		#Alembic Import
		#------------------------------------------------------------------
		
		#btnRugbybugAssignShader
		self.btnRugbybugAssignShader.clicked.connect(functools.partial(self.rbAutoShaderAssignmentAndGroupingInstance.assignMaterials, self.rbAutoShaderAssignmentAndGroupingInstance.rugbybugAssignmentDict))
		
		#btnRugbybugGroup
		self.btnRugbybugGroup.clicked.connect(functools.partial(self.rbAutoShaderAssignmentAndGroupingInstance.groupRugbybug))
		
		#btnAntAssignShader
		self.btnAntAssignShader.clicked.connect(functools.partial(self.rbAutoShaderAssignmentAndGroupingInstance.assignMaterials, self.rbAutoShaderAssignmentAndGroupingInstance.antAssignmentDict))
		
		#btnAntGroup
		self.btnAntGroup.clicked.connect(functools.partial(self.rbAutoShaderAssignmentAndGroupingInstance.groupAnt))
		
		#btnFrogAssignShader
		self.btnFrogAssignShader.clicked.connect(functools.partial(self.rbAutoShaderAssignmentAndGroupingInstance.assignMaterials, self.rbAutoShaderAssignmentAndGroupingInstance.frogAssignmentDict))
		
		#btnFrogGroup
		self.btnFrogGroup.clicked.connect(functools.partial(self.rbAutoShaderAssignmentAndGroupingInstance.groupFrog))
		
		#btnChrystalGroup
		self.btnChrystalGroup.clicked.connect(functools.partial(self.rbAutoShaderAssignmentAndGroupingInstance.groupChrystal))
		
		
		
		
	
	
	
	#FootRigA
	#------------------------------------------------------------------
	
	#createFootRigAPosLocators
	def createFootRigAPosLocators(self):
		self.rbRiggingInstance.createFootRigAPosLocators(prefix = self.getFootRigAPrefix())
	
	#createFootRigA
	def createFootRigA(self):
		self.rbRiggingInstance.createFootRigA(prefix = self.getFootRigAPrefix())
	
	
	#getFootRigAPrefix
	def getFootRigAPrefix(self):
		return str(self.leFootRigAPrefix.text())
		
		
		
		
		
	
	
	#FootRigB
	#------------------------------------------------------------------
	
	#createFootRigBPosLocators
	def createFootRigBPosLocators(self):
		self.rbRiggingInstance.createFootRigBPosLocators(prefix = self.getFootRigBPrefix())
	
	#createFootRigB
	def createFootRigB(self):
		self.rbRiggingInstance.createFootRigB(prefix = self.getFootRigBPrefix())
	
	
	#getFootRigBPrefix
	def getFootRigBPrefix(self):
		return str(self.leFootRigBPrefix.text())
		
		
		
		
	
	
	
	#DynamicChain
	#------------------------------------------------------------------
	
	#createDynamicChainPosLocators
	def createDynamicChainPosLocators(self):
		self.rbRiggingInstance.createDynamicChainLocators(prefix = self.getDynamicChainPrefix())
	
	#createDynamicChain
	def createDynamicChain(self):
		self.rbRiggingInstance.createDynamicChain(prefix = self.getDynamicChainPrefix(), jointCount = self.getDynamicChainJointCount())
	
	
	#getDynamicChainPrefix
	def getDynamicChainPrefix(self):
		return str(self.leDynamicChainPrefix.text())
		
		
	#getDynamicChainJointCount
	def getDynamicChainJointCount(self):
		return int(float(str(self.leDynamicChainJointCount.text())))
		
		
	


	#IkFkBlendArm
	#------------------------------------------------------------------
	
	#createIkFkBlendArmLocators
	def createIkFkBlendArmLocators(self):
		self.rbRiggingInstance.createIkFkBlendArmLocators(prefix = self.getIkFkBlendArmPrefix())
	
	#createIkFkBlendArm
	def createIkFkBlendArm(self):
		self.rbRiggingInstance.createIkFkBlendArm(prefix = self.getIkFkBlendArmPrefix())
	
	
	#getIkFkBlendArmPrefix
	def getIkFkBlendArmPrefix(self):
		return str(self.leIkFkBlendArmPrefix.text())
	
	
	
	
	
	
	#DynamicChainFromCurves
	#------------------------------------------------------------------
	
	
	#createDynamicChainFromCurves
	def createDynamicChainFromCurves(self):
		self.rbRiggingInstance.createDynamicChainFromCurves(prefix = self.getDynamicChainFromCurvesPrefix())
	
	
	#getDynamicChainFromCurvesPrefix
	def getDynamicChainFromCurvesPrefix(self):
		return str(self.leDynamicChainFromCurvesPrefix.text())
		
	
	
	
	
	
	
	#BakeAnimation
	#------------------------------------------------------------------
	
	#bakeAnimationTransformOnly
	def bakeAnimationTransformOnly(self):
		
		self.rbBakeAnimationInstance.bakeAnimationTransformOnly(self.getAnimationStartTime(), self.getAnimationEndTime(), self.getLocalSpace())
		
		
	#bakeAnimation
	def bakeAnimation(self):
		
		self.rbBakeAnimationInstance.bakeAnimation(self.getAnimationStartTime(), self.getAnimationEndTime())
		
	
	#setAnimationRange
	def setAnimationRange(self):
		
		self.leAnimationStart.setText(str(pm.playbackOptions(minTime = True, q = True)))
		self.leAnimationEnd.setText(str(pm.playbackOptions(maxTime = True, q = True)))
	
	
	#getAnimationStartTime
	def getAnimationStartTime(self):
		return int(float(str(self.leAnimationStart.text())))
		
	#getAnimationEndTime
	def getAnimationEndTime(self):
		return int(float(str(self.leAnimationEnd.text())))
		
	#getLocalSpace
	def getLocalSpace(self):
		return self.chkbxLocalSpace.isChecked()
		
		
		
		
	
	
	
	
	
	
	#PaintFxHair
	#------------------------------------------------------------------
	
	
	#refreshNamespacesComboboxPaintFxHair
	def refreshNamespacesComboboxPaintFxHair(self):
		
		
		
		#Get namespaceList
		namespacesList = self.rbPaintFxTransferAnimationInstance.getNamespaces()
		
		#Clear and set cmbbxNamespace
		self.comboBoxNamespacesPaintFxHair.clear()
		self.comboBoxNamespacesPaintFxHair.addItems(namespacesList)
		
		
		
	#getNamespacePaintFxHair
	def getNamespacePaintFxHair(self):
		return str(self.comboBoxNamespacesPaintFxHair.currentText())
		
		
	#connectToAlembicCache
	def connectToAlembicCache(self):
		
		self.rbPaintFxTransferAnimationInstance.connectToAlembicCache(self.getNamespacePaintFxHair())
		
		
	#transferAnimationByBlendshapes
	def transferAnimationByBlendshapes(self):
		
		self.rbPaintFxTransferAnimationInstance.transferAnimationByBlendshapes(self.getNamespacePaintFxHair())
	
	
	
	
	
	#applyPresetToSelection
	def applyPresetToSelection(self):
		
		self.rbApplyPresetToSelectionInstance.applyPresetToSelection(self.getPresetName())
	
	
	#getPresetName
	def getPresetName(self):
		return str(self.lePresetName.text())
	
	
	

	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------	
	
	#setStatus
	def setStatus(self, msg):
		self.leStatus.setText(msg)
		
	#getStatus
	def getStatus(self):
		return str(self.leStatus.text())
		
	
	
		
		
		
		
		
		
		
		
		
