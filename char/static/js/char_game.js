let charScene = new Phaser.Scene('Character');
console.log(document.getElementById('phaser-canvas'))
let config = {
  type: Phaser.AUTO,
  parent: 'phaser-canvas',
  width: document.getElementById('phaser-canvas').clientWidth,
  height: document.getElementById('phaser-canvas').clientHeight,
  scene: charScene,
}

let game = new Phaser.Game(config);
