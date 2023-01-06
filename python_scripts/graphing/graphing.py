# ../../docs/README.md
from ob import ob
import socket
import os
import time
import requests
from datetime import date, timedelta
from pprint import pprint
from collections import deque

def graphing():
  ob.new()
  ob.user.move.to("0,10,10")
  ob.draw.path("[0,0,0],[0,1,0]")

"""

def generate_time_series():

  shuf -i 0-999 -n 1000

"""

def draw_x_axis_value(CURRENT_X, COUNTER):
    ob.brush.size.set(f"0.1")
    ob.brush.transform.push()
    ob.brush.move.to(f"{CURRENT_X},2,0")
    ob.draw.text(f"{COUNTER % 100}")
    print(f"{COUNTER % 100}")
    ob.brush.transform.pop()

def draw_chunk_path(CURRENT_X, draw_values):
  draw_path = ""
  for i in range(0,len(draw_values)):
    draw_path += f"[{CURRENT_X+i},{draw_values[i]},0],"
  # print(draw_path)
  ob.draw.path(draw_path)
  draw_path = ""
  for i in range(0,len(draw_values)):
    draw_path += f"[{CURRENT_X+i+0.2},{draw_values[i]+0.2},0.2],"
  # print(draw_path)
  ob.color.set.html("ff1493")
  ob.draw.path(draw_path)
  ob.color.set.html("00ff7f")

def draw_time_series():

  COUNTER = 0
  CURRENT_X = 0
  Y_OFFSET = 5
  USER_Z_OFFSET = 40
  CHUNK_SIZE = 5

  ob.new()
  ob.brush.type(f"Paper")
  draw_x_axis_value(CURRENT_X,COUNTER)
  ob.brush.move.to(f"0,{Y_OFFSET},0")
  ob.user.move.to(f"{CURRENT_X},0,{USER_Z_OFFSET}")

  Y_VALUES = []
  with open("/root/temp/tmp/time_series.txt") as file:
    for line in file:
      # print(line.rstrip())
      line_data = line.rstrip().split()
      EPOCH_VAL = line_data[0]
      Y = int(line_data[0])/100
      Y_VALUES.append(Y)

    draw_values = []
    for i in range(0,len(Y_VALUES)):
      draw_values.append(Y_VALUES[i])
      if COUNTER % CHUNK_SIZE == 0 and (COUNTER > 0):
        print(draw_values)
        # ob.brush.type(f"Paper")
        draw_x_axis_value(CURRENT_X,COUNTER)
        draw_chunk_path(CURRENT_X-CHUNK_SIZE, draw_values)
        draw_values = [Y_VALUES[i]]


      # if COUNTER % USER_Z_OFFSET == 0 and (COUNTER > 0):
      SCROLL_SMOOTH_FACTOR = 20 # REALLY SMOOTH SCROLLING FORWARD; BIGGER = SMOOTHER
      SPEED_FACTOR = 0.5 # SMALLER = FASTER UPDATES
      for i in range(0,SCROLL_SMOOTH_FACTOR):
        ob.user.move.by(f"{1/SCROLL_SMOOTH_FACTOR},0,0")
        time.sleep(SPEED_FACTOR/SCROLL_SMOOTH_FACTOR) 

      COUNTER += 1
      CURRENT_X += 1

      if (COUNTER > 200):
        break

    if COUNTER % CHUNK_SIZE != 0 and (COUNTER > 0): # FLUSH
      ob.draw.path(draw_path)


