# Class for saving the faces

# Dont need each vertex, just the faces!!

import Coordinates as C
import math as M
import Edge as E
from decimal import Decimal
import config as CF
from numbers import Number



class IcoFace:

    def __init__(self, n, freq ):
        self.name = n
        self.freq_n = freq

    def Set_Vertices( self, a, b, c):
        self.x1 = a
        self.x2 = b
        self.x3 = c

    def Print_Vertices(self):
        self.x1.Print_Cartesian()
        self.x2.Print_Cartesian()
        self.x3.Print_Cartesian()

    def Get_Edges_Equal_Angles(self):
        # Calculate the edge coordinates based on the division of the angle between the points

        ret_list = list()

        # Coordinates of the starting point
        x0 = self.x1
        y0 = self.x2
        z0 = self.x3

        delta_theta_x1x2 = (y0.theta - x0.theta)/self.freq_n
        delta_phi_x1x2 = (y0.phi - x0.phi)/self.freq_n


        delta_theta_x1x3 = (z0.theta - x0.theta)/self.freq_n
        delta_phi_x1x3 = (z0.phi - x0.phi)/self.freq_n


        if (delta_theta_x1x2 > -CF.TINY) and (delta_theta_x1x2 < CF.TINY):
            delta_theta_x1x2 = 0
        if (delta_theta_x1x3 > -CF.TINY) and (delta_theta_x1x3 < CF.TINY):
            delta_theta_x1x3 = 0


        for i in range(0,self.freq_n+1):

            for j in range( 1, self.freq_n - i +1 ):

                # All marked as points?? Doesnt matter, vertices already stored!!
                # Can remove any vertices from the list if we want, although all the same

                a = C.Coordinates("pointA")
                a.Set_Point_Number(CF.nPoint)
                CF.nPoint += 1
                b = C.Coordinates("pointB")
                b.Set_Point_Number(CF.nPoint)
                CF.nPoint += 1
                c = C.Coordinates("pointC")
                c.Set_Point_Number(CF.nPoint)
                CF.nPoint += 1

                # r, theta, phi
                
                # Calculate the new coordinates based on the offset from the initial point (A)
                a.Set_Polar( x0.r, x0.theta + j*delta_theta_x1x2 + i*delta_theta_x1x3, x0.phi + j*delta_phi_x1x2 + i*delta_phi_x1x3)

                #a.Set_Polar( x0 + i*delta_x1x2.x + j*delta_x1x3.x, y0 + i*delta_x1x2.y + j*delta_x1x3.y, z0 + i*delta_x1x2.z + j*delta_x1x3.z)

                b.Set_Polar( x0.r, x0.theta + (j-1)*delta_theta_x1x2 + i*delta_theta_x1x3, x0.phi + (j-1)*delta_phi_x1x2 + i*delta_phi_x1x3)
                #b.Set_Polar( x0 + i*delta_x1x2.x + (j-1)*delta_x1x3.x, y0 + i*delta_x1x2.y + (j-1)*delta_x1x3.y, z0 + i*delta_x1x2.z + (j-1)*delta_x1x3.z)

                c.Set_Polar( x0.r, x0.theta + (j-1)*delta_theta_x1x2 + (i+1)*delta_theta_x1x3, x0.phi + (j-1)*delta_phi_x1x2 + (i+1)*delta_phi_x1x3)
                #c.Set_Polar( x0 + (i+1)*delta_x1x2.x + (j-1)*delta_x1x3.x, y0 + (i+1)*delta_x1x2.y + (j-1)*delta_x1x3.y, z0 + (i+1)*delta_x1x2.z + (j-1)*delta_x1x3.z)
                        

                e1 = E.Edge("edge" + str(CF.nEdge) )
                e1.Set_Edge_Number( CF.nEdge )
                e1.Set_Points( a, b )
                CF.nEdge += 1

                e2 = E.Edge("edge" + str(CF.nEdge) )
                e2.Set_Edge_Number( CF.nEdge )
                e2.Set_Points( b, c )
                CF.nEdge += 1

                e3 = E.Edge("edge" + str(CF.nEdge) )
                e3.Set_Edge_Number( CF.nEdge )
                e3.Set_Points( c, a )
                CF.nEdge += 1

                ret_list.append(e1)
                ret_list.append(e2)
                ret_list.append(e3)

        return ret_list

    def Get_Edges_Equal_Distance(self):
        # Based on equal division of the face into triangles - This leads to different sized strut lengths
        # If it was based on the equal division of the angle at the same radius then all strut lengths the same!!
        # What does this do to the structural integrity of the dome??
        # Return all the points/vertices of the face divided into equilateral triangles based on the frequency

        ret_list = list()

        # Coordinates of the starting point
        x0 = self.x1.x
        y0 = self.x1.y
        z0 = self.x1.z

        delta_x1x2 = self.Get_Delta_Vector( self.x1, self.x2 )

        delta_x1x3 = self.Get_Delta_Vector( self.x1, self.x3 )


        for i in range(0,self.freq_n+1):

            for j in range( 1, self.freq_n - i + 1):


                # All marked as points?? Doesnt matter, vertices already stored!!
                # Can remove any vertices from the list if we want, although all the same

                a = C.Coordinates("pointA")
                a.Set_Point_Number(CF.nPoint)
                CF.nPoint += 1
                b = C.Coordinates("pointB")
                b.Set_Point_Number(CF.nPoint)
                CF.nPoint += 1
                c = C.Coordinates("pointC")
                c.Set_Point_Number(CF.nPoint)
                CF.nPoint += 1
                
                

                # Calculate the new coordinates based on the offset from the initial point (A)
                a.Set_Cartesian( x0 + i*delta_x1x2.x + j*delta_x1x3.x, y0 + i*delta_x1x2.y + j*delta_x1x3.y, z0 + i*delta_x1x2.z + j*delta_x1x3.z)

                b.Set_Cartesian( x0 + i*delta_x1x2.x + (j-1)*delta_x1x3.x, y0 + i*delta_x1x2.y + (j-1)*delta_x1x3.y, z0 + i*delta_x1x2.z + (j-1)*delta_x1x3.z)

                c.Set_Cartesian( x0 + (i+1)*delta_x1x2.x + (j-1)*delta_x1x3.x, y0 + (i+1)*delta_x1x2.y + (j-1)*delta_x1x3.y, z0 + (i+1)*delta_x1x2.z + (j-1)*delta_x1x3.z)
                
                

                e1 = E.Edge("edge" + str(CF.nEdge) )
                e1.Set_Edge_Number( CF.nEdge )
                e1.Set_Points( a, b )
                CF.nEdge += 1

                e2 = E.Edge("edge" + str(CF.nEdge) )
                e2.Set_Edge_Number( CF.nEdge )
                e2.Set_Points( b, c )
                CF.nEdge += 1

                e3 = E.Edge("edge" + str(CF.nEdge) )
                e3.Set_Edge_Number( CF.nEdge )
                e3.Set_Points( c, a )
                CF.nEdge += 1

                ret_list.append(e1)
                ret_list.append(e2)
                ret_list.append(e3)

        return ret_list

    def Get_Vertex_Coord(self):
        # Return the coordinates of each of the vertices
        return 0

    def Get_Delta_Vector(self, a, b ):
        # Return the delta vector
        del_vec = C.Coordinates("Delta_" + a.name + b.name)
        del_vec.Set_Cartesian( (b.x - a.x)/self.freq_n , (b.y - a.y)/self.freq_n, (b.z - a.z)/self.freq_n )

        return del_vec

    def dotproduct(v1, v2):
      return sum((a*b) for a, b in zip(v1, v2))

    def length(v):
      return math.sqrt(dotproduct(v, v))

    def angle(v1, v2):
      return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

    def __repr__(self):
        return "Face:" + self.name
