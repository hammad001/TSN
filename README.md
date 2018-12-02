# TSN

This repository derives from the Temporal Segment Network for Action Recognition.

Paper: [Temporal Segment Network](https://arxiv.org/pdf/1608.00859.pdf)

## Preparing dataset

The model has been trained on UCF-101 dataset. The dataset can be obtained from [UCF-101](http://crcv.ucf.edu/data/UCF101.php)

### Extracting RGB frames

We need to extract RGB frames to train the model. RGB frames can be extracted by:
`bash scripts/extract_frames.sh SRC_DIR OUT_DIR`

### Creating list files

A list file containing path of the video frames, number of frames in a video and label of the video is required to be passed to the model for training.

List file can be created by:
`bash scripts/build_list_file.sh ucf101 FRAME_PATH OUT_FILE_PATH`

FRAME_PATH: Path to which the frames were extracted.

## Training model with BNInception backbone
`
python main.py ucf101 RGB TRAIN_SPLIT_FILE_PATH VAL_SPLIT_FILE_PATH 
   --arch BNInception  --num_segments 3 
   --gd 20 --lr 0.001 --lr_steps 30 60 --epochs 80 
   -b 128 -j 8 --dropout 0.8 
   --snapshot_pref ucf101_bninception_  --gpus 0 1 2 3
   `
   
## Testing model

`
   python test_models.py ucf101 RGB VAL_SPLIT_FILE_PATH ucf101_bninception__rgb_model_best.pth.tar   
   --arch BNInception --save_scores scores_bninception --workers 4 --gpus 0 1 2 3
`
