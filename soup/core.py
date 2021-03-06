#!/usr/bin/env python

import argparse
import os
import bs4
import re

# TODO Implement optional output format as JSON
# TODO Show the children of the children with the option --values


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


def read_file(filename):
    with open(filename) as f:
        if args.ignore_case:
            content = lower_case_all_tags(f.read())
        else:
            content = f.read()
    return content


parser = argparse.ArgumentParser()
parser.add_argument('tagname', help='The name of the tag')
parser.add_argument('filename', help='The XML file', nargs='+')
parser.add_argument('--ignore-case', '-i',
                    help='Ignore the case of the tags in the XML FILE',
                    action='store_true')
parser.add_argument('--children', '-c',
                    help='List all the children in the tag',
                    action='store_true')
parser.add_argument('--values', '-V',
                    help='Add the values of the children with the --children option',
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

        soup = bs4.BeautifulSoup(read_file(filename), 'xml')

        # The children of the tag
        if args.children:
            element = soup.find(args.tagname)
            if args.values:
                print('\n'.join(': '.join(( x.name, x.text )) for x in element.children if x.name))
            else:
                print('\n'.join(x.name for x in element.children if x.name))

        # All the occurrences
        else:
            print(show(soup.find_all(args.tagname.split(','))))
