from mcje.minecraft import Minecraft
import param_MCJE
import time

def setchar(char,color,x,y,z):
    mc = Minecraft.create(port=param_MCJE.PORT_MC)
    mc.postToChat('hello, minecraft!!')
    #charは数字（Aは0，Bは1、、、、って感じ）,colorはブロックの種類(param_MCJEを参照しろ),x,y,zは普通に数字
    #print('Set' + ' ' + char + '.')
    f = open('C:/Users/uchiy/Documents/ibuv/ibuki/pygame_samples/sotsugyo_seisaku/f.txt', 'r')
    datalist = f.readlines()
    #print(datalist)
    new_datalist = str(datalist[0])
    #print(new_datalist)
    f.close()
    new_x = x
    new_y = y
    new_z = z
    for i  in range(35):
        print(new_datalist[i+char*35])
        if int(new_datalist[i+char*35]) == 1:
            mc.setBlock(new_x, new_y, new_z,  param_MCJE.GLOWSTONE)
            print('moo')
            mc.postToChat('I setted gold block!!')
            #mc.setBlock(5, 75, 5,  param_MCJE.GRASS_BLOCK)
            
            
            time.sleep(0.1)

        new_x = new_x + 1

        if new_x > x + 4:
            new_x= x
            new_y = new_y - 1