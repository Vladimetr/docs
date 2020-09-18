# в текущей директории найти sub_package
from .sub_package import sub_module
# в текущей директории найти module2
from . import module2

def func_module1():
    # наш модуль использует под_пакет и из него модуль и функцию
    sub_module.func_sub_module()
    module2.func_module2()
    print('func_module1')
    
    
    
# try:
#     # run inside package
#     from embedding.alex2 import Alex2
#     import preprocess
#     import sys
#     sys.path.append("..")   <- run sub_module
#     import module
# except ImportError:
#     # run outside package
#     from .embedding.alex2 import Alex2
#     from . import preprocess
#     from .. import module1  <- run sub_module