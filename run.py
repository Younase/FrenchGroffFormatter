# -*- coding: utf-8 -*-
source=open('source.txt',encoding='utf-8')
drain=open('res.txt', 'w')
i=0
d={'’':'\'','é':"\\'e",'à':'\`a','è':"\`e",'ù':'\`u','ç':'\c c','â':"\^a",'ê':"\^e",'î':"\^i",'ô':"\^o",'û':"\^u",'ë':"\:e",'ï':"\:i",'ü':"\:u"
    ,'À':'\`A', 'É':"\\'E", 'È':'\`E','Ç':'\c C','’':'\'','‘':'\''}
l=d.keys()
c=""
for e in source.read():
    if e in l:
        c+=d[e]
    else:
        c+=e
    i+=1

drain.write(c)
source.close()
drain.close() 