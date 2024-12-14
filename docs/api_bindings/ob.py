import urllib.request
import urllib.parse

class ob:

    OB_HOST = "localhost"
    
    STATIC_BRUSHES = ["Light","Icing","OilPaint","Ink","ThickPaint","WetPaint","Marker","TaperedMarker","PinchedMarker","Highlighter","Flat","TaperedFlat","PinchedFlat","SoftHighlighter","VelvetInk"
    ,"DuctTape","Paper","CelVinyl", "Toon"]
    DYNAMIC_BRUSHES= ["Fire","DrWigglez","Hypercolor","Comet","Disco","Rainbow","Waveform","Electricity","ChromaticWave","NeonPulse","Dots","Plasma","Streamers"]
    FILL_BRUSHES = ["Diamond","ShinyHull","MatteHull","UnlitHull"]

    CAPTURE_COMMAND = True
    CAPTURE_FILE = "/tmp/ob_command_capture.txt"
    def logCommand(log):
      print(log.replace(log.split('?')[0] + '?', ''), file=open(ob.CAPTURE_FILE, 'a'))

    class listenfor:
        @staticmethod
        def strokes(url):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?listenfor.strokes={url}")
    class showfolder:
        @staticmethod
        def scripts():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?showfolder.scripts")
        @staticmethod
        def exports():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?showfolder.exports")
        @staticmethod
        def sketch(index):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?showfolder.sketch={index}")
    class spectator:
        class move:
            @staticmethod
            def to(position):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.move.to={position}")
            @staticmethod
            def by(amount):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.move.by={amount}")
        class turn:
            @staticmethod
            def y(angle):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.turn.y={angle}")
            @staticmethod
            def x(angle):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.turn.x={angle}")
            @staticmethod
            def z(angle):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.turn.z={angle}")
        @staticmethod
        def direction(direction):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.direction={direction}")
        class look:
            @staticmethod
            def at(position):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.look.at={position}")
        @staticmethod
        def mode(mode):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.mode={mode}")
        @staticmethod
        def show(thing):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.show={thing}")
        @staticmethod
        def hide(thing):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.hide={thing}")
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.toggle")
        @staticmethod
        def on():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.on")
        @staticmethod
        def off():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?spectator.off")
    class user:
        class move:
            @staticmethod
            def to(position):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?user.move.to={position}")
                if ob.CAPTURE_COMMAND:
                  ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?user.move.to={position}")
            @staticmethod
            def by(amount):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?user.move.by={amount}")
                if ob.CAPTURE_COMMAND:
                  ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?user.move.by={position}")
    class brush:
        class move:
            @staticmethod
            def to(position):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.move.to={position}")
                if ob.CAPTURE_COMMAND:
                  ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?brush.move.to={position}")
            @staticmethod
            def by(position):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.move.by={position}")
                if ob.CAPTURE_COMMAND:
                  ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?brush.move.by={position}")
            @staticmethod
            def straight(distance):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.move={distance}")
          # @staticmethod
        # def move(distance):
            # urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.move={distance}")
        @staticmethod
        def draw(distance):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.draw={distance}")
        class turn:
            @staticmethod
            def y(angle):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.turn.y={angle}")
            @staticmethod
            def x(angle):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.turn.x={angle}")
            @staticmethod
            def z(angle):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.turn.z={angle}")
        class look:
            @staticmethod
            def at(direction):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.look.at={direction}")
            @staticmethod
            def forwards():
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.look.forwards")
            @staticmethod
            def up():
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.look.up")
            @staticmethod
            def down():
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.look.down")
            @staticmethod
            def left():
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.look.left")
            @staticmethod
            def right():
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.look.right")
            @staticmethod
            def backwards():
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.look.backwards")
        class home:
            @staticmethod
            def set():
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.home.set")
        class transform:
            @staticmethod
            def push():
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.transform.push")
                if ob.CAPTURE_COMMAND:
                  ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?brush.transform.push")
            @staticmethod
            def pop():
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.transform.pop")
                if ob.CAPTURE_COMMAND:
                  ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?brush.transform.pop")
        @staticmethod
        def forcepainting(active):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.forcepainting={active}")
        @staticmethod
        def type(brushType):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.type={brushType}")
            if ob.CAPTURE_COMMAND:
              ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?brush.type={brushType}")
        class size:
            @staticmethod
            def set(size):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.size.set={size}")
                if ob.CAPTURE_COMMAND:
                  ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?brush.size.set={size}")
            @staticmethod
            def add(amount):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?brush.size.add={amount}")
    class debug:
        @staticmethod
        def brush():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?debug.brush")
    class image:  
        @staticmethod
        def import_(location):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?image.import={location}")
        @staticmethod
        def position(index, position):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?image.position={index},{position}")
    class environment:
        @staticmethod
        def type(name):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?environment.type={name}")
    class layer:
        @staticmethod
        def add():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?layer.add")
        @staticmethod
        def clear(layer):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?layer.clear={layer}")
        @staticmethod
        def delete(layer):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?layer.delete={layer}")
        @staticmethod
        def squash(squashedLayer, destinationLayer):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?layer.squash={squashedLayer},{destinationLayer}")
        @staticmethod
        def activate(layer):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?layer.activate={layer}")
        @staticmethod
        def show(layer):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?layer.show={layer}")
        @staticmethod
        def hide(layer):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?layer.hide={layer}")
        @staticmethod
        def toggle(layer):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?layer.toggle={layer}")
    class model:
        @staticmethod
        def import_(location):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?model.import={location}")
        @staticmethod
        def rotation(index,rotation):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?model.rotation={index},{rotation}")
        @staticmethod
        def scale(index,scale):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?model.scale={index},{scale}")
        @staticmethod
        def position(index, position):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?model.position={index},{position}")
        @staticmethod
        def webimport(url):
            data = urllib.parse.urlencode({"model.webimport":f"{url}"}).encode()
            req  = urllib.request.Request(f"http://{ob.OB_HOST}:40074/api/v1", data=data)
            resp = urllib.request.urlopen(req)
            if ob.CAPTURE_COMMAND:
              ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?model.webimport={url}")
            return resp
    class guide:
        @staticmethod
        def add(type):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?guide.add={type}")
    class draw:
        @staticmethod
        def paths(jsonString):
            data = urllib.parse.urlencode({"draw.paths":f"{jsonString}"}).encode()
            req  = urllib.request.Request(f"http://{ob.OB_HOST}:40074/api/v1", data=data) # "POST"
            resp = urllib.request.urlopen(req)
            if ob.CAPTURE_COMMAND:
              ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?draw.paths={jsonString}")
            # urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?draw.paths={jsonString}")
        @staticmethod
        def path(jsonString):
            data = urllib.parse.urlencode({"draw.path":f"{jsonString}"}).encode()
            req  = urllib.request.Request(f"http://{ob.OB_HOST}:40074/api/v1", data=data) # POST
            resp = urllib.request.urlopen(req)
            if ob.CAPTURE_COMMAND:
              ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?draw.path={jsonString}")
            # urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?draw.path={jsonString}") # GET
        @staticmethod
        def stroke(jsonString):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?draw.stroke={jsonString}")
        @staticmethod
        def polygon(sides, radius, angle):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?draw.polygon={sides},{radius},{angle}")
            if ob.CAPTURE_COMMAND:
              ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?draw.polygon={sides},{radius},{angle}")
        @staticmethod
        def text(text):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?draw.text={text}")
        @staticmethod
        def opentypetext(text):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?draw.opentypetext={text}")
        @staticmethod
        def svg(svgPathString):
            # urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?draw.svg={svgPathString}")
            data = urllib.parse.urlencode({"draw.svg":f"{svgPathString}"}).encode()
            req  = urllib.request.Request(f"http://{ob.OB_HOST}:40074/api/v1", data=data) # "POST"
            resp = urllib.request.urlopen(req)
            if ob.CAPTURE_COMMAND:
              ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?draw.svg={svgPathString}")
        @staticmethod
        def camerapath(index):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?draw.camerapath={index}")
    class color:
        class add:
            @staticmethod
            def hsv(hsv):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?color.add.hsv={hsv}")
            @staticmethod
            def rgb(rgb):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?color.add.rgb={rgb}")
        class set:
            @staticmethod
            def rgb(rgb):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?color.set.rgb={rgb}")
                if ob.CAPTURE_COMMAND:
                  ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?color.set.rgb={rgb}")
            @staticmethod
            def hsv(hsv):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?color.set.hsv={hsv}")
            @staticmethod
            def html(color):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?color.set.html={color}")
                if ob.CAPTURE_COMMAND:
                  ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?color.set.html={color}")
    class save:
        @staticmethod
        def overwrite():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?save.overwrite")
        @staticmethod
        def new():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?save.new")
    class export:
        @staticmethod
        def all():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?export.all")
        @staticmethod
        def current():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?export.current")
        @staticmethod
        def selected():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?export.selected")
    class drafting:
        @staticmethod
        def visible():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?drafting.visible")
        @staticmethod
        def transparent():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?drafting.transparent")
        @staticmethod
        def hidden():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?drafting.hidden")
    class load:
        @staticmethod
        def user(slot):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?load.user={slot}")
        @staticmethod
        def curated(slot):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?load.curated={slot}")
        @staticmethod
        def liked(slot):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?load.liked={slot}")
        @staticmethod
        def drive(slot):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?load.drive={slot}")
        @staticmethod
        def named(filename):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?load.named={filename}")
    class merge:
        @staticmethod
        def named(filename):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?merge.named={filename}")
    @staticmethod
    def new():
        urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?new")
        if ob.CAPTURE_COMMAND:
          import os
          try:
            os.remove(ob.CAPTURE_FILE)
          except OSError:
            pass
          ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?new")
    class symmetry:
        @staticmethod
        def mirror():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?symmetry.mirror")
        @staticmethod
        def doublemirror():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?symmetry.doublemirror")
    class twohandeded:
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?twohandeded.toggle")
    class straightedge:
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?straightedge.toggle")
    class autoorient:
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?autoorient.toggle")
    @staticmethod
    def undo():
        urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?undo")
        if ob.CAPTURE_COMMAND:
          ob.logCommand(f"http://{ob.OB_HOST}:40074/api/v1?undo")
    @staticmethod
    def redo():
        urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?redo")
    class panels:
        @staticmethod
        def reset():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?panels.reset")
    class sketch:
        @staticmethod
        def origin():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?sketch.origin")
    class viewonly:
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?viewonly.toggle")
    class autosimplify:
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?autosimplify.toggle")
    class guides:
        @staticmethod
        def disable():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?guides.disable")
    @staticmethod
    def disco():
        urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?disco")
    class selection:
        @staticmethod
        def duplicate():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?selection.duplicate")
        @staticmethod
        def group():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?selection.group")
        @staticmethod
        def invert():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?selection.invert")
        @staticmethod
        def flip():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?selection.flip")
        @staticmethod
        def recolor():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?selection.recolor")
        @staticmethod
        def rebrush():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?selection.rebrush")
        @staticmethod
        def resize():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?selection.resize")
        @staticmethod
        def trim(count):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?selection.trim={count}")
        class points:
            @staticmethod
            def addnoise(axis, scale):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?selection.points.addnoise={axis},{scale}")
    class camerapath:
        @staticmethod
        def render():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?camerapath.render")
        @staticmethod
        def togglevisuals():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?camerapath.togglevisuals")
        @staticmethod
        def togglepreview():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?camerapath.togglepreview")
        @staticmethod
        def delete():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?camerapath.delete")
        @staticmethod
        def record():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?camerapath.record")
    class profiling:
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?profiling.toggle")
    class settings:
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?settings.toggle")
    class mirror:
        @staticmethod
        def summon():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?mirror.summon")
    class select:
        @staticmethod
        def all():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?select.all")
    class postprocessing:
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?postprocessing.toggle")
    class watermark:
        @staticmethod
        def toggle():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?watermark.toggle")
    class stroke:
        @staticmethod
        def delete(index):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?stroke.delete={index}")
        @staticmethod
        def select(index):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?stroke.select={index}")
        class points:
            @staticmethod
            def quantize(grid):
                urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?stroke.points.quantize={grid}")
        @staticmethod
        def join():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?stroke.join")
        @staticmethod
        def add(index):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?stroke.add={index}")
    class strokes:
        @staticmethod
        def select(start, end):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?strokes.select={start},{end}")
        @staticmethod
        def join(start, end):
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?strokes.join={start},{end}")
    class tool:
        @staticmethod
        def sketchsurface():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.sketchsurface")
        @staticmethod
        def selection():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.selection")
        @staticmethod
        def colorpicker():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.colorpicker")
        @staticmethod
        def brushpicker():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.brushpicker")
        @staticmethod
        def brushandcolorpicker():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.brushandcolorpicker")
        @staticmethod
        def sketchorigin():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.sketchorigin")
        @staticmethod
        def autogif():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.autogif")
        @staticmethod
        def canvas():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.canvas")
        @staticmethod
        def transform():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.transform")
        @staticmethod
        def stamp():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.stamp")
        @staticmethod
        def freepaint():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.freepaint")
        @staticmethod
        def eraser():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.eraser")
        @staticmethod
        def screenshot():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.screenshot")
        @staticmethod
        def dropper():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.dropper")
        @staticmethod
        def saveicon():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.saveicon")
        @staticmethod
        def threedofviewing():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.threedofviewing")
        @staticmethod
        def multicam():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.multicam")
        @staticmethod
        def teleport():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.teleport")
        @staticmethod
        def repaint():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.repaint")
        @staticmethod
        def recolor():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.recolor")
        @staticmethod
        def rebrush():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.rebrush")
        @staticmethod
        def pin():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.pin")
        @staticmethod
        def camerapath():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.camerapath")
        @staticmethod
        def fly():
            urllib.request.urlopen(f"http://{ob.OB_HOST}:40074/api/v1?tool.fly")

