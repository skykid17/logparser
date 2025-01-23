#!/usr/bin/env python

import sys
sys.path.append('C:/Users/georgelai/Documents/GItHub/logparser')

from logparser.NuLog.NuLog_George import LogParser

input_dir = './data/test_log/'
output_dir = 'demo_result/' 
log_file = 'nxlog.log'
log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'  # HDFS log format
# Regular expression list for optional preprocessing (default: [])
regex = [
    r'blk_(|-)[0-9]+' , # block id
    r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', # IP
    r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', # Numbers
]
filters = r"(\s+blk_)|(:)|(\s)"
k = 15
nr_epochs = 1 # Number of epochs to run
num_samples = 0

parser = LogParser(log_format=log_format, indir=input_dir, outdir=output_dir, filters=filters, k=k)
parser.load_data()
