@ag100.route('/ss1')
def solvespace1():
    outstring = '''
 <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  

def ss1(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M46.933 33.321 C55.450,32.452 74.800,33.645 67.133,40.721 C59.466,47.797 24.783,60.755 17.733,70.121 C10.684,79.487 31.270,85.260 49.533,81.121 C67.797,76.982 83.739,62.932 92.133,48.721 C100.527,34.511 101.373,20.140 94.133,17.921 C86.893,15.703 71.567,25.636 63.533,23.321 C55.500,21.006 54.758,6.442 42.133,5.721 C29.508,5.000 5.000,18.121 25.533,33.121 C40.733,37.121 38.417,34.190 46.933,33.321 "
    #cgoChamber = window.svgToCgoSVG(chamber)
    # -centerx 為 x 座標的 offset 值, 也就是新原點位於 (centerx, centery)
    #cgoChamber = window.svgToCgoSVG(chamber, -centerx, -centery)
    cgoChamber = window.svgToCgoRHC(chamber, -107.373, -91.26)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 放大 2 倍
    cgo.render(cmbr, x, y, 2, rot)

ss1(0, 0, 0, 0, 0, "blue", True, 4)
</script>
</body>
</html>
'''
