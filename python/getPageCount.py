import re
import os
import glob

__author__ = 'milicjx'

countpage = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE | re.DOTALL)

def count_pages(filename):
    data = file(filename, "rb").read()
    return len(countpage.findall(data))

if __name__ == "__main__":
    parent = "/Users/username/Desktop"
    
    #for infile in glob.glob(os.path.basename('*.pdf')):
    
    # replace * extension with pdf, txt, docx, etc.
    for infile in glob.glob(os.path.join(parent, '*.*')):
        page_count = str(count_pages(infile))
        # \t specifies tab space
        print "".join([infile, "\t", page_count])
