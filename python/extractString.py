import os

__author__ = 'milicjx'

select = raw_input('Single-File (s) or Multi-File Extract (m)? ')

if (select == "m") or (select == "M"):

    # specify path to input file
    dirIn = raw_input('Input Directory Path: ')
    # specify path to output file
    dirOut = raw_input ('Output FIle Path: ')
    
    # specify beginning string
    strBeg = raw_input('Begin String: ')
    # specify ending string
    strEnd = raw_input('End String: ')
    
    directory = os.listdir(dirIn)
    
    for infile in directory:
        # ignore hidden files on *nix platforms
        if not infile.startswith('.'):
            print 'looping through ' + infile
            
elif (select == 's') or (select == 'S'):
    docIn = raw_input('Input File Path: ')
    docOut = raw_input('Output File Path: ')
    
    strBeg = raw_input('Begin String: ')
    strEnd = raw_input('End String: ')
    
    inFile = open(docIn)
    outFile = open(docOut, "w")
    
    copyDataSet = False
    
    for line in inFile:
        if line.startswith(strEnd):
            copyDataSet = False
            
        if copyDataSet:
            outFile.write(line)
            
        if line.startswith(strBeg):
            copyDataSet = True
            
    inFile.close()
    outFile.close()
    
else:
    print 'This option does not exist...'

#inFile = open("prod_server_name_audit.out")
#outFile = open("etc_sudoers/orod_server_name_audit_sudoers.out", "w")
#copyDataSet = False
#for line in inFile:
#    if line.startswith("</Checking /etc/sudoers>"):
#        copyDataSet = False
#    if copyDataSet:
#        outFile.write(line)
#    if line.startswith("<Checking /etc/sudoers>"):
#        copyDataSet = True
#inFile.close()
#outFile.close()
