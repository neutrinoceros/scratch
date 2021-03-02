# open a directory from licallo (first argument) with Jupyter
nblic () {
    myport=8899
    com="cd $1 && jupyter lab --no-browser --port=$myport"
    ssh crobert@licallo.oca.eu -L localhost:$myport\:localhost:$myport -g -C -t $com
}
