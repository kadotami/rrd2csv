# rrd2csv

## About 

This is cheap convert script for rrd file to csv.

## Requirements

* rrdtool

```
# installation
pip install rrdtool
```

## Usage

python rrd2csv.py file_path consolidation_function(cf)

cf: 'AVERAGE' or 'MIN' or 'MAX' or 'ALL'

### convert single file

```
python rrd2csv.py sample.rrd AVERAGE

# output is sample_average.csv
```

### convert all files in a directory

```
python rrd2csv.py /path/to/dir AVERAGE

# output is /path/to/dir/csv/average/**.csv
```

