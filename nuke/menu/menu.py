


#rugbyBugs menu.py (startup procedures / gui only)
#------------------------------------------------------------------








#Imports
#------------------------------------------------------------------
import nuke
from nukescripts import panels
import functools


#Reload Bool
doReload = True

from rugbyBugs.nuke.rbRenderReconstruct import rbRenderReconstruct
if(doReload): reload(rbRenderReconstruct)

from rugbyBugs.nuke.rugbyBugsNukeInterface import rugbyBugsNukeInterface
if(doReload): reload(rugbyBugsNukeInterface)





#Methods
#------------------------------------------------------------------





#Create RugbyBugs menu (Nodes)
#------------------------------------------------------------------

#Main Menubar
rugbyBugsMainMenu = nuke.menu( 'Nodes' ).addMenu( 'RugbyBugs', icon='\\\\grey09\\rugbybugs\\Production\\Scripts\\deploy\\rugbyBugs\\nuke\\icons\\iconNukeRugbyBugsMain.png' )


#RenderReconstruct Menu
rugbyBugsRenderReconstructMenu = rugbyBugsMainMenu.addMenu('RenderReconstruction')
#cmds
rugbyBugsRenderReconstructMenu.addCommand( 'Reconstruct all Elements', lambda: rbRenderReconstruct.RbRenderReconstruct().reconstructAll())
rugbyBugsRenderReconstructMenu.addCommand( 'Reconstruct Light Elements', lambda: rbRenderReconstruct.RbRenderReconstruct().reconstructLightREs())
rugbyBugsRenderReconstructMenu.addCommand( 'Reconstruct Framebuffer Elements', lambda: rbRenderReconstruct.RbRenderReconstruct().reconstructFramebufferREs())
rugbyBugsRenderReconstructMenu.addCommand( 'Reconstruct Data Elements', lambda: rbRenderReconstruct.RbRenderReconstruct().reconstructDataREs())
rugbyBugsRenderReconstructMenu.addCommand( 'Reconstruct Multi Matte Elements', lambda: rbRenderReconstruct.RbRenderReconstruct().reconstructMultiMatteREs())
rugbyBugsRenderReconstructMenu.addCommand( 'Reconstruct Shadow Elements', lambda: rbRenderReconstruct.RbRenderReconstruct().reconstructShadowREs())




#Create RugbyBugs Ui (Pane)
#------------------------------------------------------------------

#registerWidgetAsPanel
panels.registerWidgetAsPanel('rugbyBugsNukeInterface.RugbyBugsNukeInterface', 'RugbyBugsUi', 'uk.co.thefoundry.NukeTestWindow')







#Import and execute Carls Startup scripts
#------------------------------------------------------------------

#import and execute rbNukeStartupCarl module
try:
	#import
	from rugbyBugs.nuke.rbNukeStartupCarl import rbNukeStartupCarl
	if(doReload): reload(rbNukeStartupCarl)
	
	#execute	
	nuke.addOnScriptLoad(rbNukeStartupCarl.RbNukeStartupCarl().createInitialSetup)
	
	nuke.tprint('Successfully loaded and executed Carls startup scripts')
	
except:
	nuke.tprint('Error loading Carls Nuke startup module')
	
	
	
	
	
	
	
	
	
	
	





