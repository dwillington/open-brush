# Class for Edges

import math as M
from numbers import Number
from decimal import Decimal


class Edge:
    # Edge between two coordinates
    def __init__(self, n):
        self.name = n
        
        self.edge_number = 0

    def Set_Points(self, a, b):
        self.x1 = a
        self.x2 = b

        
    
    def Set_Edge_Number(self, n):
      self.edge_number = n

    def Get_Length(self):

        t1 = M.pow((self.x1.x - self.x2.x),2)
        t2 = M.pow((self.x1.y - self.x2.y),2)
        t3 = M.pow((self.x1.z - self.x2.z),2)
        
        ans = M.sqrt( t1 + t2 + t3 )
        dans = Decimal(str(ans)).quantize(Decimal(10) ** -2)

        return dans


    def __repr__(self):
        return "\n" + self.name + " --- \n" + str(self.x1.name) + "\n - \n" + str(self.x2.name) #+ " : " + str(self.length)

        
    def Get_CATIA_Desc(self):

        # Create the VB script code to generate a line between two points

        self.ret_string = "Set hybridShapePointCoord1 = hybridShapes1.Item(\"Point." + str(self.x1.point_number) + "\")\n"
        self.ret_string += "Set reference1 = part1.CreateReferenceFromObject(hybridShapePointCoord1)\n" 
        self.ret_string += "Set hybridShapePointCoord2 = hybridShapes1.Item(\"Point." + str(self.x2.point_number) + "\")\n" 
        self.ret_string += "Set reference2 = part1.CreateReferenceFromObject(hybridShapePointCoord2)\n" 
        #self.ret_string += "Dim hybridShapeLinePtPt" + str(self.edge_number) +" As HybridShapeLinePtPt\n" 
        self.ret_string += "Set hybridShapeLinePtPt" + str(self.edge_number) +" = hybridShapeFactory1.AddNewLinePtPt(reference1, reference2)\n" 
        self.ret_string += "body1.InsertHybridShape hybridShapeLinePtPt" + str(self.edge_number) +"\n" 
        self.ret_string += "part1.InWorkObject = hybridShapeLinePtPt" + str(self.edge_number) +"\n" 
        self.ret_string += "part1.Update\n"

        return self.ret_string


    def Get_Edge_Coordinates(self):
        return self.name + ": " + str(self.x1) + " - " + str(self.x2)


    
    def Update_Point(self, x, pt):
        if self.x1 == pt:
            self.x1 = x
        if self.x2 == pt:
            self.x2 = x


    def __eq__(self, other):

        fnd = False

        if isinstance(other, Edge):
            # Check if both the points are the same regardless of order
            if (self.x1 == other.x1 and self.x2 == other.x2) or (self.x1 == other.x2 and self.x2 == other.x1):
                fnd = True

        return fnd
