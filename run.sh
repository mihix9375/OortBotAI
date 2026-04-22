#!/bin/bash

export OMP_NUM_THREADS=3
export TF_NUM_INTRAOP_THREADS=3
export TF_NUM_INTEROP_THREADS=3

taskset -c 1,2,3 python3 main.py
