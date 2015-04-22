#!/usr/bin/env python3
import os

def split_file(filepath, lines=300): # specify number of lines per file
    path, filename = os.path.split(filepath)
    # filename.split('.') would not work for filenames with more than one .
    basename, ext = os.path.splitext(filename)
    # open input file
    with open(filepath, 'r') as f_in:
        try:
            # open the first output file
            f_out = open(os.path.join(path, '{}_{}{}'.format(basename, 0, ext)), 'w')
            # loop over all lines in the input file, and number them
            for i, line in enumerate(f_in):
                # every time the current line number can be divided by the
                # wanted number of lines, close the output file and open a
                # new one
                if i % lines == 0:
                    f_out.close()
                    f_out = open(os.path.join(path, '{}_{}{}'.format(basename, i, ext)), 'w')
                # write the line to the output file
                f_out.write(line)
        finally:
            f_out.close()
            
if __name__ == '__main__':
    with open('split_file.txt', 'w') as f:
        for x in range(950): # the last line to split
            f.write('{}\n'.format(x))
    split_file('file_to_split.txt')
