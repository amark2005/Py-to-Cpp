import ctypes
import os
engine_path=os.path.join(os.getcwd(),"engine.so") #this line builds the path of the desired file, os.path.join joins the strings into a valid path and os.getcwd() gets current path and os.path.join stiches both cwd and file name
engine=ctypes.CDLL(engine_path) #this line declares the .so file as CDLL (C dynamic link library)
print("Lets find out Force")
m=int(input("Enter the mass: "))
a=int(input("Enter the Accelertion: "))
f=engine.force(m,a)
print(f"the force is {f}")