#!/bin/bash
#SBATCH -n 1
#SBATCH -t 01:00
#SBATCH -o {{slurm_output}}
#SBATCH -e {{slurm_output}}.err

/home/SHARED/software/biokepler-1.2/kepler.sh -runwf -nogui -redirectgui $HOME -i {{i}} -j {{j}} workflows/demo/DemoWorkflow.xml 
