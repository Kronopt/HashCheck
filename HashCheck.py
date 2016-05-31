#!/usr/bin/env python
# coding: utf-8

'''
HASHCHECK

Calculates file hashes (single file or entire directories) using different hashing algorithms

DEPENDENCIES:
    - Python 2.7
    ### - WINDOWS

HOW TO RUN:
    - Directly, by double clicking the script.
      Calculates md5 hashes for every file available in the current directory
      
    - Through the command line.
      Allows for the hashing of single files or other specific directories;
      Allows the selection of the hashing algorithm;
      For more help, call the script with the -h parameter
'''

import argparse
import hashlib
import os

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.3'
__date__ = '18:53h, 31/05/2016'
__status__ = 'Production'




# Verbose mode (time it takes to hash, number of files to hash, etc)
# Feeding file a chunk at a time, instead of loading it as a whole to memory
# Allow multithreading
# Allow to compare an input hash (returns true or false if hash is the same or not)
# Allow relative path of files (relative to current directory)




def main(hashAlgorithm, directory):
    '''
    Runs the hashCheck function for every file in a directory or for a single file
    Checks wether 'directory' exists and if it's really a directory or just a file

    
    hashAlgorithm: str, representing a hashing algorithm
    directory: str, representing a file path or a directory

    REQUIRES:
        Hashing algorithm available in the hashlib library
    
    ENSURES:
        Hash of 'directory' using 'hashAlgorithm' if it's a file or hash of every file in
        the directory if it's a directory
    '''

    # only allows full paths... yet
    if os.path.exists(directory):
        if os.path.isdir(directory):
            os.chdir(directory)

            filesToHash = filter(os.path.isfile, os.listdir(directory))
            filesToHash.sort()

            for i in filesToHash:
                print hashAlgorithm, "hash for '" + i + "': " + hashCheck(hashAlgorithm, i)
                
        elif os.path.isfile(directory):
            hashCheck(hashAlgorithm, directory)
            # only prints the actual file name, not the whole path
            print hashAlgorithm, "hash for '" + os.path.split(directory)[1] + "': " + \
                  hashCheck(hashAlgorithm, directory)

        raw_input()
            
    else:
        print "'" + directory + "' does not exist..."

def hashCheck(hashAlgorithm, fileName):
    '''
    Main function
    Calculates the hash of 'fileName' using the hashing algorithm specified in 'hashAlgorithm'


    hashAlgorithm: str, representing a hashing algorithm
    fileName: str, representing a file path
    
    REQUIRES:
        - Hashing algorithm available in the hashlib library
        - Existing file 'fileName'
    
    ENSURES:
        Hash of 'fileName' using 'hashAlgorithm'
    '''
    
    with open(fileName, 'rb') as fileToCheck:
        # defaults to md5
        hashOutput = getattr(hashlib, hashAlgorithm, 'md5')(fileToCheck.read()).hexdigest()

        return hashOutput

if __name__ == '__main__':
    # Default = -hash md5 -file os.getcwd()
    parser = argparse.ArgumentParser(description = 'Multiple hash algorithm check tool')

    parser.add_argument('-hash', choices = hashlib.algorithms, default = 'md5',
                        help = 'Available hash algorithms (chose one)')
    parser.add_argument('-file', nargs ='?', const= os.getcwd(), default = os.getcwd(),
                        metavar = 'dir', help = 'Directory or file path')

    parser = parser.parse_args()
    
    main(parser.hash, parser.file)
