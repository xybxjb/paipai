

s = '\xe4\xb8\x80\xe5\x8f\xb7\xe8\x81\x94\xe7\x9b\x9f'
ss = s.encode('raw_unicode_escape')
print(ss)  
sss = ss.decode()    
print(sss)   
