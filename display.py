
# This is a prototype of Heidi's honor's study
# spring 2019
# generating the great wave

#old versions
# import matplotlib.pyplot as plt
#
#
# # creating fake data points
# X = [590,540,740,130,810,300,320,230,470,620,770,250]
# Y = [32,36,39,52,61,72,77,75,68,57,48,48]
#
# plt.scatter(X,Y)
# plt.show()


import pygame, sys
from pygame.locals import *
import numpy as np
import random
import csv


class TheWave:

    def __init__(self):
        self.matrix_data = []

        self.countryData = [] #2d array for country data
        self.countryNum = 0
        self.countryName = []

        self.yearData = [] #an list for year data
        self.yearNum = 0

        self.EDGE = 5

    #read data from csv file
    def read_data(self, filename):
        with open(filename, mode='r') as csv_file:
            datareader = csv.reader(csv_file, skipinitialspace=True,delimiter=',', quoting=csv.QUOTE_NONE)

            row1 = next(datareader)  # gets the first line - headers
            row1.pop()
            row1.pop(0) # pop year
            self.countryNum = len(row1) #number of country
            self.countryName = row1
            for i in range(self.countryNum):
                self.countryData.append([]) #2d array for country data

            #loop over data and add to list
            for row in datareader:
                self.yearNum += 1
                row.pop()
                for num in range(len(row)):
                    if(num==0):#if years
                        self.yearData.append(row[num])
                    else:
                        self.countryData[num-1].append(row[num])
                # print('\t '.join(row))


        print(f"country name is {self.countryName}")
        print(f"country number is {self.countryNum}")
        print(f"year number is {self.yearNum}")
        print(self.yearData)
        print(self.countryData)


    #data in array from for testing
    def data_for_test(self):
        X = [1990,1995,2000,2005,2010,2015,2020, 2025, 2030, 2035, 2040, 2050,2055,2060,2065,2070] #for years
        Y0 = [32,36,39,52,61,72,77,75,80, 82, 83, 87,95,103,104,150]
        Y1 = []
        Y2 = []
        for num in Y0:
            num1 = num + random.randint(-20,20)
            Y1.append(num1)
            num2 = num + random.randint(0,40)
            Y2.append(num2)

        # need to manipulate data here
        self.matrix_data = np.array([X, Y0, Y1, Y2])


    # normalize data so it fits the screen
    def nomalize_data_test(self):
        X = self.matrix_data[0]
        Y0 = self.matrix_data[1]
        Y1 = self.matrix_data[2]
        Y2= self.matrix_data[3]
        # normalize X
        self.matrix_data[0] = self.EDGE + ((X - min(X))/(max(X) - min(X)))*1000
        self.matrix_data[1] = 500 -  ((Y0 - min(Y0))/(max(Y0) - min(Y0)))*500
        self.matrix_data[2] = 500 -  ((Y1 - min(Y1))/(max(Y1) - min(Y1)))*500
        self.matrix_data[3] = 500 -  ((Y2 - min(Y2))/(max(Y2) - min(Y2)))*500
        print("normalized data")

    def load_image(self, imgName):
        return

    def main(self):


        self.read_data("aging_data.csv")
        sys.exit()

        self.data_for_test()
        self.nomalize_data_test()
        curData = self.matrix_data

        print('curData is : ')
        for row in curData:
            print(row)
        X = curData[0]
        Y0 = curData[1]
        Y1 = curData[2]
        Y2 = curData[3]

        # print(curData)
        pygame.init()

        # DISPLAY=pygame.display.set_mode((1920,1080),0,32)
        DISPLAY=pygame.display.set_mode((1280,720),0,32)
        pygame.display.set_caption('The Wave')


        WHITE=(255,255,255)
        BLUE=(0,0,255)

        # fill canvas
        DISPLAY.fill(WHITE)

        # draw img
        # background = pygame.image.load("mountFuji.png")
        background = pygame.image.load("the_great_wave.jpg")
        elementImg = pygame.image.load("trans_wave.png")
        elementImg2 = pygame.image.load("invert_wave.png")

        background = pygame.transform.scale(background, (3000, 2000))
        DISPLAY.blit(background, (1,1))

        # pygame.draw.circle(screen, color, (x,y), radius, thickness)
        for i in range(max(len(Y0),len(X))):
            # randomlize the size
            height = random.randint(40,100)
            width = int(height*1.5)
            eachElementImg = elementImg.copy()
            eachElementImg = pygame.transform.scale(eachElementImg, (width, height))
            DISPLAY.blit(eachElementImg, (X[i],Y0[i]))
            # pygame.draw.circle(DISPLAY, BLUE, (X[i],Y[i]), 3, 1)

        for i in range(max(len(Y1),len(X))):
            # randomlize the size
            height = random.randint(40,100)
            width = int(height*1.5)
            height2 = random.randint(40,100)
            width2 = int(height*1.5)
            eachElementImg = elementImg2.copy()
            eachElementImg = pygame.transform.scale(eachElementImg, (width, height))
            eachElementImg2 = pygame.transform.scale(eachElementImg, (width2, height2))
            DISPLAY.blit(eachElementImg, (X[i],Y1[i]))
            DISPLAY.blit(eachElementImg2, (X[i],Y1[i]+random.randint(-50, 50)))
            # pygame.draw.circle(DISPLAY, BLUE, (X[i],Y[i]), 3, 1)

        for i in range(max(len(Y2),len(X))):
            # randomlize the size
            height = random.randint(40,100)
            width = int(height*1.5)
            eachElementImg = elementImg.copy()
            eachElementImg = pygame.transform.scale(eachElementImg, (width, height))
            DISPLAY.blit(eachElementImg, (X[i],Y2[i]))
            # pygame.draw.circle(DISPLAY, BLUE, (X[i],Y[i]), 3, 1)





        # pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))

        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()



#----------------------------run-------------
if __name__ == "__main__":
    tw = TheWave()
    tw.main()
