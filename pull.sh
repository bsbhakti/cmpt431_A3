#!/bin/bash
#
#SBATCH --cpus-per-task=8
#SBATCH --time=10:00
#SBATCH --mem=5G
#SBATCH --partition=slow

srun python /home/bsb10/Downloads/scripts/page_rank_tester.pyc --execPath=/home/bsb10/Downloads/ --scriptPath=/home/bsb10/Downloads/scripts/page_rank_evaluator.pyc --inputPath=/home/bsb10/Downloads/input_graphs/