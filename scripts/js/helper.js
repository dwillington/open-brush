function initBrushes() {
  var brushes = ["Light","Icing","OilPaint","Ink","ThickPaint","WetPaint","Marker","TaperedMarker","PinchedMarker","Highlighter","Flat","TaperedFlat","PinchedFlat","SoftHighlighter","Fire","Embers","Smoke","Snow","Rainbow","Stars","VelvetInk","Waveform","Splatter","DuctTape","Paper","CoarseBristles","DrWigglez","Electricity","Streamers","Hypercolor","Bubbles","NeonPulse","CelVinyl","HyperGrid","LightWire","ChromaticWave","Dots","Petal","Toon","Wire","Spikes","Lofted","Disco","Comet","ShinyHull","MatteHull","UnlitHull","Diamond","Leaves","DotMarker","Plasma","Taffy","Flat"];
  var menu = document.getElementById("brush.type");
  for (var brush of brushes) {
    var option = document.createElement("option");
    option.text = brush;
    option.name = brush;
    menu.add(option);
  }
}

function setBrushOptions() {
  sendCommands([
    'color.set.html=' + document.getElementById("brush.color").value,
    'brush.size.set=' + document.getElementById("brush.size").value,
    'brush.type=' + document.getElementById("brush.type").value
  ]);
}

function clearScene() {
  sendCommands(["new"]);
  sendCommands(["brush.move.to=0,0,0","brush.look.up"]);
  sendCommands(["user.move.to=0,0," + document.getElementById("user.Z").value]);
}

function clearSceneAndMoveTo(x,y,z) {
  sendCommands(["new"]);
  sendCommands(["brush.move.to=0,0,0","brush.look.up"]);
  sendCommands([`user.move.to=${x},${y},${z}`]);
}

function sendCommands(commandStrings) {
  var xmlHttp = new XMLHttpRequest();
  var url = 'http://localhost:40074/api/v1?' + commandStrings.join('&');
  log(commandStrings.join('\n'));
  xmlHttp.open('GET', url, async=false);
  try {
    xmlHttp.send();
  }
  catch(err) {
  }
}

function log(message) {
  var textarea = document.getElementById("results");
  textarea.value += `${message}\n`;
  textarea.scrollTop = textarea.scrollHeight; // Scroll to the end
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getRandomColorInHex() {
  var letters = '0123456789ABCDEF';
  var color = "";
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

 function shouldIExit(){
  var r = confirm("Exit?");
  if (r == true) {
    throw new Error("exit");
  }
}
      
