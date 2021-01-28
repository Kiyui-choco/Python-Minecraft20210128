from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()
import random 

x,y,z = BergOnlyLoveElla.player.getTilePos()

for i in range(100):
    r = random.randrange(1,5)
    if r == 1:
        BergOnlyLoveElla.setBlocks(x,y,z,x,y,z+4,166)
        z = z+4
    if r == 2:
        BergOnlyLoveElla.setBlocks(x,y,z,x,y,z-4,166)
        z = z-4
    if r == 3:
        BergOnlyLoveElla.setBlocks(x,y,z,x+4,y,z,166)
        x = x+4
    if r == 4:
        BergOnlyLoveElla.setBlocks(x,y,z,x-4,y,z,166)
        x = x-4
    
    
    