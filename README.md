# SageMaker BERT Endpoint
The following project will demonstrate the process of deploying a BERT model fine-tuned on the SQuAD dataset provided by HuggingFace. The model will be deployed to an Amazon SageMaker PyTorch endpoint. This process makes use of Amazon SageMaker, CloudFormation, Elastic Container Service (ECS) and the HuggingFace transformers library.

## Prerequisites
* An AWS Account with an IAM (SageMaker Execution) Role which can be created using `sagemaker-execution-role.yaml` CloudFormation template.
* An appropriate SageMaker Instance limit. A request for a service limit increase can raised by following [this process](https://docs.aws.amazon.com/deepcomposer/latest/devguide/deepcomposer-service-limit.html).

## Getting Started
The easiest way to get started is to spin up an Amazon SageMaker notebook instance using the SageMaker Execution Role that you previously created. You can select a smaller instance such as the `ml.t2.medium` for this step. The process of creating a SageMaker Notebook instance is described [here](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-setup-working-env.html).

The repository can be cloned via the following command.
```
git clone https://github.com/nialdaly/sagemaker-bert-endpoint.git
```

## Resource Cleanup
Any resources created in this project can be simply removed by destroying the CloudFormation stacks that you created using the CloudFormation console. The SageMaker Notebook instance must be terminated yourself. **Remember to stop the instance if you aren't using it as you will be charged otherwise.**

## Additional Resources
* [SageMaker Pre-built Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html)
* [BERT Deployment on SageMaker](https://aws.amazon.com/blogs/machine-learning/fine-tuning-a-pytorch-bert-model-and-deploying-it-with-amazon-elastic-inference-on-amazon-sagemaker/)