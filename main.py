@namespace
class SpriteKind:
    GUI = SpriteKind.create()
    fire = SpriteKind.create()
    ice = SpriteKind.create()
    misc = SpriteKind.create()
    shop = SpriteKind.create()
    youreawful = SpriteKind.create()
    bomb = SpriteKind.create()
    boss = SpriteKind.create()
    evil = SpriteKind.create()

def on_up_pressed():
    animation.run_image_animation(wackman, player_animations[3], 350, False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

# shop

def on_on_overlap(sprite, otherSprite):
    global RandomGreetings, RandomGoodbyes, temp, luck
    RandomGreetings = ["hey yeah yeah welcome to shawppa shawp",
        "yeah give me heart",
        "yyeaahhh",
        "today i have for you a selection of SEVERAL"]
    RandomGoodbyes = ["give haerts for the best EVER",
        "always welcome back",
        "give more hearts for good luck everytime",
        "thankyou thanks",
        "It is never enough.",
        "DOWNLOAD"]
    game.show_long_text(RandomGreetings._pick_random(), DialogLayout.BOTTOM)
    # player input
    if game.ask("Give Shawppa 1 heart?"):
        # result
        if Math.percent_chance(luck * 5):
            temp = randint(6, 8)
        else:
            temp = randint(0, 5)
        music.ba_ding.play()
        info.change_life_by(-1)
        for index in range(4):
            inventory.unshift(temp)
    else:
        game.show_long_text("please my rent is due tomorrow", DialogLayout.BOTTOM)
    luck += 1
    game.show_long_text(RandomGoodbyes._pick_random(), DialogLayout.BOTTOM)
    DisplayInv()
    otherSprite.destroy(effects.smiles, 1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.shop, on_on_overlap)

def on_b_pressed():
    global vitality, fire2, maxenem, ice2, luck, landmine
    # super long item use script
    if inventory[1] == 5:
        vitality += 1
        music.beam_up.play()
        inventory.remove_at(1)
    elif inventory[1] == 3:
        wackman.start_effect(effects.fire, 1000)
        wackman.start_effect(effects.warm_radial, 2000)
        for index2 in range(10):
            fire2 = sprites.create_projectile_from_sprite(img("""
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
                """),
                wackman,
                randint(-30, 30),
                randint(-30, 30))
            fire2.set_kind(SpriteKind.fire)
        maxenem += 1
        inventory.remove_at(1)
    elif inventory[1] == 4:
        info.change_life_by(randint(1, vitality))
        inventory.remove_at(1)
        music.jump_up.play()
    elif inventory[1] == 0:
        wackman.start_effect(effects.fountain, 1000)
        wackman.start_effect(effects.cool_radial, 2000)
        for index3 in range(10):
            ice2 = sprites.create_projectile_from_sprite(img("""
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
                """),
                wackman,
                randint(-10, 10),
                randint(-10, 10))
            ice2.set_kind(SpriteKind.ice)
        inventory.remove_at(1)
    elif inventory[1] == 2:
        maxenem += -3
        inventory.remove_at(1)
        wackman.start_effect(effects.blizzard, 500)
    elif inventory[1] == 1:
        inventory.remove_at(1)
        luck += 1
    elif inventory[1] == 6:
        inventory.remove_at(1)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy, effects.ashes, 500)
        sprites.destroy_all_sprites_of_kind(SpriteKind.shop, effects.ashes, 500)
        music.spooky.play()
    elif inventory[1] == 7:
        for index4 in range(20):
            fire2 = sprites.create_projectile_from_sprite(assets.image("""
                    blueflames
                """),
                wackman,
                randint(-50, 50),
                randint(-50, 50))
            fire2.set_kind(SpriteKind.fire)
        inventory.remove_at(1)
    elif inventory[1] == 8:
        inventory.remove_at(1)
        landmine = sprites.create(assets.image("""
            napalm_bomb
        """), SpriteKind.bomb)
        landmine.set_position(wackman.x, wackman.y)
    else:
        inventory.remove_at(1)
    DisplayInv()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    global item_pickup, enemies_killed
    otherSprite2.vx += -30
    otherSprite2.vy += -30
    otherSprite2.destroy(effects.fire, 1000)
    item_pickup = sprites.create(assets.image("""
        myImage4
    """), SpriteKind.food)
    item_pickup.set_position(otherSprite2.x, otherSprite2.y)
    enemies_killed += 1
