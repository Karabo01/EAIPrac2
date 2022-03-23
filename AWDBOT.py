
import numpy as np
import csv
import random
import matplotlib.pyplot as plt

class Node(object):

    def __init__(self, character):
        self.character = character
        self.left = None
        self.center = None
        self.right = None
        self.parent = None
        self.full = 0
        self.height = 0


class RPS(object):

    def __init__(self):
        self.rootNode = None

    def putin(self, levels):
        i = 0
        j = 0
        while (j <= levels):
            i = 0
            while (i < 3 ** (levels - j)):

                if (self.rootNode == None):
                    self.rootNode = self.putItem(self.rootNode, "start")
                else:
                    self.rootNode = self.putItem(self.rootNode, "R")
                    self.rootNode = self.putItem(self.rootNode, "P")
                    self.rootNode = self.putItem(self.rootNode, "S")
                    i += 1
            j += 1

    def putItem(self, node, key):

        if node == None:
            node = Node(key)
            return node

        if (node.full == 3):
            node = self.check(node, key)

        if (key == "R"):
            node.left = self.putItem(node.left, key)
            node.left.parent = node
            node.full += 1

        if (key == "P"):
            node.center = self.putItem(node.center, key)
            node.center.parent = node
            node.full += 1

        if (key == "S"):
            node.right = self.putItem(node.right, key)
            node.right.parent = node
            node.full += 1

        return self.rootNode

    def check(self, node, key):

        if (node.left.full < 3):
            return node.left
        elif (node.center.full < 3):
            return node.center
        elif (node.right.full < 3):
            return node.right
        else:
            if (rheight(node.left) > rheight(node.center)):
                return self.check(node.center, key)
            elif (rheight(node.center) > rheight(node.right)):
                return self.check(node.right, key)
            else:
                return self.check(node.left, key)


# Function to print level order traversal of tree
def printLevelOrder(root, began):
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i, began)


# Print nodes at a current level
def printCurrentLevel(root, level, began):#Prints leves of BFS
    temp = root

    allParents = ""
    if root is None:
        return
    if level == 1:
        finished = root.character
        while temp.character != "start" and temp.parent.character != "start":
            allParents = allParents + temp.parent.character
            temp = temp.parent
        # finished = printP(root, play, began)
        bfs.append(allParents + root.character)
        #print(allParents + root.character, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level - 1, began)
        printCurrentLevel(root.center, level - 1, began)
        printCurrentLevel(root.right, level - 1, began)


""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""


def printP(node, play):#Prints parents of tree
    if node is None:
        return ""
    elif node.parent is None:
        return ""
    elif node.parent == "start":
        play += node.character
        return play
    else:
        play += printP(node.parent, play)
        return play


def rheight(node):#Computes right subtree height
    Rheight=0
    if node is None:
        return 0
    else:
        while(node!=None):
            node=node.right
            Rheight+=1
        return Rheight

def height(node):#Computes height of tree
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
        cheight = height(node.center)
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        elif(cheight>rheight):
            return cheight+1
        else:
            return rheight+1
def reConvert(val):#Converts integers into RPS
    if val==1:
        return 'R'
    if val==2:
        return 'P'
    if val==3:
        return 'S'
    else:
        return Random()
def convert(Char):#Converts RPS into integers
    if Char=="R":
        return 1
    if Char=="P":
        return 2
    if Char=="S":
        return 3
    else:
        return 0
def Random():#Produces random gene
    return random.choice(["R", "P", "S"])

def RandomNum():#Produces random gene as integer
    return random.choice([1, 2, 3])

def Mutation(pop,factor):#Mutaion done by creating random gened individuals
    i=0
    print("Mutation Initiated!!")
    while(i<len(pop)):
        for j in range(81):
            pop[i][j]=convert(Random())
        i+=factor
        print(str(i-4)+"=", end="")
    print("Mutation Completed!!")



def GA(population,max):#Genetic Algorithm
    generation=[]

    i=0
    fitness=[]
    final=[]
    while(len(population)>3):#fitness computed until population is left with 3 indviduals
        i+=1
        generation.append(i)
        fitness.append(Fitness(population,len(population)))
    cvs=[]
    final=(finalForm(population))
    for j in range(len(final)):
        cvs.append(reConvert(final[j]))
    filename="AWD.txt"

    with open(filename, 'w') as csvfile: # Write data to text file
        csvwriter= csv.writer(csvfile)
        csvwriter.writerow(cvs)


    #Plot generation fitness
    plt.figure('Fitness of the best individual from each generation')
    plt.plot(generation, fitness)
    plt.title('Fitness vs Generation')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.show()



def Crossover(Altered):#Function for mating two individuals
    print("Starting: Cross Over ")
    tempList = []
    for r in range(len(Altered)-1):
        for c in range (41):
            tempList.append(Altered[r][c])
        for c in range (41):
            Altered[r][c] = Altered[r+1][c]
            Altered[r+1][c] = tempList[c]
    tempList.clear()
    for r in range(len(Altered) - 2):
        for c in range (81):
            tempList.append(Altered[r][c])
        for c in range (81):
            Altered[r][c] = Altered[r+2][c]
            Altered[r+2][c] = tempList[c]
        print("=", end="" )
    print("Cross Over Completed!!")


