import requests
import random

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
