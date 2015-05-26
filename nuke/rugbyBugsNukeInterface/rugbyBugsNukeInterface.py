





#rugbyBugsNukeInterface Module
#------------------------------------------------------------------


'''
Interface for all Rugby Bugs Nuke Tools
'''

'''
ToDo:

'''


#Imports
#------------------------------------------------------------------
from PySide import QtGui, QtCore, QtUiTools
import sys, os
import functools

#Import variable
doReload = True

#rbRenderReconstruct
from rugbyBugs.nuke.rbRenderReconstruct import rbRenderReconstruct
if(doReload):reload(rbRenderReconstruct)


#Add path of ressource_rc.py and import
#------------------------------------------------------------------
ressourceFilePath = os.path.join(os.path.dirname(__file__), 'media')
sys.path.append(ressourceFilePath)
import rugbyBugsNukeInterfaceRessources_rc
if(doReload):reload(rugbyBugsNukeInterfaceRessources_rc)



#RugbyBugsNukeInterface class
#------------------------------------------------------------------

class RugbyBugsNukeInterface(QtGui.QWidget):
	
	#Constructor
	def __init__(self, parent = None):
		super(RugbyBugsNukeInterface, self).__init__(parent)
		
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = False
		self.uiFilePath = None
		self.uiFileWidget = None
		
		
		#Init procedure
		#------------------------------------------------------------------
		
		#Get path to .ui file
		self.uiFilePath = os.path.join(os.path.dirname(__file__), 'media\\rugbyBugsNukeInterfaceUi.ui')
		
		#Create Widget from Ui File
		self.createWidgetFromUiFile(self.uiFilePath)
		
		#setUiInstanceVars
		self.setUiInstanceVars()
		
		#connectUi
		self.connectUi()
		
		#Configure Instance and show
		self.configureInstance()
		
		
		
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	#createWidgetFromUiFile
	def createWidgetFromUiFile(self, uiFilePath):
		#Create widget from ui file
		loader = QtUiTools.QUiLoader()
		#file to load in as unicode obj
		file = QtCore.QFile(uiFilePath)
		file.open(QtCore.QFile.ReadOnly)
		#Create Widget
		uiFileWidget = loader.load(file, self)
		#close File
		file.close()
	
	
	
	
	#setUiInstanceVars
	def setUiInstanceVars(self):
		
		#Form Widget
		self.uiFileWidget = self.findChild(QtGui.QWidget, 'Form')
		
		#leStatus
		self.leStatus = self.uiFileWidget.findChild(QtGui.QLineEdit, 'leStatus')
		
		#btnReconstructAll
		self.btnReconstructAll = self.uiFileWidget.findChild(QtGui.QPushButton, 'btnReconstructAll')
		#btnReconstructLight
		self.btnReconstructLight = self.uiFileWidget.findChild(QtGui.QPushButton, 'btnReconstructLight')
		#btnReconstructFramebufferContributions
		self.btnReconstructFramebufferContributions = self.uiFileWidget.findChild(QtGui.QPushButton, 'btnReconstructFramebufferContributions')
		#btnReconstructDataPasses
		self.btnReconstructDataPasses = self.uiFileWidget.findChild(QtGui.QPushButton, 'btnReconstructDataPasses')
		#btnReconstructMultiMattes
		self.btnReconstructMultiMattes = self.uiFileWidget.findChild(QtGui.QPushButton, 'btnReconstructMultiMattes')
		#btnReconstructShadowPasses
		self.btnReconstructShadowPasses = self.uiFileWidget.findChild(QtGui.QPushButton, 'btnReconstructShadowPasses')
	
	
	
	
	#connectUi
	def connectUi(self):
		
		#Connect btnReconstructAll
		self.btnReconstructAll.clicked.connect(functools.partial(rbRenderReconstruct.RbRenderReconstruct().reconstructAll, self.setStatus))
		
		#Connect btnReconstructLight
		self.btnReconstructLight.clicked.connect(functools.partial(rbRenderReconstruct.RbRenderReconstruct().reconstructLightREs, self.setStatus))
		
		#Connect btnReconstructFramebufferContributions
		self.btnReconstructFramebufferContributions.clicked.connect(functools.partial(rbRenderReconstruct.RbRenderReconstruct().reconstructFramebufferREs, self.setStatus))
		
		#Connect btnReconstructDataPasses
		self.btnReconstructDataPasses.clicked.connect(functools.partial(rbRenderReconstruct.RbRenderReconstruct().reconstructDataREs, self.setStatus))
		
		#Connect btnReconstructMultiMattes
		self.btnReconstructMultiMattes.clicked.connect(functools.partial(rbRenderReconstruct.RbRenderReconstruct().reconstructMultiMatteREs, self.setStatus))
		
		#Connect btnReconstructShadowPasses
		self.btnReconstructShadowPasses.clicked.connect(functools.partial(rbRenderReconstruct.RbRenderReconstruct().reconstructShadowREs, self.setStatus))
		
	
	
	
	#configureInstance
	def configureInstance(self):
		
		#Embed created ui file in Layout
		lyt = QtGui.QVBoxLayout()
		lyt.addWidget(self.uiFileWidget)
		self.setLayout(lyt)
		
		#Configure instance size Policies
		self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
		self.uiFileWidget.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
		

	
	
	
	
	#get & Set Methods
	#------------------------------------------------------------------	
	
	#setStatus
	def setStatus(self, msg):
		self.leStatus.setText(msg)
		
	#getStatus
	def getStatus(self):
		return str(self.leStatus.text())
		
		


#Create Instance TMP
#------------------------------------------------------------------
'''
from rugbyBugs.nuke.rugbyBugsNukeInterface import rugbyBugsNukeInterface
rugbyBugsNukeInterfaceInstance = rugbyBugsNukeInterface.RugbyBugsNukeInterface()
'''
		
		
		
		
		

		