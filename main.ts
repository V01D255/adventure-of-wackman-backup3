namespace SpriteKind {
    export const GUI = SpriteKind.create()
    export const fire = SpriteKind.create()
    export const ice = SpriteKind.create()
    export const misc = SpriteKind.create()
    export const shop = SpriteKind.create()
    export const youreawful = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    wackman,
    player_animations[3],
    350,
    false
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.shop, function (sprite, otherSprite) {
    RandomGreetings = ["hey yeah yeah welcome to shawppa shawp", "yeah give me heart", "yyeaahhh"]
    RandomGoodbyes = ["give haerts for the best EVER", "always welcome back", "give more hearts for good luck everytime"]
    game.showLongText(RandomGreetings._pickRandom(), DialogLayout.Bottom)
    if (game.ask("Give Shawppa 1 heart?")) {
        temp = randint(0, 5)
        info.changeLifeBy(-1)
        for (let index = 0; index < 4; index++) {
            inventory.unshift(temp)
        }
    } else {
        game.showLongText("please my rent is due tomorrow", DialogLayout.Bottom)
    }
    luck += 1
    game.showLongText(RandomGoodbyes._pickRandom(), DialogLayout.Bottom)
    DisplayInv()
    otherSprite.destroy(effects.smiles, 1000)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (inventory[1] == 5) {
        vitality += 1
        inventory.removeAt(1)
    } else if (inventory[1] == 3) {
        wackman.startEffect(effects.fire, 1000)
        wackman.startEffect(effects.warmRadial, 2000)
        for (let index = 0; index < 10; index++) {
            fire = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . 4 4 . . . . . . . 
                . . . . . . 4 5 5 4 . . . . . . 
                . . . . . . 2 5 5 2 . . . . . . 
                . . . . . . . 2 2 . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, wackman, randint(-30, 30), randint(-30, 30))
            fire.setKind(SpriteKind.fire)
        }
        maxenem += 1
        inventory.removeAt(1)
    } else if (inventory[1] == 4) {
        info.changeLifeBy(randint(1, vitality))
        inventory.removeAt(1)
    } else if (inventory[1] == 0) {
        wackman.startEffect(effects.fountain, 1000)
        wackman.startEffect(effects.coolRadial, 2000)
        for (let index = 0; index < 10; index++) {
            ice = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . 6 6 6 5 5 6 6 6 . . . . 
                . . . 7 7 7 7 6 6 6 6 6 6 . . . 
                . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
                . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
                . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
                . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
                . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
                . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
                . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
                . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
                . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                . . . . 6 6 8 8 8 8 6 6 . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, wackman, randint(-10, 10), randint(-10, 10))
            ice.setKind(SpriteKind.ice)
        }
        inventory.removeAt(1)
    } else if (inventory[1] == 2) {
        maxenem += -3
        inventory.removeAt(1)
        wackman.startEffect(effects.blizzard, 500)
    } else if (inventory[1] == 1) {
        inventory.removeAt(1)
        luck += 1
    } else if (inventory[1] == 6) {
        inventory.removeAt(1)
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy, effects.ashes, 500)
        sprites.destroyAllSpritesOfKind(SpriteKind.shop, effects.ashes, 500)
    } else {
        inventory.removeAt(1)
    }
    DisplayInv()
})
sprites.onOverlap(SpriteKind.fire, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.vx += -30
    otherSprite.vy += -30
    otherSprite.destroy(effects.fire, 1000)
    item_pickup = sprites.create(assets.image`myImage4`, SpriteKind.Food)
    item_pickup.setPosition(otherSprite.x, otherSprite.y)
    enemies_killed += 1
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (inventory[0] == 5) {
        vitality += 1
        inventory.removeAt(0)
    } else if (inventory[0] == 3) {
        wackman.startEffect(effects.fire, 1000)
        wackman.startEffect(effects.warmRadial, 2000)
        for (let index = 0; index < 10; index++) {
            fire = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . 4 4 . . . . . . . 
                . . . . . . 4 5 5 4 . . . . . . 
                . . . . . . 2 5 5 2 . . . . . . 
                . . . . . . . 2 2 . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, wackman, randint(-30, 30), randint(-30, 30))
            fire.setKind(SpriteKind.fire)
        }
        maxenem += randint(1, vitality)
        inventory.removeAt(0)
    } else if (inventory[0] == 4) {
        info.changeLifeBy(1)
        inventory.removeAt(0)
    } else if (inventory[0] == 0) {
        wackman.startEffect(effects.fountain, 1000)
        wackman.startEffect(effects.coolRadial, 2000)
        for (let index = 0; index < 10; index++) {
            ice = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . 6 6 6 5 5 6 6 6 . . . . 
                . . . 7 7 7 7 6 6 6 6 6 6 . . . 
                . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
                . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
                . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
                . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
                . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
                . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
                . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
                . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
                . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                . . . . 6 6 8 8 8 8 6 6 . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, wackman, randint(-10, 10), randint(-10, 10))
            ice.setKind(SpriteKind.ice)
        }
        inventory.removeAt(0)
    } else if (inventory[0] == 2) {
        maxenem += -3
        inventory.removeAt(0)
        wackman.startEffect(effects.blizzard, 500)
    } else if (inventory[0] == 1) {
        inventory.removeAt(0)
        luck += 1
    } else if (inventory[0] == 6) {
        inventory.removeAt(0)
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy, effects.ashes, 500)
        sprites.destroyAllSpritesOfKind(SpriteKind.shop, effects.ashes, 500)
    } else {
        inventory.removeAt(0)
    }
    DisplayInv()
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    wackman,
    player_animations[1],
    350,
    false
    )
})
function DisplayInv () {
    item1.setImage(item_sprite[inventory[0]])
    item2.setImage(item_sprite[inventory[1]])
    if (inventory.length == 0) {
        item1.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `)
        item2.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `)
    } else if (inventory.length == 1) {
        item2.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `)
    }
}
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    tiles.setTileAt(location, sprites.dungeon.floorLight0)
    inventory.push(randint(0, 5))
    DisplayInv()
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    wackman,
    player_animations[2],
    350,
    false
    )
})
sprites.onOverlap(SpriteKind.ice, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.setVelocity(0, 0)
    pause(1000)
    otherSprite.destroy(effects.fountain, 500)
    enemies_killed += 1
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    pause(1000)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    wackman,
    player_animations[0],
    350,
    false
    )
})
sprites.onOverlap(SpriteKind.fire, SpriteKind.shop, function (sprite, otherSprite) {
    otherSprite.setImage(assets.image`shopkeep_man_death`)
    game.showLongText("not a fan of dying to be honest", DialogLayout.Bottom)
    otherSprite.destroy(effects.fire, 1000)
    luck = 0
    maxenem = 50
    vitality = 0
    deathorb = sprites.create(assets.image`death_orb`, SpriteKind.youreawful)
    deathorb.setPosition(otherSprite.x, otherSprite.y)
})
scene.onOverlapTile(SpriteKind.Player, sprites.castle.tileDarkGrass2, function (sprite, location) {
    vitality += 1
    tiles.setTileAt(location, sprites.castle.tileDarkGrass3)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.youreawful, function (sprite, otherSprite) {
    inventory.push(6)
    otherSprite.destroy()
    DisplayInv()
})
info.onLifeZero(function () {
    let floor = 0
    item_bonus = inventory.length * 10
    game.splash("ITEM BONUS", item_bonus)
    for (let index = 0; index < item_bonus; index++) {
        info.changeScoreBy(1)
    }
    game.splash("FLOORS CLEARED", level)
    for (let index = 0; index < floor * 10; index++) {
        info.changeScoreBy(10)
    }
    game.splash("ENEMIES KILLED", enemies_killed)
    for (let index = 0; index < enemies_killed * 2; index++) {
        info.changeScoreBy(5)
    }
    game.splash("TRAPS HIT", traps_hit)
    for (let index = 0; index < enemies_killed * 1; index++) {
        info.changeScoreBy(-5)
    }
    game.splash("What a totally fair death!")
    game.over(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    inventory.push(4)
    otherSprite.destroy()
    DisplayInv()
})
function new_room (EnemiesNum: number) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.shop)
    tiles.setCurrentTilemap(areas._pickRandom())
    tiles.placeOnRandomTile(wackman, sprites.dungeon.collectibleInsignia)
    for (let index = 0; index < EnemiesNum; index++) {
        if (Math.percentChance(70)) {
            enemy1 = sprites.create(assets.image`blorb`, SpriteKind.Enemy)
            enemy1.setBounceOnWall(true)
            enemy1.vx = randint(-50, 50)
            enemy1.vy = randint(-50, 50)
        } else {
            enemy1 = sprites.create(assets.image`vexfly`, SpriteKind.Enemy)
            enemy1.follow(wackman)
            tiles.placeOnRandomTile(enemy1, assets.tile`enemy`)
        }
    }
    for (let value of tiles.getTilesByType(assets.tile`enemy`)) {
        tiles.setTileAt(value, sprites.dungeon.floorLight0)
    }
    for (let value of tiles.getTilesByType(sprites.dungeon.floorDarkDiamond)) {
        shawppa = sprites.create(assets.image`shopkeep_man`, SpriteKind.shop)
        tiles.placeOnTile(shawppa, value)
    }
}
sprites.onOverlap(SpriteKind.misc, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.vx += -100
    otherSprite.vy += -100
    if (Math.percentChance(25)) {
        sprite.destroy()
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairLarge, function (sprite, location) {
    level += 1
    new_room(randint(4, maxenem))
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.floorLight4, function (sprite, location) {
    if (Math.percentChance(30)) {
        inventory.shift()
    } else if (Math.percentChance(10)) {
        info.changeLifeBy(-1)
    } else {
        vitality += -0.5
    }
    tiles.setTileAt(location, sprites.dungeon.floorLight3)
    traps_hit += 1
    maxenem += 1
    DisplayInv()
})
let shawppa: Sprite = null
let enemy1: Sprite = null
let traps_hit = 0
let level = 0
let item_bonus = 0
let deathorb: Sprite = null
let enemies_killed = 0
let item_pickup: Sprite = null
let ice: Sprite = null
let fire: Sprite = null
let luck = 0
let temp = 0
let RandomGoodbyes: string[] = []
let RandomGreetings: string[] = []
let item_sprite: Image[] = []
let item2: Sprite = null
let item1: Sprite = null
let maxenem = 0
let vitality = 0
let wackman: Sprite = null
let inventory: number[] = []
let player_animations: Image[][] = []
let areas: tiles.TileMapData[] = []
areas = [
tilemap`room1`,
tilemap`level3`,
tilemap`die1`,
tilemap`level4`,
tilemap`level7`,
tilemap`level10`,
tilemap`level12`,
tilemap`ruins_garden1`
]
player_animations = [
assets.animation`wacky boy forward`,
assets.animation`wacky boy left`,
assets.animation`wacky boy right`,
assets.animation`wacky boy back`,
assets.animation`the wacky thing`,
assets.animation`wacky boy DEAD`
]
inventory = [3]
wackman = sprites.create(assets.image`wacky boy item`, SpriteKind.Player)
vitality = 1
controller.moveSprite(wackman, 50, 50)
scene.cameraFollowSprite(wackman)
info.setLife(3)
new_room(5)
maxenem = 6
let inv1 = sprites.create(assets.image`inv1`, SpriteKind.GUI)
let inv2 = sprites.create(assets.image`inv0`, SpriteKind.GUI)
inv1.setFlag(SpriteFlag.RelativeToCamera, true)
inv2.setFlag(SpriteFlag.RelativeToCamera, true)
inv1.setPosition(5, 15)
inv2.setPosition(16, 15)
item1 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.GUI)
item2 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.GUI)
item1.setPosition(7, 17)
item1.setFlag(SpriteFlag.RelativeToCamera, true)
item2.setPosition(18, 17)
item2.setFlag(SpriteFlag.RelativeToCamera, true)
item_sprite = [
assets.image`myImage3`,
assets.image`myImage2`,
assets.image`shield`,
assets.image`myImage0`,
assets.image`myImage4`,
assets.image`myImage1`,
assets.image`death_orb`
]
let item_ID = [
0,
1,
2,
3,
4,
5,
6
]
DisplayInv()
