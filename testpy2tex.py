"""
Test file for py2tex.


Using "import testpy2tex" will allow to test changes in the notebook

"""
from py2tex import PrettyPrint

ip=get_ipython()
magicPrettyPrint = PrettyPrint(ip)
ip.register_magics(magicPrettyPrint)
