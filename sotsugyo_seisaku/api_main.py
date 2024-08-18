import pygame
import time
from mcje.minecraft import Minecraft
import param_MCJE
import a
def main():
    a_x = 5
    a_y = 70
    a_z = 5
    pygame.init()       # Pygameを初期化
    screen = pygame.display.set_mode((800, 600))    # 画面作成
    #image = pygame.image.load("image/icon.png")     # 画像読み込み
    x, y = 0, 0         # XY座標
    running = True      # 実行継続フラグ

    while running:
        pygame.display.update()     # 画面を更新
        screen.fill(pygame.Color(10, 0, 0))  # 画面を塗りつぶす

        for event in pygame.event.get():    # イベント
            if event.type == pygame.QUIT: running = False   # 終了
            if event.type == pygame.KEYDOWN:
                a_x = a_x + 3    # キー押下
                if event.key == pygame.K_r: x = 0; y = 0    # Rでリセット

        keys = pygame.key.get_pressed() # キー保持
        if keys[pygame.K_a]:  a.setchar(0,param_MCJE.GLOWSTONE,a_x,a_y,a_z)   # A 
        if keys[pygame.K_b]: a.setchar(1,param_MCJE.GLOWSTONE,a_x,a_y,a_z)   # B
        if keys[pygame.K_c]:  a.setchar(2,param_MCJE.GLOWSTONE,a_x,a_y,a_z)   # C
        if keys[pygame.K_d]:  a.setchar(3,param_MCJE.GLOWSTONE,a_x,a_y,a_z)   # D
        if keys[pygame.K_e]:  a.setchar(4,param_MCJE.GLOWSTONE,a_x,a_y,a_z)  #E
        if keys[pygame.K_f]:  a.setchar(5,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_g]: a.setchar(6,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_h]: a.setchar(7,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_i]: a.setchar(8,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_j]: a.setchar(9,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_k]: a.setchar(10,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_l]: a.setchar(11,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_m]: a.setchar(12,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_n]: a.setchar(13,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_o]: a.setchar(14,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_p]: a.setchar(15,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_q]: a.setchar(16,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_r]: a.setchar(17,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_s]: a.setchar(18,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_t]: a.setchar(19,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_u]: a.setchar(20,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_v]: a.setchar(21,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_w]: a.setchar(22,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_x]: a.setchar(23,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_y]: a.setchar(24,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_z]: a.setchar(25,param_MCJE.GLOWSTONE,a_x,a_y,a_z)
        if keys[pygame.K_LALT]: a_y = a_y + 7
        if keys[pygame.K_RALT]: a_x = 5

        #screen.blit(image, (x, y))  # 描画
        pygame.display.flip()   # 画面フリップ
        time.sleep(0.3)    #一回のキー入力で複数回検知しないため
    pygame.quit()


#mc = Minecraft.create(port=param_MCJE.PORT_MC)
#mc.postToChat('hello, minecraft!!')







        
            
        


#↓ブロック設置方法
#mc.setBlock(0, 0, 15,  param_MCJE.GOLD_BLOCK)

main()

if __name__ == "__main__":
    main()