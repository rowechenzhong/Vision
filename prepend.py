import fileinput
import sys

"""
This code is used to add a prefix to each line of a file.
"""

# get the prefix from preamble.sty
prefix = ''
with open('preamble.sty', 'r') as f:
    prefix = f.read()
print(prefix[:100])
prefix = "$\n" + prefix + "\n$\n"


for line in fileinput.input(['./ampo.txt'], inplace=True):
    sys.stdout.write('EDF {l}'.format(l=line))
