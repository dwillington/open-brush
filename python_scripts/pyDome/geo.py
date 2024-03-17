#! /usr/bin/env python
# -*- python -*-

#----------------------------------------------------------------
# References:
#   The calculations used in this program are all from the site
#   http://www.vb-helper.com/tutorial_platonic_solids.html
#   Many thanks for making this information available!
#
#----------------------------------------------------------------

import os
import random
import math
import decimal as D
import Coordinates as C
import IcoFace as F
import GeoSphere as G
import config as CF

import socket
import sys
sys.path.append("..")
import ob_helper

# getDrawPathCoordinates
def getDPC(point):
  SCALER=1000
  Y_ADJUST=11
  return f"{point.x/SCALER},{(point.y/SCALER)+Y_ADJUST},{point.z/SCALER}"

def geodesicDome():
    print("/**********************************************************/")
    print(" *     Geodesic Dome Calculator - PyDome                  *")
    print(" *     Version 0.2                                        *")
    print(" *     http://ausrockets.blogspot.com.au                  *")
    print("/**********************************************************/")

    dPi = D.Decimal( str(math.pi) )


    #Centre angle of pentagon
    t1_rad = D.Decimal(2 * dPi / 5)
    t2_rad = D.Decimal( dPi / 10)
    t3_rad = D.Decimal(-3 * dPi / 10)
    t4_rad = D.Decimal(dPi / 5)

    S_mm_t = 2 * CF.R_mm * math.sin(t4_rad)     # Side Length   
    S_mm = D.Decimal( str(S_mm_t) )

    H_mm_t = math.cos(t4_rad) * CF.R_mm         # Height of triangle
    H_mm = D.Decimal( str(H_mm_t) )

    Cx_mm_t = CF.R_mm * math.cos(t2_rad)
    Cx_mm = D.Decimal( str(Cx_mm_t) )

    Cy_mm_t = CF.R_mm * math.sin(t2_rad)
    Cy_mm = D.Decimal( str(Cy_mm_t) )
        
    H1_mm = D.Decimal(str(math.sqrt( S_mm * S_mm - CF.R_mm * CF.R_mm )))
    H2_mm = D.Decimal(str(math.sqrt((H_mm+CF.R_mm)*(H_mm+CF.R_mm) - (H_mm*H_mm))))

        
    Z2_mm = D.Decimal((H2_mm-H1_mm)/2)          # Coordinate of points (b-f)
    Z1_mm = D.Decimal(Z2_mm + H1_mm)            # Coordinate of point (a)   


    #-------------------------------------------
    # Icosahedron Coordinate Equations
    #   http://www.vb-helper.com/tutorial_platonic_solids.html
    #
    # a = (   0,   0,  Z1)
    # b = (   0,   R,  Z2)
    # c = (  Cx,  Cy,  Z2)
    # d = ( S/2,  -H,  Z2)
    # e = (-S/2,  -H,  Z2)
    # f = ( -Cx,  Cy,  Z2)
    # g = (   0,  -R, -Z2)
    # h = ( -Cx, -Cy, -Z2)
    # i = (-S/2,   H, -Z2)
    # j = ( S/2,   H, -Z2)
    # k = (  Cx, -Cy, -Z2)
    # l = (   0,   0, -Z1)

    gs = G.GeoSphere("Sphere", CF.frequency_n, CF.R_mm);

    # Test coordinates
    #t1 = C.Coordinates("t1")
    #t1.Set_Cartesian( -500, -500, 500 )
    #t1.Set_Point_Number( CF.nPoint )
    #CF.nPoint += 1
    #gs.Add_Vertex(t1)

    #t2 = C.Coordinates("t2")
    #t2.Set_Cartesian( 500, -500, 500 )
    #t2.Set_Point_Number( CF.nPoint )
    #CF.nPoint += 1
    #gs.Add_Vertex(t2)

    #t3 = C.Coordinates("t3")
    #t3.Set_Cartesian( 0, 500, 500 )
    #t3.Set_Point_Number( CF.nPoint )
    #CF.nPoint += 1
    #gs.Add_Vertex(t3)



    # Icosahedron vertice coordinates
    a = C.Coordinates("a")
    a.Set_Cartesian( 0, 0, D.Decimal(Z1_mm) )
    a.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(a)

    b = C.Coordinates("b")
    b.Set_Cartesian( 0, CF.R_mm, Z2_mm )
    b.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(b)

    c = C.Coordinates("c")
    c.Set_Cartesian( Cx_mm, Cy_mm, Z2_mm)
    c.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(c)

    d = C.Coordinates("d")
    d.Set_Cartesian( S_mm/2, -H_mm, Z2_mm)
    d.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(d)

    e = C.Coordinates("e")
    e.Set_Cartesian(-S_mm/2, -H_mm, Z2_mm)
    e.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(e)

    f = C.Coordinates("f")
    f.Set_Cartesian(-Cx_mm, Cy_mm, Z2_mm)
    f.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(f)

    g = C.Coordinates("g")
    g.Set_Cartesian(0, -CF.R_mm, -Z2_mm)
    g.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(g)

    h = C.Coordinates("h")
    h.Set_Cartesian(-Cx_mm, -Cy_mm, -Z2_mm)
    h.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(h)

    i = C.Coordinates("i")
    i.Set_Cartesian(-S_mm/2, H_mm, -Z2_mm)
    i.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(i)

    j = C.Coordinates("j")
    j.Set_Cartesian(S_mm/2, H_mm, -Z2_mm)
    j.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(j)

    k = C.Coordinates("k")
    k.Set_Cartesian(Cx_mm, -Cy_mm, -Z2_mm)
    k.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(k)

    l = C.Coordinates("l")
    l.Set_Cartesian(0, 0, -Z1_mm)
    l.Set_Point_Number( CF.nPoint )
    CF.nPoint += 1
    gs.Add_Vertex(l)


    #---------------------------------------------
    # Add the 20 icosahedron faces to the object
    #


    # Test Face Only
    #gs.Add_Face( t1, t2, t3 )
    #gs.Print_Vertices()

    # Top 5 faces
    gs.Add_Face( a, b, c )
    gs.Add_Face( a, c, d )
    gs.Add_Face( a, d, e )
    gs.Add_Face( a, e, f )
    gs.Add_Face( a, f, b )

    # Middle faces
    gs.Add_Face( j, k, c )
    gs.Add_Face( k, d, g )
    gs.Add_Face( g, e, h )
    gs.Add_Face( h, f, i )
    gs.Add_Face( i, b, j )

    gs.Add_Face( c, k, d )
    gs.Add_Face( d, g, e )
    gs.Add_Face( e, h, f )
    gs.Add_Face( f, i, b )
    gs.Add_Face( b, j, c )

    # Bottom faces
    gs.Add_Face( l, k, j )
    gs.Add_Face( l, j, i )
    gs.Add_Face( l, i, h )
    gs.Add_Face( l, h, g )
    gs.Add_Face( l, g, k )

    #---------------------------------
    # Calculations

    # Once all faces added, derive list of unique points
    gs.Point_List_From_Edges()

    # Create the list of edges with the new numbered and unique points
    gs.Create_New_Edges()

    # Remove duplicate edges as faces joining up will have the same edge
    gs.Remove_Duplicate_Edges()

    # Set all the points to have the same radius
    #gs.Set_Edges_Pt_Radius( CF.R_mm )

    # For each point find the edges which meet there
    gs.Hub_List_From_Edges()

    #---------------------------------
    # Print Results
    print("/**********************************************************/")
    print(" *     Points                                             *")
    print("/**********************************************************/")

    # for p in sorted(gs.Point_Hash.keys()):
        # print("x: ", p.x, ", y: ", p.y, ", z: ", p.z)
        # print p.Get_Cartesian_Coordinates()


    print("/**********************************************************/")
    print(" *     Edges                                              *")
    print("/**********************************************************/")

    for e in gs.Edge_List:
        randomColor = format(random.randint(0,16777215),'x')
        ob_helper.sendCommands([f"color.set.html={randomColor}"])
        ob_helper.sendCommands([f"draw.path=[{getDPC(e.x1)}],[{getDPC(e.x2)}]"])
        # print(e.Get_Edge_Coordinates())

    exit()


    print("/**********************************************************/")
    print(" *     Hubs                                              *")
    print("/**********************************************************/")

    for h in gs.Point_Hash.keys():
        h.Print_Edges()


    print("/**********************************************************/")
    print(" *     Summary                                            *")
    print("/**********************************************************/")


    print("Frequency: " + str(CF.frequency_n))
    print("Radius (mm): " + str(CF.R_mm))

    print("Number of points: ", len(gs.Point_Hash.keys()))
    print("Number of edges: ", len(gs.Temp_Edge_List))

    # Print the count of the hubs
    gs.Count_Point_Intersections()


    # Print the count of edge lengths
    gs.Count_Edge_Lengths()

    print("\nNumber of Edge Lengths: ", len(gs.Edge_Count))

    for b in gs.Edge_Count.keys():
        print("\tLength: " + str(b) + "\t- Count: " + str(gs.Edge_Count[b]))


    print("\nHub details:")

    for h in gs.Hub_Count.keys():
        print("\tCount of " + str(h) + "-edged hub = " + str(gs.Hub_Count[h]))


    #-------------------------------------------------------------------------
    # Option - print CAD formatted results
    # Comment out these lines if you do not need
    # Modify these functions in Coordinates.py and Edges.py for other formats

    # Create custom points text
    for p in sorted(gs.Point_Hash.keys()):
        # Need to sort in the number order
        print(p.Get_CATIA_Desc())

    # Create custom edges text
    for e in gs.Edge_List:
        print(e.Get_CATIA_Desc())


def main():

    hostname = socket.gethostname()
    if "OB_HOST" in os.environ:
      ob_helper.ob_host=os.environ['OB_HOST']

    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.type=Light"])
    ob_helper.sendCommands(["user.move.to=0,5,22"])

    geodesicDome()



if __name__ == '__main__':
    main()
