import os
import sys
sys.path.append("/home/pushpendra//Documents/IIITB/HPC/visit3_1_4.linux-x86_64-ubuntu20/visit3_1_4.linux-x86_64/3.1.4/linux-x86_64/lib/site-packages/")
sys.path.append("/usr/local/lib/python3.8/dist-packages/")
import visit
from pathlib import Path
testfile_path ='/home/pushpendra/Documents/IIITB/HPC/forPE_rotturbruns/maxhelmaxrot/velocity.400000.h5'
#  raw_input("Enter Path of Database : ")


my_file = Path(testfile_path)



if my_file.is_file():
	visit.OpenDatabase(testfile_path)
else :
	print("File Not Found !!")
	sys.exit(1)


DefineVectorExpression("v","{<PS/vx>,<PS/vy>,<PS/vz>}")
DeleteAllPlots()
AddPlot("Vector","v")


a=AnnotationAttributes()
a.axes3D.visible=0
a.axes3D.triadFlag=0
a.axes3D.bboxFlag=0
a.databaseInfoFlag=0
a.legendInfoFlag=0
SetAnnotationAttributes(a)

va=VectorAttributes()
va.colorTableName="amino_shapely"
va.nVectors=40000
va.lineStem=0
SetPlotOptions(va)


viewatt=View3DAttributes()
viewatt.imageZoom=1.47
SetView3D(viewatt)
DrawPlots()
SaveWindow()



exit()
