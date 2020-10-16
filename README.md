# SageMaker BERT Endpoint
The following project will demonstrate the process of deploying a BERT model fine-tuned on the SQuAD dataset provided by HuggingFace. The model will be deployed to an Amazon SageMaker PyTorch endpoint. This process makes use of Amazon SageMaker, CloudFormation, Elastic Container Service (ECS) and the HuggingFace transformers library.

## Prerequisites
* AWS Account with an IAM (SageMaker Execution) Role

## Getting Started
The easiest way to get started is to spin up an Amazon SageMaker notebook instance and clone the repository via the following command.
```
git clone https://github.com/nialdaly/sagemaker-bert-endpoint.git
```
