title: Holo Prism Calc
template: template.html

---

<div>
  <h1>Reflective Prism Template Generator</h1>
  <p>This calculator generates a template for cutting a 2 sides of a reflective prism from a sheet of material with minimal waste and maximum size.<p>
</div>
<div>
  Sheet Height: <input id="sheight" type="number" name="sheight" min="1" max="600" value="100" onchange="redraw()"/> <br>
  Sheet Width: <input id="swidth" type="number" name="swidth" min="1" max="900" value="100" onchange="redraw()"/> <br>
  <br>
  <canvas id="myCanvas" width="600" height="400"></canvas>
  <br>
  Prism Height: <input id="pheight" type="number" name="pheight" readonly/> <br>
  Prism Small Base:  <input id="pwidth" type="number" name="pwidth" readonly/> <br>
  Prism Large Base:  <input id="pwidth2" type="number" name="pwidth" readonly/> <br>
</div>
<script>
  function redraw() {
    var canvas = document.getElementById('myCanvas');
    canvas.width = document.getElementById('swidth').value;
    canvas.height = document.getElementById('sheight').value;
    if(canvas.width > canvas.height*1.5) {
      canvas.width = canvas.height*1.5;
      document.getElementById('swidth').value = canvas.height*1.5
    }
    var context = canvas.getContext('2d');
    var base = (canvas.width/2)/Math.tan(Math.PI/3);

    document.getElementById('pwidth').value = canvas.height-(2*base);
    document.getElementById('pwidth2').value = canvas.height;
    document.getElementById('pheight').value = canvas.width/2;

    var triheight = canvas.height*(Math.sqrt(3)/2)
    context.beginPath();
    context.moveTo(0, 0);
    context.lineTo(triheight, canvas.height/2);
    context.lineTo(0, canvas.height);
    context.strokeStyle = 'darkgray';
    context.stroke();

    context.beginPath();
    context.moveTo(canvas.width, 0);
    context.lineTo(canvas.width-triheight, canvas.height/2);
    context.lineTo(canvas.width, canvas.height);
    context.strokeStyle = 'darkgray';
    context.stroke();

    context.beginPath();
    context.moveTo(0, 0);
    context.lineTo(canvas.width/2, base);
    context.lineTo(canvas.width/2, canvas.height-base);
    context.lineTo(0, canvas.height);
    context.closePath();
    context.strokeStyle = 'black';
    context.stroke();
    
    context.beginPath();
    context.moveTo(canvas.width, 0);
    context.lineTo(canvas.width/2, base);
    context.lineTo(canvas.width/2, canvas.height-base);
    context.lineTo(canvas.width, canvas.height);
    context.closePath();
    context.strokeStyle = 'black';
    context.stroke();
  }
  redraw();
</script>
