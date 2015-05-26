




#rbChrystalGui Interface Module
#------------------------------------------------------------------

'''
Interface for ChrystalGui rig
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

from lib import rbChrystalGuiFunctionality
if(doReload): reload(rbChrystalGuiFunctionality)

from lib import MayaFunctionality
if(doReload): reload(MayaFunctionality)




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
uiFilePath = os.path.join(os.path.dirname(__file__), 'media\\rbChrystalGuiUi.ui')
uiClassesList = uic.loadUiType(uiFilePath)





#RbChrystalGui class
#------------------------------------------------------------------
class RbChrystalGui(uiClassesList[0], uiClassesList[1]):
	
	
	#Constructor
	#------------------------------------------------------------------	
	def __init__(self, parent = getMayaQMainWindow()):
		super(RbChrystalGui, self).__init__(parent)
		
		
		#Instance Vars
		#------------------------------------------------------------------
		
		self.verbose = True
		self.windowTitle = 'rbChrystalGui'
		self.versionNumber = 0.1
		
		#rbChrystalGuiFunctionalityInstance
		self.rbChrystalGuiFunctionalityInstance = rbChrystalGuiFunctionality.RbChrystalGuiFunctionality()
		
		
		
		#Dockability
		self.dockIt = True
		self.dockArea = 'left'
		self.label = self.windowTitle +' ' +str(self.versionNumber)
		
		
		#Startup Routine
		#------------------------------------------------------------------
		
		#setupUi
		self.setupUi(self)
		self.setWindowTitle(self.windowTitle +' ' +str(self.versionNumber))
		
		#ConnectUi
		self.connectUi()
		
		#makeDockable
		if(self.dockIt):
			windowWidth = self.geometry().width()
			MayaFunctionality.makeDockable(self, self.dockArea, windowWidth, self.label)
		
		
		#show Ui
		self.show()
		
	
	
	
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	#connectUi
	def connectUi(self):
		
		#btnNamespace
		self.btnNamespace.clicked.connect(self.refreshNamespacesCombobox)
		
		#btnSelectAllPieceManips
		self.btnSelectAllPieceManips.clicked.connect(self.selectAllPieceManipulators)
		
		
		#Parentspace Switching
		self.btnParentspaceChrystal.clicked.connect(functools.partial(self.rbChrystalGuiFunctionalityInstance.switchParentspace, weightChrystal = 1, weightWorld = 0, weightWildcard1 = 0 , weightWildcard2 = 0 , weightWildcard3 = 0 , weightWildcard4 = 0))
		self.btnParentspaceWorld.clicked.connect(functools.partial(self.rbChrystalGuiFunctionalityInstance.switchParentspace, weightChrystal = 0, weightWorld = 1, weightWildcard1 = 0 , weightWildcard2 = 0 , weightWildcard3 = 0 , weightWildcard4 = 0))
		self.btnParentspaceWildcard1.clicked.connect(functools.partial(self.rbChrystalGuiFunctionalityInstance.switchParentspace, weightChrystal = 0, weightWorld = 0, weightWildcard1 = 1 , weightWildcard2 = 0 , weightWildcard3 = 0 , weightWildcard4 = 0))
		self.btnParentspaceWildcard2.clicked.connect(functools.partial(self.rbChrystalGuiFunctionalityInstance.switchParentspace, weightChrystal = 0, weightWorld = 0, weightWildcard1 = 0 , weightWildcard2 = 1 , weightWildcard3 = 0 , weightWildcard4 = 0))
		self.btnParentspaceWildcard3.clicked.connect(functools.partial(self.rbChrystalGuiFunctionalityInstance.switchParentspace, weightChrystal = 0, weightWorld = 0, weightWildcard1 = 0 , weightWildcard2 = 0 , weightWildcard3 = 1 , weightWildcard4 = 0))
		self.btnParentspaceWildcard4.clicked.connect(functools.partial(self.rbChrystalGuiFunctionalityInstance.switchParentspace, weightChrystal = 0, weightWorld = 0, weightWildcard1 = 0 , weightWildcard2 = 0 , weightWildcard3 = 0 , weightWildcard4 = 1))
	
		
		#SelectionButtons
		self.btnSelectPieceManip0.clicked.connect(functools.partial(self.selectPieceManipulator, 0))
		self.btnSelectPieceManip1.clicked.connect(functools.partial(self.selectPieceManipulator, 1))
		self.btnSelectPieceManip2.clicked.connect(functools.partial(self.selectPieceManipulator, 2))
		self.btnSelectPieceManip3.clicked.connect(functools.partial(self.selectPieceManipulator, 3))
		self.btnSelectPieceManip4.clicked.connect(functools.partial(self.selectPieceManipulator, 4))
		self.btnSelectPieceManip5.clicked.connect(functools.partial(self.selectPieceManipulator, 5))
		self.btnSelectPieceManip6.clicked.connect(functools.partial(self.selectPieceManipulator, 6))
		self.btnSelectPieceManip7.clicked.connect(functools.partial(self.selectPieceManipulator, 7))
		self.btnSelectPieceManip8.clicked.connect(functools.partial(self.selectPieceManipulator, 8))
		self.btnSelectPieceManip9.clicked.connect(functools.partial(self.selectPieceManipulator, 9))
		
		self.btnSelectPieceManip10.clicked.connect(functools.partial(self.selectPieceManipulator, 10))
		self.btnSelectPieceManip11.clicked.connect(functools.partial(self.selectPieceManipulator, 11))
		self.btnSelectPieceManip12.clicked.connect(functools.partial(self.selectPieceManipulator, 12))
		self.btnSelectPieceManip13.clicked.connect(functools.partial(self.selectPieceManipulator, 13))
		self.btnSelectPieceManip14.clicked.connect(functools.partial(self.selectPieceManipulator, 14))
		self.btnSelectPieceManip15.clicked.connect(functools.partial(self.selectPieceManipulator, 15))
		self.btnSelectPieceManip16.clicked.connect(functools.partial(self.selectPieceManipulator, 16))
		self.btnSelectPieceManip17.clicked.connect(functools.partial(self.selectPieceManipulator, 17))
		self.btnSelectPieceManip18.clicked.connect(functools.partial(self.selectPieceManipulator, 18))
		self.btnSelectPieceManip19.clicked.connect(functools.partial(self.selectPieceManipulator, 19))
		
		self.btnSelectPieceManip20.clicked.connect(functools.partial(self.selectPieceManipulator, 20))
		self.btnSelectPieceManip21.clicked.connect(functools.partial(self.selectPieceManipulator, 21))
		self.btnSelectPieceManip22.clicked.connect(functools.partial(self.selectPieceManipulator, 22))
		self.btnSelectPieceManip23.clicked.connect(functools.partial(self.selectPieceManipulator, 23))
		self.btnSelectPieceManip24.clicked.connect(functools.partial(self.selectPieceManipulator, 24))
		self.btnSelectPieceManip25.clicked.connect(functools.partial(self.selectPieceManipulator, 25))
		self.btnSelectPieceManip26.clicked.connect(functools.partial(self.selectPieceManipulator, 26))
		self.btnSelectPieceManip27.clicked.connect(functools.partial(self.selectPieceManipulator, 27))
		self.btnSelectPieceManip28.clicked.connect(functools.partial(self.selectPieceManipulator, 28))
		self.btnSelectPieceManip29.clicked.connect(functools.partial(self.selectPieceManipulator, 29))
		
		self.btnSelectPieceManip30.clicked.connect(functools.partial(self.selectPieceManipulator, 30))
		self.btnSelectPieceManip31.clicked.connect(functools.partial(self.selectPieceManipulator, 31))
		self.btnSelectPieceManip32.clicked.connect(functools.partial(self.selectPieceManipulator, 32))
		self.btnSelectPieceManip33.clicked.connect(functools.partial(self.selectPieceManipulator, 33))
		self.btnSelectPieceManip34.clicked.connect(functools.partial(self.selectPieceManipulator, 34))
		self.btnSelectPieceManip35.clicked.connect(functools.partial(self.selectPieceManipulator, 35))
		self.btnSelectPieceManip36.clicked.connect(functools.partial(self.selectPieceManipulator, 36))
		self.btnSelectPieceManip37.clicked.connect(functools.partial(self.selectPieceManipulator, 37))
		self.btnSelectPieceManip38.clicked.connect(functools.partial(self.selectPieceManipulator, 38))
		self.btnSelectPieceManip39.clicked.connect(functools.partial(self.selectPieceManipulator, 39))
		
		self.btnSelectPieceManip40.clicked.connect(functools.partial(self.selectPieceManipulator, 40))
		self.btnSelectPieceManip41.clicked.connect(functools.partial(self.selectPieceManipulator, 41))
		self.btnSelectPieceManip42.clicked.connect(functools.partial(self.selectPieceManipulator, 42))
		self.btnSelectPieceManip43.clicked.connect(functools.partial(self.selectPieceManipulator, 43))
		self.btnSelectPieceManip44.clicked.connect(functools.partial(self.selectPieceManipulator, 44))
		self.btnSelectPieceManip45.clicked.connect(functools.partial(self.selectPieceManipulator, 45))
		self.btnSelectPieceManip46.clicked.connect(functools.partial(self.selectPieceManipulator, 46))
		self.btnSelectPieceManip47.clicked.connect(functools.partial(self.selectPieceManipulator, 47))
		self.btnSelectPieceManip48.clicked.connect(functools.partial(self.selectPieceManipulator, 48))
		self.btnSelectPieceManip49.clicked.connect(functools.partial(self.selectPieceManipulator, 49))
		
		self.btnSelectPieceManip50.clicked.connect(functools.partial(self.selectPieceManipulator, 50))
	
		
	
		#btnZeroSelectedManips
		self.btnZeroSelectedManips.clicked.connect(functools.partial(self.rbChrystalGuiFunctionalityInstance.zeroSelectedManipulators))
		
		
		#btnSelectChrystalManip
		self.btnSelectChrystalManip.clicked.connect(functools.partial(self.selectSpecialManipulator, 'manip_rolling_ball'))
		
		#btnSelectWorldManip
		self.btnSelectWorldManip.clicked.connect(functools.partial(self.selectSpecialManipulator, 'world_parent_dummy_loc'))
		
		#btnSelectWildcard1Manip
		self.btnSelectWildcard1Manip.clicked.connect(functools.partial(self.selectSpecialManipulator, 'manip_wildcard_1'))
		#btnSelectWildcard2Manip
		self.btnSelectWildcard2Manip.clicked.connect(functools.partial(self.selectSpecialManipulator, 'manip_wildcard_2'))
		#btnSelectWildcard3Manip
		self.btnSelectWildcard3Manip.clicked.connect(functools.partial(self.selectSpecialManipulator, 'manip_wildcard_3'))
		#btnSelectWildcard4Manip
		self.btnSelectWildcard4Manip.clicked.connect(functools.partial(self.selectSpecialManipulator, 'manip_wildcard_4'))
		
		
		#btnParentspaceKey
		self.btnParentspaceKey.clicked.connect(functools.partial(self.rbChrystalGuiFunctionalityInstance.keyframeParentspaceForSelectedManipulators))
		
		#btnSelectParentConstraint
		self.btnSelectParentConstraint.clicked.connect(functools.partial(self.rbChrystalGuiFunctionalityInstance.selectParentConstraintForSelectedManipulators))
		
		
		#btnTogglePieceViz
		self.btnTogglePieceViz.clicked.connect(functools.partial(self.togglePieceVisibility))
		
		#btnUnhideAllPieces
		self.btnUnhideAllPieces.clicked.connect(functools.partial(self.unhideAllPieces))
		
		#btnToggleInnerChrystalViz
		self.btnToggleInnerChrystalViz.clicked.connect(functools.partial(self.toggleInnerChrystalVisibility))
		
		#btnToggleMeshlightsViz
		self.btnToggleMeshlightsViz.clicked.connect(functools.partial(self.toggleMeshlightsVisibility))
		
		#btnToggleSmoothMeshPreviewForSelected
		self.btnToggleSmoothMeshPreviewForSelected.clicked.connect(functools.partial(self.toggleSmoothMeshPreviewForSelected))
		
		#btnUnsmoothAll
		self.btnUnsmoothAll.clicked.connect(functools.partial(self.unsmoothAll))
	
	
	
	
	
	
	
	
	
	
	#selectPieceManipulator
	def selectPieceManipulator(self, index):
		self.rbChrystalGuiFunctionalityInstance.selectPieceManipulator(self.getNamespace(), index, self.getSelectionAdditive())
	
	#selectAllPieceManipulators
	def selectAllPieceManipulators(self):
		self.rbChrystalGuiFunctionalityInstance.selectAllPieceManipulators(self.getNamespace())
	
	#selectSpecialManipulator
	def selectSpecialManipulator(self, manipName):
		self.rbChrystalGuiFunctionalityInstance.selectSpecialManipulator(self.getNamespace(), manipName)
	
	
	#togglePieceVisibility
	def togglePieceVisibility(self):
		self.rbChrystalGuiFunctionalityInstance.togglePieceVisibility(self.getNamespace())
		
	#unhideAllPieces
	def unhideAllPieces(self):
		self.rbChrystalGuiFunctionalityInstance.unhideAllPieces(self.getNamespace())
	
	#toggleInnerChrystalVisibility
	def toggleInnerChrystalVisibility(self):
		self.rbChrystalGuiFunctionalityInstance.toggleGroupsVisibility(self.getNamespace(), ['inner_chrystal', 'inner_chrystal_rockremainder_grp', 'inner_chrystal_logo', 'manip_inner_chrystal_logo'])
		
	#toggleMeshlightsVisibility
	def toggleMeshlightsVisibility(self):
		self.rbChrystalGuiFunctionalityInstance.toggleGroupsVisibility(self.getNamespace(), ['chrystal_meshlights_grp'])
	
	#toggleSmoothMeshPreviewForSelected
	def toggleSmoothMeshPreviewForSelected(self):
		self.rbChrystalGuiFunctionalityInstance.toggleSmoothMeshPreviewForSelected(self.getNamespace())
		
	#unsmoothAll
	def unsmoothAll(self):
		self.rbChrystalGuiFunctionalityInstance.unsmoothAll(self.getNamespace())
	
	
	
	
	
	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------

	
	#refreshNamespacesCombobox
	def refreshNamespacesCombobox(self):
		
		#get Namespaces List
		namespacesList = self.rbChrystalGuiFunctionalityInstance.getNamespaces()
		
		#clear and set combobox
		self.cmbboxNamespace.clear()
		self.cmbboxNamespace.addItems(namespacesList)
		
	
	#getNamespace
	def getNamespace(self):
		return str(self.cmbboxNamespace.currentText())
	

	
	#getSelectionAdditive
	def getSelectionAdditive(self):
		return self.chkbxSelectionAdditive.isChecked()
	

	



#Test Module
#------------------------------------------------------------------
'''

from rugbyBugs.maya.rbChrystalGui import rbChrystalGui

doReload = True
if(doReload): reload(rbChrystalGui)

rbChrystalGuiInstance = rbChrystalGui.RbChrystalGui()


'''