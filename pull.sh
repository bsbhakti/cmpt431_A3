#!/bin/bash
#
#SBATCH --cpus-per-task=8
#SBATCH --time=02:00
#SBATCH --mem=1G
#SBATCH --partition=slow

srun python /home/bsb10/cmpt431_A3/scripts/page_rank_tester.pyc --execPath=/home/bsb10/Downloads/cmpt431_A3/page_rank_pull_parallel --scriptPath=/home/bsb10/Downloads/cmpt431_A3/scripts/page_rank_evaluator.pyc --inputPath=/home/bsb10/Downloads/cmpt431_A3/input_graphs/roadNet-CA