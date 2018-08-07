import rrdtool
import argparse
import time

def rrd_fetch(file, cf):
    first = str(rrdtool.first(file))
    last = str(rrdtool.last(file))
    return rrdtool.fetch(file, cf, "-s", first, "-e", last)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file path")
    parser.add_argument("cf", help="'AVERAGE' or 'MIN' or 'MAX'")
    args = parser.parse_args()

    result = rrd_fetch(args.file, args.cf)
    times = range(result[0][0],result[0][1],result[0][2])
    head = "time"
    for val in result[1]:
        head = head + ", " + val
    
    print(head)

    for i, time in enumerate(times):
        row = time
        for val in result[2][i]:
            row = str(row) + ", " + str(val)
        print(row)
        
        
        
