#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import shutil
import zipfile

def copy_file_todir(src, dest):
    for file in src:
        shutil.copy2(file, dest)

def copy_file_tozip(src, dest):
    zipf = zipfile.ZipFile(dest + 'special.zip', 'w')
    for file in src:
        zipf.write(file)
    zipf.close()

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    if(len(todir) > 0):
        copy_file_todir(args, todir)

    if(len(tozip) > 0):
        copy_file_tozip(args, tozip)

if __name__ == "__main__":
    main()
