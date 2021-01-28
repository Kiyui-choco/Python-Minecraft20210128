from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()
from random import randrange


for i in range(10):
    x,y,z = BergOnlyLoveElla.player.getTilePos()
    z = z+i
    for j in range(10):
        color = randrange(0,16)
        x = x+1
        BergOnlyLoveElla.setBlock(x,y,z,35,color)
        
        
ans = randrange(0,16)
while True:
    hits = BergOnlyLoveElla.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        block = BergOnlyLoveElla.getBlockWithData(h.pos)
        data = block.data
        
        if data == ans:
            BergOnlyLoveElla.postToChat('恭喜你找到了！')
            BergOnlyLoveElla.setBlock(h.pos,57)
            break
        
        elif data < ans:
            BergOnlyLoveElla.postToChat('找錯囉~再找大一點的吧~')
        
        elif data > ans:
            BergOnlyLoveElla.postToChat('找錯囉~再找小一點的吧~')