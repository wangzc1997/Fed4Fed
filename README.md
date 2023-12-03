## Project Description
This project uses the code from https://github.com/Accenture/Labs-Federated-Learning/blob/clustered_sampling to train models, and writes and executes test logic based on trained iid and non-iid mnist/cifar models, using the test results as inputs for this work.

## Model Training

The following four commands are used to run iid and non-iid models for mnist and cifar10:
```
python FL.py MNIST_iid random any 0 50 0.01 1.0 0.1 False 
python FL.py MNIST_shard random any 0 50 0.01 1.0 0.1 False 
python FL.py CIFAR10_iid random any 0 100 0.05 1.0 0.1 False
python FL.py CIFAR10_bbal_0.001 random any 0 100 0.05 1.0 0.1 False
```
According to the original code's readme, only the first parameter setting is related to the dataset and IID, so we only change the first parameter and use the default parameters of the source code for all parameters other than the first. The settings for the first parameter are as follows:
- `MNIST_iid`: Train the model using the mnist iid dataset
- `MNIST_shard`: Train the model using the mnist non-iid dataset (obtained through shard)
- `CIFAR10_iid`: Train the model using the cifar10 iid dataset
- `CIFAR10_bbal_0.001`: Train the model using the cifar10 non-iid dataset (obtained by the Dirichlet method, with α value of 0.001)

The specific details of model training can be found at https://github.com/Accenture/Labs-Federated-Learning/blob/clustered_sampling

## Model Bootstrap

Next, enter the sampling_test directory and run the following 4 commands to run the test results for mnist and cifar10 iid and non-iid:
```
python test.py mnist True
python test.py mnist False
python test.py cifar True
python test.py cifar False
```

In this, the first parameter can be either `mnist` or `cifar`, indicating which trained model is being tested; the second parameter can be either `True` or `False`, indicating whether the model being tested is iid or not.

The final test results will be stored in the directory: sampling_test/saved_exp_info.


## Model Fairness Verification
In the fairness hypothesis testing folder, we run ag1.py and ag2.py by inputting the output results from Model Bootstrap:
```
python ag1.py

python ag2.py
```
In this way, the probability of committing a Type I error for two fairness verification methods can be obtained.


## Calculation of Model Performance Confidence Interval
In the performance confidence interval folder, we run the `confidence interval.py` script by inputting the output results from Model Bootstrap:
```
python confidence interval.py
```
In this way, we can calculate the credible performance confidence interval for the federated learning model.

