# Class for Cartesian/Polar coordinates

import math as M
from numbers import Number
from decimal import Decimal

class Coordinates(object):
    # Cartesian coordinates
    # x, y, z

    # Polar coordinates
    # int r, theta, phi

    # Tolerance for calculations
    #TINY = Decimal(1e-4)
    TINY = Decimal('0.0001')
    
    def __init__(self, n):

        self.x=Decimal(0)
        self.y=Decimal(0)
        self.z=Decimal(0)

        self.r=Decimal(0)
        self.theta=Decimal(0)
        self.phi=Decimal(0)

        self.name = n
        self.point_number = 0

        # Track which edges it is part of for getting lengths and angles!!
        self.Edge_List = list()
        self.edge_count = 0

    def __lt__(self, other):
        return self.point_number < other.point_number
        
    def Set_Cartesian( self, a, b, c ):

        nbrd = Decimal('1e-10')

        #znew = Decimal(c)

        self.x = Decimal(a).quantize(nbrd).normalize()
        self.y = Decimal(b).quantize(nbrd).normalize()
        
        # This one is the issue. Data coming in is not a decimal???
        # print 'Decimal z: %.2f' % c
        self.z = Decimal(c).quantize(nbrd).normalize()

        # Ensure that the coordinates always match
        # by recalculating the polar coords from the cartesian
        
        rtemp = M.sqrt( self.x * self.x + self.y * self.y + self.z * self.z )
        self.r = Decimal( str( rtemp ) )
        
        thetatemp = M.acos( self.z / self.r )
        self.theta = Decimal( str(thetatemp) )
        
        phitemp = M.atan2( self.y , self.x )
        self.phi = Decimal( str(phitemp) )

    def Set_Radius( self, r):

        self.r = r

        #Recalculate the cartesian coordinates
        self.x = M.sin( self.theta) * M.cos( self.phi ) * self.r
        self.y = M.sin( self.theta) * M.sin( self.phi ) * self.r
        self.z = M.cos( self.theta) * self.r

        if (self.x > -self.TINY) and (self.x < self.TINY):
            self.x = 0
        if (self.y > -self.TINY) and (self.y < self.TINY):
            self.y = 0
        if (self.z > -self.TINY) and (self.z < self.TINY):
            self.z = 0

    def Set_Polar( self, r, theta, phi):

        self.r = r
        self.theta = theta
        self.phi = phi


        if (self.r > -self.TINY) and (self.r < self.TINY):
            self.r = 0
        if (self.theta > -self.TINY) and (self.theta < self.TINY):
            self.theta = 0
        if (self.phi > -self.TINY) and (self.phi < self.TINY):
            self.phi = 0

        # Ensure that the coordinates always match
        # by recalculating the cartesian coords from the polar

        self.x = r * Decimal(M.sin(self.theta)) * Decimal(M.cos(self.phi))
        self.y = r * Decimal(M.sin(self.theta)) * Decimal(M.sin(self.phi))
        self.z = r * Decimal(M.cos(self.theta))

        if (self.x > -self.TINY) and (self.x < self.TINY):
            self.x = 0
        if (self.y > -self.TINY) and (self.y < self.TINY):
            self.y = 0
        if (self.z > -self.TINY) and (self.z < self.TINY):
            self.z = 0


    def Print_Polar(self):

        print(self.name," = ( r=",self.r,", theta=",self.theta,", phi=",self.phi,")")

    def Get_Cartesian_Coordinates(self):

        desc = self.name + " = (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

        return desc

    def __add__(self, other):

        a = Coordinates("ans")
        a.Set_Cartesian( self.x + other.x, self.y + other.y, self.z + other.z )      
        
        return a


    def __eq__(self, other):

        if isinstance(other, Coordinates):

            # Compare only to 5 decimal places.
            if ( round( self.x, 5 ) == round( other.x, 5 )) and ( round( self.y, 5 ) == round( other.y, 5 )) and ( round( self.z, 5 ) == round( other.z, 5 )):
                return True
            else:
                return False
        return NotImplemented


    def __hash__(self):

        return hash((self.x,self.y,self.z))

    def __mul__(self, other):

        #note that there are much better ways to write this
        #code, here we're trying to write self-explanatory code
        #instead of "good" code

        a = Coordinates("ans")

        if isinstance(other,Number):

            a.Set_Cartesian( self.x * other, self.y * other, self.z * other )
            
        else:

            a.Set_Cartesian( self.x * other.x, self.y * other.y, self.z * other.z )      
        
        return a
    
    def dot( self, other ):

        # Vector dot product operator
        return M.sqrt( self.x * other.x + self.y * other.y + self.z * other.z )    

    def cross( self, b):

        # Not Implemented - here for completeness
        return Coordinates("ans")
       
    def __repr__(self):

        return self.name + " = [ " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

    def Get_CATIA_Desc(self):

        # Return the string of VB code for the creation of the CATIA point

        self.cat_desc = "Set hybridShapePointCoord" + str(self.point_number) + " = hybridShapeFactory1.AddNewPointCoord(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")\n"
        self.cat_desc = self.cat_desc + "body1.InsertHybridShape hybridShapePointCoord" + str(self.point_number) + "\n" + "part1.InWorkObject = hybridShapePointCoord" + str(self.point_number) + "\n"
        self.cat_desc = self.cat_desc + "part1.Update\n"

        return self.cat_desc

    def Get_Point_Number(self):
        return self.point_number

    def Set_Point_Number(self, nbr):

        self.point_number = nbr
        self.name = "Pt" + str(nbr)
                                         
    def Add_Edge(self, ed):

        self.Edge_List.append(ed)

    def Print_Edges(self):

        print("\nPoint " + self.name + " Edge List:\n----------------------------------")

        for e in self.Edge_List:
            print(e.Get_Edge_Coordinates())

    def __cmp__(self, other):
        return cmp(self.point_number, other.point_number)
