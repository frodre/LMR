#!/bin/bash
#SBATCH --time=72:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --job-name=LMR
#SBATCH --mail-user=fengzhu@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --mem=30000

python -u LMR_wrapper.py config_cesm_linear_850-2005.yml &> test_cesm_linear_850-2005.log
