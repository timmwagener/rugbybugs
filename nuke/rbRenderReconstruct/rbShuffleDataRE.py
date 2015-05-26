

#rbShuffleDataRE Module
#------------------------------------------------------------------

'''
Description:
Reconstructs the data render elements (with exception of rbEtAmbOcc) of one or several read files according to our pipeline standards
'''

'''
ToDo:

'''



#Imports
#------------------------------------------------------------------
import nuke, nukescripts




#RbShuffleDataRE class
#------------------------------------------------------------------

class RbShuffleDataRE():
	
	#Constructor
	def __init__(self):
		
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		self.backdropColorData = [0.68,1,0.36]
	

	
	
	
	#Toplevel Methods
	#------------------------------------------------------------------
	
	#reconstructDataRenderElements
	def reconstructDataRenderElements(self, node):
		
		#check if node is read node
		if not(self.nodetypeMatches(node, 'Read')):
			print('%s is not of type Read' %(node.name()))
			return False
				
			
		#Reconstruct data elements
		#------------------------------------------------------------------
			
		dataShuffleNodesList = []
			
		#check if rbNormals channel exists and if so, shuffle it
		if(self.getLayers(node, 'rbNormals')): dataShuffleNodesList.append(self.shuffleRE(node, 'rbNormals'))
		
		#check if rbBumpNormals channel exists and if so, shuffle it
		if(self.getLayers(node, 'rbBumpNormals')): dataShuffleNodesList.append(self.shuffleRE(node, 'rbBumpNormals'))
			
		#check if rbEtSTMap channel exists and if so, shuffle it
		if(self.getLayers(node, 'rbEtSTMap')): dataShuffleNodesList.append(self.shuffleRE(node, 'rbEtSTMap'))
			
		#check if rbEtWorldPos channel exists and if so, shuffle it
		if(self.getLayers(node, 'rbEtWorldPos')): dataShuffleNodesList.append(self.shuffleRE(node, 'rbEtWorldPos'))
			
		#check if rbVelocityFiltered channel exists and if so, shuffle it
		if(self.getLayers(node, 'rbVelocityFiltered')): dataShuffleNodesList.append(self.shuffleRE(node, 'rbVelocityFiltered'))
		
		#check if rbVelocityUnfiltered channel exists and if so, shuffle it
		if(self.getLayers(node, 'rbVelocityUnfiltered')): dataShuffleNodesList.append(self.shuffleRE(node, 'rbVelocityUnfiltered'))
		
		#check if depth channel exists and if so, shuffle it
		if(self.getLayers(node, 'rbZDepth')): dataShuffleNodesList.append(self.shuffleDepthRE(node, 'rbZDepthFiltered'))
		if(self.getLayers(node, 'rbZDepth')): dataShuffleNodesList.append(self.shuffleDepthRE(node, 'rbZDepthUnfiltered'))
		
		#check if rbRenderId channel exists and if so, shuffle it
		if(self.getLayers(node, 'rbRenderId')): dataShuffleNodesList.append(self.shuffleRE(node, 'rbRenderId'))
			
			
			
		#check if dataShuffleNodeList has content to add backdrop
		if(len(dataShuffleNodesList) > 0):		
			#create backdrop
			backdrop = self.createBackdrop(dataShuffleNodesList, self.rgbToHexString(self.backdropColorData))
			backdrop.knob('label').setValue(node.name() +'_dataPasses')
			backdrop.knob('note_font_size').setValue(20)
			
		
		
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	#shuffleRE
	def shuffleRE(self, node, layer):
		
		#shuffleRE
		shuffleRE = nuke.nodes.Shuffle(label = layer +'_rbg', inputs = [node])
		shuffleRE['in'].setValue( layer )
		shuffleRE['in2'].setValue( 'rgba' )
		shuffleRE['alpha'].setValue( 'alpha2' )
		shuffleRE['postage_stamp'].setValue( True )
		shuffleRE['hide_input'].setValue(True)
		
		return shuffleRE
		
		
	#shuffleDepthRE
	def shuffleDepthRE(self, node, layer):
		
		#rbZDepthFiltered
		if(layer == 'rbZDepthFiltered'):
		#shuffleDepthRE
			shuffleDepthRE = nuke.nodes.Shuffle(label = 'rbZDepthFiltered_rbg', inputs = [node])
			shuffleDepthRE['in'].setValue( 'rbZDepth' )
			
			shuffleDepthRE['red'].setValue( 'red' )
			shuffleDepthRE['green'].setValue( 'red' )
			shuffleDepthRE['blue'].setValue( 'red' )
			shuffleDepthRE['alpha'].setValue( 'black' )
			
			shuffleDepthRE['postage_stamp'].setValue( True )
			shuffleDepthRE['hide_input'].setValue(True)
			
			
			
			
		#rbZDepthUnfiltered
		elif(layer == 'rbZDepthUnfiltered'):
			#shuffleDepthRE
			shuffleDepthRE = nuke.nodes.Shuffle(label = 'rbZDepthUnfiltered_rbg', inputs = [node])
			shuffleDepthRE['in'].setValue( 'rbZDepth' )
			
			shuffleDepthRE['red'].setValue( 'green' )
			shuffleDepthRE['green'].setValue( 'green' )
			shuffleDepthRE['blue'].setValue( 'green' )
			shuffleDepthRE['alpha'].setValue( 'black' )
			
			shuffleDepthRE['postage_stamp'].setValue( True )
			shuffleDepthRE['hide_input'].setValue(True)
			
		
		return shuffleDepthRE
		
		

		
		
	
	
	#Shared Methods
	#------------------------------------------------------------------
	
	
	
	#nodetypeMatches
	def nodetypeMatches(self, node, nodetype):
		
		if(node.Class() == nodetype): return True
		return False
		
	
	
	#getLayers
	def getLayers(self, node, prefix = False):
		
		#Get channelsList
		channelsList = node.channels()
		
		#iterate over channelslist, split name and append layer
		layerList = []
		for channel in channelsList:
			layer = channel.split('.')[0]
			layerList.append(layer)
			
		#remove duplicates
		layerList = list(set(layerList))
		
		
		#If prefix is set, iterate again to return all layers starting with prefix
		if(prefix):
			layerListPrefix = []
			prefixLength = len(prefix)
			for layer in layerList:
				if(layer[0:prefixLength] == prefix): layerListPrefix.append(layer)
				
			return layerListPrefix
		
		return layerList
		
	
	
	#createBackdrop
	def createBackdrop(self, nodesList, hexColor):
		
		#deselect all
		self.deselectAll()
		
		#Select nodesList in viewport
		for node in nodesList:
			node.setSelected(True)
		
		
		#nukescripts autobackdrop
		backdrop = nukescripts.autoBackdrop()
		backdrop['tile_color'].setValue(hexColor)
		
		return backdrop
		
		
	
	#deselectAll
	def deselectAll(self):
		#Select All to invert the selection XD
		nuke.selectAll()
		nuke.invertSelection() 
		
		

	#rgbToHexString
	def rgbToHexString(self, colorList = [0,0,0]):
		
		#getColors
		r = colorList[0]
		g = colorList[1]
		b = colorList[2]
		
		#get hexColor
		hexColor = int('%02x%02x%02x%02x' % (r*255,g*255,b*255,1),16)
		
		return hexColor	
	
	
	
	
	
	
	