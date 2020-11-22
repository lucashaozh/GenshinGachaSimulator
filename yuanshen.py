import matplotlib.pyplot as plt
import numpy as np
import random


def simulationOfgenshin():
    """ 
    模拟原神连续抽100次UP池
    以下为游戏中的概率描述：
    五星祈愿的基础概率为0.600%，综合概率(含保底)为1.600%，最多九十次必定通过保底获得五星角色
    如本次起源获取的五星角色非本期UP角色，下次祈愿获取的五星角色必定是本期UP角色
    四星物品祈愿的基础概率为5.100%，四星角色祈愿的基础概率为2.550%，四星武器祈愿的基础概率为2.550%
    四星去拼祈愿综合概率(含保底)为13.000%，最多十次祈愿必定能通过保底获得四星或以上物品
    如本次起源获取的四星角色非本期UP角色，下次祈愿获取的四星角色必定是本期UP角色
    抽到五星概率为0.6%
    抽到四星概率为5.1%
    UP五星的概率为五星的50%
    UP四星的概率为四星的50%
    """
    fiveStar = 0.006                    # 设定概率
    fourStar = 0.051
    numOfDraw = 100                     # 总的抽卡次数
    numOffiveStar = 0                   # 记录抽到的各种卡的次数
    numOfupFiveStar = 0
    numOffourStar = 0
    numOfupFourStar = 0
    guaranTimesOfFiveStar = 0           # 抽到五星之前的次数
    guaranTimesOfFourStar = 0           # 抽到四星之前的次数
    hasupFiveStar = False               # 是否已经抽到了五星


    for i in range(numOfDraw):
        if guaranTimesOfFiveStar == 90: 
            numOffiveStar += 1
            guaranTimesOfFiveStar = 0
            guaranTimesOfFourStar = 0
            if not hasupFiveStar:                               # 前一发保底歪了
                numOfupFiveStar += 1
                hasupFiveStar = True
                print("180发大保底...")
            elif hasupFiveStar and random.randInt(0, 1) == 0:   # 90保底但是没有歪
                numOfupFiveStar += 1
                hasupFiveStar = True
                print("90发保底...")
            else:                                               # 90保底但是歪了...
                print("90发保底歪了...")
                hasupFiveStar = False
        elif guaranTimesOfFourStar == 10:                           
            """ 
            这里的设定是十连保底时
            抽到五星的概率和抽到四星的概率一起算保底
            也就是十发保底时抽到五星的概率是
            fiveStar/(fiveStar+fourStar)
            """
            if random.uniform(0, fiveStar+fourStar) <= fiveStar:
                numOffiveStar += 1
                if guaranTimesOfFiveStar <= 50:
                    print("吸吸吸吸吸吸！第%d次抽中"%guaranTimesOfFiveStar)
                else:
                    print("第%d次抽中"%guaranTimesOfFiveStar)
                if not hasupFiveStar or random.randint(0, 1) == 0:
                    numOfupFiveStar += 1
                else:
                    print('歪了...')
                    hasupFiveStar = False
                guaranTimesOfFiveStar = 0
                guaranTimesOfFourStar = 0
            else:
                print("十连保底...")
                numOffourStar += 1
                guaranTimesOfFiveStar += 1
                guaranTimesOfFourStar = 0
                if random.randint(0, 1) == 0:
                    numOfupFourStar += 1
        else:                                           # no guarantee
            generateNum = random.random()
            if generateNum <= fiveStar:                 # draw a fiveStar
                numOffiveStar += 1
                if guaranTimesOfFiveStar <= 50:
                    print("吸吸吸吸吸吸！！！第%d次抽中"%guaranTimesOfFiveStar)
                else:
                    print("第%d次抽中"%guaranTimesOfFiveStar)
                
                if not hasupFiveStar or random.randint(0, 1) == 0:
                    numOfupFiveStar += 1
                    hasupFiveStar = True
                else:
                    print("歪了。。。")
                    hasupFiveStar = False
                guaranTimesOfFiveStar = 0
                guaranTimesOfFourStar = 0
            elif fiveStar < generateNum <= (fiveStar + fourStar):
                numOffourStar += 1
                guaranTimesOfFiveStar += 1
                guaranTimesOfFourStar = 0
                if random.randint(0, 1) == 0:
                    numOfupFourStar += 1
            else:
                guaranTimesOfFiveStar += 1
                guaranTimesOfFourStar += 1
    
    print("Number of five star character:%d"%numOffiveStar)
    print("Number of UP five star character:%d"%numOfupFiveStar)
    print("Number of four star character:%d"%numOffourStar)
    print("Number of UP four star character:%d"%numOfupFourStar)
        


def main():
    simulationOfgenshin()

if __name__ == '__main__':
    main()    

