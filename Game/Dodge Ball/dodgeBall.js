PIXI.utils.sayHello();
// size of the game
/*if (window.innerWidth > window.innerHeight) {
	console.log(window.innerWidth);
	console.log(window.innerHeight);
	var xSize = window.innerWidth - 20; // 800 originally
	var ySize = window.innerHeight - 20; // 600 originally
} else {
	var xSize = window.innerHeight - 20; // 800 originally
	var ySize = window.innerWidth - 20; // 600 originally
	console.log(window.innerWidth);
	console.log(window.innerHeight);
}*/

var xSize = window.innerWidth - 20; // 800 originally
var ySize = window.innerHeight - 20; // 600 originally

// current time
var d = new Date();
var n = d.getTime();

// -------------Balls Variables-----------------
// starting position of other balls
var xStart = 100;
var yStart = 200;

// startign position of the player's ball
var xPlayerStart = 300;
var yPlayerStart = 400;

// radius of the playerball
var playerBallRadius = 30;

// radius of the ball
var ballRadius = 30;

// velocity of the playerball
var playerBallVelocity = 24;

// number of balls in the screen
var ballNumber = 2;

// current game level
var curretLevels = 0;

// -------------Time Variables-------------------
// wait time between each level (in milliseconds)
var waitLevelTime = 1000;

// the time player is invincible (in milliseconds)
var invincibleTime = 3000;

// the time to play for each level (in milliseconds)
var levelTime = 10000;

// the time to display the instruction (in milliseconds)
var instructionDisplayTime = 5000;

// the time to display countdown text (in milliseconds)
var countdownDisplayTime = 1000;

// the time to display all text before the game starts
var allTextDisplayTime = countdownDisplayTime * 3 + instructionDisplayTime;

// the time to dispaly the announcement (in milliseconds)
var announcementTime = 2000;

// ------------------Other Variables---------------------
// the scale for the score (update when capture the reward)
var scale = 1;

// set reward present in the screen
var rewardPresent = true;

// initialize mouse/touch reading
var mouseX = -1;
var mouseY = -1;

// ----------------Elements Variables----------------
// set up current game environment
var app = new PIXI.Application(xSize, ySize, {backgroundColor: 0x1099bb});
document.body.appendChild(app.view);
//app.renderer.resize(window.innerWidth, window.innerHeight);

// initialize reward
var reward = new PIXI.Graphics();
reward.beginFill(0x39ff2b); // green
reward.drawRect(0, 0, 20, 20);
reward.x = 50;
reward.y = 50;
reward.endFill();
app.stage.addChild(reward);
rewardXSpeed = Math.floor(Math.random() * 8) - 4;
rewardYSpeed = Math.floor(Math.random() * 8) - 4;

// initialize player ball
var playerBall = new PIXI.Graphics();
playerBall.beginFill(0xffffff); // white
playerBall.drawCircle(0, 0, playerBallRadius);
playerBall.x = xPlayerStart;
playerBall.y = yPlayerStart;
playerBall.endFill();
app.stage.addChild(playerBall);

initializeBallsAndDraw();

/*// add player info to the screen (optional after v0.2)
let xCo = playerBall.x.toString();
let yCo = playerBall.y.toString();
var playerInfoText = new PIXI.Text("X: " + xCo + " " + "Y: " + yCo + " V: " + playerBallVelocity, {
	fontSize: 20
});
playerInfoText.x = 0;
playerInfoText.y = 0;
app.stage.addChild(playerInfoText);*/

// add announcement to the screen
var announcementText = new PIXI.Text("Score Doubled!", {
	fontSize: 50,
	fill: '0xffffff'
});
announcementText.x = 20;
announcementText.y = 0;
announcementText.alpha = 0;
app.stage.addChild(announcementText);

// add currect score text
var scoreText = new PIXI.Text("Score: " + 0, {fontSize: 50});
scoreText.x = app.screen.width / 2 - 110;
scoreText.y = 0;
app.stage.addChild(scoreText);

