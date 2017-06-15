# Code is more simplified and only defaced urls will be stored.
# use this script if in case you just need the defaced domains only
# check on line 11 and 14 to make sure you changed that to any extra file that you are using(hacked.html).
import urllib
x = open('l.txt', 'r').readlines()
for l in x:
    l = l.replace('\n', '')
    if 'http://' not in l:
        l = 'http://' + l
    try:
        if 'Hacked' in urllib.urlopen(l + '/hacked.html').read():
            print l, 'defaced'
            v = open('def.txt', 'a+')
            v.write(l + '/hacked.html\n')
        else:
            print l, 'not defaced'
    except:
        pass
