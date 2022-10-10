// PATH=/c/tools/node-v16.17.1-win-x64:$PATH

var XMLHttpRequest = require('xhr2');

var START_X = -15, START_Y = 22, START_Z = 0;

function log(message) {
  console.log(message);
  // console.log(`${message}\n`);
}

var callUrl = function(url) {
    try {
      var xhr = new XMLHttpRequest();
      xhr.addEventListener("load", function() { xhr.response; }, false);
      xhr.open('GET', url);
      xhr.send();
    }
    catch(e) {
      console.error(e, e.stack);
    }
}

var sendCommands = function(commandStrings) {
    var url = 'http://localhost:40074/api/v1?' + commandStrings.join('&');
    log(commandStrings.join('\n'));
    callUrl(url);
}

var clearScene = function() {
  sendCommands(["new"]);
  sendCommands(["brush.move.to=0,0,0","brush.look.up"]);
  sendCommands(["user.move.to=0,0," + 20]);
}

clearScene();

var commandStrings = [];

var mind_map_ideas = 
  [
  "idea 1", 
  "idea 2", 
  "great idea 3",
  "someday ideal 4",
  "crazy idea 5",
  "whoa idea 6",
  ];

for (let i = 0; i < mind_map_ideas.length; i++) {
  var text = encodeURIComponent(mind_map_ideas[i]);
  var randomColor = Math.floor(Math.random()*16777215).toString(16);
  commandStrings.push("brush.move.to=" + START_X + "," + (START_Y - (i*2)) + "," + START_Z + 
    "&color.set.html=" + randomColor + "&draw.text=" + text);
}

sendCommands(commandStrings);

// for (var i=0; i<1; i++) {
  // console.log("HELLO WORLD!");
// }
