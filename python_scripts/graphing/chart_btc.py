from ob import ob
import sys
import os
from datetime import datetime
sys.path.append("../")
import ob_helper
import glob
from xml.dom import minidom
import time
from re import sub
from decimal import Decimal
from mycolorpy import colorlist as mcp
import random
import calendar

def read_csv():
  file_name = "/mnt/c/temp/tmp/btc/btc_historical.csv"
  # import pandas as pd
  # data = pd.read_csv(file_name,nrows=10)
  # print(data)
  # return

  import csv
  with open(file_name, newline='') as f:
    reader = csv.reader(f)
    next(reader, None)
    data = list(reader)
  # print(data[0])
  return data


svgDict = {}
def parseSVGs():
  files = glob.glob("../text/Aldrich-Regular/*.svg")
  for fullfile in files:
    filename = os.path.basename(fullfile)
    name = os.path.splitext(f"{filename}")[0]
    # print(name)
    doc = minidom.parse(fullfile)
    glyphs = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
    # print(glyphs[0])
    svgDict[name] = glyphs[0]
    
  # print(svg_files)
  return

SVG_CHAR_UNIT_LENGTH = 0.25
def drawText(text, x,y,z):
  # ob.brush.transform.push()
  num_of_chars = len(text)
  for char in text:
    move_to = f"{dpc_helper.get(x-(num_of_chars*SVG_CHAR_UNIT_LENGTH/2),y,z)}"
    # print(move_to)
    ob.brush.move.to(move_to)
    ob.draw.svg(svgDict[char].replace(" ", "%20"))
    x += SVG_CHAR_UNIT_LENGTH
    # ob.brush.transform.pop()
  ob.brush.move.to("0,0,0")

def draw_x_values(start, end, step):
  ob.color.set.html("F000FF")
  x = 0
  for i in range(start,end,step):
    # color = ocean_colors[x].replace('#','')
    # ob.color.set.html(color)
    value = str(i).zfill(2)
    drawText(value, x,-0.5,0)
    x += 1

def draw_y_values(start, end, step):
  ocean_colors = list(reversed(mcp.gen_color(cmap="ocean",n=int((end-start)/step))))
  y = 0
  for i in range(start,end,step):
    color = ocean_colors[y].replace('#','')
    ob.color.set.html(color)
    value = str(i).zfill(4)
    drawText(value, -1, y+SVG_CHAR_UNIT_LENGTH-0.1, 0)
    y += 1

def draw_z_values():
  z = 0
  for i in range(1,7):
    ob.color.set.html(bar_colors[i].replace('#',''))    
    value = calendar.month_name[i][:3].upper()
    drawText(value, -1, -0.5, z)
    z += 1

def drawBar(value, x,y,z):
  half_bar_width = 0.1
  # RECTANGULAR BAR
  a = dpc_helper.get(x-half_bar_width,y,z)
  b = dpc_helper.get(x+half_bar_width,y,z)
  c = dpc_helper.get(x+half_bar_width,y+value,z)
  d = dpc_helper.get(x-half_bar_width,y+value,z)
  # dp = f"[[{a}],[{b}]],[[{b}],[{c}]],[[{c}],[{d}]],[[{d}],[{a}]]"
  dp = f"[[{a}],[{b}],[{c}],[{d}],[{a}]]"
  # print(dp)
  ob.draw.paths(dp)

# bar_colors = mcp.gen_color(cmap="plasma_r",n=5)
bar_colors = [ '#AA48FB', '#12E8FD', '#80E9D1', '#5400A2', '#FF7BF7', '#F732B5', '#5116A3' ]
# bar_colors = [ '#071828', '#113E4D', '#A4B49D', '#EAD868', '#1C8D92', '#BFD88F' ]
dpc_helper = ob_helper.DPC(1,0,1,0)
def chart():
  data = read_csv()
  draw_x_values(1,11,1)
  draw_y_values(0,10000,1000)
  draw_z_values()

  CURRENT_X = 0
  COUNTER = 0
  Z = -1
  if True:
    for row in data:
      # "Date","value","Open","High","Low","Vol.","Change %"
      print(row)
      date_string = row[0]
      date_format = "%b %d, %Y"
      date_object = datetime.strptime(date_string, date_format)

      if (date_object.month - 1) > Z:
        Z = date_object.month - 1
        ob.color.set.html(bar_colors[Z].replace('#',''))

      if date_object.day > 10:
        continue
      
      CURRENT_X = int(date_object.day) - 1
      # DRAW X-AXIS LABEL
      # if Z == 0:
        # day_of_month = str(date_object.day).zfill(2)
        # drawText(day_of_month, CURRENT_X,-0.5,0)
      
      if Z > 3: break

      # DRAW BAR
      open_value = Decimal(sub(r'[^\d.]', '', row[1]))
      scaled_open_value = round(float(open_value)/1000,2)
      drawBar(scaled_open_value, CURRENT_X,0,Z)

      COUNTER += 1
    

def main():
  if "OB_HOST" in os.environ:
    ob.OB_HOST = os.environ['OB_HOST']
  ob.new()
  ob.user.move.to("-3,12,15")
  parseSVGs()
  chart()

if __name__ == '__main__':
    main()


# supported values are 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'