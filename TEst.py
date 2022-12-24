from collections import Counter
import sys
import pickle

def bytes(current_byte,out_f):   # Метод для байтовой записи 
    while len(current_byte)>8:         
        out_f.write(int(current_byte[0:8],2).to_bytes(1,"big")) 
        current_byte = current_byte[8:]
    return current_byte


def dictionary(text): # Метод для создания словаря вида [буква: кол-во вхождений]
    dctnr = dict()
    for line in text:
        for i in line:
            if i in dctnr:
                dctnr[i] += 1
            else:
                dctnr.update({i: 1})
    return dctnr


def graph_creator(arr): # метод для создания графа
    vertexes = [[el, arr[el], [], []] for el in arr] # создаем массив вида [элемент, его размер, ребенок, ребенок]

    while len(vertexes) > 1:
        vertexes.sort(key=lambda x: x[1])
        x1 = vertexes.pop(0)
        x2 = vertexes.pop(0)
        new = [x1[0] + x2[0], x1[1] + x2[1], x1, x2]
        vertexes.append(new)

    codes = {}

    def search(path, vertex): # метод для поиска адреса вершины
        if len(vertex[2]) > 1:
            search(path + "0", vertex[2])

        if len(vertex[3]) > 0:
            search(path + "1", vertex[3])

        else:
            codes[vertex[0]] = path
            return

    search("", vertexes[0])
    return codes


def encode(infile, outfile: str):
    inf = open(infile, 'r')
    out = open(outfile, 'w')
    text = inf.readlines()
    a = dictionary(text) # создаем словарь
    codes = graph_creator(a) # создаем граф
    coding_str = ''
    for i in text: 
        for line in i:
            coding_str += codes[line]
    #len_codes = len(codes)
    encode_string = f"{len(codes)} {codes} \n{coding_str}"
    out.write(encode_string)
    out.close()
    file = open(outfile.replace("txt", "bin"), "wb")
    pickle.dump(f"{len(codes)} {codes}", file)
    pickle.dump(int(coding_str, 2), file)
    inf.close()
    file.close()
    '''out.write(f'{len_codes}\n'.encode("UTF-8")) # записываем в файл мощность словаря
    for i in a.keys(): # записываем в файл словарь вида {символ : кол-во вхождений}
        line = i + " "
        out.write(line.encode("UTF-8"))
        out.write(int(a[i]).to_bytes(2, "big"))
        out.write("\n".encode(("UTF-8")))
    current_byte = ''
    for i in text: #
        for line in i:
            current_byte += codes[line] # Для каждого символа записываем в current_byte его код в виде строки     
            current_byte = bytes(current_byte, out) # Отправляем в метод для побайтовой записи
            
    extra_bits = 8-len(current_byte)  # проверяем на недозаписанные биты                   
    current_byte = current_byte + "0"*extra_bits # Дозаполняем строку нулями      
    out.write(int(current_byte,2).to_bytes(1,"big"))  
    out.write(extra_bits.to_bytes(1,"big")) # Сохраняем то, сколько битов дописали
    inf.close()
    out.close()'''

def decode(input_file, output_file):
    inp = open(input_file, 'r')      
    out = open(output_file, 'w')    

    freq_dict = {}      
    current_byte = ""    
    current_code = ""
    a = ''.join(inp) 

    #n = int(inp.readline())   
    '''for i in range(n): # дешифруем словарь
        current_line = inp.readline() # Считываем очередную строку    
        if current_line == b'\n': # проверяем на перенос строки        
            current_line = inp.readline() # если перенос, считываем следующую и оновляем словарь            
            key = int.from_bytes(current_line[1:3], "big") 
            char = "\n"
            freq_dict.update({char: key})     
            continue
        key = int.from_bytes(current_line[2:4], "big")  
        char = chr(current_line[0])
        freq_dict.update({char: key})'''  
    codes = eval(a[a.find("{"): a.find("}") + 1])
   
    codes_dict_new = {}
    for i in codes.keys():  # Меняем местами ключ и значения словаря с кодами                   
        codes_dict_new.update({codes[i]:i})
    current_byte = a[a.find("}") + 1:].strip()
    for i in current_byte:
        current_code += i    # Наращиваем пока не станет соответствовать одному из шифров           
        if current_code in codes_dict_new.keys(): 
            out.write(codes_dict_new[current_code])
            current_code = "" 

    '''for line in inp.readlines(): # Переводим каждый байт входного файла в строку
        for i in line:
            current_byte += "0"*(10 - len(str(bin(i)))) + str(bin(i))[2:]  

    extra_bits = int(current_byte[-8:], 2) # Проверяем последний байт, в котором содержится лишние биты
    current_byte = current_byte[:-(8+extra_bits)]   # Удаляем лишние биты
    codes_dict_new = {}
    
    
                     
'''
    inp.close()            
    out.close()
    
codes = {}
encode('1.txt', '2.txt')
decode('2.txt', '3.txt')

'''if len(sys.argv) < 4:
    raise "Not enough arguments"
else:
    method = sys.argv[1]
    in_path = sys.argv[2]
    out_path = sys.argv[3]
if method == '--encode':
    encode(in_path,out_path)
elif method == '--decode':
    decode(in_path,out_path)'''
