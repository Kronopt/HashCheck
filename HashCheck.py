#!python2
# coding: utf-8

"""
HASH CHECK
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
"""

import argparse
import hashlib
import os

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.6'
__date__ = '03:09h, 20/02/2017'
__status__ = 'Production'


def main(hash_algorithm, directory):
    """
    Runs the hash_check function for every file in a directory or for a single file
    Checks whether 'directory' is really a directory or just a file

    PARAMETERS:
        hash_algorithm : str
            Represents a hashing algorithm
        directory : str
            Represents a file path or a directory (using forward slashes: /)

    REQUIRES:
        Hashing algorithm available in the hashlib library

    ENSURES:
        Hash of 'directory' using 'hash_algorithm' if it's a file or hash of every file in
        the directory if it's a directory
    """
    # Apart from the default directory, all other directories (inputted by user) must have forward slashes
    if "\\" in directory and directory != os.getcwd():
        print "Please use forward slashes ('/') on your file/directory path"

    else:
        directory = os.path.normpath(directory)  # Regularizes path slashes

        # Handles directories
        if os.path.isdir(directory):
            files_to_hash = filter(lambda file_path: os.path.isfile(os.path.join(directory, file_path)),
                                   os.listdir(directory))
            files_to_hash.sort()

            for i in files_to_hash:
                print hash_algorithm, "hash for '" + i + "': " + hash_check(hash_algorithm, os.path.join(directory, i))

        # Handles single files
        elif os.path.isfile(directory):
            hash_check(hash_algorithm, directory)
            # only prints the actual file name, not the whole path
            print hash_algorithm, "hash for '" + os.path.split(directory)[1] + "': " \
                                  + hash_check(hash_algorithm, directory)

        else:
            print "'" + directory + "' does not exist..."

    raw_input("\nPress Enter to exit...")


def hash_check(hash_algorithm, file_name):
    """
    Main function
    Calculates hash of file_name using the hashing algorithm specified in hash_algorithm

    PARAMETERS:
        hash_algorithm : str
            Represents a hashing algorithm
        file_name : str
            Represents a file path

    REQUIRES:
        - Hashing algorithm available in the hashlib library
        - Existing file file_name

    ENSURES:
        Hash of file_name using hash_algorithm
    """

    with open(file_name, 'rb') as file_to_check:
        # defaults to md5
        hash_output = getattr(hashlib, hash_algorithm, 'md5')()

        for line in file_to_check:
            hash_output.update(line)

        return hash_output.hexdigest()


if __name__ == '__main__':
    # Default = -hash md5 -file os.getcwd()
    parser = argparse.ArgumentParser(description='Multiple hash algorithm check tool')

    parser.add_argument('-hash', choices=hashlib.algorithms, default='md5',
                        help='Available hash algorithms (chose one)')
    parser.add_argument('-file', nargs='?', const=os.getcwd(), default=os.getcwd(),
                        metavar='dir', help='Directory or file path, using forward slashes (/)')

    parser = parser.parse_args()

    main(parser.hash, parser.file)
