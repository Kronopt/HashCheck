#!/usr/bin/env python
# coding: utf-8

'''
HASHCHECK

TO DO DESCRIPTION

TO DO DEPENDENCIES
TO DO HOW TO RUN
TO DO REQUIRES
TO DO ENSURES
'''

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.2'
__date__ = '02:00h, 25/05/2016'
__status__ = 'Production'

# Feeding file a chunk at a time, instead of loading it as a whole to memory
# When Hashing every file on the same directory, ask ipermission to proceed with hash if multiple "not dir" files exist
# Allow multithreading
# Allow to compare an input hash (returns true or false if hash is the same or not)
# Allow relative path of files (relative to current directory)


def hashCheck(hashAlgorithm, fileName):
    """
    """
    
    with open(fileName, 'rb') as fileToCheck:
        # defaults to md5
	hashOutput = getattr(hashlib, hashAlgorithm, 'md5')(fileToCheck.read()).hexdigest()

	# only prints the actual file name, not the whole path
	# The "\" might fail on non windows operating systems...
	print hashAlgorithm, "hash for '" + os.path.split(fileName.rstrip('\\'))[1] + "': " + hashOutput


def multipleHashCheck(hashAlgorithm, directory):
    """
    """

    # only allows full paths... yet
    if os.path.exists(directory):
        if os.path.isdir(directory):
            os.chdir(directory)

            filesToHash = filter(os.path.isfile, os.listdir(directory))
            filesToHash.sort()

            for i in filesToHash:
                hashCheck(hashAlgorithm, i)

        elif os.path.isfile(directory):
            hashCheck(hashAlgorithm, directory)

        raw_input()
            
    else:
        print "'" + directory + "' does not exist..."


if __name__ == '__main__':
    import argparse
    import hashlib
    import os

    # Default = -hash md5 -file os.getcwd()
    parser = argparse.ArgumentParser(description = 'Multiple hash algorithm check tool')

    parser.add_argument('-hash', choices = hashlib.algorithms, default = 'md5',
                        help = 'Available hash algorithms (chose one)')
    parser.add_argument('-file', nargs ='?', const= os.getcwd(), default = os.getcwd(),
                        metavar = 'dir', help = 'Directory or file path')

    parser = parser.parse_args()
    
    multipleHashCheck(parser.hash, parser.file)
