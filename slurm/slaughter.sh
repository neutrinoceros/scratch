#!/bin/bash
#
# author: clement.robert@oca.eu
# -----------------------------
# Written for SLURM environment, tested @licallo.oca.eu
#
#
# Politely ask if you really wish it to kill *all* your simulations, then proceed.
#
# Optional argument "picky" (-p|-P|--picky) + str :
# restrict the tokill list to jobs whose descriptive line in 
# squeue matches this string.

echo
echo "slaughter.sh"
echo "------------"
echo

# PARSING
#----------------------------------------------------------------------

GREPING="grep $USER"

while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -p|-P|--picky)
        target="$2"
        GREPING="$GREPING | grep $target"
        shift
        ;;
    *)
        ;;
esac
shift
done

squeue -u $USER > queue.tmp
jobs=$(cat queue.tmp | eval $GREPING)
tokill=$(echo $jobs | awk '{print $1}')

# PROCEDURE
#----------------------------------------------------------------------

echo "The following jobs are about to be killed :"
echo "------------------------------------------------------------------------------------"
echo "             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)"
echo "------------------------------------------------------------------------------------"
echo -e "$jobs\n"
read -p "proceed (y/[n])?    " choice

case "$choice" in
    y|Y|yes|YES) for jobnumber in ${tokill[*]}
        do 
        echo 'killing' $jobnumber
        scancel $jobnumber
        done
        ;;
    *) echo "I'm sorry Dave. I'm afraid I can't do that"
        ;;
esac

rm queue.tmp
