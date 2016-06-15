# HashCheck
Calculates file hashes using several hashing algorithms

#### Dependencies
Python 2.7

#### How to run
Double click HashCheck.py to calculate the md5 hash for every file in the current directory of the script

Further algorithms and options can be selected if run from the command line.
Type `HashCheck.py -h` on the command line for more information

#### Ideas for possible future features
* Verbose mode (time it takes to hash each file, number of files to hash, directory, etc)
* Feeding file a chunk at a time, instead of loading it as a whole to memory
* Option for providing input hash and checking wether the calculated hash is the same
* Create separate script to add option to context menu (windows) to launch script (run to add to registry, run again to remove)
