import sys
import os
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
sys.path.append("..")
import ob_helper

def three_body():
  # plt.style.use('dark_background')

  # masses of planets
  m_1 = 15
  m_2 = 15
  m_3 = 15

  # starting coordinates for planets
  # p1_start = x_1, y_1, z_1
  p1_start = np.array([-10, 10, -11])
  v1_start = np.array([-3, 0, 0])

  # p2_start = x_2, y_2, z_2
  p2_start = np.array([0, 0, 0])
  v2_start = np.array([0, 0, 0])

  # p3_start = x_3, y_3, z_3
  p3_start = np.array([10, 10, 12])
  v3_start = np.array([3, 0, 0])


  def accelerations(p1, p2, p3):
    """
    A function to calculate the derivatives of x, y, and z
    given 3 object and their locations according to Newton's laws
    
    """

    # m_1, m_2, m_3 = self.m1, self.m2, self.m3
    planet_1_dv = -9.8 * m_2 * (p1 - p2)/(np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**3) - \
             9.8 * m_3 * (p1 - p3)/(np.sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2 + (p1[2] - p3[2])**2)**3)

    planet_2_dv = -9.8 * m_3 * (p2 - p3)/(np.sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2 + (p2[2] - p3[2])**2)**3) - \
             9.8 * m_1 * (p2 - p1)/(np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)**3)

    planet_3_dv = -9.8 * m_1 * (p3 - p1)/(np.sqrt((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2 + (p3[2] - p1[2])**2)**3) - \
             9.8 * m_2 * (p3 - p2)/(np.sqrt((p3[0] - p2[0])**2 + (p3[1] - p2[1])**2 + (p3[2] - p2[2])**2)**3)

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

    step_size = 500
    if (i % step_size) == 0:
      # print(p1[i+1])

      def draw_orbit_segment(p1, i):
        p = -step_size
        np0 = dpc_helper.get(p1[i+p][0],p1[i+p][1]+1,p1[i+p][2])
        np = dpc_helper.get(p1[i+p][0],p1[i+p][1],p1[i+p][2])
        # n0 = "0,0,0"
        n0 = dpc_helper.get(p1[i+1][0],p1[i+1][1]+1,p1[i+1][2])
        n1 = dpc_helper.get(p1[i+1][0],p1[i+1][1],p1[i+1][2])

        draw_path = f"draw.paths=[[{n0}],[{n1}]]"

        draw_path = f"draw.paths=[[{n0}],[{n1}]],[[{np}],[{n1}]],[[{np0}],[{n0}]]"

        ob_helper.sendCommands([f"{draw_path}"])
        return draw_path
      
      ob_helper.sendCommands([f"color.set.html=red"])
      draw_path = draw_orbit_segment(p1, i)

      ob_helper.sendCommands([f"color.set.html=white"])
      draw_path = draw_orbit_segment(p2, i)

      ob_helper.sendCommands([f"color.set.html=blue"])
      draw_path = draw_orbit_segment(p3, i)

    # if i > 2000: 
      # return


def main():
  if "OB_HOST" in os.environ:
    ob_helper.ob_host = os.environ['OB_HOST']

  ob_helper.sendCommands(["new"])
  ob_helper.sendCommands(["brush.type=Light"])
  ob_helper.sendCommands(["brush.move.to=0,0,0"])
  # ob_helper.sendCommands(["user.move.to=-60,4,80"])

  three_body()

if __name__ == '__main__':
  main()
