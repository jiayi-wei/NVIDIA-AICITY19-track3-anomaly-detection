#!/bin/bash
# Usage:
# ./run.sh TASKNAME PARTITION MODEL WEIGHTS
#
# Example:
# ./run.sh test Test model.caffemodel

set -x
set -e

TASKNAME=$1
PARTITION=$2
WEIGHTS=$3
TIMESTAMP="`date +%Y-%m-%d-%H-%M-%S`"

# Temp environment variables
MV2_USE_CUDA=1
MV2_ENABLE_AFFINITY=0
MV2_SMP_USE_CMA=0

srun --partition=${PARTITION} --mpi=pmi2 --gres=gpu:1 -n1 --ntasks-per-node=1 --job-name=${TASKNAME} \
  /mnt/lustre/weijiayi/sensenet/example/build/tools/caffe demo_test \
  --model=./test.prototxt --weights=${WEIGHTS} \
  --config=./config.json \
  --test_image_list=/mnt/lustre/weijiayi/AIC19/aic19-track3/test_bg.txt \
  --image_dir=/mnt/lustre/weijiayi/AIC19/aic19-track3/ \
  --vis_img=1 --out_dir=./vis_res 2>&1 | tee ./log/log_${TASKNAME}
