#!/usr/bin/env python
# coding: utf-8

'''
HASHCHECK
Calculates file hashes (single file or entire directories) using different hashing algorithms

DEPENDENCIES:
    - Python 2.7

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
__version__ = '0.4'
__date__ = '14:27h, 15/06/2016'
__status__ = 'Production'

def main(hashAlgorithm, directory):
    '''
    Runs the hashCheck function for every file in a directory or for a single file
    Checks whether 'directory' is really a directory or just a file

    PARAMETERS:
        hashAlgorithm : str
            Represents a hashing algorithm
        directory : str
            Represents a file path or a directory

    REQUIRES:
        Hashing algorithm available in the hashlib library
    
    ENSURES:
        Hash of 'directory' using 'hashAlgorithm' if it's a file or hash of every file in
        the directory if it's a directory
    '''

    # Handles directories
    if os.path.isdir(directory):
        filesToHash = filter(os.path.isfile, os.listdir(directory))
        filesToHash.sort()

        for i in filesToHash:
            print hashAlgorithm, "hash for '" + i + "': " + hashCheck(hashAlgorithm, i)

    # Handles single files
    elif os.path.isfile(directory):
        hashCheck(hashAlgorithm, directory)
        # only prints the actual file name, not the whole path
        print hashAlgorithm, "hash for '" + os.path.split(directory)[1] + "': " \
              + hashCheck(hashAlgorithm, directory)
        
    else:
        print "'" + directory + "' does not exist..."

    raw_input()

def hashCheck(hashAlgorithm, fileName):
    '''
    Main function
    Calculates the hash of 'fileName' using the hashing algorithm specified in 'hashAlgorithm'

    PARAMETERS:
        hashAlgorithm : str
            Represents a hashing algorithm
        fileName : str
            Represents a file path
    
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
