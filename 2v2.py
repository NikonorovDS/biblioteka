import time
start_time = time.time()
#test
from .cryptography import *
str_a = input.input_strings['String_1']
str_b = input.input_strings['String_2']
str_c = input.input_strings['String_3']
str_d = input.input_strings['String_4']

str_a = del_string(str_a)
str_b = del_string(str_b)
str_c = del_string(str_c)
str_d = del_string(str_d)

strchr_a = string_chr(str_a)
strchr_b = string_chr(str_b)
strchr_c = string_chr(str_c)
strchr_d = string_chr(str_d)

key1='Has your daughter ever been to London?'
key1chr=str_elements(key1)
print('пробный в char')
print(key1chr)

x=spiski_vvod(0)

db=xor_strings_nochar(key1chr,strchr_d,strchr_b)
print('d^b')
print(db)
dc=xor_strings_nochar(key1chr,strchr_d,strchr_c)
print('d^c')
print(dc)
ad=xor_strings_nochar(key1chr,strchr_a,strchr_d)
print('a^d')
print(ad)

adchr=xor_string_chr(ad)
print('a ^ d в char')
print(adchr)

dbchr=xor_string_chr(db)
print('d ^ b в char')
print(dbchr)

dcchr=xor_string_chr(dc)
print('d ^ c в char')
print(dcchr)


a=xor_strings_nochar(key1chr,adchr,key1chr)
print('тект a в 10ой СС')   
print(a)
a=xor_string_chr(a)
print('тект a')   
print(a)

b=xor_strings_nochar(key1chr,dbchr,key1chr)
print('тект b в 10ой СС')   
print(b)
b=xor_string_chr(b)
print('тект b')   
print(b)

c=xor_strings_nochar(key1chr,dcchr,key1chr)
print('тект c в 10ой СС')   
print(c)
c=xor_string_chr(c)
print('тект c')   
print(c)
"""
d=xor_strings_nochar(key1chr,adchr,key1chr)
print('тект d в 10ой СС')   
print(d)
d=xor_string_chr(d)
print('тект d')   
print(d)
"""
print("--- %s seconds ---" % (time.time() - start_time))
