#!/bin/sh
##
## This file reinitializes some variables in the FAST model, because
## if OpenFOAM restarts from a previous timestep FAST should also
## reinitialize using previous time values
##


## The files to modify
cd ..
fileFAST_MAIN=$PWD/primary.fst
fileFAST_FOAM=$PWD/constant/turbineArrayProperties
cd -


## Find the name of last time directory where OpenFOAM and FAST stopped
## these are the most recently modified files
lastTimeFAST=$(ls -t ./../turbineOutput/ | head -n 1)
lastTimeFOAM=$(ls -t ./../processor0/ | head -n 1)


## now find the lastTime directory of the FAST output files
## (note: the rotorSpeed and azimuth files share same format)
#lastDirFAST=$(realpath ./../turbineOutput/$lastTimeFAST/)
lastDirFAST=(./../turbineOutput/$lastTimeFAST)


## now read the columns for Time and Azimuth
timesFAST=$(awk '{print $2}' $lastDirFAST/azimuth)
azimuth=$(awk '{print $4}' $lastDirFAST/azimuth)
## convert to list so we can refer to elements using index
timesFAST=($timesFAST)
azimuth=($azimuth)


## find the index of matching element in list
for ((i=0; i < ${#timesFAST[@]}; ++i)); do
    if [ ${timesFAST[$i]} ==  $lastTimeFOAM ]; then
        index=$i
    fi
done


## define the new intital conditions to restart with
init_azimuth=${azimuth[$index]}

## Read the last known blade azimuth, and overwite to FAST input file
./overwrite-line.sh 72 "$init_azimuth    Azimuth     - Initial azimuth angle for blade 1 (degrees), using Azimuth from previous OpenFOAM timestep of t = $lastTimeFOAM" $fileFAST_MAIN > $fileFAST_MAIN.replace
mv $fileFAST_MAIN.replace $fileFAST_MAIN


## also need to overwrite in the file constant/turbineArrayProperties
## need to search for the line (or multiple lines for each turbine) containing the "Azimuth" keyword
## find the line number where azimuth is initialized (this returns all line numbers)
lineNumbers=$(grep -n 'Azimuth' $fileFAST_FOAM)


## only read the numbers, the first words separate by
lines=$(echo "${lineNumbers[@]}" | awk -F":" '{print $1}')
## convert to list so we can refer to elements using index
lines=($lines)


## replace the line number within each turbine's dictionary
for ((i=0; i < ${#lines[@]}; ++i)); do

    ./overwrite-line.sh ${lines[$i]} "    Azimuth        $init_azimuth;         // Initial azimuth angle for blade 1 (degrees), using Azimuth from previous OpenFOAM timestep of t = $lastTimeFOAM" $fileFAST_FOAM > $fileFAST_FOAM.replace
    
    mv $fileFAST_FOAM.replace $fileFAST_FOAM
done

