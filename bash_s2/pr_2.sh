#! /bin/bash

generate=false
move=false
year_max=2024
year_min=1968
month_max=12
day_max=30

while getopts ":ab" opt; do
    case ${opt} in
        a) generate=true ;;
        b) move=true ;;
        *) echo "neznama volba ${opt}" ;; esac
done

# handle arguments
shift $((OPTIND - 1))

if [ $# -gt 0 ] && [ -d "$@" ] && ! $generate; then
    eval_path="$@/"

elif [ $# -gt 0 ] && [ ! -d "$@" ] && ! $generate; then
    echo "The directory ${@} does not exist."
    exit 11
elif [ $# -gt 0 ] && $generate; then
    echo "-a doesn't take any arguments"
    exit 11
else
    echo "Files will be generated."
fi

if $generate; then
    for ((i=1; i <=1000; i++ ))
    do
        fname=$(printf "foo%04d.txt" ${i})
        day=$(shuf -i 1-${day_max} -n 1)
        month=$(shuf -i 1-${month_max} -n 1)
        year=$(shuf -i ${year_min}-${year_max} -n 1)

        printf "%02d/%02d/%04d" ${day} ${month} ${year} > ${fname}
    done


elif $move; then
    
    files=( ${eval_path}*[0-9][0-9][0-9][0-9]* )

    if [ ${#files[@]} -eq 0 ]; then
        echo "No files *NNNN.txt in the directory."
        exit 11
    else
        for file in ${eval_path}*[0-9][0-9][0-9][0-9]*; do
            y=$(cat ${file} | awk -F "/" '{print $3; exit}')
            m=$(cat ${file} | awk -F "/" '{print $2; exit}')
            d=$(cat ${file} | awk -F "/" '{print $1; exit}')

            mkdir -p ${eval_path}/${y} && cp ${file} ${eval_path}/${y}
            mkdir -p ${eval_path}/${y}/${m} && cp ${file} ${eval_path}/${y}/${m}
            mkdir -p ${eval_path}/${y}/${m}/${d} && cp ${file} ${eval_path}/${y}/${m}/${d}
            rm ${file}
        done
        echo "All files were moved into sub-directories"
    fi

fi


