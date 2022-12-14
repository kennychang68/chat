
#read file
def read_file(filename):   
    lines = [] 
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
        return lines    

#convert format
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person +':'+line)
    return new

#write_file
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

    

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)



main()




