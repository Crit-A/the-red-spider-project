#!/usr/bin/python

# Copyright 2012 Neil Forrester
# Licensed under the Red Spider Project License.
# See the License.txt that shipped with your copy of this software for details.

import os
import sys

def set_red_spider_root():
	os.putenv('RED_SPIDER_ROOT', os.path.split(os.path.abspath(os.path.dirname(sys.argv[0])))[0])

if __name__ == "__main__":
	set_red_spider_root()
	os.system(" ".join(sys.argv[1:]))
