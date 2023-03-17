Settings = {
    description = "Fire Polygons!"
}

Parameters = {
    rate = { label = "Rate", type = "int", min = 1, max = 10, default = 10 },
    sides = { label = "Sides", type = "int", min = 3, max = 10, default = 3 },
}

function getCG1()
    local mcg = { "fafa6e",
        "e5f56f",
        "d1f072",
        "bdea75",
        "aae479",
        "98de7c",
        "86d780",
        "75d084",
        "64c987",
        "54c18a",
        "44b98d",
        "34b28e",
        "23aa8f",
        "10a18f",
        "00998f",
        "00918d",
        "00898a",
        "008087",
        "007882",
        "0d707d",
        "176877",
        "1f5f70",
        "245769",
        "285061",
        "2a4858",
    }
    return mcg
end

function getCGExpanded(colors)
    local mcg = {}
    for i = 1, #colors - 1, 1 do
        -- print(i)
        local gradients = colorGradient(colors[i], colors[i + 1], 4)
        mcg = TableConcat(mcg, gradients)
    end
    return mcg
end

function getCG2()
    local cg = { "03071e", "370617", "6a040f", "9d0208", "d00000", "dc2f02", "e85d04", "f48c06", "faa307", "ffba08" }
    -- cg1 = {"ffbe0b","fb5607","ff006e","8338ec","3a86ff"}
    local mcg = getCGExpanded(cg)
    -- print(#mcg)
    return mcg
end

function getCG3()
    randColor1 = rgbToHex(math.random(63), math.random(63), math.random(63))
    randColor2 = rgbToHex(math.random(255), math.random(255), math.random(255))
    randColor1 = "03071e"
    randColor2 = "ffba08"
    -- print(randColor1)
    -- print(randColor2)
    local mcg = colorGradient(randColor1, randColor2, 20)
    return mcg
end

function Start()
    brush.forcePaintingOff(true)
end

function OnTriggerPressed()
    initialPos = {
        brush.position.x,
        brush.position.y,
        brush.position.z,
    }
    currentPos = initialPos

    --Store the brush transform
    drawingPosition = brush.position
    currentRotation = brush.rotation


    -- brush.colorHtml = randColor1

    myColorGradient = {}
    cgChoice = math.random(3)
    print(cgChoice)
    if cgChoice == 1 then
        myColorGradient = getCG1()
    elseif cgChoice == 2 then
        myColorGradient = getCG2()
    else
        myColorGradient = getCG3()
    end

    colorIndex = 1

    return { drawingPosition, currentRotation }
end

function WhileTriggerPressed()
    currentPos = {
        brush.position.x,
        brush.position.y,
        brush.position.z,
    }

    -- local radius = app.time % 3
    -- local r = radius
    local radius = 1
    local r = 1
    if (brush.triggerIsPressed) then
        r = radius * brush.timeSincePressed
    end

    if app.frames % (4 * rate) == 0 then
        -- print(r)
        -- turtle.lookAt({brush.position.x+1,brush.position.y+1,brush.position.z,})
        -- brush.colorHtml = lighten_color(brush.colorHtml, 1)
        -- newColor = cg1[colorIndex]
        newColor = myColorGradient[colorIndex]
        brush.colorHtml = newColor
        colorIndex = colorIndex + 1
        -- print(brush.colorHtml)
        DrawShape(sides, r)
    end

    drawingPosition = {
        brush.position.x,
        brush.position.y,
        brush.position.z + r,
    }

    turtle.moveTo(drawingPosition)

    return { currentPos }
end

function End()
    brush.forcePaintingOff(false)
end

function TableConcat(t1, t2)
    for i = 1, #t2 do
        t1[#t1 + 1] = t2[i]
    end
    return t1
end

function DrawShape(sides, length)
    -- local radius = length / (2 * math.sin(math.pi / sides))
    local radius = length / sides
    local size = 2 * radius * math.sin(math.pi / sides)
    if size < 0.058 then return end -- OB CANNOT DRAW SMALLER THAN THIS (FOR NON HULL)
    turtle.moveBy({ -radius, -radius, 0 })
    turtle.lookUp()
    for i = 0, sides, 1 do
        turtle.draw(size)
        turtle.turnY(360 / sides)
    end

    -- if sides == 4
    --     center_nmove = radius / 2
    --     if sides == 5 then
    --         -- https://www.redcrab-software.com/en/Calculator/Pentagon
    --         center_nmove = radius / 1.17557
    --     end
    --     turtle.lookUp()
    --     turtle.moveBy({-center_nmove, -center_nmove, 0})
    --     for i = 0, sides, 1 do
    --         print(i)
    --         turtle.draw(radius)
    --         turtle.turnY(360/sides)
    --     end
    -- else
    --     turtle.lookForwards()
    --     draw.polygon(sides, radius, 0)
    -- end
end

function lighten_color(hex_color, amount)
    -- Convert hex color to RGB
    local red = tonumber(hex_color:sub(1, 2), 16)
    local green = tonumber(hex_color:sub(3, 4), 16)
    local blue = tonumber(hex_color:sub(5, 6), 16)

    -- Lighten the color
    red = math.min(255, math.floor(red + amount))
    green = math.min(255, math.floor(green + amount))
    blue = math.min(255, math.floor(blue + amount))

    -- Convert back to hex color
    local new_hex_color = string.format("%02X%02X%02X", red, green, blue)
    return new_hex_color
end

function hexToRgb(hex)
    hex = hex:gsub("#", "")
    -- print(hex:sub(1, 2))
    -- print("n" .. tonumber(hex:sub(1, 2), 16))
    -- return tonumber("0x" .. hex:sub(1, 2)), tonumber("0x" .. hex:sub(3, 4)), tonumber("0x" .. hex:sub(5, 6))
    return tonumber(hex:sub(1, 2), 16), tonumber(hex:sub(3, 4), 16), tonumber(hex:sub(5, 6), 16)
end

function rgbToHex(r, g, b)
    -- print(r,g,b)
    r = string.format("%X", math.floor(r))
    g = string.format("%X", math.floor(g))
    b = string.format("%X", math.floor(b))
    if #r == 1 then r = "0" .. r end
    if #g == 1 then g = "0" .. g end
    if #b == 1 then b = "0" .. b end
    return r .. g .. b
end

function colorGradient(startColor, endColor, steps)
    -- print("s" .. startColor)
    -- print("e" .. endColor)
    -- print(hexToRgb(startColor))
    -- print(hexToRgb(endColor))
    local startR, startG, startB = hexToRgb(startColor)
    local endR, endG, endB = hexToRgb(endColor)
    local stepR = (endR - startR) / steps
    local stepG = (endG - startG) / steps
    local stepB = (endB - startB) / steps
    local colors = {}
    for i = 0, steps do
        local r = startR + (stepR * i)
        local g = startG + (stepG * i)
        local b = startB + (stepB * i)
        table.insert(colors, rgbToHex(r, g, b))
    end
    return colors
end
