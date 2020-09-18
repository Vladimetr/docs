# мы также отсюда можем импортировать module2
# поднявшись на уровень выше
from .. import module2

def func_sub_module():
    module2.func_module2()
    print('func_sub_module')
    
    