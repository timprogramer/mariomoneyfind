import math
import random

import wrap
wrap.world.create_world(900,600,200,200)
wrap.world.set_back_color(187, 255, 182)

#созданике марио
wrap.sprite.add("mario-1-big",60,60,"duck")
wrap.sprite.set_size(0,56,56)

#создание точки
randomx=random.randint(350,800)
randomy=random.randint(250,550)
wrap.sprite.add("mario-items",randomx,randomy,"star")

#движение 1
pyt=math.sqrt((randomx-60)**2+(randomy-60)**2)
pyt1shag=pyt/3
wrap.actions.move_at_angle_point(0,randomx,randomy,pyt1shag)
marioposx=wrap.sprite.get_centerx(0)
marioposy=wrap.sprite.get_centery(0)
wrap.sprite.add("mario-items",marioposx,marioposy+70,"coin")

#движение 2
wrap.actions.move_at_angle_point(0,randomx,randomy,pyt1shag)
marioposx=wrap.sprite.get_centerx(0)
marioposy=wrap.sprite.get_centery(0)
wrap.sprite.add("mario-items",marioposx,marioposy+70,"coin")

#движение 3
wrap.actions.move_at_angle_point(0,randomx,randomy,pyt1shag)
marioposx=wrap.sprite.get_centerx(0)
marioposy=wrap.sprite.get_centery(0)
wrap.sprite.add("mario-items",marioposx,marioposy+70,"coin")
wrap.sprite.remove(1)