Settings = {
    description="Delegate",
    previewType="quad"
}

function Start()
    inUse = 0
end

function Main()
    if App.frames % 10 == 0 then

      if inUse == 0 then
        inUse = 1
      else
        return
      end

      WebRequest:Get("http://10.6.23.235:8080", getSvgPath, onError, {["Accept"] = "application/json"}, context)

      -- WebRequest:Get("http://localhost:40074/api/v1?scripts.toolscript.deactivate")
    
      -- svgPath = "M213.588,120.982L115,213.445l-98.588-92.463C-6.537,96.466-5.26,57.99,19.248,35.047l2.227-2.083 c24.51-22.942,62.984-21.674,85.934,2.842L115,43.709l7.592-7.903c22.949-24.516,61.424-25.784,85.936-2.842l2.227,2.083 C235.26,57.99,236.537,96.466,213.588,120.982z"
      -- local stroke = Svg:ParsePathString(svgPath)
      -- stroke:Normalize(2) -- Scale and center inside a 2x2 square
      -- stroke:SampleByDistance(0.1) -- Make the stroke evenly spaced
      -- return stroke

      -- svgPath = "M703 1129l306 139l61 -188l-328 -68v14q0 53 -39 103zM732 983l226 -248l-160 -116l-166 291q63 18 100 73zM601 910l-165 -291l-160 116l226 248q37 -55 99 -73zM492 1012l-328 68l61 188l305 -139q-38 -50 -38 -104v-13zM555 1147l-37 333h198l-37 -333q-35 13 -62 13t-62 -13z"
      if svgPath ~= nil then
        paths = Svg:ParsePathString(svgPath)
        path = paths:Longest() -- Get the longest path
        path:Normalize(2)
        path:SampleByDistance(0.1)
        return paths
      end
      
    end

end

function getSvgPath(result)
  json_data = json:parse(result)
  svgPath = json_data.svgPath

  -- svgPath = "M703 1129l306 139l61 -188l-328 -68v14q0 53 -39 103zM732 983l226 -248l-160 -116l-166 291q63 18 100 73zM601 910l-165 -291l-160 116l226 248q37 -55 99 -73zM492 1012l-328 68l61 188l305 -139q-38 -50 -38 -104v-13zM555 1147l-37 333h198l-37 -333q-35 13 -62 13t-62 -13z"
  -- paths = Svg:ParsePathString(svgPath)
  -- path = paths:Longest()
  -- path:Normalize(2)
  -- path:SampleByDistance(0.1)
  -- paths:Draw()

  WebRequest:Get("http://10.6.23.235:8080/xxxxxxxxx", onSuccess, onError, {["svgPathReceived"] = svgPath})
  inUse = 0
  WebRequest:Get("http://localhost:40074/api/v1?scripts.toolscript.deactivate")
end

function onSuccess(result)
end

