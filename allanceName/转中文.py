

s = '\xe9\xb8\xbf\xe8\x92\x99\xe5\x8c\x97\xe7\x9b\x9f'
ss = s.encode('raw_unicode_escape')
print(ss)  
sss = ss.decode()    
print(sss)   
