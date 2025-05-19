from ob import ob
import sys
import os
import random
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
sys.path.append("..")
import ob_helper


def three_body():
  # plt.style.use('dark_background')

  def get_within_5():
    return round(random.uniform(-5, 5),2)

  # starting coordinates for planets
  # p1_start = np.array([get_within_5(), 0, get_within_5()])
  # p2_start = np.array([get_within_5(), 0, get_within_5()])
  # p3_start = np.array([get_within_5(), 0, get_within_5()])

  # masses of planets
  m_1 = 15
  m_2 = 15
  m_3 = 15

  p1_start = np.array([-10, 10, -11])
  p2_start = np.array([0, 0, 0])
  p3_start = np.array([10, 10, 12])
  v1_start = np.array([-3, 0, 0])
  v2_start = np.array([0, 0, 0])
  v3_start = np.array([3, 0, 0])

  # p1_start = np.array([-1, 0, 0])
  # p3_start = np.array([1, 0, 0])
  # p2_start = np.array([0, 0, 0])
  # v1_start = np.array([0.306893,0.125507,0])
  # v3_start = np.array([0.306893,0.125507,0])
  # v2_start = np.array([-0.613786,-0.251014,0])


  def accelerations(p1, p2, p3):
    """
    A function to calculate the derivatives of x, y, and z
    given 3 object and their locations according to Newton's laws
    """
    # m_1, m_2, m_3 = self.m1, self.m2, self.m3
    planet_1_dv = (-9.8 * m_2 * (p1 - p2)/(np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**3) - 
                   9.8 * m_3 * (p1 - p3)/(np.sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2 + (p1[2] - p3[2])**2)**3))
    
    planet_2_dv = (-9.8 * m_3 * (p2 - p3)/(np.sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2 + (p2[2] - p3[2])**2)**3) - 
                   9.8 * m_1 * (p2 - p1)/(np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)**3))
    
    planet_3_dv = (-9.8 * m_1 * (p3 - p1)/(np.sqrt((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2 + (p3[2] - p1[2])**2)**3) - 
                   9.8 * m_2 * (p3 - p2)/(np.sqrt((p3[0] - p2[0])**2 + (p3[1] - p2[1])**2 + (p3[2] - p2[2])**2)**3))

    return planet_1_dv, planet_2_dv, planet_3_dv
    

  # parameters
  delta_t = 0.001
  steps = 200000

  # initialize trajectory array
  p1 = np.array([[0.,0.,0.] for i in range(steps)])
  v1 = np.array([[0.,0.,0.] for i in range(steps)])

  p2 = np.array([[0.,0.,0.] for j in range(steps)])
  v2 = np.array([[0.,0.,0.] for j in range(steps)])

  p3 = np.array([[0.,0.,0.] for k in range(steps)])
  v3 = np.array([[0.,0.,0.] for k in range(steps)])


  # starting point and velocity
  p1[0], p2[0], p3[0] = p1_start, p2_start, p3_start
  v1[0], v2[0], v3[0] = v1_start, v2_start, v3_start


  dpc_helper = ob_helper.DPC(0.5,0,5)
  counter = 0
  step_size = 500
  segment_counter = 0

  # https://matplotlib.org/stable/users/explain/colors/colormaps.html
  from mycolorpy import colorlist as mcp
  color1 = mcp.gen_color(cmap="ocean",n=int(steps/step_size))
  color2 = mcp.gen_color(cmap="autumn",n=int(steps/step_size))
  color3 = mcp.gen_color(cmap="spring",n=int(steps/step_size))

  # evolution of the system
  for i in range(steps-1):
    # calculate derivatives
    dv1, dv2, dv3 = accelerations(p1[i], p2[i], p3[i])

    v1[i + 1] = v1[i] + dv1 * delta_t
    v2[i + 1] = v2[i] + dv2 * delta_t
    v3[i + 1] = v3[i] + dv3 * delta_t

    p1[i + 1] = p1[i] + v1[i] * delta_t
    p2[i + 1] = p2[i] + v2[i] * delta_t
    p3[i + 1] = p3[i] + v3[i] * delta_t

    if (i % step_size) == 0:
      if i == 0: continue # OR ELSE WE GET (0,0,0) AS THE STARTING POINT
      # print(p1[i+1])
      # INCREMENT COUNTER ON EVERY (steps / 100) UNITS B/C COLORMAPS ARE MAX = 100
      if (i % (steps / 100)) == 0:
        counter += 1

      def draw_orbit_segment(p1, i):
        p = -step_size
        rect_height = 0.2
        np0 = dpc_helper.get(p1[i+p][0],p1[i+p][1]+rect_height,p1[i+p][2])
        np = dpc_helper.get(p1[i+p][0],p1[i+p][1],p1[i+p][2])
        # n0 = "0,0,0"
        n0 = dpc_helper.get(p1[i+1][0],p1[i+1][1]+rect_height,p1[i+1][2])
        n1 = dpc_helper.get(p1[i+1][0],p1[i+1][1],p1[i+1][2])
        
        ob.draw.path(f"[{np}],[{n1}]")
      
      color = color1[counter].replace('#','')
      ob.color.set.html(color)
      draw_path = draw_orbit_segment(p1, i)

      color = color2[counter].replace('#','')
      ob.color.set.html(color)
      draw_path = draw_orbit_segment(p2, i)

      color = color3[counter].replace('#','')
      ob.color.set.html(color)
      draw_path = draw_orbit_segment(p3, i)

      if segment_counter > 1: # FIRST 1-2 SEGMENTS CAN BE NEONPULSE TO INDICATE BODY ORIGINS
        global BRUSH_TYPE
        if BRUSH_TYPE != "DuctTape":
          BRUSH_TYPE = "DuctTape"
          ob.brush.type(BRUSH_TYPE)
      
    segment_counter += 1

    # if i > 20000:
      # return


BRUSH_TYPE = "NeonPulse"

def main():
  if "OB_HOST" in os.environ:
      ob.OB_HOST = os.environ['OB_HOST']

  ob.new()
  ob.brush.type(BRUSH_TYPE)
  ob.brush.size.set(0.1)
  ob.brush.move.to("0,0,0")
  ob.user.move.to("-20,-5,-7")

  three_body()

if __name__ == '__main__':
  main()
