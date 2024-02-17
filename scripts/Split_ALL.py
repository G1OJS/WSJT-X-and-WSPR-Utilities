# This script opens ALL.TXT and copies entries into files named ALL_YYMM.txt in the same directory
# It is left to the user to decide how to manage the resulting files.
# You may wish to delete the existing ALL.TXT after the script has run, and replace it by renaming the latest ALL_YYMM.txt file to ALL.TXT
# This way you won't create duplicate entries when you run the script again
# Tip - don't do this whilst WSJT-X is running as it will recreate the ALL.TXT file as soon as you delete it
#
# TO RUN:
# Make sure Python is installed
# Copy or download this script, edit path to point to where ALL.TXT is stored, ans save the script as "Split_ALL.py"
# Open a command window, change directory to wherever you've saved this script, and type Python "Split_ALL.py"
#
# USE AT YOUR OWN RISK & BACK UP important files FIRST







import os

path=r"C:\Users\drala\AppData\Local\WSJT-X"

fi = open(path + "\\ALL.TXT" , "r")
fo_me = open(path + "\\ALL_me.TXT" , "a")

mth=""
for line in fi:
	if("G1OJS" in line): fo_me.write(line)

	if(line[0:4]!=mth):
		mth=line[0:4]
		if mth.isnumeric(): fo = open(path + "\\ALL_" + mth + ".txt" , "w")
	else:
		fo.write(line)

fi.close()
		