def finalForm(populus):#Function to determin fittest individual out of final 3
    finalPop = []
    if(len(populus) == 3):
        for t in range(len(populus[0])):
            if populus[0][t] == populus[1][t]:
                finalPop.append(populus[0][t])
            else:
                if populus[2][t] != 0:
                    finalPop.append(populus[2][t])
                else:
                    if ((populus[0][t] == 1 and populus[1][t] == 2) or (populus[0][t] == 2 and populus[1][t] == 1)):
                        finalPop.append(3)
                    elif ((populus[0][t] == 1 and populus[1][t] == 3) or (populus[0][t] == 3 and populus[1][t] == 1)):
                        finalPop.append(2)
                    elif ((populus[0][t] == 3 and populus[1][t] == 2) or (populus[0][t] == 2 and populus[1][t] == 3)):
                        finalPop.append(1)
                    elif ((populus[0][t] == 1 and populus[2][t] == 2) or (populus[0][t] == 2 and populus[2][t] == 1)):
                        finalPop.append(3)
                    elif ((populus[0][t] == 1 and populus[2][t] == 3) or (populus[0][t] == 3 and populus[2][t] == 1)):
                        finalPop.append(2)
                    elif ((populus[0][t] == 3 and populus[2][t] == 2) or (populus[0][t] == 2 and populus[2][t] == 3)):
                        finalPop.append(1)
                    elif ((populus[2][t] == 1 and populus[1][t] == 2) or (populus[2][t] == 2 and populus[1][t] == 1)):
                        finalPop.append(3)
                    elif ((populus[2][t] == 1 and populus[1][t] == 3) or (populus[2][t] == 3 and populus[1][t] == 1)):
                        finalPop.append(2)
                    elif ((populus[2][t] == 3 and populus[1][t] == 2) or (populus[2][t] == 2 and populus[1][t] == 3)):
                        finalPop.append(1)
                    else:
                        finalPop.append(random.choice([1, 2, 3]))

    else:
        for t in range(len(populus[0])):
            if populus[0][t] == populus[1][t]:
                finalPop.append(populus[0][t])
            else:
                if(populus[0][t]==0 and populus[1][t]==0):
                    finalPop.append(random.choice([1, 2, 3]))
                elif populus[0][t]==0:
                    finalPop.append(populus[1][t])
                elif populus[1][t]==0:
                    finalPop.append(populus[0][t])
                elif((populus[0][t] == 1 and populus[1][t] == 2) or (populus[0][t] == 2 and populus[1][t] == 1)):
                    finalPop.append(3)
                elif((populus[0][t] == 1 and populus[1][t] == 3) or (populus[0][t] == 3 and populus[1][t] == 1)):
                    finalPop.append(2)
                elif((populus[0][t] == 3 and populus[1][t] == 2) or (populus[0][t] == 2 and populus[1][t] == 3)):
                    finalPop.append(1)
    return finalPop


def Fitness(populus,max):# fitness computed by getting most played genes
    fitness=0

    print("Calculating Fitness: ")
    p1 = 0
    p2 = 0
    r=0
    mutant = 0
    while(r<int(round(max/8))):
        for c in range(len(populus[0])):
            if(populus[r][c] == populus[r+1][c]):
                p1 += 1
            if (populus[r+2][c] == populus[r+3][c]):
                p2 += 1
        if(p2 < p1):
            fitness=p1
            populus.pop(r+2)
            populus.pop(r+3)
        elif(p1 <= p2):
            fitness=p2
            populus.pop(r)
            populus.pop(r+1)
        if(p1==p2):
            mutant+=1
        r += 4
        p1 = 0
        p2 = 0
        print("=", end="")
    print("Fitness Completed")
    print("Length of new population is: "+str(len(populus)))
    Crossover(populus)
    x=10
    if(mutant >= max/x):
        Mutation(populus,x)

    return fitness


#reading data from csv file
sequence_filename = "data1.csv"
with open(sequence_filename, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


print("Data extracted!!")
tree = RPS()
tree.putin(3)
began=False
bfs=[]
twin=[]
#aranging data according to BFS tree
printLevelOrder(tree.rootNode,began)
for i in range(len(bfs)-81):
    bfs.pop(0)

for i in range(len(bfs)):
    twin.append(0)

for i in range(len(data)):
    stringPl=""
    for j in range(len(bfs)):
        stringPl=str(data[i])
        if(bfs[j]==stringPl[2:6]):
            twin[j]+=1
            break

max=0
for i in range(len(twin)):
    if(twin[i]>max):
        max=twin[i]


temp=[]
population = [[0 for i in range(81)] for j in range(max)]
print("Generating Population")
for i in range(len(bfs)):
    for j in range(len(data)):
        stringPl=str(data[j])
        if(bfs[i]==stringPl[2:6]):
            temp.append(data[j])
    #here

    for j in range(max):
        if(j<len(temp)):
            play=str(temp[j])
            population[j][i]= convert(play[10:11])
        else:
            break

    print("=", end="")
print("Population Generated")



GA(population,max)
print("GA Completed ")