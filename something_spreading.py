import numpy as np
from  time import sleep
import os 
from copy import deepcopy
import random


# config
WIDTH = 50
SLEEP_SECONDS = 0.5
SEED = 1
RESIST = 1


class life:
    x, y = 0, 0
    def __init__(self):
        print("--------------------------------")
        # 「自分」の行列を0埋めで初期化
        self.old_many_me = np.zeros((WIDTH,WIDTH))
        self.new_many_me = np.zeros((WIDTH,WIDTH))
        self.have_heard = np.zeros((WIDTH,WIDTH))
        # 「親密度」の行列を初期化（親密度は自分から一方的なものとする）
        self.friendly = np.random.rand(WIDTH, WIDTH, 8) # 一様分布
        
        # スタートするセルをランダムに決定
        for _ in range(SEED):
            x, y = np.random.randint(1, WIDTH, (1, 2))[0]
            print(x, y)
            self.old_many_me[x][y] = RESIST


    def start(self):
        # 状態を更新していく
        a=0
        while a==0:
            for i in range(len(self.old_many_me)):
                for j in range(len(self.old_many_me[i])):
                    if self.old_many_me[i][j] >= 1:
                        self.have_heard[i][j] = 1
                        self.update_me(i, j)
                        self.new_many_me[i][j] -= 1
                        
                    # os.system("clear") # windowsの場合はcls？
            sleep(SLEEP_SECONDS)
            self.show(self.new_many_me)
            self.old_many_me = deepcopy(self.new_many_me)


    def update_me(self, x, y):
        criteria = np.random.rand() # 0-1の乱数
        cnt = 0
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if i==0 and j==0:
                    continue
                # 噂を知らない場合のみ噂を新しく知るようにする
                if (
                    self.friendly[i][j][cnt] >= criteria 
                    and self.old_many_me[i][j] == 0
                    and self.have_heard[i][j] == 0
                ):
                    X = x+i if x+i < WIDTH else x+i - WIDTH
                    X = X if X >= 0 else X + WIDTH
                    Y = y+j if y+j < WIDTH else y+j - WIDTH
                    Y = Y if Y < WIDTH else Y - WIDTH
                    self.new_many_me[X][Y] = RESIST
                    cnt += 1


    def show(self, many_me):
        _show = "--------------------------------\n"
        for li in many_me:
            for l in li:
                if l > 0:
                    _show += "@"
                else:
                    _show += "　"
            _show += "\n"
        # \033[nAはカーソルの移動を表す．WIDTH行上にカーソルを移動して，
        # 同じところを上書きするようにしてる
        _show += f"\033[{WIDTH+2}A"
        print(_show)
    # 噂が伝わる様子を表示
    
        
if __name__ == '__main__':
    l = life()
    l.start()

