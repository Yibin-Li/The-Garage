var app = new PIXI.Application(800, 600, {backgroundColor : 0xe0e4ff});
document.body.appendChild(app.view);

/*PIXI.loader
    .add("../img/boomBaloon.json")
    .load(setup);*/

PIXI.loader
    .add("/dodgeball-test-version/img/boomBaloon.json")
    .add("/dodgeball-test-version/img/bird.json")
    .load(setup);

function setup() {
    // get a reference to the sprite sheet we've just loaded:
    //console.log("sheet");
    //let sheet = PIXI.loader.resources["/dodgeball-test-version/img/boomBaloon.json"].spritesheet;
    //console.log(sheet);

    console.log("startanimate");

    // baloon
    let alienImagesBaloon = ["FLOURISH-_BoomBaloon-_BaloonAssets_01.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_02.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_03.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_04.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_05.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_06.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_07.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_08.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_09.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_10.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_11.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_12.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_13.png",
    "FLOURISH-_BoomBaloon-_BaloonAssets_14.png"];
    let textureArrayBaloon = [];

    for (let i=0; i < 14; i++)
    {
         let textureBaloon = PIXI.Texture.from(alienImagesBaloon[i]);
         textureArrayBaloon.push(textureBaloon);
    };

    // create an animated sprite
    let animatedBoomBaloon = new PIXI.extras.AnimatedSprite(textureArrayBaloon);
    // set speed, start playback and add it to the stage
    animatedBoomBaloon.animationSpeed = 0.167;
    animatedBoomBaloon.play();
    app.stage.addChild(animatedBoomBaloon);


    // bird
    let alienImagesBird = []
    for (let i=1; i <8; i++){
      let string = "FLOURISH-_BoomBaloon-_BirdAssets_0" + String(i) + ".gif";
      alienImagesBird.push(string);
    }
    //console.log(alienImagesBird);
    let textureArrayBird = [];

    for (let i=0; i < 14; i++)
    {
         let textureBird = PIXI.Texture.from(alienImagesBird[i]);
         textureArrayBird.push(textureBird);
    };

    // create an animated sprite
    let animatedBird = new PIXI.extras.AnimatedSprite(textureArrayBird);

    // set speed, start playback and add it to the stage
    animatedBird.position.x = 100
    animatedBird.animationSpeed = 0.167;
    animatedBird.play();
    app.stage.addChild(animatedBird);

}
