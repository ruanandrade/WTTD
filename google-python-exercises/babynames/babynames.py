#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from csv import excel

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    extracted = []

    # Extract the year
    pattern = re.compile("Popularity in \d{4}")
    year = ""
    for line in open(filename):
        for match in re.finditer(pattern, line):
            print(match.group())
            year = match.group()

    extracted.append(year.split(" ")[2])

    # Extract the names
    pattern = re.compile("<td>\d*</td><td>[a-zA-Z]*</td><td>[a-zA-Z]*</td>")
    for line in open(filename):
        for match in re.finditer(pattern, line):
            current_names = match.group()
            splited_names = re.split("(<td>|</td>)", current_names)
            extracted.append(splited_names[6]+" "+splited_names[2])
            extracted.append(splited_names[10] + " " + splited_names[2])

    return sorted(extracted)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
        for file in args:
            extracted = extract_names(file)
            print(extracted)
            test(len(extracted), 2001)

        # For each filename, get the names, then either print the text output
        # or write it to a summary file

if __name__ == '__main__':
    main()
