# Main class for the Geodesic Sphere
# Contains Vertices, IcoFace's, Coordinates

import IcoFace as IF

import config as C
import Edge as E



class GeoSphere:
    def __init__(self, n, freq, rad ):
        self.name = n               # Text description of this sphere object
        self.freq_n = freq          # Frequency of the sphere

        self.FaceList = list()
        self.R_mm = rad             # Circle radius in mm

        self.delta_mm = rad/freq    # the side length of the smallest triangles

        self.Vertex_List = list()
        
        self.Edge_List = list()
        self.Temp_Edge_List = list()
        self.Updated_Edge_List = list()
        
        self.Edge_Count = {}

        self.Hub_Count = {}

        self.Point_Hash = dict()


        self.nPoint_Number = 1
        self.nEdge_Number = 1


    def Set_Side_Length( self, dist_mm ):
        self.S_mm = dist_mm

    def Add_Vertex(self, v):

        self.Vertex_List.append(v)      

    def Print_Points_CATIA(self):
        for x in self.Point_List:
            print(x.Get_CATIA_Desc())


    def Print_Vertices(self):

        print("Print Vertices: " + str(len(self.Vertex_List)))

        for x in self.Vertex_List:
            #print x.Print_Polar()

            print(x.Get_Cartesian())
            
            #print x.Get_CATIA_Desc()

    def Print_Edges(self):
        for x in self.Edge_List:
            print(f"[{x.x}, {x.y}, {x.z}]")

    #def Renumber_Points(self):
        # Since some points will be dupes the numbers are not incremental.
        # Renumber them in order so that they will match the CATIA details
    #    n = 1

    #    for x in self.Point_List:
    #        x.point_number = n
    #        n += 1


    def Set_Edges_Pt_Radius(self, rad_mm):
        # Must also set the radius for the edge list??
        for x in self.Vertex_List:
            x.Set_Radius(rad_mm)

        # Update both points in an edge
        for x in self.Edge_List:
            x.x1.Set_Radius(rad_mm)
            x.x2.Set_Radius(rad_mm)

    def Add_Face( self, a, b, c):

        F1 = IF.IcoFace( a.name + b.name + c.name, self.freq_n)
        F1.Set_Vertices( a,b,c)

        self.FaceList.append( F1 )

        #----------------------------------------------------
        # Use this function to divide faces by equal distance
        #
        edge_list = F1.Get_Edges_Equal_Distance()
        
        #----------------------------------------------------
        # Use this function to divide faces by equal angle
        # 20/3/2013 - Not working yet, needs more work
        #edge_list = F1.Get_Edges_Equal_Angles()     

        for e in edge_list:

            # For Domes ignore any edges below the Z plane
            if ( C.Dome_calc == True ) and (( e.x1.z < 0 ) or ( e.x2.z < 0 )): 
                #print "Ignoring edge " + e.name + " x1.z = " + str(e.x1.z) + " x2.z = " + str(e.x2.z)
                continue # Continue with next 'e' in the FOR loop


            # Otherwise add the edge
            edge_found = False

            # Keep them in a temp list to dedupe once all loaded
            for x in self.Temp_Edge_List:
                if e == x:
                    edge_found = True
                
            if edge_found == False:
                self.Temp_Edge_List.append(e)




    def Remove_Duplicate_Edges(self):
        # Double check the edge list for dupes

        for e in self.Updated_Edge_List:

            found = False
            
            for ef in self.Edge_List:
                if e == ef:
                    found = True

            if found == False:
                self.Edge_List.append(e)

            # Otherwise dont add it to the list
                
    def Point_List_From_Edges(self):
        # All faces added, get a list of unique points    

        for c in self.Temp_Edge_List:

            self.Add_Point_To_List( c.x1 )
            self.Add_Point_To_List( c.x2 )

            # The numbers are getting lost when the point already exists!!
            # How to update the copy



    def Add_Point_To_List(self, pt):
            # Check if a point exists in the Point_List, otherwise add it.
            #point_found = False

            #for x in self.Point_List:
            #    if x == pt:
            #        point_found = True

            #if point_found == False:

            

            if pt not in self.Point_Hash:

                # Fix the number once its a new point
                pt.point_number = self.nPoint_Number
                pt.name = "Pt" + str(self.nPoint_Number)


                #if pt not in self.Point_Hash:
                self.Point_Hash[pt] = pt
                #else:
                #    print "Found in Point_Hash: " + pt

                self.nPoint_Number += 1



    def Check_Point_Exists(self, pt):
        pt_found = False

        #for x in self.Point_List:
        #    if x == pt:
        #        pt_found = True
        #return pt_found

        if pt in self.Point_Hash:
            pt_found = True

        return pt_found



    def Get_Point(self, pt): 
        # Return the point from the hash

        if pt in self.Point_Hash:

            a = self.Point_Hash[ pt ]

            #print "Found point hash\n" + str(a)
            return a
        
#        for x in self.Point_List:
#            if x == pt:
#                return x

        return None

    def Create_New_Edges(self):

        # For each existing edge, create a new edge with the right edge numbers!!
        for old_edge in self.Temp_Edge_List:
            
            new_edge = E.Edge("Edge" + str(self.nEdge_Number) )
            self.nEdge_Number += 1

            pt1 = self.Get_Point( old_edge.x1 )
            new_edge.x1 = pt1
            #print "new_edge.x1 = " + str(new_edge.x1)

            pt2 = self.Get_Point( old_edge.x2 )
            new_edge.x2 = pt2

            self.Updated_Edge_List.append( new_edge )


    def Remove_Duplicate_Pt_From_Edges(self):
        # Once we have the list of unique points, replace the old points in the edges

        for e in self.Temp_Edge_List:
            #print "Checking edge: ", e
            
            # Check if the point exists in the final list and return the details if so....
            if ( self.Check_Point_Exists( e.x1 ) == True ):
                new_pt = self.Get_Point( e.x1 )

                e.Update_Point( new_pt, e.x1 )

            else:
                print("Couldnt match x1: " + e.x1)


            # Check if the point exists in the final list and return the details if so....
            if ( self.Check_Point_Exists( e.x2 ) == True ):
                new_pt = self.Get_Point( e.x2 )

                # Update the edge for the new point
                e.Update_Point( new_pt, e.x2 )

            else:
                print("Couldnt match x2: " + e.x2)


    def Count_Edge_Lengths(self):
        #Calculate the edge lengths only for the final edge list without duplicates
        for i in self.Updated_Edge_List:
            #print e

            len = i.Get_Length()

            if len in self.Edge_Count:
                #print "Adding to count"
                self.Edge_Count[len] += 1

            else:
                self.Edge_Count[len] = 1  
                #print "New Edge length: ", i

    def Hub_List_From_Edges(self):
        # For each point, scan the Edge_List and get all the associated edges

        # This is still matching old points??? Hence getting double numbers?? Or duplicate edges not getting removed??

        for pt in self.Point_Hash.keys():
            for e in self.Updated_Edge_List:
                if e.x1 == pt or e.x2 == pt:
                    # Add edge to the point list.
                    pt.Add_Edge(e)




    def Count_Point_Intersections(self):
        # Count how many of the hubs have 4/5/6 connections etc.

        for h in self.Point_Hash.keys():
#        for h in self.Point_List:
            c = len(h.Edge_List)

            if c in self.Hub_Count:
                self.Hub_Count[c] += 1
            else:
                self.Hub_Count[c] = 1
