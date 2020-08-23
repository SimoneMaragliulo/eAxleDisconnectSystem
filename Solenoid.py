import FreeCAD, FreeCADGui, Draft, Part
from FreeCAD import Base
import time

Sample_n = 120
Sample_t = 0.1


ii = iib = FreeCAD.getDocument("Solenoid").getObject("Helix001").Pitch.Value
a = i = ib = FreeCAD.getDocument("Solenoid").getObject("Helix001").Height.Value


pas = 1

for ii2 in range(int(Sample_n)):
    if pas == 0:
        if ii > iib-1:
            pas = 1
        else:
            ii += 1
            i = (ii * 10)
    else:
        if ii < 2:
            pas = 0
        else:
            ii -= 1
            i = (ii * 10)

   
    FreeCAD.getDocument("Solenoid").getObject("Helix001").Pitch = ii
    FreeCAD.getDocument("Solenoid").getObject("Helix001").Height = i
    displacement = i-a
    FreeCAD.getDocument("Solenoid").getObject("Fusion009").Placement.Base.z = displacement
    App.getDocument("Solenoid").Cut002.Placement=App.Placement(App.Vector(0,0,displacement),
                                                                  App.Rotation(App.Vector(0,0,1),ii2*10), App.Vector(0,0,0))
    App.getDocument("Solenoid").Fusion010.Placement=App.Placement(App.Vector(0,0,0),
                                                                  App.Rotation(App.Vector(0,0,1),ii2*10), App.Vector(0,0,0))
    App.getDocument("Solenoid").Cut011.Placement=App.Placement(App.Vector(0,0,0),
                                                                  App.Rotation(App.Vector(0,0,1),ii2*10), App.Vector(0,0,0))

    App.Console.PrintMessage("SimTime [sec]: "+str(round(ii2*Sample_t,2))+"  Plunger displacement [mm]: " + str(displacement)+"\n")
    Gui.updateGui()
    time.sleep(Sample_t)	

