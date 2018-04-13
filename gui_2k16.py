from Tkinter import *
import tkMessageBox
import tkFont
from PIL import ImageTk,Image
import Tkinter as Tk
from prj import *
import jpype
from jpype import*
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import csv
import numpy as np
from numpy import genfromtxt

#list of cities
cities=[] 
# list of nodes
nodes =[]
# array of calculated z 
zarr=[]
# length of cities array
x=0
# total no of trending topics
y=0


def callback():
    #print "button clicked!"
    #print "value of city1 is ", var1.get()
    cities.append(var1.get())
    #print "value of city2 is ", var2.get()
    cities.append(var2.get())
    #print "value of city3 is ", var3.get()
    cities.append(var3.get())
    #print "value of city4 is ", var4.get()
    cities.append(var4.get())
    #print "value of city5 is ", var5.get()
    cities.append(var5.get())
    #print cities
    '''for  ci in cities:
        #call tweetproc
        node = frequency()
        nodes.append(node)
        #print ci'''
    nodes.append(['job', 'gujarat', 'hiring', 'gandhi', 'keertysharma'])   
    nodes.append(['upanayanam', 'swamipraful', 'king_ranjhna', 'mh', 'arvindkejriwal'])
    nodes.append(['hiring', 'analyst', 'oracle', 'anju9822850', 'intel'])
    nodes.append(['endomondo', 'national', 'technology', 'cmmadhyapradesh', 'simhasth'])
    nodes.append(['delhi', 'gurmeetramrahim', 'msgthoughts', 'businessmgmt', 'hiring'])
    first=[]
    output=[]
    ylist=[]
    for j in nodes:
        for i in j:
          first.append(i) 
    #print first    
    for xl in first:
        if xl not in output:
            output.append(xl)
    #print output   
    ylist = sorted(output) 
    #print ylist
    y = len(ylist)
    x = len(cities)
    #ct = len(cities)
    
    #print y
    for i in range(x):
        for j in range(y):
            if ylist[j] in nodes[i]:
             z = nodes[i].index(ylist[j])
             zarr.append(5-z)
            else:
              zarr.append(0)
    #print zarr
   
    #zl = len(zarr)    
    #graph()   
    #print 'donecallback'
    # graph plotting starts here
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
 

    for i in range(x):
     f = open('e:points1.csv','wt')  
     try:
      writer = csv.writer(f)
      for j in range(y):
          writer.writerow((i+1,j+1,zarr[y*i+j]))
     finally:
      f.close()       
   
     f1 = open('e:points1.csv','rt')
     rd = csv.reader(f1,delimiter=',')
     for row in rd:
      x1=int(row[0])
      x2=int(row[1])
      x3=int(row[2])
      #print x1
      #print x2
      #print x3
     
      #print list[x1-1][5-x3]
      if x3 !=0:
       let = nodes[x1-1] 
       tt= let[5-x3] 
       #print tt
       ax.text(x1,x2,x3, tt , size=10, color='purple') 
      for j in range(x):
       ax.text(j+1,0,0, cities[j] , size=10, color='brown')
     
      my_data = genfromtxt('e:points1.csv', delimiter=',')
      points1X = my_data[:,0]
      points1Y = my_data[:,1]
      points1Z = my_data[:,2]  
      points1X = np.reshape(points1X,points1X.size)
      points1Y = np.reshape(points1Y,points1Y.size)
      points1Z = np.reshape(points1Z,points1Z.size)
      ax.set_xlabel('Cities')
      ax.set_ylabel('Topics')
      ax.set_zlabel('Frequency')
      ax.plot(points1X, points1Y, points1Z)
    plt.show()  
    #print 'done graph'



root = Tk.Tk()
background_image=Tk.PhotoImage(file="C:\\Users\\Snehal\\Documents\\NetBeansProjects\\Sample\\src\\img.gif")
background_label = Tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.wm_geometry("500x250+20+40")
root.title('Topography of Tweets')
Label(root, text="TOPOGRAPHY OF TWEETS",bg="skyblue", font = "Verdana 10 bold").grid(row=0 , column=8 ,rowspan=2 )
Label(root, text="Select city 1--->").grid(row=3, column=4)
Label(root, text="Select city 2--->").grid(row=4, column=4)
Label(root, text="Select city 3--->").grid(row=5, column=4)
Label(root, text="Select city 4--->").grid(row=6, column=4)
Label(root, text="Select city 5--->").grid(row=7, column=4)
var1 = StringVar(root)
var1.set("Select City") 
option1 = OptionMenu(root, var1, "Ahmedabad","Aurangabad","Banglore","Bhopal","Delhi","Jaipur","Lucknow","Mumbai","Nagpur","Pune")
option1.pack()
var2 = StringVar(root)
var2.set("Select City") 
option2 = OptionMenu(root, var2, "Ahmedabad","Aurangabad","Banglore","Bhopal","Delhi","Jaipur","Lucknow","Mumbai","Nagpur","Pune")
option2.pack()
var3 = StringVar(root)
var3.set("Select City") 
option3 = OptionMenu(root, var3, "Ahmedabad","Aurangabad","Banglore","Bhopal","Delhi","Jaipur","Lucknow","Mumbai","Nagpur","Pune")
option3.pack()
var4 = StringVar(root)
var4.set("Select City")
option4 = OptionMenu(root, var4, "Ahmedabad","Aurangabad","Banglore","Bhopal","Delhi","Jaipur","Lucknow","Mumbai","Nagpur","Pune")
option4.pack()
var5 = StringVar(root)
var5.set("Select City") 
option5 = OptionMenu(root, var5, "Ahmedabad","Aurangabad","Banglore","Bhopal","Delhi","Jaipur","Lucknow","Mumbai","Nagpur","Pune")
option5.pack()
option1.grid(row=3, column=7)
option2.grid(row=4, column=7)
option3.grid(row=5, column=7)
option4.grid(row=6, column=7)
option5.grid(row=7, column=7)
b = Button(root, text="GET TOPOGRAPHY", command=callback,bg="skyblue")
b.pack()
b.grid(row=15 , column=8)
root.mainloop()
#print 'doneall'

 
