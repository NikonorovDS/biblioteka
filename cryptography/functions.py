def del_string(string):
    '''
    Деление строки по 2 символа
    '''

    string = [string[i:i+2] for i in range(0, len(string), 2)]
    #print(string)
    return(string)


def key_lenght(string,left_limit,right_limit): 
    '''
    Нахождение длины ключа для шифра Виженера
    '''    
    smax=0
    for i in range(-left_limit, -right_limit-1, -1):
        # сдвиг вправо, с -
        str_b = string[i:] + string[:i]
        s=sum(s1 == s2 for s1, s2 in zip(string, str_b))
        if  s > smax:
            smax = s
            dk=abs(i)
    return dk


def frq(string):
    '''
    Нахождение частоты вхождения элемента в спсике
    '''
    counter = 0
    num = 0

    for i in string:
        
        curr_frequency = string.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i

    return num


def xor_strings(string,t):
    '''
    Ксор двух строк через орд и чар
    '''
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(string,t))


def string_chr(string):
    '''
    Перевод строки из 16ой в char
    '''
    str_10=list(map(lambda x: int(x,16),string))
    str_chr_=list(map(chr,str_10))
    return str_chr_


def xor_strings_nochar(string,str_chr_1,str_chr_2):
    '''
    Ксор двух строк через орд
    '''
    aa=[]
    for i in range(len(string)):
        aa.append(ord(str_chr_1[i])^ord(str_chr_2[i]))          
    return aa


def str_elements(string):
    '''
    Распределление строки по элементам
    '''
    key_10=list(map(lambda x: ord(x) ,string))
    key_chr=list(map(lambda x: chr(x) ,key_10))
    return key_chr
   
def xor_string_chr(string):
    '''
    Перевод строки в char
    ''' 
    str_chr=list(map(lambda x: chr(x) ,string))
    return str_chr


def spiski_vvod(self):
    '''
    Ввод необходимых списков
    '''
    db=[]
    dc=[]
    ad=[]
    dbchr=[]
    dcchr=[]
    adchr=[]
    a=[]
    b=[]
    c=[]
    d=[]
    
    
