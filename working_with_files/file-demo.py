# File objects

# Context manager; no need to close the file
# methods for reading read() , readlines(), readline()
with open('test.txt', 'r') as f: 
    pass
    #for line in f: 
    #   print(line, end='')
    size_to_read = 10

    f_contents = f.read(size_to_read)
    #print(f_contents, end='')

    f.seek(0) # -> changes the position of the read

    f_contents = f.read(size_to_read)
    #print(f_contents)


    #while len(f_contents) > 0:
    #    print(f_contents, end='*')
    #    f_contents = f.read(size_to_read)

    #f_contents = f.readline()
    #print(f_contents, end='')


#not recommended
#second argument defines what we do with the file(mode)
# f = open('test.txt', 'r')

# print(f.name)
# print(f.mode)
# print(f.closed)

with open('test2.txt', 'w') as f: 
    f.write('Test')
    f.seek(0)
    f.write('R')

with open('test.txt', 'r') as rf: 
    with open('test_copy.txt', 'w') as wf:
        for line in rf: 
            wf.write(line)

with open('gin.png', 'rb') as rf: 
    with open('gin_copy.png', 'wb') as wf:
        chunk_size = 4096 
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0: 
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)