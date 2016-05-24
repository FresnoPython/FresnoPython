#!/usr/bin/env python

import argparse
import FresnoPython


def main(args):
    if args.website:
        FresnoPython.open_website()

    if args.map:
        FresnoPython.open_map()

    if args.twitter:
        FresnoPython.open_twitter()

    print(FresnoPython.message())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--website', action='store_true', help='Open the website.')
    parser.add_argument('--map', action='store_true', help='Open the location on Google Maps.')
    parser.add_argument('--twitter', action='store_true', help='Open the twitter account.')
    args = parser.parse_args()
    main(args)
