
try:
    f = open('test_file.txt')
    if f.name == 'test_file.txt':
        raise Exception
except FileNotFoundError as e:
    print("Sorry this file does not exist")
except Exception as e: 
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")