// add time of survival
var timeText = new PIXI.Text("Time: " + 0 + "s", {
	fontSize: 30
});
timeText.x = app.screen.width - 160;
timeText.y = 0;
app.stage.addChild(timeText);

// UI text
var levelText = new PIXI.Text("Next Level", {
			fontWeight: 'bold',
			fontStyle: 'italic',
			fontSize: 80
});
levelText.x = app.screen.width / 2 - 180;
levelText.y = app.screen.height / 2 - 50;
levelText.alpha = 0;
app.stage.addChild(levelText);

// add level info
var levelInfoText = new PIXI.Text("Level: " + curretLevels, {
	fontSize: 30
});
levelInfoText.x = app.screen.width - 160;
levelInfoText.y = 40;
app.stage.addChild(levelInfoText);

// instruction text before the game starts
var instructionText = new PIXI.Text("			        			          The game is easy \n Avoid the read objects by sliding on the screen \n		     For extra points capture the green objects", {
		fontWeight: 'bold',
		fontSize: 30
});
instructionText.alpha = 0;
app.stage.addChild(instructionText);

instructionText.x = app.screen.width / 2 - 300;
instructionText.y = app.screen.height / 2 - 80;

var sanText = new PIXI.Text("San", {
		fontWeight: 'bold',
		fontSize: 75
});
sanText.alpha = 0;
app.stage.addChild(sanText);

var erText = new PIXI.Text("Er", {
		fontWeight: 'bold',
		fontSize: 75
});
erText.alpha = 0;
app.stage.addChild(erText);

var yiText = new PIXI.Text("Yi", {
		fontWeight: 'bold',
		fontSize: 75
});
yiText.alpha = 0;
app.stage.addChild(yiText);

sanText.x = app.screen.width / 2 - 30;
sanText.y = app.screen.height / 2 -30;
erText.x = app.screen.width / 2 - 30;
erText.y = app.screen.height / 2 - 30;
yiText.x = app.screen.width / 2 - 30;
yiText.y = app.screen.height / 2 - 30;


// add functions to each frame
//app.ticker.add(instructionDisplay);
instructionDisplay = displayText(instructionText, instructionDisplayTime, 0);

sanTextDisplay = displayText(sanText, countdownDisplayTime, instructionDisplayTime);
erTextDisplay = displayText(erText, countdownDisplayTime, instructionDisplayTime + countdownDisplayTime);
yiTextDisplay = displayText(yiText, countdownDisplayTime, instructionDisplayTime + 2 * countdownDisplayTime);

announcementDisplay = "";
app.ticker.add(instructionDisplay);
app.ticker.add(sanTextDisplay);
app.ticker.add(erTextDisplay);
app.ticker.add(yiTextDisplay);
app.ticker.add(motion);
app.ticker.add(nextLevel);
app.ticker.add(end);

// Add three events (keydown, mousemove, touchmove) listener to our document
//document.addEventListener('keydown', onKeyPressed);
document.addEventListener('mousemove', onMouseMove);
document.addEventListener("touchmove", onTouchMove);

/* Helper functions
-----------------------------------------------------
*/

// function that displayes text in a given time
function displayText(textToDisplay, duration, startTime) {
	function helper() {
		// update time
		let date = new Date();
		let timeElapsed = date.getTime() - n;

		//console.log("time passed: " + timeElapsed);
		//console.log("time supposed to stop: " + startTime + duration);

		if ((startTime < timeElapsed) && (timeElapsed < startTime + duration)) {
			textToDisplay.alpha = 100;
		}
		else {
			textToDisplay.alpha = 0;
		}
	}
	return helper;
}


