'''
    rbNukeStartupCarl Module
    
        initial Nuke setup for rugbybugs
    
    last edit: 20121210 
    by: Carl
    
    2Do:
		(set shot + version in rr_submit)
'''

import sys, os, nuke

class RbNukeStartupCarl():
	
	
	#Constructor
	def __init__(self):
	
		self.setFavorites()
		self.addFormats()
		self.setProjectSettings()
		
		self.buildMenu()
	
	# set favs in open-file dialog
	def setFavorites(self):
    
		# add project specific shortcuts
		nuke.addFavoriteDir('Desktop', 'C:/Users/' + os.environ['USERNAME'] + '/Desktop')
		nuke.addFavoriteDir('RB','//grey09/rugbybugs/')
		nuke.addFavoriteDir('RB_SHOTS', '//grey09/rugbybugs/Production/2d/comp/')
		nuke.addFavoriteDir('RB_RnD', self.getPersonalRndFolder())
		
		# remove generic favorites
		nuke.removeFavoriteDir("Home")
		nuke.removeFavoriteDir("Root")
		nuke.removeFavoriteDir("Nuke")
		nuke.removeFavoriteDir("Current")
		
	# build path for user specific _RnD favorite
	def getPersonalRndFolder(self):   
		team = {"cschroeter":"carl",
				"efuchs":"emmi",
				"ffricke":"fabian",
				"mseifert":"manuel",
				"mlapp":"martin",
				"mbaeuerle":"matti",
				"slanger":"sascha",
				"twagener":"timm"}
		path = "//grey09/rugbybugs/Production/_Rnd/Rnd." + team[os.environ['USERNAME']]
		return path

	# setting basic project settings 
	def setProjectSettings(self):
		print "test setProjectSettings"
		nuke.Root()['project_directory'].setValue('//grey09/rugbybugs/Production/2d/comp/')
		nuke.Root()['fps'].setValue(24)
		nuke.Root()['format'].setValue('HD')

	# add formats to the list
	def addFormats(self):
		nuke.addFormat( '1920 1038 ITFS_cropped' )
	
	# ROYAL RENDER SUBMIT	
	def rrSubmit_Nuke_5(self):
		nuke.scriptSave()
		rootNode = nuke.toNode('root')
		CompName = rootNode.name()
		rrRoot = os.environ['RR_Root']
		if ((CompName==None) or (len(CompName)==0)):
			return
		if ((sys.platform.lower() == "win32") or (sys.platform.lower() == "win64")):
			os.system(rrRoot+"\\win__rrSubmitter.bat  \""+CompName+"\"")
#			os.system(rrRoot+"\\win__rrSubmitter.bat  \""+CompName+"\" \"CSCN=0~RB\" \"CSHN=0~180\" \"CVN=0~0005\"") #---------------------- SHOT VERSION
		elif (sys.platform.lower() == "darwin"):
			os.system(rrRoot+"/bin/mac/rrSubmitter.app/Contents/MacOS/rrSubmitter  \""+CompName+"\"")
		else:
			os.system(rrRoot+"/lx__rrSubmitter.sh  \""+CompName+"\"")

	def buildMenu(self):
		toolbar = nuke.toolbar("Nodes")
		m =   toolbar.findItem("RugbyBugs")
		m.addCommand( 'submit to RR', 'rbNukeStartupCarl.RbNukeStartupCarl().rrSubmit_Nuke_5()', '^r')
