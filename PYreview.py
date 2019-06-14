"""
review

python-interpreted language
high-level
"""

#print the current date
import time
import datetime

print ("Time(s) since epoch: %s" %time.time())
print ("Current datetime: " , datetime.datetime.now())
print ("#day of Month year week#(day)# dayOfWeek: ")
print(datetime.date.today().strftime("%j %d %B %Y %W %w %A"))
print (time.strftime("%m|%d~{%H:%M}"))

some_limit = 3
condition = True #1
#condition for
#while loop
while(condition<some_limit):
    print("do something repetetive a couple times")
    condition+=1
#for iterating though lists
example_list = ["collection", "of", 'things'] #group of objects
#we can use a for-loop to iterate through items
for thing in example_list:
    print("{} {}".format(thing,example_list.index(thing)))
    #prints thing and it's position in the listth
#or a range of numbers (from, to, by)
for x in range (4,47,3):
    print("{}".format(x), end=" ")
    #print that number
    #and if that number is even/divisible by 2
    even = x%2
    if(even==0):
        print('e', end = " ") #for even
    #takes the square
    power = x**2
    arbitrary_limit = 1437
    #less than arbitrary limit
    if(power<arbitrary_limit):
        continue
    #greater than or equal to number
    elif(power>=arbitrary_limit):
        break
    #is never reached, but is here just in case
    else:
        break

#encapsulate a function in a...function
def printList(some_list) :
    for entry in some_list:
        print(some_list.index(entry), entry)
        
list_of_parameters = ["example", "parameters"]  
#perhaps list primes? 
printList(list_of_parameters)

x = 427300000 #grand scope
#global?
print(x)
#this x is just a placeholder and the 
for x in range(20, 2200000000,x):
    print(x, end = ' ')
    print("local scope")
#since we used x it changed
print(x)

def speakOnErrors():
    print("some common errors:")
    print("variableName != variableName")
    print("    don't forget your indentation")
    print("close your opening statements")
speakOnErrors()

#writing to a file
writeThis = "to a file"
#(over)write file
saveFile = open("somefile.txt", 'w')
#write to file(
saveFile.write(writeThis)
#close open resource
saveFile.close()

#appending to a file
appendThis = 'to some file'
saveFile = open("somefile.txt",'a')
#append to somefile.txt
saveFile.write(appendThis)
#CLOSE RESOURCE
saveFile.close()

#check when last opened
saveFile = open('somefile.txt','r').readlines()
print(saveFile)

#reading from a file
readThis = open('somefile.txt', 'r').read()
print(readThis)

#splitlines
splitThis = readThis.split('\n')
print(splitThis)
 
#easier split
readThis2 = open('somefile.txt', 'r').readlines()
print(readThis2)

#write the date/time to the file
appendThis = time.strftime("%m|%d~{%H:%M}")
saveFile = open("somefile.txt",'a')
saveFile.write(appendThis)
saveFile.close()

#CLASSES!
class calc:
#these are class functions+
    
    def add(x, y):
        answer = x+y
        print(answer)

    def sub(x, y):
        answer = x-y
        print(answer)

    
    def mult(x, y):
        answer = x*y
        print(answer)

    
    def div(x, y):
        answer = x/y
        print(answer)

#these are referenced with a basic call class.function()
calc.add(2,2)
    
#finally, input
feeling = input('how are you?')
<<<<<<< HEAD
print("this one doesn't understand what "+feeling+
" means, but hopes you make the most of your day, anyway.") 
=======
print("this one doesn't understand what "+feeling+" means, but i hope you make the most of your day, anyway.") 
>>>>>>> af78f722976d2a9ab26e42b09af763e147e94a6e
        
#it is trivial to do statistics in python on someList
someList = [1, 2, 3, 4, 7, 5, 6, 9, 47, 47]

#contained in statistics
import statistics
#however, if we want to make this a little simpler we can say
#import module as alias or

#from package import functions as alias, separated, by, commas

#to import all of them, we can use
#from statistics import *

mean = statistics.mean(someList)
print('mean = ', end = " ")
print(mean)

median = statistics.median(someList)
print('median = ', end = " ")
print(median)

mode = statistics.mode(someList)
print("mode = ", end = " ")
print(mode)

stdev = statistics.stdev(someList)
print("stdev = ",end = " ")
print(stdev)

variance = statistics.variance(someList)
print("variance = ", end = " ")
print(variance)

#it is important to note that this script is a module that can be called
#any functions or classes defined in here can be called as
#moduleName.[className.]functionName(parameters)
#will not be available to python in general unless you add to packages

#error handling-for when the world gets in the way
try:
    print('running try')
    print('5'+5)
    print('5'+x)
    import mars

except TypeError as t:
    print('type error prollems')

#allows the code to continue to run
except Exception as e:
#this could be written to a log file >.>
    print(str(e))
    print("something else went wrong")

print("codin continues!")

#lists vs tuples
#a list is enclosed in []
pythonList=[3,4,5,6,2,6,3,4,4]
#print full list
print(pythonList)
#print index
print(pythonList[4])
#append to end of list
pythonList.append(35)
#insert 7 to 5th index
pythonList.insert(5,7)
print(pythonList)
#remove first something from a list
pythonList.remove(6)
print(pythonList)
#print an index
print(pythonList.index(5))
#count something
print(pythonList.count(4))
#sort a list
pythonList.sort()
print(pythonList)
pythonList.reverse()
print(pythonList)

#tuples are immutable
def example():
#this function returns a tuple
    return 15, 19
#unpacks by unit
#slightly faster
(a, b) = example()
print(a)
print(b)

#dictionaries are {k:v, k:v} -paired hash-sorted table
gradeDict = {'David':65,'Kelly':82,'George':79}

print(gradeDict)
print(gradeDict['David'])
gradeDict["Jessie"] = 92
print(gradeDict)
del gradeDict['David']
print(gradeDict)
gradeDict['overachiever'] = [102,103]
print(gradeDict)
