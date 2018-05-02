# -*- coding: utf-8 -*-

import pygame, sys, traceback
import pandas as pd
import numpy as np
from pygame.color import THECOLORS
import matplotlib.pyplot as plt
from matplotlib import cm



def get_lifegame(data):
    (height , width) = data.shape
    res = data.copy()
    for i in range(height-2):
        for j in range(width-2):
            sum_ij = data[i,j]+data[i, j+1]+data[i,j+2]+\
                     data[i+1,j]+data[i+1,j+2]+\
                     data[i+2,j]+data[i+2, j+1]+data[i+2,j+2]
                     
            #sum_ij = 2
            if data[i+1,j+1]==0:
                if sum_ij == 2 or sum_ij == 3:
                    res[i+1,j+1]=1
                else:
                    res[i+1,j+1]=0
            else:
                if sum_ij == 3:
                    res[i+1,j+1]=1
                else:
                    res[i+1,j+1]=0
    #render text
    info_text = my_font.render("LifeNum:%3d"%res.sum(), True, (0,200,0))
    screen.blit(info_text, (550,50))
    return res

def get_forest_fire(data, p_grow=0.1, p_fire = 0.1):
    (height , width) = data.shape
    res = data.copy()
    blank=0
    fire=0
    tree=0
    for i in range(1,height-1):
        for j in range(1,width-1):
            if data[i, j]==9:
                res[i,j]=0
                blank+=1
            elif data[i,j]==1:
                sum_ij = data[i-1,j-1]+data[i-1, j]+data[i,j+1]+\
                     data[i,j-1]+data[i,j+1]+\
                     data[i+1,j-1]+data[i+1, j+1]+data[i+1,j]
                if sum_ij>8:
                    res[i,j]=9
                    fire+=1
                elif np.random.rand()<p_fire:
                    res[i,j]=9
                    fire+=1
                else:
                    res[i,j]=1
                    tree+=1
            elif np.random.rand()<p_grow:
                res[i,j]=1
                tree+=1
            else:
                res[i,j]=0
                blank+=1
    #render text
    info_text = my_font.render("TreeNum:%3d"%\
                               (tree), True, (0,200,0))
    screen.blit(info_text, (550,50))
    info_text = my_font.render("Fire:%3d"%\
                               (fire), True, (0,200,0))
    screen.blit(info_text, (550,70))
    info_text = my_font.render("Blank:%3d"%\
                               (blank), True, (0,200,0))
    screen.blit(info_text, (550,90))
    lifes.append(tree)
    blanks.append(blank)
    fires.append(fire)
    return res, tree, blank, fire

#init pygame
pygame.init()
bg_size = bg_width, bg_height = 650, 550
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('CellAuto')
my_font = pygame.font.SysFont("timesnewroman", 16)
lifes = []
fires = []
blanks = []
values = 1000
datas_tree = pd.DataFrame(np.zeros((values, 9)))
datas_fire = datas_tree.copy()
datas_blank = datas_tree.copy()
df_columns = pd.Series(['0.0001', '0.001', '0.01', '0.1', '0.2', '0.3', '0.5', '0.75', '1'])
datas_blank.columns = df_columns
datas_fire.columns = df_columns
datas_tree.columns = df_columns


def draw_cells(cells, cell_size=5):
    
    surf = pygame.Surface((cells.shape[1]*cell_size, cells.shape[0]*cell_size))
    x_offset, y_offset = 20, 20
    for i in range(1,cells.shape[0]-1):
            for j in range(1,cells.shape[1]-1):
                if cells[i,j]==1:
                    pygame.draw.rect(surf,[0,200,0],\
                                     [cell_size*i,cell_size*j\
                                      ,cell_size,cell_size],1)
                    #pygame.display.update()
                elif cells[i,j]==9:
                    pygame.draw.rect(surf,[200,0,0],\
                                     [cell_size*i,cell_size*j\
                                      ,cell_size,cell_size],1)
    screen.blit(surf, (x_offset, y_offset))           
                
                
def main():

    background = 0,0,0
    clock = pygame.time.Clock()
    
    #generate a ball
    count=0
    size=100
    probs=[0.0001, 0.001, 0.01, 0.1, 0.2, 0.3, 0.5, 0.75, 1]
    color = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    
    
    index=0
    cells = np.random.randint(0, high=4, size=(size+2, size+2))
    cells=cells//3
    cells[[0,size+1],:]=0
    cells[:,[0,size+1]]=0
    runing = True
    while runing:
        
            
        if index==10: break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plt.plot(lifes)
                plt.plot(blanks)
                plt.plot(fires)
                plt.show()
                pygame.quit()
                sys.exit()
        
        screen.fill(background)
        
        #单次测量
        cells,t,b,f = get_forest_fire(cells,0.1,0.01)
# =============================================================================
#         ##自动测量各种不同概率
#         cells,t,b,f = get_forest_fire(cells,probs[index],probs[index])
#         datas_blank.loc[count,df_columns[index]]=b
#         datas_fire.loc[count,df_columns[index]]=f
#         datas_tree.loc[count,df_columns[index]]=t
#         count+=1
#         if count % values == 0:
#             cells = np.random.randint(0, high=2, size=(size+2, size+2))
#             index+=1
#             count=0
#             plt.plot(lifes,color=cm.Greens(color[index]))
#             plt.plot(blanks,color=cm.Greys(color[index]))
#             plt.plot(fires,color=cm.Reds(color[index]))
# =============================================================================
        draw_cells(cells)
        pygame.display.update()
        clock.tick(60)
    datas_blank.to_csv('blank.txt')
    datas_fire.to_csv('fire.txt')
    datas_tree.to_csv('fire.txt')
    plt.show()
    
    
if __name__=='__main__':
    try:
# =============================================================================
#         size=100
#         cells = np.random.randint(0, high=2, size=(size, size))
#         while(True):
#             cells=get_lifegame(cells)
#             print(cells.sum())
# =============================================================================
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()

