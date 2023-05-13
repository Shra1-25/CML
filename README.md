# CML
##Cloud &amp; ML final project -- Dynamic Quantisation using TensorRT

###Instructions to execute on Greene:    

###First create a conda environment  
conda env create --name envname --file=environments.yml

###Then we use the appropriate overlay image and use the imagenet dataset provided in GCP (You need to copy the imagenet dataset to Greene using scp) 
singularity exec --overlay /scratch/ssc10020/IndependentStudy/CML/imagenet-val.sqf --overlay /scratch/ssc10020/overlay-50G-10M.ext3:ro --nv /scratch/work/public/singularity/cuda11.2.2-cudnn8-devel-ubuntu20.04.sif /bin/bash   

source /ext3/miniconda3/bin/activate
conda activate cml  

Command to execute the python command  
python run.py --pretrained
