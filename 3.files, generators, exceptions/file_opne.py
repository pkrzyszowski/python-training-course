with open('sample_file.txt', 'r') as f:
    lines = []
    for line in f:
        print(line, end='')
        lines.append(line)
    print(lines)


f.close()