sprites.on_overlap(SpriteKind.fire, SpriteKind.enemy, on_on_overlap2)

def on_a_pressed():
    global vitality, fire2, maxenem, ice2, luck, landmine
    if inventory[0] == 5:
        vitality += 1
        music.beam_up.play()
        inventory.remove_at(0)
    elif inventory[0] == 3:
        wackman.start_effect(effects.fire, 1000)
        wackman.start_effect(effects.warm_radial, 2000)
        for index5 in range(10):
            fire2 = sprites.create_projectile_from_sprite(img("""
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
                """),
                wackman,
                randint(-30, 30),
                randint(-30, 30))
            fire2.set_kind(SpriteKind.fire)
        maxenem += 1
        inventory.remove_at(0)
    elif inventory[0] == 4:
        info.change_life_by(randint(1, vitality))
        inventory.remove_at(0)
        music.jump_up.play()
    elif inventory[0] == 0:
        wackman.start_effect(effects.fountain, 1000)
        wackman.start_effect(effects.cool_radial, 2000)
        for index6 in range(10):
            ice2 = sprites.create_projectile_from_sprite(img("""
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
                """),
                wackman,
                randint(-10, 10),
                randint(-10, 10))
            ice2.set_kind(SpriteKind.ice)
        inventory.remove_at(0)
    elif inventory[0] == 2:
        maxenem += -3
        inventory.remove_at(0)
        wackman.start_effect(effects.blizzard, 500)
    elif inventory[0] == 1:
        inventory.remove_at(0)
        luck += 1
    elif inventory[0] == 6:
        inventory.remove_at(0)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy, effects.ashes, 500)
        sprites.destroy_all_sprites_of_kind(SpriteKind.shop, effects.ashes, 500)
        music.spooky.play()
    elif inventory[0] == 7:
        for index7 in range(20):
            fire2 = sprites.create_projectile_from_sprite(assets.image("""
                    blueflames
                """),
                wackman,
                randint(-50, 50),
                randint(-50, 50))
            fire2.set_kind(SpriteKind.fire)
        inventory.remove_at(0)
    elif inventory[0] == 8:
        inventory.remove_at(0)
        landmine = sprites.create(assets.image("""
            napalm_bomb
        """), SpriteKind.bomb)
        landmine.set_position(wackman.x, wackman.y)
    else:
        inventory.remove_at(0)
    DisplayInv()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap3(sprite3, otherSprite3):
    global fire2
    for index8 in range(10):
        fire2 = sprites.create_projectile_from_sprite(img("""
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
            """),
            otherSprite3,
            randint(-35, 35),
            randint(-35, 35))
        fire2.set_kind(SpriteKind.fire)
    otherSprite3.destroy()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.bomb, on_on_overlap3)

