from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()
import random 

x,y,z = BergOnlyLoveElla.player.getTilePos()

for i in range(100):
    r = random.randrange(1,7)
    if r == 1:
        BergOnlyLoveElla.setBlocks(x,y,z,x,y,z+4,57)
        z = z+4
    if r == 2:
        BergOnlyLoveElla.setBlocks(x,y,z,x,y,z-4,57)
        z = z-4
    if r == 3:
        BergOnlyLoveElla.setBlocks(x,y,z,x+4,y,z,57)
        x = x+4
    if r == 4:
        BergOnlyLoveElla.setBlocks(x,y,z,x-4,y,z,57)
        x = x-4
    if r == 5:
        BergOnlyLoveElla.setBlocks(x,y,z,x,y+4,z,57)
        y = y+4
    if r == 6:
        BergOnlyLoveElla.setBlocks(x,y,z,x,y-4,z,57)
        y = y-4
    
    
    