def draw_series(data):

  COUNTER = 0
  CURRENT_X = 0
  Y_OFFSET = 5
  USER_Z_OFFSET = 40
  CHUNK_SIZE = 10

  ob.new()
  ob.brush.size.set(f"1")
  ob.brush.type(f"Paper")
  ob.brush.move.to(f"0,{Y_OFFSET},0")
  ob.user.move.to(f"{CURRENT_X},0,{USER_Z_OFFSET}")

  draw_path = ""
  while data:
    values = data.pop()
    x_axis_value = values[0]
    Y_VALUE = values[1]
    print(f"{x_axis_value}, {Y_VALUE}")

    ########################################
    # X_AXIS_LABEL
    ########################################
    ob.brush.size.set(f"0.1")
    ob.brush.transform.push()
    ob.brush.move.to(f"{CURRENT_X-3.5},2,0")
    ob.color.set.html("ff1493")
    ob.draw.text(f"{x_axis_value}")
    ob.brush.transform.pop()

    ########################################
    # BAR VERTICAL LINE
    ########################################
    ob.color.set.html("ff1493")
    ob.brush.type(f"NeonPulse")
    bar_path = f"[{CURRENT_X},0,0],[{CURRENT_X},{Y_VALUE},0]"
    ob.draw.path(bar_path)

    ########################################
    # T0 - T1 LINE
    ########################################
    ob.brush.type(f"Paper")
    ob.color.set.html("00ff7f")
    draw_path += f"[{CURRENT_X},{Y_VALUE},0]"
    # print(draw_path)
    ob.draw.path(draw_path)
    draw_path = f"[{CURRENT_X},{Y_VALUE},0],"

    ########################################
    # Y VALUE AT TOP OF GRAPH
    ########################################
    # ob.brush.size.set(f"0.1")
    ob.brush.transform.push()
    ob.brush.move.to(f"{CURRENT_X-(1 if Y_VALUE>9 else 0.5)},{Y_VALUE+Y_OFFSET+1},0")
    ob.color.set.html("ffa500")
    ob.draw.text(f"{Y_VALUE}")
    ob.brush.transform.pop()

    # SCROLL_SMOOTH_FACTOR = 20 # REALLY SMOOTH SCROLLING FORWARD; BIGGER = SMOOTHER
    # SPEED_FACTOR = 1 # SMALLER = FASTER UPDATES

    SECONDS_PER_CHUNK_ADVANCE = 1
    INCREMENT = 0.25
    i = 0
    while i < (CHUNK_SIZE):
      ob.user.move.by(f"{INCREMENT},0,0")
      sleep_time = (SECONDS_PER_CHUNK_ADVANCE/(CHUNK_SIZE/INCREMENT))
      # print(i)
      time.sleep(sleep_time)
      i += INCREMENT

    COUNTER += 1
    CURRENT_X += CHUNK_SIZE

    if (COUNTER > 25):
      break


def is_sunday(day):
    return day.weekday() == 6

def sundays_within_last_x_days(num_days = 90):
    result = []
    end_date = date.today()
    start_date = end_date - timedelta(days = num_days)
    while start_date <= end_date:
        if is_sunday(start_date):
            result.append(start_date.strftime('%Y-%b-%d'))
        start_date += timedelta(days = 1)
    return result

def git_weekly_commits():
  url = 'https://api.github.com/repos/icosa-gallery/open-brush/stats/participation'
  headers = {'Accept': 'application/vnd.github+json',
             'X-GitHub-Api-Version': '2022-11-28'}
  resp = requests.get(url, "", headers=headers)

  weekly_commits = []
  if resp.status_code == 200:
    # print(resp.json()['all'])
    weekly_commits = resp.json()['all']
    # print(f"weekly_commits:{len(weekly_commits)}")
  return weekly_commits

def draw_git_weekly_commits():
  weekly_commits = git_weekly_commits(); weekly_commits.reverse()  # GET WEEKLY COMMITS IN DESCENDING ORDER BY MOST RECENT WEEK FIRST
  print(weekly_commits[-5:])
  sundays = sundays_within_last_x_days(400); sundays.reverse() # GET WEEKS IN DESCENDING ORDER
  commits_by_week = deque()
  for i in range(len(weekly_commits)):
    commits_by_week.append([sundays[i],weekly_commits[i]])

  draw_series(commits_by_week)

  # sundays = sundays[(len(sundays)-52):] # REMOVE 
  # print(commits_by_week)
  # while commits_by_week:
    # print(f"{commits_by_week.pop()}")

  
def main():
  if "OB_HOST" in os.environ:
      ob.OB_HOST = os.environ['OB_HOST']

  # draw_time_series()

  draw_git_weekly_commits()


if __name__ == '__main__':
    main()
