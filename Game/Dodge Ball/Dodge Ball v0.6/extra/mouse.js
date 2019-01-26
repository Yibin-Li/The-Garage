(function() {

    var _mouseY = 0;
    var _mouseX = 0;
    var _debugText;

    var _stage = new PIXI.Stage(0xFF0000, true);

    var _renderer = new PIXI.CanvasRenderer(1024, 768, null, true);
        _renderer.view.style.display = "block";

    document.getElementById("canvas-holder").appendChild(_renderer.view);

    var _target = new PIXI.DisplayObjectContainer();
        _target.setInteractive(true);

    _stage.addChild(_target);
  
    _stage.mousedown = _stage.touchstart = onMouseDown;
    _stage.mousemove = _stage.touchmove = onMouseMove;
    _stage.mouseup = _stage.touchend = onMouseUp;

    _debugText = new PIXI.Text("Hello! Move your mouse about!", {font: "italic 28px Georgia", fill: "white", align: "left"});
    _debugText.position.x = 30;
    _debugText.position.y = 30;
    _target.addChild(_debugText);

    animate();

    function onMouseDown(mouseData){
        console.log("onMouseDown");
    }

    function onMouseUp(mouseData){
        console.log("onMouseUp");
    }

    function onMouseMove(mouseData) {
        console.log("onMouseMoved2");
        var mouse = mouseData.getLocalPosition(_stage);
        _debugText.position.x = mouse.x
        _debugText.position.y = mouse.y;
        _mouseY = mouse.y;
        _mouseX = mouse.y;
        _debugText.setText(_mouseX+","+_mouseY);
    }

    function animate() {
        _renderer.render(_stage);
        requestAnimFrame(animate);
    }

})();