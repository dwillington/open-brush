import requests
import random
import math

ob_host = "127.0.0.1"

def callUrl(url):
  try:
    # urllib.request.urlopen(url)
    requests.get(url)
  except Exception as e: print(e)

def sendCommands(commandStrings):
  url = "http://" + ob_host + ":40074/api/v1?" + "&".join(commandStrings)
  print("\n".join(commandStrings))
  callUrl(url);

# LARGER SCALER VALUE MAKES SMALLER LINES
def drawLineOB(p0, p1, scaler=100, generateRandomColor=False):
  sx = p0[0] / scaler
  sy = p0[1] / scaler
  fx = p1[0] / scaler
  fy = p1[1] / scaler
  if generateRandomColor == True:
    randomColor = format(random.randint(0,16777215),'x')
    sendCommands([f"color.set.html={randomColor}"])
  sendCommands([f"draw.path=[{sx},{sy},0],[{fx},{fy},0]"]);

def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)

class DPC:
  def __init__(self, scaler=1, x_offset=0, y_offset=0, z_offset=0):
    self.SCALER = scaler
    self.X_OFFSET = x_offset
    self.Y_OFFSET = y_offset
    self.Z_OFFSET = z_offset

  # "1.0,2.0,3.0"
  def get(self, x, y, z):
    return f"{round((x*self.SCALER)+self.X_OFFSET,2)},{round((y*self.SCALER)+self.Y_OFFSET,2)},{round((z*self.SCALER)+self.Z_OFFSET,2)}"
    
  # "1.0,2.0,3.0" -> [1.0 2.0 3.0]
  def get_as_list(self,s):
    x = [float(i) for i in s.split(',')]
    if len(x) != 3:
      print("error")
      return
    return x

  @staticmethod
  def below_threshold(p0, p1, THRESHOLD=0.058, printout=False):
    distance = math.dist(p0,p1)
    if distance <= THRESHOLD:
      if printout == True:
        print(f"{distance} < {THRESHOLD}")
      return True
    return False

class Point:

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def flip_over_Y_axis(self):
        self.y = self.y * -1

    def rotate_ccw_90(self):
        temp = self.x
        self.x = self.y
        self.y = temp

    def get_3d_coordinates(self):
        return [self.x, self.y, self.z]

    def origin_compress(self, compress_factor):
        self.x = self.x * compress_factor
        self.y = self.y * compress_factor
        self.z = self.z * compress_factor

    def set_X_offset(self, x_offset):
        self.x = self.x + x_offset

    def set_Y_offset(self, y_offset):
        self.y = self.y + y_offset

    def set_Z_offset(self, z_offset):
        self.z = self.z + z_offset