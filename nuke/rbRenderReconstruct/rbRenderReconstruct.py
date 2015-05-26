





#rbRenderReconstruct Module
#------------------------------------------------------------------


'''
Reconstructs the rugbyBugs multichannel imagesequences according to our pipeline standards
'''

'''
ToDo:

'''


#Imports
#------------------------------------------------------------------
import sys, os
import nuke



doReload = True

#rbShuffleLightRE
from rugbyBugs.nuke.rbRenderReconstruct import rbShuffleLightRE
if(doReload): reload(rbShuffleLightRE)

#rbShuffleDataRE
from rugbyBugs.nuke.rbRenderReconstruct import rbShuffleDataRE
if(doReload): reload(rbShuffleDataRE)

#rbShuffleFramebufferRE
from rugbyBugs.nuke.rbRenderReconstruct import rbShuffleFramebufferRE
if(doReload): reload(rbShuffleFramebufferRE)

#rbShuffleMmRE
from rugbyBugs.nuke.rbRenderReconstruct import rbShuffleMmRE
if(doReload): reload(rbShuffleMmRE)

#rbShuffleShadowRE
from rugbyBugs.nuke.rbRenderReconstruct import rbShuffleShadowRE
if(doReload): reload(rbShuffleShadowRE)




#RbRenderReconstruct class
#------------------------------------------------------------------

