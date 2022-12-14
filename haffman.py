from collections import Counter
import sys


def encode(input_file, output_file):
    s = ''
    outp = open(f'{output_file}','w')
    inp = open(f'{input_file}','r')
 
    
    def dict(string): # Создаем закодированный словарь из строки

        arr = Counter(string) # Создаем словарь из строки

        vertexes = [[el, arr[el], [], []] for el in arr]


        #print(vertexes) 

        while len(vertexes) > 1:  
            vertexes.sort(key=lambda x: x[1])
            x1 = vertexes.pop(0)
            x2 = vertexes.pop(0)
            
            new = [x1[0] + x2[0], x1[1] + x2[1], x1, x2]
            
            vertexes.append(new)
            
        #print(vertexes)

        codes = {} 

        def search(paht, vertex): 
            if len(vertex[2]) > 1:
                search(paht+"0", vertex[2])
                
            if len(vertex[3]) > 0:
                search(paht+"1", vertex[3])
            
            else:  
                codes[vertex[0]] = paht
                return 

        search("", vertexes[0])
        return codes
    
    text = ''
    a_1 = ' '
    while a_1 != '':
        a_1 = inp.readline()
        text += a_1
    
    codes_n = dict(text)
    len_codes_b = str(bin(len(codes_n)))
    outp.write(len_codes_b[2:]+ '\n')  # Записываем в файл мощность словаря

        
    for i in codes_n:
        outp.write(str(format(ord(i),'b')) + ' ' + str(codes_n.get(i)) + '\n')  # Записываем в файл словарь
    
    for i in text:
        s += codes_n.get(i)
    outp.write(s) # Записываем в файл закодированную строку
    outp.close()
    return s
    
def decode(input_file, output_file):
    inp = open(f'{input_file}','r')
    outp = open(f'{output_file}', 'w')
    
    codes = {}
    len_dict = int(inp.readline(),2) # Считываем из файла мощность словаря
    for i in range(len_dict): # Записываем словарь для декодирования
        a,b = map(str,inp.readline().split())
        codes.update({b:chr(int(a,2))})
            
    print(codes)
    string_row = inp.readline()
    str_result = ''
    s = ''
    for ii in string_row: # Проходимся по строке и декодируем ее
        s += ii
        if s in codes:
            str_result += codes.get(s)
            s = ''
    outp.write(str_result)
    outp.close()


if len(sys.argv) < 4:
    raise "Not enough arguments"
else:
    method = sys.argv[1]
    in_path = sys.argv[2]
    out_path = sys.argv[3]
if method == '--encode':
    encode(in_path,out_path)
elif method == '--decode':
    decode(in_path,out_path)

    

    

   


