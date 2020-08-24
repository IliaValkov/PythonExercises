
import os
from datetime import datetime

#print(os.getcwd())

os.chdir('/home/iliav/tutorials')

print(os.getcwd())

#os.mkdir('os-demo-02/')
os.makedirs('os-demo-02/subdir1')

print(os.listdir())

#os.rmdir('os-demo-02/')
os.removedirs('os-demo-02/subdir1')

print(os.listdir())

os.chdir('/home/iliav/tutorials/os_module')

os.rename('test.txt', 'demo.txt')

print(os.listdir())
os.rename('demo.txt', 'test.txt')

print(os.stat('test.txt'))

mod_time = os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(mod_time)) 

os.chdir('/home/iliav/tutorials')

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print()

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'path_demo.txt')

print(file_path)

print(os.path.basename('/tmp/test.txt'))

print(os.path.dirname('/tmp/test.txt'))

print(os.path.split('/tmp/test.txt'))

print(os.path.exists('/tmp/test.txt'))

print(os.path.isdir('/tmp/test.txt'))

print(os.path.isfile('/tmp/test.txt'))

print(os.path.splitext('/tmp/test.txt'))

