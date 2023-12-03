# Clustered Sampling: Low-Variance and Improved Representativity for Clients Selection in Federated Learning

## Download the dependencies

This work is done using PyTorch 1.4.0 .


## Datasets

Datasets are creaeted from CIFAR10 and MNIST. These datasets are not included in this repository but are automatically downloaded using `torchvision` library when running a simulation. 

## Initial Model

We detail in the paper the different models used. To have a fair comparison between different simulations, we allow the user to input the seed used to initialize the model. In all of our experiments, we use `seed=0`.


## Required Experiments

We run a wide range of experiments in this work. `experiments.txt`


## Running an experiment

Running an experiment requires to use `FL.py`. 

Every experiment saves by default the training loss, the testing accuracy, in the folder `saved_exp_info`. The global model and local models histories can also be saved.









