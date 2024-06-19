To download the contents of the repository - gitclone https://github.com/rahul-dethe/ann_software.git

1) To set-up the enviroment open "Parallel ANN-CI Installation Guide.pdf" and follow the steps.
2) codempi_01 - If dependencies and required packages are aleready installed in your conda environment, create your input and bond file in this directory and run the software.
3) environment_setup - It contains the files and steps for installation and setup of the conda environment.
4) test_inputs - It contains test inputs.
5) ann_run_check - To check if the software is running smoothly. Activate the appropriate conda environment and run the software by using command
   " mpirun -np 48 python exe.py input_chain14_singlet.in "
