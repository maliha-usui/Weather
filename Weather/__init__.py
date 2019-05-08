class VirtualModule(object):
   def __init__(self,name):
      import sys
      sys.modules[name]=self
   def __getattr__(self,name):
      return globals()[name]
VirtualModule("__main__")