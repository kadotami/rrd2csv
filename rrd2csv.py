import rrdtool
import argparse
import time
import glob
import os
from pathlib import Path

def rrd_fetch(file, cf):
    first = str(rrdtool.first(file))
    last = str(rrdtool.last(file))
    return rrdtool.fetch(file, cf, "-s", first, "-e", last)

def convert_single_file(file, cf):
    rrd_data = rrd_fetch(file, cf)
    first, end, step = rrd_data[0]
    times = range(first, end, step)
    lines = ["time, " + ', '.join(rrd_data[1])]

    write_file_name = ('.').join(file.split('.')[:-1]) + '_' + cf + '.csv' 

    for i, time in enumerate(times):
        lines.append(str(time)+ ', '  +  ', '.join(tuple(map(str, rrd_data[2][i]))))
        
    with open(write_file_name, mode='w') as f:
        for line in lines:
            f.write('%s\n' % line)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="file or directory path")
    parser.add_argument("cf", help="'AVERAGE' or 'MIN' or 'MAX' or 'ALL'. ALL is 3 types ('AVERAGE' and 'MIN' and 'MAX')")
    args = parser.parse_args()

    if(os.path.isdir(args.path)):
        files = glob.glob(args.path + "/**/*.rrd", recursive=True)
        for file in files:
            print(file)
    else:
        convert_single_file(args.path, args.cf)
