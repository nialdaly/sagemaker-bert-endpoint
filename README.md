# SageMaker BERT Endpoint
The following project will demonstrate the process of deploying a BERT model fine-tuned on the SQuAD dataset provided by HuggingFace. The model will be deployed to an Amazon SageMaker PyTorch endpoint. This process makes use of Amazon SageMaker, CloudFormation, Elastic Container Service (ECS) and the HuggingFace transformers library.

## Prerequisites
* AWS Account with an IAM (SageMaker Execution) Role which can be created using `sagemaker-execution-role.yaml` CloudFormation template.

## Getting Started
The easiest way to get started is to spin up an Amazon SageMaker notebook instance using the SageMaker Execution Role that you previously created. You can select a smaller instance such as the `ml.medium` for this step.

Th  repository can be cloned via the following command.
```
git clone https://github.com/nialdaly/sagemaker-bert-endpoint.git
```

## Updates
add sagemaker execution role creation to pre-req
talk about sgaemaker pytorch container

## Additional Resources
* [SageMaker Pre-built Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html)
* [BERT Deployment on SageMaker](https://aws.amazon.com/blogs/machine-learning/fine-tuning-a-pytorch-bert-model-and-deploying-it-with-amazon-elastic-inference-on-amazon-sagemaker/)
