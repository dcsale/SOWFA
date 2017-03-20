#!/bin/bash

## --------------------------------------------------------
## NOTE: to submit jobs to Hyak use
##       qsub <script.sh>
##
## #PBS is a directive requesting job scheduling resources
## and ALL PBS directives must be at the top of the script, 
## standard bash commands can follow afterwards. 
## --------------------------------------------------------

## --------------------------------------------------------
## RENAME for your job
## --------------------------------------------------------
#PBS -N stf-ftle


## --------------------------------------------------------
## SPECIFY the working directory for this job
## --------------------------------------------------------
## PBS -d /gscratch/stf/dsale/OpenFOAM/dsale-2.4.x/fastFlume-branches/fastFlume-Coarse-e1


## --------------------------------------------------------
## GROUP to run under, or run under backfill
## --------------------------------------------------------
## PBS -W group_list=hyak-motley
#PBS -W group_list=hyak-stf
## PBS -q bf


## --------------------------------------------------------
## NUMBER nodes, CPUs per node, and MEMORY
## --------------------------------------------------------
## PBS -l nodes=1:ppn=16,mem=10gb,feature=intel
## PBS -l nodes=2:ppn=16,mem=30gb,feature=intel
## PBS -l nodes=3:ppn=16,mem=50gb,feature=intel
#PBS -l nodes=6:ppn=16,mem=300gb,feature=intel
## PBS -l nodes=8:ppn=16,mem=32gb,feature=intel
## PBS -l nodes=16:ppn=16,mem=32gb,feature=intel


## --------------------------------------------------------
## WALLTIME (defaults to 1 hour, always specify for longer jobs)
## --------------------------------------------------------
#PBS -l walltime=4:05:00


## --------------------------------------------------------
## LOG the (stderr and stdout) job output in the directory
## --------------------------------------------------------
#PBS -j oe -o /gscratch/motley/dsale/job_logs
## PBS -j oe -o /gscratch/stf/dsale/job_output/logs


## --------------------------------------------------------
## EMAIL to send when job is aborted, begins, and terminates
## --------------------------------------------------------
## PBS -m abe -M dsale@uw.edu
#PBS -m abe -M sale.danny@gmail.com


## --------------------------------------------------------
## END of PBS commmands ... BASH from here and below
## --------------------------------------------------------

## CHANGE directory to where job was submitted (careful, PBS defaults to user home directory)
cd $PBS_O_WORKDIR

## LOAD the appropriate environment modules and variables
module load icc_15.0.3-impi_5.0.3
source /sw/contrib/OpenFOAM/OpenFOAM-2.4.x/etc/bashrc
#source /sw/contrib/OpenFOAM/OpenFOAM-2.4.x/src/LEMOS-2.4.x/bashrc
#source /sw/contrib/OpenFOAM/OpenFOAM-2.3.x/etc/bashrc
#source /sw/contrib/OpenFOAM/OpenFOAM-2.3.x/src/LEMOS-2.3.x/bashrc


## Some applications (particularly FORTRAN) require a larger 
## than usual data stack size. Uncomment if your job exits unexpectedly
ulimit -s unlimited


## DUBUGGING information (include jobs logs in any help requests)
## Total Number of nodes and processors (cores) to be used by the job
echo "** JOB DEBUGGING INFORMATION  *************************"
HYAK_NNODES=$(uniq $PBS_NODEFILE | wc -l )
HYAK_NPE=$(wc -l < $PBS_NODEFILE)
echo "This job will run on $HYAK_NNODES nodes with $HYAK_NPE total CPU-cores"
echo ""
echo "Node:CPUs Used"
uniq -c $PBS_NODEFILE | awk '{print $2 ":" $1}'
echo ""
echo "ENVIRONMENT VARIABLES"
set
echo "** END DEBUGGING INFORMATION  *************************"
echo ""



## --------------------------------------------------------
## Specify the applications to run here
## -------------------------------------------------------- 

## my script to run all OpenFOAM things
./run.all

## BE CAREFUL about CLEANING, make sure your scripts do not 
## clean the job (delete files) if re-submitting this case to queue
