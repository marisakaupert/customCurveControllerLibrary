
import os
import json
import logging
import pymel.core as pm

try:
	import cPickle as pickle
except:
	import pickle

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

# path to default pickle file
defaultLibraryPath = os.path.join(os.path.dirname(__file__), 'consPickle.pkl')
iconFolderPath = os.path.join(os.path.dirname(__file__), 'screenCaptures')
iconsConvertPath = os.path.join(os.path.dirname(__file__),'iconConvert.py')

# if exists, need to reload it everytime
try:
	consDictionary = pickle.load(open(defaultLibraryPath, 'rb'))
	tempDictionaryString = json.dumps(consDictionary,indent = 4)
	_logger.debug("consDict: {0}".format(tempDictionaryString))
except:
	_logger.warn("No Existing Library of Controls : {0}".format(defaultLibraryPath))
	consDictionary = {}

def consList():
	""" returns a list of available controllers
	"""

	return sorted(consDictionary.keys())

def saveCon(con=None, conName=None, doScreenGrab=False, doCrop=True, debug=False):
	""" saves selected nurbs curve to te pickle file
		con = short for controller
	"""

	global consDictionary

	con = con or pm.selected()[0]

	conShape = con.getShape()

	degree = conShape.degree() # 1 or 3
	form = conShape.form().key # periodic or open
	spans = conShape.spans.get() # number of CVS, same as number of CVs
	knots = conShape.getKnots() # list of float values
	cvs = conShape.getCVs() # list of CV points

	conName = conName or pm.promptBox("Provide Controller Name", "Name: " , "Ok" , "Cancel")

	if not conName:
		return

	tempDictionary = {}

	tempDictionary['degree'] = degree
	tempDictionary['knots'] = knots
	tempDictionary['form'] = form
	tempDictionary['spans'] = spans

	# convert verts to tuples so json will not choke on the date
	tempDictionary['cvs'] = [  tuple(cv)  for cv in cvs ]

	# appending to main dictionary
	consDictionary[conName] = tempDictionary

	tempDictionaryString = json.dumps(consDictionary,indent = 4)

	# export to pickle
	pickle.dump(consDictionary, open(defaultLibraryPath, 'wb'))

	if debug:
		with open(defaultLibraryPath.replace(".pkl",".json"), 'w') as outfile:
			json.dump(consDictionary,outfile,indent=4)

	if doScreenGrab:
		screenGrab(conName)
		_logger.info("Created screen grab")

	if doCrop:
		cropImage(conName)

def cropImage(conName):
	""" runs a subprocess to crop the image to 400x400
	"""

	import subprocess

	imageStart = os.path.join(iconFolderPath,"{0}.png".format(conName))
	imageResult = os.path.join(iconFolderPath,"{0}.jpg".format(conName))

	cmd = ['python', iconsConvertPath, 
           '-ip', imageStart, 
           '-irp', imageResult]

	p = subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	res,err = p.communicate()

def screenGrab(conName):
	""" captures the 3d viewport as an Icon Picture
	"""

	import maya.OpenMaya as api
	import maya.OpenMayaUI as apiUI

	# get the viewer window
	view = apiUI.M3dView.active3dView()

	# create an empty image holder
	img = api.MImage()

	view.readColorBuffer(img,True)

	iconFileName = os.path.join(iconFolderPath,"{0}.png".format(conName))

	# write to disk
	img.writeToFile(iconFileName, 'png')

def generateCon(conName = None,scale=1.0,color=6):
	""" generate a nurbs curve controller
	"""

	if not conName:
		_logger.warn("No Controller Name Provided. Ex: conName = 'diamond' ")
		return

	conToCreate = consDictionary.get(conName, None)

	if not conToCreate:
		_logger.error("Control does not exist in the pickle file")
		return

	tempDictionaryString = json.dumps(conToCreate,indent = 4)

	periodic = True  if conToCreate.get('form') == 'periodic' else False 
	degree = conToCreate.get('degree')
	cvs = conToCreate.get('cvs')
	knots = conToCreate.get('knots')

	#create the curve
	crv = pm.curve(n="{0}#".format(conName), d=degree, p=cvs, k=knots, per=periodic)
	crv.scale.set((scale,scale,scale))
	pm.makeIdentity(crv,apply=True,t=0,r=0,s=1,n=0)

	# set color
	crv.getShape().overrideEnabled.set(1)
	crv.getShape().overrideColor.set(color)

	return crv
