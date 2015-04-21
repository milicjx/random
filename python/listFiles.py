import os

__author__ = 'milicjx'

# specify directory path
path = '/Users/username/Downloads'

listing = os.listdir(path)

for infile in listing:
    # ignore hidden files on *nix platforms
    if not infile.startswith('.'):
        print 'looping through ' + infile
