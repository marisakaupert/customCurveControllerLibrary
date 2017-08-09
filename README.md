My Curve Controller Library is UI made with PyMel, and based off the UI made by Geordie Martinez through his course on https://www.cgcircuit.com/. The UI uses an API to save controllers and adds them to a .json file. The user can customize the color and scale of their controls.

'''To use:'''
* Download controllerLibUI.py and conGen.py
* Put both files in your Maya scripts directory or add the folder with them to your python path
* Put iconConvert.py in your **Python** directory
* Type this into the Script Editor:
```python
# to add path
import sys 
sys.path.append( 'C:\Users\yourName\Documents/folderName' )

# otherwise, run this
import controllerLibUI_v0011 as conLibUI
reload(conLibUI)
conLibUI.run()
```