// initialize balls and their random velocity
function initializeBallsAndDraw() {
	// store all balls graphics to allGraphic, velocity to allGraphicVelocity
	allGraphic = [];
	allGraphicVelocity = [];

	// create balls
	for (let i = 0; i < ballNumber; i++) {
		let newBall = new PIXI.Graphics();
		allGraphic.push(newBall);
		app.stage.addChild(newBall);
		xv = Math.floor(Math.random() * 30) - 15;
		yv = Math.floor(Math.random() * 30) - 15;
		allGraphicVelocity.push([xv, yv]);
	};

	// draw all ball graphics on the screen
	for (let j = 0; j < allGraphic.length; j++) {
		let ball = allGraphic[j];
		ball.beginFill(0xff0000); // white
		ball.drawCircle(0, 0, ballRadius); // drawCircle(x, y, radius)
		ball.x = xStart;
		ball.y = yStart;
		allGraphic[j].endFill();
	};
};

// the core function for animation
function motion() {
	// update time
	let d = new Date();
	let timeElapsed = d.getTime() - n - allTextDisplayTime;

	if (timeElapsed > 0) {

		// check if need to display text (130000 means 13s, 10s for each
		// level, 3s for display text)
		if (timeElapsed > (levelTime - 50) + curretLevels*(levelTime + waitLevelTime)) {
			// console.log("movingballs called curretLevels: " + curretLevels)
			levelText.alpha = 100;
		};

		// playerBall blinks to show invincibility
		let levelOngoingTime = timeElapsed - curretLevels*(levelTime + waitLevelTime);
		if (levelOngoingTime < 3000){
			if (levelOngoingTime / 400 % 2 <= 1) {
				playerBall.alpha = 0.6;
			} else {
				playerBall.alpha = 1;
			}

		} else{
			playerBall.alpha = 100;
		}


		if (rewardCollided() && rewardPresent){
			app.stage.removeChild(reward);
			scale = scale * 2;
			rewardPresent = false;
			announcementDisplay = displayText(announcementText, announcementTime, d.getTime() - n);
			app.ticker.add(announcementDisplay);
			announcementText.alpha = 100;
		};
		// update text
		/*let xCo = playerBall.x.toString();
		let yCo = playerBall.y.toString();
		playerInfoText.text = "X: " + xCo + " Y: " + yCo + " V: " + playerBallVelocity;
		*/

		//update score and time
		scoreText.text = "Score: " + (timeElapsed - curretLevels*waitLevelTime) * scale;
		timeText.text = "Time: " +
		(1 + Math.floor((timeElapsed - curretLevels*waitLevelTime)/ 1000)) + "s";
		levelInfoText.text = "Level: " + (curretLevels + 1);

		// update red balls' position
		for (let j = 0; j < allGraphic.length; j++) {
			let xPos = allGraphic[j].x + allGraphicVelocity[j][0];
			let yPos = allGraphic[j].y + allGraphicVelocity[j][1];
			if (xPos > xSize || xPos < 0) {
				allGraphicVelocity[j][0] = -allGraphicVelocity[j][0];
			};
			if (yPos > ySize || yPos < 0) {
				allGraphicVelocity[j][1] = -allGraphicVelocity[j][1];
			};
			allGraphic[j].x += allGraphicVelocity[j][0];
			allGraphic[j].y += allGraphicVelocity[j][1];
		};

		// update reward's position
		rewardXPos = reward.x;
		rewardYPos = reward.y;
		//console.log("x: ", rewardXPos);
		//console.log("y: ", rewardYPos);
		if (rewardXPos > xSize || rewardXPos < 0) {
			rewardXSpeed = -rewardXSpeed;
		};
		if (rewardYPos > ySize || rewardYPos < 0) {
			rewardYSpeed = -rewardYSpeed;
		};
		reward.x += rewardXSpeed;
		reward.y += rewardYSpeed;
	};
};

// return if the palyer collided with the balls
function collided() {
	for (let j = 0; j < allGraphic.length; j++) {
		let ball = allGraphic[j];
		let dis = Math.sqrt((playerBall.x - ball.x) ** 2
		+ (playerBall.y - ball.y) ** 2);
		if (dis <= ballRadius) {
			return true;
		};
	};
	return false;
};

