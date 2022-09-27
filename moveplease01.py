#!/usr/bin/env python3

#importing shutil and os library

import shutil
import os

#change dirctyory to home/student/mycode directory
os.chdir('/home/student/mycode/')

#moves folder from home to ceph storage directory
shutil.move('raynor.obj', 'ceph_storage/')

#will prompt user for a name for the kerrigan.obj file
xname = input('What is the new name for kerrigan.obj? ')

#renames kerrigan.obj to what the user decides name should be
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


