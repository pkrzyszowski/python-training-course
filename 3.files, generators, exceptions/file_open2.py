with open('out_file.txt', 'w') as f:
    for i in range(10):
        f.write('{}\n'.format(i))