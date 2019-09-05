#!/usr/bin/env bash

#SBATCH -o hostname_%j.out
#SBATCH -t 01:00:02
#SBATCH -p ariel
#SBATCH -N 1

srun ./matrix_matrix_single_file 4 4 4 4 2  -t15 --hpx:print-counter=/threads{locality#*/total}/count/cumulative

