#3-8

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18) #leaves
    mc.setBlocks(x,y,z,x,y+4,z,17) #trunk

#install
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#getPos
x,y,z = mc.player.getTilePos()

for i in range(0,100,5):
    for j in range(8):
        for k in range(10):
            plantTree(x+i,y+j*8,z+k*5)