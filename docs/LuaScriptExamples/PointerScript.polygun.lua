Settings = {
    description="As you draw, extra lines are added from the start of your stroke to the current position"
}

Parameters = {
    rate ={label="Rate", type="int", min=1, max=10, default=10},
    sides={label="Sides", type="int", min=3, max=10, default=3},
 }

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
    --Store the brush transform at the moment we start drawing a line
    drawingPosition = brush.position
    currentRotation = brush.rotation


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

    if app.frames % (4*rate) == 0 then

        -- print(brush.colorRgb)
        -- color.add.rgb()
        brush.colorRgb ={math.random(), math.random(), math.random()}
        -- turtle.lookAt({brush.position.x+1,brush.position.y+1,brush.position.z,})
        DrawShape(sides,r)
    end

    drawingPosition = {
        brush.position.x,
        brush.position.y,
        brush.position.z + r,
    }

    turtle.moveTo(drawingPosition)

    return {currentPos}
end

function End()
    brush.forcePaintingOff(false)
end

function DrawShape(sides,length)

    -- local radius = length / (2 * math.sin(math.pi / sides))
    local radius = length / sides
    local size = 2 * radius * math.sin(math.pi / sides)
    if size < 0.058 then return end -- OB CANNOT DRAW SMALLER THAN THIS (FOR NON HULL)
    turtle.moveBy({-radius, -radius, 0})
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