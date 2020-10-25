import matplotlib.pyplot as plt
import numpy as np
import random

# simulate the process of drawing the card
def simulationOfgenshin():
    fiveStar = 0.006
    fourStar = 0.051
    # upFiveStar = fiveStar / 2
    # upFourStar = fourStar / 2
    numOfDraw = 100
    numOffiveStar = 0
    numOfupFiveStar = 0
    numOffourStar = 0
    numOfupFourStar = 0
    guaranTimesOfFiveStar = 0
    guaranTimesOfFourStar = 0
    hasupFiveStar = False


    for i in range(numOfDraw):
        
        if guaranTimesOfFiveStar == 90: 
            print("保底了...")
            numOffiveStar += 1
            guaranTimesOfFiveStar = 0
            guaranTimesOfFourStar = 0
            if not hasupFiveStar or random.randint(0, 1) == 0:
                numOfupFiveStar += 1
                hasupFiveStar = True
            else:
                print("保底歪了...")
                hasupFiveStar = False
        elif guaranTimesOfFourStar == 10:                           # guarantee for at least fourStar
            if random.uniform(0, fiveStar+fourStar) <= fiveStar:    # draw a fiveStar under the 10th guarantee
                numOffiveStar += 1
                if guaranTimesOfFiveStar <= 50:
                    print("吸吸吸吸吸吸！第%d次抽中"%guaranTimesOfFiveStar)
                guaranTimesOfFiveStar = 0
                guaranTimesOfFourStar = 0
                if not hasupFiveStar or random.randint(0, 1) == 0:
                    numOfupFiveStar += 1
                else:
                    print('歪了...')
                    hasupFiveStar = False
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
                guaranTimesOfFiveStar = 0
                guaranTimesOfFourStar = 0
                if not hasupFiveStar or random.randint(0, 1) == 0:
                    numOfupFiveStar += 1
                    hasupFiveStar = True
                else:
                    print("歪了。。。")
                    hasupFiveStar = False
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

