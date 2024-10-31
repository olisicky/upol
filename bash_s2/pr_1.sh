#!/bin/bash

eval_path=(".* *")    # include hidden files
hidden=false

while getopts ":a" opt; do
    case ${opt} in
        a) hidden=true ;;
        *) echo "neznama volba ${opt}" ;; esac
done

# handle arguments
shift $((OPTIND - 1))

if [ $# -gt 0 ] && [ -d "$@" ]; then
    eval_path=("$@"/.* "$@"/*)

elif [ $# -gt 0 ] && [ ! -d "$@" ]; then
    echo "The directory ${@} does not exist."
    exit 11
fi

for dir in ${eval_path[@]}
do
    # without -x for linux
    # get relevant data using stat
    fname=$(stat "${dir}" | awk 'NR==1{print $2; exit}')    
    ftype=$(stat "${dir}" | awk 'NR==2{print $8 "        "$9; exit}')
    symlink=$(stat "${dir}" | awk 'NR==1{print $3$4; exit}')
    prava=$(stat "${dir}" | awk 'NR==4{print $2; exit}')
	
    file_name=$(basename "$fname")
    if [[ -d "${dir}" || -f "${dir}" ]] && [[ "${file_name}" == .* ]]; then
	if $hidden; then
	    echo ${fname} ${symlink} ${ftype} ${prava} 
        else
            continue
        fi
    else
        echo ${fname} ${symlink} ${ftype} ${prava} 
    fi
done
