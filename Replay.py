import FreeCAD, FreeCADGui, Draft, Part
from FreeCAD import Base
import time

ColSel = 1
Samp_t = 0.5

f=open("mydir\\Data.csv")
lines=f.readlines()

coords=[]
RplVect = []

for i in lines[1:]:
    c=i.strip().split(",")
    coords.append([float(j.strip('TO')) for j in c])
    coords[-1][0]=str(int(coords[-1][0]))

for i in coords:
	RplVect.append(int(i[ColSel]))

for i in RplVect:
    FreeCAD.getDocument("Solenoid").getObject("Cut001").Placement.Base.z = i
    FreeCAD.getDocument("Solenoid").getObject("Cut002").Placement.Base.z = i
    Gui.updateGui()
    time.sleep(Samp_t)