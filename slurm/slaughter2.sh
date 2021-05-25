set -euxo pipefail
squeue -u $USER | grep $USER | awk '{print $1}' | xargs -n 1 scancel