// function that terminates the game (when the player collide with the red balls)
function end() {

	// find elapsed time from the game starts
	let d = new Date();
	let timeElapsed = d.getTime() - n - allTextDisplayTime;

	if (timeElapsed > invincibleTime +
		curretLevels*(levelTime + waitLevelTime) && collided()) {
		app.ticker.stop();
		scoreText.alpha = 0;
		// playerInfoText.alpha = 0;

		/*// clean the screen
		for (var i = app.stage.children.length - 1; i >= 0; i--) {
			app.stage.removeChild(app.stage.children[i]);
		};*/
		var endText = new PIXI.Text("Game Over", {
			fontWeight: 'bold',
			fontStyle: 'italic',
			fontSize: 90,
			//fontFamily: 'Arvo',
			//fill: '#3e1707',
			//align: 'center',
			//stroke: '#a4410e',
			//strokeThickness: 7
		});

		var endTextScore = new PIXI.Text("  Score: "+
		(timeElapsed - curretLevels*waitLevelTime) * scale, {
			fontWeight: 'bold',
			fontStyle: 'italic',
			fontSize: 50,
		});

		endText.x = app.screen.width / 2 - 200;
		endText.y = app.screen.height / 2 - 50;
		endTextScore.x = app.screen.width / 2 - 150;
		endTextScore.y = app.screen.height / 2 - 105;
		app.stage.addChild(endText);
		app.stage.addChild(endTextScore);
	};
	// return score, time
};

// if the player survive more than 10s, game goes to next level
function nextLevel() {
	let d = new Date();
	let timeElapsed = d.getTime() - n - allTextDisplayTime;

	if (timeElapsed > (levelTime + 1) + curretLevels*(levelTime + waitLevelTime)) {
		curretLevels += 1;

		// increase difficulty
		ballNumber += 1;
		ballRadius += 1;

		app.ticker.stop();

		// stop for waitLevelTime milliseconds
		let dd = new Date();
		let timer = dd.getTime() - d.getTime();
		while (timer < waitLevelTime) {
			let dd = new Date();
			timer = dd.getTime() - d.getTime();
		}

		// clean the screen
		for (let i = app.stage.children.length - 1; i >= 0; i--) {
			app.stage.removeChild(app.stage.children[i]);
		};

		app.ticker.start();

		// consider remove this line in the future?
		app.ticker.remove(instructionDisplay);
		app.ticker.remove(announcementDisplay);

		// make levelInfoText invisible during the game
		levelText.alpha = 0;
		repeat();
	};
};

// repeat the game process after finishing one level
function repeat() {
	app.stage.addChild(reward);
	let rewardXSpeed = Math.floor(Math.random() * 2) + 3;
	let rewardYSpeed = Math.floor(Math.random() * 2) + 3;
	rewardPresent = true;
	announcementText.alpha = 0;
	app.stage.addChild(playerBall);
	app.stage.addChild(scoreText);
	//app.stage.addChild(playerInfoText);
	app.stage.addChild(announcementText)
	app.stage.addChild(timeText);
	app.stage.addChild(levelText);
	app.stage.addChild(levelInfoText);
	initializeBallsAndDraw();
};

function rewardCollided() {
	//let d = new Date();
	//let timeElapsed = d.getTime() - n - instructionDisplayTime;
	let dis = Math.sqrt((playerBall.x - reward.x - 5) ** 2
		+ (playerBall.y - reward.y - 5) ** 2);
	if (dis <= ballRadius) {
		return true;
	};
	return false;
};

