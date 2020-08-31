#!/usr/bin/env python3.8
import sys
import json
import argparse
from difflib import SequenceMatcher

scores = {}

def sim(line_no,line_data,data,scores):
    '''
    Analyze data
    '''
    m_key = max(scores, key = int)
    scores[line_no+1] = {}
    print(line_no)
    print(m_key+1)
    line_data = line_data.replace('\n','')
    for c,l in enumerate(data):
        l = l.replace('\n','')
        ratio = SequenceMatcher(None,l,line_data).ratio()
        scores[line_no+1][c+1] = ratio

if __name__ == '__main__':


    parser = argparse.ArgumentParser(description = 'Find text familiarity.')

    parser.add_argument('--file',
                        action = 'store',
                        required = True,
                        help = 'Input file.')

    args = parser.parse_args()

    with open(args.file) as f:
        data = f.readlines()

    # Process data
    for line_no,line_data in enumerate(data):
        scores[line_no+1] = {}
        sim(line_no=line_no,line_data=line_data,data=data,scores=scores)
    print(json.dumps(scores))
