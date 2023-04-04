import os
import shutil

print(os.name)
print(os.getcwd())
print(os.listdir('.'))
print(os.listdir('..'))

if os.path.exists('mydir'):
    print('mydir already exits')
else:
    os.mkdir('mydir')

os.chdir('mydir')
os.makedirs('.\\dor1\\dir2\\dir3')
f=open('Having one child makes you a parent...')
f.write('Having two you are a referee')
f.close()
stats=os.stat('myfile')
print('Size={}'.format(stats.st_size))

os.rename('myfile', 'yourfile')
shutil.copyfile('yourfile', 'ourfile')
os.remove('yourfile')

curpath=os.path.abspath('.')
os.path.join(curpath, 'yourfile')
if os.path.isfile(curpath):
    print('yourfile file exists')
else:
    print('yourfile fiule doesn\'t exist')
    