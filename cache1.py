'''
Created on Jan 23, 2020

@author: ashish
'''
from varnish import VarnishManager as varnish_manager
manager = varnish_manager( ('localhost:6082', 'localhost:6083') )
manager.run('ping')
manager.close()