def on_left_pressed():
    animation.run_image_animation(wackman, player_animations[1], 350, False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def DisplayInv():
    item1.set_image(item_sprite[inventory[0]])
    item2.set_image(item_sprite[inventory[1]])
    if len(inventory) == 0:
        item1.set_image(img("""
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
        """))
        item2.set_image(img("""
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
        """))
    elif len(inventory) == 1:
        item2.set_image(img("""
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
        """))

def on_overlap_tile(sprite4, location):
    tiles.set_tile_at(location, sprites.dungeon.floor_light0)
    inventory.append(randint(0, 5))
    DisplayInv()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def on_right_pressed():
    animation.run_image_animation(wackman, player_animations[2], 350, False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap4(sprite5, otherSprite4):
    global enemies_killed
    otherSprite4.set_velocity(0, 0)
    pause(1000)
    otherSprite4.destroy(effects.fountain, 500)
    enemies_killed += 1
sprites.on_overlap(SpriteKind.ice, SpriteKind.enemy, on_on_overlap4)

def on_on_overlap5(sprite6, otherSprite5):
    music.knock.play()
    info.change_life_by(-1)
    pause(1000)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap5)

def new_room(EnemiesNum: number, BossRoom: bool):
    global BossHP, Boss, enemy1, shawppa
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.shop)
    if BossRoom:
        for index9 in range(4):
            music.play_melody("C F G A C5 B A E ", 800)
        for index10 in range(4):
            music.play_melody("C E G A C5 A E C ", 800)
        if FOXBANE_route:
            tiles.set_current_tilemap(tilemap("""
                room_of_the_damned1
            """))
            BossHP = 60
            Boss = sprites.create(assets.image("""
                god_of_torment
            """), SpriteKind.evil)
        elif Math.percent_chance(60):
            tiles.set_current_tilemap(tilemap("""
                monarch_hall1
            """))
            BossHP = 20
            Boss = sprites.create(assets.image("""
                slime_king
            """), SpriteKind.boss)
            Boss.follow(wackman, 10)
        else:
            tiles.set_current_tilemap(tilemap("""
                monarch_hall1
            """))
            Boss = sprites.create(assets.image("""
                wasp_queen
            """), SpriteKind.boss)
            BossHP = 30
    else:
        tiles.set_current_tilemap(areas._pick_random())
        tiles.place_on_random_tile(wackman, sprites.dungeon.collectible_insignia)
        for index11 in range(EnemiesNum):
            if Math.percent_chance(70):
                enemy1 = sprites.create(assets.image("""
                    blorb
                """), SpriteKind.enemy)
                enemy1.set_bounce_on_wall(True)
                enemy1.vx = randint(-50, 50)
                enemy1.vy = randint(-50, 50)
            else:
                enemy1 = sprites.create(assets.image("""
                    vexfly
                """), SpriteKind.enemy)
                enemy1.follow(wackman)
            tiles.place_on_random_tile(enemy1, assets.tile("""
                enemy
            """))
        for value in tiles.get_tiles_by_type(assets.tile("""
            enemy
        """)):
            tiles.set_tile_at(value, sprites.dungeon.floor_light0)
        for value2 in tiles.get_tiles_by_type(sprites.dungeon.floor_dark_diamond):
            shawppa = sprites.create(assets.image("""
                shopkeep_man
            """), SpriteKind.shop)
            tiles.place_on_tile(shawppa, value2)

def on_down_pressed():
    animation.run_image_animation(wackman, player_animations[0], 350, False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap6(sprite7, otherSprite6):
    global luck, maxenem, vitality, deathorb, FOXBANE_route
    # killed shops. you monster
    otherSprite6.set_image(assets.image("""
        shopkeep_man_death
    """))
    music.sonar.play()
    game.show_long_text("not a fan of dying to be honest", DialogLayout.BOTTOM)
    otherSprite6.destroy(effects.fire, 1000)
    luck = 0
    maxenem = 50
    vitality = 0
    deathorb = sprites.create(assets.image("""
        death_orb
    """), SpriteKind.youreawful)
    deathorb.set_position(otherSprite6.x, otherSprite6.y)
    FOXBANE_route = True
sprites.on_overlap(SpriteKind.fire, SpriteKind.shop, on_on_overlap6)

def on_overlap_tile2(sprite8, location2):
    global luck
    luck += 1
    tiles.set_tile_at(location2, sprites.castle.tile_dark_grass3)
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.tile_dark_grass2,
    on_overlap_tile2)

def on_on_overlap7(sprite9, otherSprite7):
    inventory.append(6)
    otherSprite7.destroy()
    DisplayInv()
sprites.on_overlap(SpriteKind.player, SpriteKind.youreawful, on_on_overlap7)

def on_life_zero():
    global item_bonus
    floor = 0
    item_bonus = len(inventory) * 10
    game.splash("ITEM BONUS", item_bonus)
    for index12 in range(item_bonus):
        info.change_score_by(1)
    game.splash("FLOORS CLEARED", level)
    for index13 in range(floor * 10):
        info.change_score_by(10)
    game.splash("ENEMIES KILLED", enemies_killed)
    for index14 in range(enemies_killed * 2):
        info.change_score_by(5)
    game.splash("TRAPS HIT", traps_hit)
    for index15 in range(enemies_killed * 1):
        info.change_score_by(-5)
    game.splash("What a totally fair death!")
    game.over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap8(sprite10, otherSprite8):
    inventory.append(4)
    otherSprite8.destroy()
    DisplayInv()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap8)

