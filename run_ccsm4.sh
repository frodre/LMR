#!/bin/bash
#SBATCH --time=72:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --job-name=LMR
#SBATCH --mail-user=fengzhu@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --mem=30000
#SBATCH --nodelist=hungus

python -u LMR_wrapper.py config_ccsm4_bilinear_0-2000.yml &> test_ccsm4_bilinear_0-2000.log
