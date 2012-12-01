import os

print type(__file__)
print __file__

dirname = os.path.dirname(__file__)
print "dirname = ", dirname
abspath = os.path.abspath(dirname)
print "abspath = ", abspath


here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
print here()
print here('..')
print here('..', '..')
