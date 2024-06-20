To download the contents of the repository - gitclone https://github.com/rahul-dethe/ann_software.git
To set-up the enviroment open "Parallel ANN-CI Installation Guide.pdf" and follow the steps.
1) codempi_01 - If dependencies and required packages are aleready installed in your conda environment, activate it, create your input and bond file in this directory and run the software.
2) environment_setup - It contains the files and steps for installation and setup of the conda environment.
3) test_inputs - It contains test input files.
4) ann_run_check - To check if the software is running smoothly. Activate the appropriate conda environment and run the software. Use this command
   " mpirun -np 48 python exe.py input_chain14_singlet.in "
