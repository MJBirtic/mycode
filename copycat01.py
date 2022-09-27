#!/usr/bin/env python3
#Importing shutil and os library
import shutil
import os

# move into the working directory
os.chdir("/home/student/mycode/")
#copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#copy the directoryA to directoryB
# The following line will create the directory if it does not exist already
shutil.copytree("5g_research/", "5g_research_backup/")

