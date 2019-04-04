
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

class TheWave:

    def __init__(self):
        self.matrix_data = None;
        self.EDGE = 5;
    #read data from csv file
    def read_data(self, filename):

    	openfile = file(filename, 'rU')
    	readfile = csv.reader( openfile, skipinitialspace=True,delimiter=',', quoting=csv.QUOTE_NONE)

    	self.raw_headers = readfile.next()
    	self.raw_types = readfile.next()

    	for row in readfile:
    		self.raw_data.append(row)

    	for i in range(len(self.raw_headers)):
    		self.header2raw[self.raw_headers[i]] = i

    	#read numeric data
    	numIndex = 0
    	numList = []# list of numeric index
    	#read enumic data
    	enumIndex = 0

    	#get the dictionary mapping header string to index of column in matrix data
    	for i in range(len(self.raw_headers)):
    		if self.raw_types[i] == 'numeric'or self.raw_types[i] == "enum":
    			numList.append(i)
    			self.header2matrix[self.raw_headers[i]] = numIndex
    			if self.raw_headers[i] == "enum":
    				self.enum_headers.append(self.raw_headers[i])
    				self.enum2num[self.raw_headers[i]] = enumIndex
    				self.enum_key.append({})
    				enumIndex += 1
    			numIndex += 1

    	#print numList
    	print(str(numIndex) + '******')

    	#**********I tried many different ways to approachments.*********
    	#a = np.zeros((len(self.raw_data),len(numList))) -- another way
    	#numArray = np.empty(shape[len(self.raw_data),len(self.header2matrix)]) #a temperary array
    	numMatrix = []
    	#make the data into floats
    	for i in range(len(self.raw_data)):
    		numRow = []
    		#counting = 0
    		for j in numList:
    			# if enum:
    			if self.raw_headers[j] in self.enum2num:
    				ti = self.enum2num[self.raw_headers[j]] #temperary index
    				if self.raw_data[i][j] in self.enum_key[ti]:
    					tf = float(self.enum_key[ti][self.raw_data[i][j]])#temperary float
    					numRow.append(tf)
    				else:
    					keyIndex = len(self.enum_key[ti])
    					self.enum_key[ti][self.raw_data[i][j]] = keyIndex
    					numRow.append(float(keyIndex))

    			# if numeric
    			else:
    				data_String = self.raw_data[i][j]
    				numRow.append(float(data_String))#append it to the temperary list after transferred to float
    			#a[i,counting] = float(data_String)
    			#counting+=1
    			#print counting
    		numRowArray = np.array(numRow)
    		numMatrix.append(numRow)

    	A = np.reshape(numMatrix, [len(self.raw_data),len(numList)])

    	self.matrix_data = np.matrix(A)

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
