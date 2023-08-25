
#read file
def read_file(filename):   
    lines = [] 
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
        return lines    
           
        
#convert format
def convert(lines):
    hank_word_count = 0
    hank_sticker_count = 0
    hank_image_count = 0
    kenny_word_count = 0
    kenny_sticker_count = 0
    kenny_image_count = 0

    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Hank':
            if s[2] == "貼圖":
                hank_sticker_count =+ 1
            elif s[2] == "圖片":
                hank_image_count =+ 1
            else:
                for m in s[2:]:
                    hank_word_count+=len(m)
         
        elif name == 'Kenny':
            if s[2] == "貼圖":
                kenny_sticker_count =+ 1
            elif s[2] == "圖片":
                kenny_image_count =+ 1
            else:
                for m in s[2:]:
                    kenny_word_count+=len(m)


    print(hank_word_count)
    print(kenny_word_count)  
    print(hank_sticker_count)
    print(kenny_sticker_count)  
    print(hank_image_count)
    print(kenny_image_count)  



#write_file
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
    

def main():
    lines = read_file('line2.txt')
    lines = convert(lines)
    write_file('output2.txt', lines)




main()





