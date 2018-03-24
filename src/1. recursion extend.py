import sys 
old = sys.getrecursionlimit( ) # perhaps 1000 is typical 
sys.setrecursionlimit(1000000) # change to allow 1 million nested calls 