/* keyboard, mouse, and touch screen operations
-----------------------------------------------------
*/
// touch screen control method
function onTouchMove(touchData){
	app.renderer.plugins.interaction.on('pointerdown', function(event) {
		MouseCoordinates = event.data.global;
		});
	//currentMousePos.x = "x:" + MouseCoordinates.x;
	//currentMousePos.y = "y: " + MouseCoordinates.y;
	mouseX = MouseCoordinates.x;
	mouseY = MouseCoordinates.y;
	let playerX = playerBall.x
	let playerY = playerBall.y
	let dist = Math.sqrt((playerX - mouseX - 6) ** 2
		+ (playerY - mouseY - 6) ** 2);
	let d = new Date();
	let timeElapsed = d.getTime() - n;

	if (timeElapsed > allTextDisplayTime && dist >= playerBallRadius) {
		let distScalar = Math.sqrt(((mouseX - playerX)**2 +
		(mouseY - playerY)**2)/ playerBallVelocity**2);
		if (((playerBall.x + (mouseX - playerX) / distScalar) >= 0 + playerBallRadius) &&
			 ((playerBall.x + (mouseX - playerX) / distScalar) <= xSize - playerBallRadius)){
			playerBall.x += (mouseX - playerX) / distScalar;
		};

		if (((playerBall.y + (mouseY - playerY) / distScalar) >= 0 + playerBallRadius) &&
			 ((playerBall.y + (mouseY - playerY) / distScalar) <= ySize - playerBallRadius)){
			playerBall.y += (mouseY - playerY) / distScalar;
		};
	};
};

// mouse control method
function onMouseMove(mouseData) {
	mouseX = mouseData.x
	mouseY = mouseData.y
	let playerX = playerBall.x
	let playerY = playerBall.y
	let dist = Math.sqrt((playerX - mouseX - 6) ** 2
		+ (playerY - mouseY - 6) ** 2);
	//console.log("onMouseMoved");
	//console.log("mouse " + "x: " + mouseX + ", " + "y: " + mouseY);
	//console.log("ball " + "x: " + playerX + ", " + "y: " + playerY)
	let d = new Date();
	let timeElapsed = d.getTime() - n;

	if (timeElapsed > allTextDisplayTime && dist >= playerBallRadius) {
		let distScalar = Math.sqrt(((mouseX - playerX)**2 +
		(mouseY - playerY)**2)/ playerBallVelocity**2);
		if (((playerBall.x + (mouseX - playerX) / distScalar) >= 0 + playerBallRadius) &&
			 ((playerBall.x + (mouseX - playerX) / distScalar) <= xSize - playerBallRadius)){
			playerBall.x += (mouseX - playerX) / distScalar;
		};

		if (((playerBall.y + (mouseY - playerY) / distScalar) >= 0 + playerBallRadius) &&
			 ((playerBall.y + (mouseY - playerY) / distScalar) <= ySize - playerBallRadius)){
			playerBall.y += (mouseY - playerY) / distScalar;
		};
	};
};

// keyboard control method
function onKeyPressed(key) {
	let d = new Date();
	let timeElapsed = d.getTime() - n;

	if (timeElapsed > allTextDisplayTime) {

		// W Key is 87, Up arrow is 87. If the W key or the Up arrow is pressed,
		// move the player up. Don't move up if the player is at the top of the stage.
		if ((key.keyCode === 87 || key.keyCode === 38)&&
			((playerBall.y - playerBallVelocity) >= 0 + playerBallRadius))	{
			playerBall.y -= playerBallVelocity;
		};

		// S Key is 83, Down arrow is 40. If the S key or the Down arrow is pressed,
		// move the player down. Don't move if the player is at the bottom.
		if ((key.keyCode === 83 || key.keyCode === 40)&&
			((playerBall.y + playerBallVelocity) <= ySize - playerBallRadius)) {
			playerBall.y += playerBallVelocity;
		};

		// A Key is 65, Left arrow is 37. If the A key or the Left arrow is pressed,
		// move the player to the left. Don't move if the player is at the left side.
		if ((key.keyCode === 65 || key.keyCode === 37)&&
			((playerBall.x - playerBallVelocity) >= 0 + playerBallRadius)) {
			playerBall.x -= playerBallVelocity;
		};

		// D Key is 68, Right arrow is 39. If the D key or the Right arrow is pressed,
		// move the player to the right.Don't move if the player is at the right side.
		if ((key.keyCode === 68 || key.keyCode === 39)&&
			((playerBall.x + playerBallVelocity) <= xSize - playerBallRadius)){
			playerBall.x += playerBallVelocity;
		};
	};
};
