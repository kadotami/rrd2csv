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

def write_file_path(file, cf, path=''):
    write_file_name = ('.').join(file.split('.')[:-1]) + '_' + cf + '.csv' 
    if path != '':
        write_file_name = path + '/csv/' + write_file_name.split(path)[1]
    write_file_name = write_file_name.replace('//', '/')
    return  write_file_name

def convert_single_file(rrd_file, cf, write_file):
    rrd_data = rrd_fetch(rrd_file, cf)
    first, end, step = rrd_data[0]
    times = range(first, end, step)
    lines = ["time, " + ', '.join(rrd_data[1])]

    for i, time in enumerate(times):
        lines.append(str(time)+ ', '  +  ', '.join(tuple(map(str, rrd_data[2][i]))))
        
    with open(write_file, mode='w') as f:
        for line in lines:
            f.write('%s\n' % line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="file or directory path")
    parser.add_argument("cf", help="'AVERAGE' or 'MIN' or 'MAX' or 'ALL'. ALL is 3 types ('AVERAGE' and 'MIN' and 'MAX')")
    args = parser.parse_args()
    path = args.path
    cf = args.cf

    if(os.path.isdir(path)):
        os.mkdir((path + '/csv').replace('//','/'))
        files = glob.glob(path + "/**/*.rrd", recursive=True)
        for file in files:
            write_file = write_file_path(file, cf, path)
            convert_single_file(file, cf, write_file)
    else:
        write_file = write_file_path(path, cf)
        convert_single_file(path, cf, write_file)
