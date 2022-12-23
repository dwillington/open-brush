#! /usr/bin/env python

import os
import random
import socket
import sys
sys.path.append("..")
import ob_helper

def getDPC(x,y,z):
  SCALER=10
  Y_ADJUST=11
  Z_ADJUST=-20
  return f"{x*SCALER},{(y*SCALER)+Y_ADJUST},{(z*SCALER)+Z_ADJUST}"

def fromDomeOutput():
    draw_path = ""
    coordinates = []

    file = open('output.OFF')
    if(len(sys.argv)>1):
      # print(f"reading file {sys.argv[1]}")
      file = open(sys.argv[1])

    content = file.readlines()

    numOfCoordinates = int(content[1].split(" ")[0])
    numOfFaces = int(content[1].split(" ")[1])

    print(f"numOfCoordinates:{numOfCoordinates}")
    print(f"numOfFaces:{numOfFaces}")

    # READ IN ALL COORDINATES
    for i in range(2,2+int(numOfCoordinates)):
        v = content[i].rstrip().split(" ")
        coord = f"{getDPC(round(float(v[0]),4), round(float(v[1]),4), round(float(v[2]),4))}"
        coordinates.append(coord)
        # print(coord)

    # READ IN AND DRAW ALL FACES
    startFaces = 2+numOfCoordinates

    # ONLY DRAW LINES
    ob_helper.sendCommands(["brush.type=Dots"])
    for i in range(startFaces,startFaces+numOfFaces):
        v = content[i].rstrip().split(" ")
        draw_path=f"draw.path=[{coordinates[int(v[1])]}],[{coordinates[int(v[2])]}],[{coordinates[int(v[3])]}],[{coordinates[int(v[1])]}]"
        # randomColor = format(random.randint(0,16777215),'x')
        # ob_helper.sendCommands([f"color.set.html={randomColor}"])
        ob_helper.sendCommands([f"{draw_path}"])

    if False:
      # ONLY DRAW THE SURFACE WITH A HULL BRUSH
      ob_helper.sendCommands(["brush.type=Diamond"]) # ShinyHull,MatteHull,UnlitHull,Diamond
      for i in range(startFaces,startFaces+numOfFaces):
          v = content[i].rstrip().split(" ")
          draw_path=f"draw.path=[{coordinates[int(v[1])]}],[{coordinates[int(v[2])]}],[{coordinates[int(v[3])]}],[{coordinates[int(v[1])]}]"
          ob_helper.sendCommands([f"{draw_path}"])

          # draw_path=f"draw.path=[{coordinates[int(v[1])]}],[{coordinates[int(v[2])]}]"
          # ob_helper.sendCommands([f"{draw_path}"])
          # draw_path=f"draw.path=[{coordinates[int(v[2])]}],[{coordinates[int(v[3])]}]"
          # ob_helper.sendCommands([f"{draw_path}"])
          # draw_path=f"draw.path=[{coordinates[int(v[3])]}],[{coordinates[int(v[1])]}]"
          # ob_helper.sendCommands([f"{draw_path}"])


def main():

    hostname = socket.gethostname()
    if "OB_HOST" in os.environ:
      ob_helper.ob_host=os.environ['OB_HOST']

    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0","brush.look.up"])
    ob_helper.sendCommands(["user.move.to=0,4,40"])

    fromDomeOutput()



if __name__ == '__main__':
    main()