class RbRenderReconstruct():
	
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#------------------------------------------------------------------
		self.verbose = True
		
	
	
	
	
	#Methods
	#------------------------------------------------------------------
	
	
	
	
	#reconstructLightREs
	def reconstructLightREs(self, setStatus = False):
		
		try:
		
			#get selected nodes
			nodesList = nuke.selectedNodes()
			
			#check if node selected
			if not(len(nodesList)):
				print('No nodes selected')
				#setStatus if not False
				if(setStatus): setStatus('No nodes selected')
				return False
			
			#iterate selected nodes and rebuild all passes
			for node in nodesList:
				#reconstruct
				rbShuffleLightRE.RbShuffleLightRE().reconstructLightRenderElements(node)
				
			#setStatus if not False
			if(setStatus): setStatus('Light Elements successfully rebuilt')
		
		except:
			#setStatus if not False
			if(setStatus): setStatus('Error rebuilding Light Elements')
		
	
	
	
	
	#reconstructDataREs
	def reconstructDataREs(self, setStatus = False):
		
		try:
			#get selected nodes
			nodesList = nuke.selectedNodes()
			
			#check if node selected
			if not(len(nodesList)):
				print('No nodes selected')
				#setStatus if not False
				if(setStatus): setStatus('No nodes selected')
				return False
			
			#iterate selected nodes and rebuild all passes
			for node in nodesList:
				#reconstruct
				rbShuffleDataRE.RbShuffleDataRE().reconstructDataRenderElements(node)
				
			#setStatus if not False
			if(setStatus): setStatus('Data Elements successfully rebuilt')
		
		except:
			#setStatus if not False
			if(setStatus): setStatus('Error rebuilding Data Elements')
	
	
	
	#reconstructFramebufferREs
	def reconstructFramebufferREs(self, setStatus = False):
		
		try:
			#get selected nodes
			nodesList = nuke.selectedNodes()
			
			#check if node selected
			if not(len(nodesList)):
				print('No nodes selected')
				#setStatus if not False
				if(setStatus): setStatus('No nodes selected')
				return False
			
			#iterate selected nodes and rebuild all passes
			for node in nodesList:
				#reconstruct
				rbShuffleFramebufferRE.RbShuffleFramebufferRE().reconstructFramebufferRenderElements(node)
			
			#setStatus if not False
			if(setStatus): setStatus('Framebuffer Elements successfully rebuilt')
		
		except:
			#setStatus if not False
			if(setStatus): setStatus('Error rebuilding Framebuffer Elements')
	
	
	
	
	#reconstructMultiMatteREs
	def reconstructMultiMatteREs(self, setStatus = False):
		
		try:
			#get selected nodes
			nodesList = nuke.selectedNodes()
			
			#check if node selected
			if not(len(nodesList)):
				print('No nodes selected')
				#setStatus if not False
				if(setStatus): setStatus('No nodes selected')
				return False
			
			#iterate selected nodes and rebuild all passes
			for node in nodesList:
				#reconstruct
				rbShuffleMmRE.RbShuffleMmRE().reconstructMultiMatteRenderElements(node)
				
			#setStatus if not False
			if(setStatus): setStatus('Multi Mattes successfully rebuilt')
		
		except:
			#setStatus if not False
			if(setStatus): setStatus('Error rebuilding Multi Matte Elements')
			
			
			
	
	#reconstructShadowREs
	def reconstructShadowREs(self, setStatus = False):
		
		try:
			#get selected nodes
			nodesList = nuke.selectedNodes()
			
			#check if node selected
			if not(len(nodesList)):
				print('No nodes selected')
				#setStatus if not False
				if(setStatus): setStatus('No nodes selected')
				return False
			
			#iterate selected nodes and rebuild all passes
			for node in nodesList:
				#reconstruct
				rbShuffleShadowRE.RbShuffleShadowRE().reconstructShadowRenderElements(node)
				
			#setStatus if not False
			if(setStatus): setStatus('Shadow Elements successfully rebuilt')
		
		except:
			#setStatus if not False
			if(setStatus): setStatus('Error rebuilding Shadow Elements')
		
	
	
	
	
	#reconstructAll
	def reconstructAll(self, setStatus = False):
		
		#get selected nodes
		nodesList = nuke.selectedNodes()
		
		#check if node selected
		if not(len(nodesList)):
			print('No nodes selected')
			#setStatus if not False
			if(setStatus): setStatus('No Nodes Selected')
			return False
		
		
		#outputDotList
		outputDotList = []
		
		#iterate selected nodes and rebuild all passes
		for node in nodesList:
		
			
			#check if node is read node
			if not(self.nodetypeMatches(node, 'Read')):
				print('%s is not of type Read' %(node.name()))
				#setStatus if not False
				if(setStatus): setStatus('%s is not of type Read' %(node.name()))
				continue
			
			
			#mergeList
			mergeNodeList = []
			
			
			#recreateLightREs
			mergeNodeList.append(rbShuffleLightRE.RbShuffleLightRE().reconstructLightRenderElements(node))
			
			#recreateFramebufferREs
			mergeNodeList.append(rbShuffleFramebufferRE.RbShuffleFramebufferRE().reconstructFramebufferRenderElements(node))
			
			#recreateDataREs
			rbShuffleDataRE.RbShuffleDataRE().reconstructDataRenderElements(node)
			
			#recreateMultiMattes
			rbShuffleMmRE.RbShuffleMmRE().reconstructMultiMatteRenderElements(node)
			
			#recreateShadowREs
			rbShuffleShadowRE.RbShuffleShadowRE().reconstructShadowRenderElements(node)
			
			
			#trim mergeNodeList from None entries
			mergeNodeListTemp = []
			for item in mergeNodeList:
				if(item):mergeNodeListTemp.append(item)
				
			mergeNodeList = mergeNodeListTemp
			
		
			#Add all Passes of single layer (except data)
			#------------------------------------------------------------------
			
			#check if node contains different contributions to merge (light or framebuffer)
			if(len(mergeNodeList) > 0):
			
				#addFramebufferContributions
				addFramebufferContributionsSingleLayer =  nuke.nodes.Merge2()
				addFramebufferContributionsSingleLayer.knob('operation').setValue('plus')
				addFramebufferContributionsSingleLayer.knob('Achannels').setValue('rgb')
				
				#position add node under last reconstructed element merge node
				posX = mergeNodeList[-1].xpos()
				posY = mergeNodeList[-1].ypos()
				offsetY = 60
				posY = posY + offsetY
				addFramebufferContributionsSingleLayer.setXYpos(posX, posY)
				
				#iterate through mergeList and connect to addFramebufferContributionsSingleLayer
				for index in range(0,len(mergeNodeList)):
					#if index is not 0 or 1 increment index for input pipe
					if(index == 0 or index == 1):addFramebufferContributionsSingleLayer.setInput(index, mergeNodeList[index])
					else:addFramebufferContributionsSingleLayer.setInput(index+1, mergeNodeList[index])
				
				
				#premultCompleteLayer
				premultCompleteLayer = nuke.nodes.Premult()
				premultCompleteLayer.setInput(0,addFramebufferContributionsSingleLayer)
				
				
				
				#outputDot
				outputDot = nuke.nodes.Dot(label = node.name() +'_rgb_OUT')
				outputDot.setInput(0, premultCompleteLayer)
				outputDotList.append(outputDot)
			
			
		
		
		#Add all Layers if more than on read was selected
		#------------------------------------------------------------------
		
		#check if outputDotList contains more than 1
		if(len(outputDotList) > 1):
			
			#addFramebufferContributionsAllLayer
			addFramebufferContributionsAllLayer =  nuke.nodes.Merge2()
			addFramebufferContributionsAllLayer.knob('operation').setValue('plus')
			addFramebufferContributionsAllLayer.knob('Achannels').setValue('rgb')
			
			#position add node under last reconstructed element merge node
			posX = outputDotList[-1].xpos()
			posY = outputDotList[-1].ypos()
			offsetY = 60
			posY = posY + offsetY
			addFramebufferContributionsAllLayer.setXYpos(posX, posY)
			
			#iterate through mergeList and connect to addFramebufferContributionsSingleLayer
			for index in range(0,len(outputDotList)):
				#if index is not 0 or 1 increment index for input pipe
				if(index == 0 or index == 1):addFramebufferContributionsAllLayer.setInput(index, outputDotList[index])
				else:addFramebufferContributionsAllLayer.setInput(index+1, outputDotList[index])
			
			
			#setStatus if not False
			if(setStatus): setStatus('Successfully Reconstructed RenderElements')
			
				
			return addFramebufferContributionsAllLayer
		
		#setStatus if not False
		if(setStatus): setStatus('Successfully Reconstructed RenderElements')
		
		return outputDotList
		
	
	
	
	
	#Shared Methods
	#------------------------------------------------------------------
	
	#nodetypeMatches
	def nodetypeMatches(self, node, nodetype):
		
		if(node.Class() == nodetype): return True
		return False
		

		


#TMP Execute in script editor
#------------------------------------------------------------------
'''
from rugbyBugs.nuke.rbRenderReconstruct import rbRenderReconstruct
reload(rbRenderReconstruct)
rbRenderReconstructInstance = rbRenderReconstruct.RbRenderReconstruct()

#shuffle light passes for selected Nodes

#rbRenderReconstructInstance.reconstructLightREs()
#rbRenderReconstructInstance.reconstructFramebufferREs()
#rbRenderReconstructInstance.reconstructDataREs()


rbRenderReconstructInstance.reconstructAll()
'''

		
		

		