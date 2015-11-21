import csv
import argparse

doc = "How to use : read.py [startPhrase], [endPhrase], [printWhenPhrase], [filename]"
epi = "Thanks, gsedubun(at)gmail.com"
p = argparse.ArgumentParser(description=doc,epilog=epi, formatter_class=argparse.RawDescriptionHelpFormatter)
p.add_argument('startPhrase', help="strting phrase to start checking")
p.add_argument('endPhrase', help="ending phrase to end writing")
p.add_argument('printWhenPhrase', help="designated phrase to start writing")
p.add_argument('filename', help="name of the .txt file.")
p.parse_args()

from sys import argv
script, startPhrase, endPhrase, printWhen, filename = argv
#script, phrase, filename = argv

print("open file : %r" % filename)
print("Check %r in file %r, stop when %r, look for lines with %r phrase.\n\n" % (startPhrase, filename, endPhrase, printWhen))
txt = open(filename,'r')

i = 0
read = txt.read().splitlines()

for r in read:
    if startPhrase in r:
        if i < len(read):
            #print(i)
            a=i
            while True:
                if a > (i+8):
                    break
                if printWhen in read[a]:
                    print(read[a])
                if endPhrase in read[a]:
                    break
                #print(read[a])
                a=a+1
    i=i+1


