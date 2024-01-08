From pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

## Apt get install
RUN apt-get update \
 && apt-get install wget unzip zip -y \
 && apt-get install sudo \
 && apt-get install git -y \
 && apt-get install gnupg -y


## Install binary version terraform
RUN wget https://releases.hashicorp.com/terraform/1.6.6/terraform_1.6.6_linux_amd64.zip \
 && sudo unzip terraform_1.6.6_linux_amd64.zip -d /usr/local/bin

## Initiate Git variable
RUN git config --global user.email "zwj63518583@gmail.com"
RUN git config --global user.name "pandasang1231"





## Command of build the docker
## docker build -t wenjia/pytorch:1.13.1-cuda11.6-cudnn8-runtime -f .\Dockerfile .

## Command of use images
## docker run -itd --name pytorch --gpus all -v //f/Zhuwenjia:/workspace wenjia/pytorch:1.13.1-cuda11.6-cudnn8-runtime bash