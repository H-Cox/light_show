# light_show
Scripts in python to control hue lights.

Mainly focussed on producing a light show which has calmer periods and more energetic periods - example use would be a party.

Most of the scripts are contained within the lightfunctions.py file. You can run lightshow.py and it will perform a quick show, the operation can then easily be changed by modifying lightshow.py itself.

This scripts use qhue to control the hue lights themselves. You can find that here: https://github.com/quentinsf/qhue

It will be automatically installed if you use the requirements.txt file.

You need to find your bridge IP address and set up a username for the scripts to use and then input it into the lightshow.py script, on lines 39 - 40. qhue can do this itself just follow the first few lines of https://github.com/quentinsf/qhue/blob/master/Qhue%20playground.ipynb
