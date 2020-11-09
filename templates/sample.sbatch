#!/bin/bash
#SBATCH -n 1
#SBATCH -t 01:00
#SBATCH -o {{slurm_output}}
#SBATCH -e {{slurm_output}}.err

sleep {{t}}
expr {{i}} + {{j}}