def on_on_overlap9(sprite11, otherSprite9):
    otherSprite9.vx += -100
    otherSprite9.vy += -100
    if Math.percent_chance(25):
        sprite11.destroy()
sprites.on_overlap(SpriteKind.misc, SpriteKind.enemy, on_on_overlap9)

def on_overlap_tile3(sprite12, location3):
    global level
    level += 1
    if level > 9:
        new_room(maxenem, True)
    else:
        new_room(randint(4, maxenem), False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_large,
    on_overlap_tile3)

# /this is a comment

def on_overlap_tile4(sprite13, location4):
    global vitality, traps_hit, maxenem
    if Math.percent_chance(30):
        music.footstep.play()
        inventory.shift()
    elif Math.percent_chance(10):
        music.knock.play()
        info.change_life_by(-1)
    else:
        music.footstep.play()
        vitality += -0.5
    tiles.set_tile_at(location4, sprites.dungeon.floor_light3)
    traps_hit += 1
    maxenem += 1
    DisplayInv()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.floor_light4,
    on_overlap_tile4)

traps_hit = 0
level = 0
item_bonus = 0
deathorb: Sprite = None
shawppa: Sprite = None
enemy1: Sprite = None
Boss: Sprite = None
BossHP = 0
FOXBANE_route = False
enemies_killed = 0
item_pickup: Sprite = None
landmine: Sprite = None
ice2: Sprite = None
fire2: Sprite = None
temp = 0
luck = 0
RandomGoodbyes: List[str] = []
RandomGreetings: List[str] = []
item_sprite: List[Image] = []
item2: Sprite = None
item1: Sprite = None
maxenem = 0
vitality = 0
wackman: Sprite = None
inventory: List[number] = []
player_animations: List[List[Image]] = []
areas: List[tiles.TileMapData] = []
# unfair room. you spawn here you die
areas = [tilemap("""
        room1
    """),
    tilemap("""
        level3
    """),
    tilemap("""
        level16
    """),
    tilemap("""
        level4
    """),
    tilemap("""
        level7
    """),
    tilemap("""
        level10
    """),
    tilemap("""
        level12
    """),
    tilemap("""
        ruins_garden1
    """),
    tilemap("""
        garden_1
    """),
    tilemap("""
        die1
    """)]
# animations list
player_animations = [assets.animation("""
        wacky boy forward
    """),
    assets.animation("""
        wacky boy left
    """),
    assets.animation("""
        wacky boy right
    """),
    assets.animation("""
        wacky boy back
    """),
    assets.animation("""
        the wacky thing
    """),
    assets.animation("""
        wacky boy DEAD
    """)]
inventory = [3]
wackman = sprites.create(assets.image("""
    wacky boy item
"""), SpriteKind.player)
vitality = 1
controller.move_sprite(wackman, 50, 50)
scene.camera_follow_sprite(wackman)
info.set_life(3)
new_room(5, False)
maxenem = 6
inv1 = sprites.create(assets.image("""
    inv1
"""), SpriteKind.GUI)
inv2 = sprites.create(assets.image("""
    inv0
"""), SpriteKind.GUI)
inv1.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
inv2.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
inv1.set_position(5, 15)
inv2.set_position(16, 15)
item1 = sprites.create(img("""
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
    """),
    SpriteKind.GUI)
item2 = sprites.create(img("""
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
    """),
    SpriteKind.GUI)
item1.set_position(7, 17)
item1.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
item2.set_position(18, 17)
item2.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
item_sprite = [assets.image("""
        myImage3
    """),
    assets.image("""
        myImage2
    """),
    assets.image("""
        shield
    """),
    assets.image("""
        myImage0
    """),
    assets.image("""
        myImage4
    """),
    assets.image("""
        myImage1
    """),
    assets.image("""
        death_orb
    """),
    assets.image("""
        blueflames
    """),
    assets.image("""
        napalm_bomb
    """)]
item_ID = [0, 1, 2, 3, 4, 5, 6, 7, 8]
DisplayInv()