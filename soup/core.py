#!/usr/bin/env python

"""
Extract the values requested from the XML files using BeautifulSoup (bs4)

Example:

- Print the text for the first node ASIN in one file
soup 'ASIN' <file>

- Print the texts for all the nodes ASIN in one file
soup --all 'ASIN' <file>

- Print the texts for multiple nodes in one file
soup --all 'ASIN','created_at' <file>

- Print all the children in a given tag
soup --children ItemAttributes <file>

"""

import argparse
import os
import bs4
import re

# TODO Implement optional output format as JSON

def check_file_existence(filename):
    if not os.path.exists(filename):
        raise ValueError("The file {} doesn't exist".format(filename))


def lower_case_all_tags(s):
    """
    Change all the tags to lower-case
    """
    return re.sub(r'(<.*?>)', lambda pat: pat.group(1).lower(), s,
                  flags=re.IGNORECASE)


def show(result):
    if isinstance(result, list):
        s = '\n'.join(x.text.strip() for x in result if x)
    elif isinstance(result, bs4.element.Tag):
        s = result.text.strip()
    else:
        s = ''
    return s


parser = argparse.ArgumentParser()
parser.add_argument('tagname', help='The name of the tag')
parser.add_argument('filename', help='The XML file', nargs='+')
parser.add_argument('--ignore-case', '-i',
                    help='Ignore the case of the tags in the XML FILE',
                    action='store_true')
parser.add_argument('--all', '-a',
                    help='Take into account all the occurrences in the file',
                    action='store_true')
parser.add_argument('--children', '-c',
                    help='List all the children in the tag',
                    action='store_true')
parser.add_argument('--verbose', '-v',
                    help='Verbose mode',
                    action='store_true')


if __name__ == '__main__':
    args = parser.parse_args()

    for filename in args.filename:
        check_file_existence(filename)
        if args.verbose:
            print('> {}'.format(filename))

        with open(filename) as f:
            if args.ignore_case:
                content = lower_case_all_tags(f.read())
            else:
                content = f.read()

        soup = bs4.BeautifulSoup(content, 'xml')

        if args.all:
            search = soup.find_all
            print(show(search(args.tagname.split(','))))
        elif args.children:
            element =soup.find(args.tagname)
            print('\n'.join(x.name for x in element.children if x.name))
        else:
            search = soup.find
            print(show(search(args.tagname.split(','))))
