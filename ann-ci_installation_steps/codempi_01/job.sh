#!/bin/bash
#SBATCH --job-name=ann-ci
##SBATCH --exclusive
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=48
#SBATCH --partition=debug
#SBATCH --time=02:00:00
#SBATCH --output=%j.out
#SBATCH --error=%j.err


source /home/miniconda3/bin/activate
conda activate ann-ci
cd $SLURM_SUBMIT_DIR
#mpirun --hosts cn087,cn088 -np 96 python exe.py input_chain14_singlet.in
mpirun -np 96 python exe.py input_chain14_singlet.in
