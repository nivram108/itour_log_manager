from User import *
from time import gmtime, strftime
file_name = strftime("%m%d_%H_%M_%S", gmtime())
print (file_name)
