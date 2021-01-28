from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()

list2 = [[166,133,57],[116,120,238]]

myID = BergOnlyLoveElla.getPlayerEntityId('BergOnlyLoveBlla')
x,y,z = BergOnlyLoveElla.entity.getTilePos(myID)

startX = x 

for i in list2:
    for j in i:
        
        BergOnlyLoveElla.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1