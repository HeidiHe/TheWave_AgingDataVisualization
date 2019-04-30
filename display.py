
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

input = 0 #float, interactive input

class TheWave:

    def __init__(self):
        self.matrix_data = []

        self.countryData = [] #2d array for country data
        self.countryNum = 0
        self.countryName = []

        self.yearData = [] #an list for year data
        self.yearNum = 0

        self.EDGE = 5

        self.input = 0

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
                        self.yearData.append(float(row[num]))
                    else:
                        self.countryData[num-1].append(float(row[num]))
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

    def nomalize_data(self):
        # normalize X
        # for i in range(len(self.yearData)):
        #     print(self.yearData[i])
        #     self.yearData[i] = self.EDGE + ((X - min(X))/(max(X) - min(X)))*1000
        #
        self.yearData = np.array(self.yearData)
        self.countryData = np.array(self.countryData)
        X = self.yearData

        self.yearData = self.EDGE + ((X - min(X))/(max(X) - min(X)))*1000
        # self.yearData = self.EDGE + ((X - min(X))/(max(X) - min(X)))*1000

        for i in range(self.countryNum):
            Y = self.countryData[i]
            self.countryData[i] = 500 -  ( (Y - min(Y))/(max(Y) - min(Y)) )*500


        return

    def load_image(self, imgName):
        return

    def drawCanvas(self):
        X = self.yearData
        Y0 = self.countryData[0]

        mousex, mousey = pygame.mouse.get_pos()
        print(mousex)
        print(mousey)

        WHITE=(255,255,255)
        BLUE=(0,0,255)

        # fill canvas
        self.DISPLAY.fill(WHITE)

        # draw img
        # background = pygame.image.load("mountFuji.png")
        # background0 = pygame.image.load("the_great_wave.jpg")
        background = pygame.image.load("dataBG.png")
        # bottom = pygame.image.load("wave_graph.png")
        elementImg = pygame.image.load("wave_tip_colored.png")
        # elementImg = pygame.image.load("trans_wave.png")
        elementImg2 = pygame.image.load("invert_wave.png")

        # background0 = pygame.transform.scale(background0, (3000, 2000))
        background = pygame.transform.scale(background, (1280,720))
        # bottom = pygame.transform.scale(bottom, (1280,720))
        # self.DISPLAY.blit(background0, (1,1))
        self.DISPLAY.blit(background, (1,1))
        # self.DISPLAY.blit(bottom, (1,1))

        '''
        # background = pygame.image.load("mountFuji.png")
        background0 = pygame.image.load("the_great_wave.jpg")
        # background = pygame.image.load("wave_middle.png")
        # bottom = pygame.image.load("wave_graph.png")
        # elementImg = pygame.image.load("wave_tip_colored.png")
        # elementImg = pygame.image.load("trans_wave.png")
        elementImg = pygame.image.load("trans_wave.png")

        background0 = pygame.transform.scale(background0, (3000, 2000))
        # background = pygame.transform.scale(background, (1280,720))
        # bottom = pygame.transform.scale(bottom, (1280,720))
        self.DISPLAY.blit(background0, (1,1))
        # self.DISPLAY.blit(background, (1,1))
        # self.DISPLAY.blit(bottom, (1,1))
        '''

        # # draw random ones
        # for i in range(max(len(Y0),len(X))):
        #     # randomlize the size
        #     height = random.randint(40,100)
        #     width = int(height*1.5)
        #     eachElementImg = elementImg.copy()
        #     eachElementImg = pygame.transform.scale(eachElementImg, (width, height))
        #     self.DISPLAY.blit(eachElementImg, (X[i],Y0[i]))
        #     # pygame.draw.circle(self.DISPLAY, BLUE, (X[i],Y[i]), 3, 1)

        # draw interactive ones

        curPos = int(mousex/25) #hard coding for mouse posision
        self.input = curPos
        print("lenght Y0 is " + str(len(Y0)))
        print("input is " + str(curPos))
        for i in range(min(len(Y0),self.input)):
            height = random.randint(40,200)
            width = int(height*1.5)
            eachElementImg = elementImg.copy()
            eachElementImg = pygame.transform.scale(eachElementImg, (width, width))
            # eachElementImg = pygame.transform.scale(eachElementImg, (width, height))
            self.DISPLAY.blit(eachElementImg, (X[i],Y0[i]))
            # pygame.draw.circle(self.DISPLAY, BLUE, (X[i],Y[i]), 3, 1)

    def main(self):


        self.read_data("aging_data.csv")
        # sys.exit()

        # self.data_for_test()
        # self.nomalize_data_test()
        self.nomalize_data()
        curData = self.countryData

        print('curData is : ')
        for row in curData:
            print(row)

        pygame.init()
        #set up pygame
        self.DISPLAY=pygame.display.set_mode((1280,720),0,32)
        pygame.display.set_caption('The Wave')
        pygame.display.set_icon(pygame.image.load("wave_tip_colored.png"))
        clock = pygame.time.Clock()

        print(f"time is {pygame.time}")
        input = pygame.time



        crashed = False


        while not crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == K_q:
                    crashed = True

            self.drawCanvas()
                # print(event)

            pygame.display.update()
            clock.tick(1)

        #quit program
        pygame.quit()
        quit()

#----------------------------run-------------
if __name__ == "__main__":
    tw = TheWave()
    tw.main()
