import sys, getopt
import shutil
#argc=len(sys.argv)
if len(sys.argv)==1:
    print('Incorrect usage')
    print('Correct usage:fileciopy source target')
    sys.exit(1)

source=''
target=''
# try:
#     options, arguments=getopt.getopt(sys.argv[1:], 'hs:t:')
# except getopt.GetoptError:
#     print('getopt.py -s <source> -t <target>')
# else:
#     for opt, arg in options:
#         if opt == '-h':
#             print('getopt.py -s <source> -t <target>')
#             sys.exit(2)
#         elif opt == '-s':
#             source = arg
#         elif opt == '-t':
#             target == arg
#     else:
#         print('source file:', source)
#         print('target file: ', target)
#         if source and target:
#             shutil.copyfile(source, target)
