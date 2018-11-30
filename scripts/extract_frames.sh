#!/usr/bin/env bash

SRC_FOLDER=$1
OUT_FOLDER=$2

proj_dir="/datasets/home/15/015/hayyubi/ActionRecognition/TSN"
tools_dir="${proj_dir}/tools"
local_dir="${proj_dir}/local"

echo "Extracting optical flow from videos in folder: ${SRC_FOLDER}"
python ${tools_dir}/extract_frames.py ${SRC_FOLDER} ${OUT_FOLDER} 2>${local_dir}/errors.log
