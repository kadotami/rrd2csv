import rrdtool
import argparse
import time

def rrd_fetch(file, cf):
    first = str(rrdtool.first(file))
    last = str(rrdtool.last(file))
    return rrdtool.fetch(file, cf, "-s", first, "-e", last)

def convert_single_file(file, cf):
    rrd_data = rrd_fetch(args.file, args.cf)
    first, end, step = rrd_data[0]
    times = range(first, end, step)
    head = "time, " + ', '.join(rrd_data[1])    
    print(head)

    for i, time in enumerate(times):
        row = str(time)+ ', '  +  ', '.join(tuple(map(str, rrd_data[2][i])))
        print(row)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file path")
    parser.add_argument("cf", help="'AVERAGE' or 'MIN' or 'MAX'")
    args = parser.parse_args()

    convert_single_file(args.file, args.cf)
