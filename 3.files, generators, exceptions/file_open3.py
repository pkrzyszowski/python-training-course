a = [1, 2, 3, 4, 5]

with open('out_file.txt', 'w') as f:
    for i in range(10):
        f.writelines((str(x) + '\n' for x in a))