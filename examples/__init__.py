import os

print('==> import examples')

# f = open('module.py', 'w+')
# f.write('# module import\n')
# dirs = os.listdir('.')
# for d in dirs:
#     if os.path.isdir(d):
#         # from .dir.file imprt *
#         f_list = os.listdir(d)
#         for file_name in f_list:
#             if '.py' in file_name:
#                 import_module = "from .%s.%s import *\n" % (
#                     d, file_name.split('.')[0])
#                 f.write(import_module)
# f.close()

from .module import *
