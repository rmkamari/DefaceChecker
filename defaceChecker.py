import urllib
import os
print '|-----------------------------------------------------------------------------|'
print '|-----------------------------[Deface Scanner Tool]---------------------------|'
print '|----------------------------[Coded By EXPLOITER~XED]-------------------------|'
print '|------------------------------[fb.com/wax.vampire]---------------------------|'
print '|HELP: make a text file that must contain urls starting with http://          |'
print '|in same folder. Then type the text file name below and hit enter and         |'
print '|wait for automated processes to complete the tasks.If program does not       |'
print '|response for very long time, then try closing program and restart again.     |'
print '|-----------------------------------[CODE_MAP]--------------------------------|'
print '|[#] defaced.txt = list containing defaced sites                              |'
print '|[#] error.txt = list containing not defaced sites                            |'
print '|[#] failed.txt = list containing unable to reach sites                       |'
print '|[*] Include \'Hacked\' or \'hacked\' in your deface page to match urls       |'
print '|-----------------------------------------------------------------------------|'
file_to_save = open('defaced.txt', 'w')
file_to_save.close()
file_to_save2 = open('error.txt', 'w')
file_to_save2.close()
file_to_save3 = open('failed.txt', 'w')
file_to_save3.close()
file_to_open = raw_input('Enter your file name to import(ex. list.txt):\n> ')
print 'SYSTEM: Automated scan is running ...'
print 'SYSTEM: A list of defaced,not defaced, invalid domain will open soon ...'
dic = {}
key = 1
try:
    with open(file_to_open) as fp:
        for vv in fp:
            dic[key] = vv
            key += 1
except IOError:
    print 'ERROR: Invalid file!Please Recheck!'
    input('Press enter to exit ...\n> ')
try:
    with open(file_to_open) as fp:
        for keys in dic:
                ofile = urllib.urlopen(dic[keys]).read()
                if 'Hacked' in ofile:
                    print 'SYSTEM:', dic[keys], 'scanned = OK'
                    file_open = open('defaced.txt', 'a')
                    file_open.write(dic[keys])
                    file_open.close()
                elif 'hacked' in ofile:
                    print 'SYSTEM:', dic[keys], 'scanned = OK'
                    file_open = open('defaced.txt', 'a')
                    file_open.write(dic[keys])
                    file_open.close()
                else:
                    print 'SYSTEM:', dic[keys], 'scanned = ERROR'
                    file_open = open('error.txt', 'a')
                    file_open.write(dic[keys])
                    file_open.close()
except IOError:
    dic1 = {}
    key1 = 1
    with open('defaced.txt') as nf:
        for nfk in nf:
            dic1[key1] = nfk
            key1 += 1
        for key in dic:
            for key1 in dic1:
                if dic[key] not in dic1[key1]:
                    print 'SYSTEM:', dic[key], 'scanned = HOST ERROR'
                    review = open('failed.txt', 'a')
                    review.write(dic[key])
                else:
                    continue
    print '[*] SYSTEM: Possible ERRORS Detected:'
    print '> ERROR: Check your internet connection!(or make sure you entered http:// before each lines)'
    print '> ERROR: One or more domains seems unreachable!'
    try:
        input('Press enter to exit ...')
    except SyntaxError:
        pass
print 'Done!Opening file ...'
os.startfile('defaced.txt')
os.startfile('error.txt')
os.startfile('failed.txt')
