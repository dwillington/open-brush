Settings = {
    description="Delegate",
    previewType="quad"
}

--------------------------------------------------------------------------------
-- Start() is called only once?
--------------------------------------------------------------------------------
function Start()
    inUse = 0

    WebRequest:Get("http://10.6.23.235:8080", handleRequest, onError)
    -- WebRequest:Get("https://jsonplaceholder.typicode.com/todos/1", handleRequest)


    -- svgPath = "M703 1129l306 139l61 -188l-328 -68v14q0 53 -39 103zM732 983l226 -248l-160 -116l-166 291q63 18 100 73zM601 910l-165 -291l-160 116l226 248q37 -55 99 -73zM492 1012l-328 68l61 188l305 -139q-38 -50 -38 -104v-13zM555 1147l-37 333h198l-37 -333q-35 13 -62 13t-62 -13z"
    -- if svgPath ~= nil then
        -- paths = Svg:ParsePathString(svgPath)
        -- path = paths:Longest() -- Get the longest path
        -- path:Normalize(2)
        -- path:SampleByDistance(0.1)
        -- return paths
    -- end

end

function handleRequest(result)
    print("in handleRequest: " .. result)
    -- result='{"svgPath": "M703 1129l306 139l61 -188l-328 -68v14q0 53 -39 103zM732 983l226 -248l-160 -116l-166 291q63 18 100 73zM601 910l-165 -291l-160 116l226 248q37 -55 99 -73zM492 1012l-328 68l61 188l305 -139q-38 -50 -38 -104v-13zM555 1147l-37 333h198l-37 -333q-35 13 -62 13t-62 -13z"}'
    -- json_string = json:encode(result)
    json_data = json:parse(result)
    svgPath = json_data.svgPath

    svgPath = 'M703 1129l306 139l61 -188l-328 -68v14q0 53 -39 103zM732 983l226 -248l-160 -116l-166 291q63 18 100 73zM601 910l-165 -291l-160 116l226 248q37 -55 99 -73zM492 1012l-328 68l61 188l305 -139q-38 -50 -38 -104v-13zM555 1147l-37 333h198l-37 -333q-35 13 -62 13t-62 -13z'

    WebRequest:Get("http://10.6.23.235:8080/xxxxxxxxx", onSuccess, onError, {["svgPathReceived"] = svgPath})
end

function Main()
    if inUse == 0 then

      inUse = 1

      paths = Svg:ParsePathString(svgPath)
      path = paths:Longest()
      path:Normalize(2)
      path:SampleByDistance(0.1)
      return path

    else
      -- WebRequest:Get("http://localhost:40074/api/v1?scripts.toolscript.deactivate")
      return
    end

end


function onSuccess(result)
end

