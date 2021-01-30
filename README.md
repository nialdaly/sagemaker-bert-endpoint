# SageMaker BERT Endpoint
The following project will demonstrate the process of deploying a BERT model fine-tuned on the SQuAD dataset provided by HuggingFace. The model will be deployed to an Amazon SageMaker PyTorch endpoint. This process makes use of Amazon SageMaker, CloudFormation, Lambda, Elastic Container Service (ECS) and the HuggingFace transformers library.

## Prerequisites
* An AWS Account with an IAM Execution Role for the SageMaker Notebook Instance which can be created using `cloudformation/sagemaker-notebook-role.yaml` CloudFormation template.
* An appropriate SageMaker Notebook Instance limit. A request for a service limit increase can raised by following [this process](https://docs.aws.amazon.com/deepcomposer/latest/devguide/deepcomposer-service-limit.html).

## Getting Started
The easiest way to get started is to spin up an Amazon SageMaker notebook instance using the *SageMaker Notebook Role* that you previously created. You can select a smaller instance such as the `ml.t2.medium` for this step as no training is needed. The process of creating a SageMaker Notebook instance is described in detail [here](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-setup-working-env.html).

## 1. S3 Bucket & Model Artefacts Creation
In order to deploy a SageMaker Model, Endpoint Configuration and Endpoint, the appropriate model artefacts must be saved to an S3 bucket with a specific directory structure. The `model_artefact_prep.ipynb` Jupyter notebook provides the code neccessary to complete this requirement. By cloning this repository into the SageMaker Notebook Instance and running the code in the notebook, you will be able to complete the following steps:
1. Create an S3 bucket
2. Pull the BERT model artefacts from HuggingFace's public S3 bucket
3. Create a tarball object from the artefacts and upload it to S3
4. Test the SageMaker Endpoint after deployment (using CloudFormation)

This repository can be cloned into the SageMaker Notebook Instance using the Jupyter Terminal with the following command:
```
git clone https://github.com/nialdaly/sagemaker-bert-endpoint.git
```

## 2. SageMaker Model Endpoint Creation
The SageMaker Model, Endpoint Configuration and Endpoint can be deployed automatically using CloudFormation. The CloudFormation template will reference the S3 bucket and the BERT model artefacts that have already been created using the code in the `model_artefact_prep.ipynb` Jupyter notebook. The `cloudformation/sagemaker-endpoint.yaml` CloudFormation template can be deployed with the following command run inside the `cloudformation/` directory:
```
aws cloudformation create-stack --stack-name sagemaker-bert-endpoint-stack \
    --template-body file://sagemaker-endpoint.yaml \
    --capabilities CAPABILITY_NAMED_IAM
```

## 3. Lambda Endpoint Trigger Creation
The `cloudformation/lambda-endpoint-trigger.yaml` CloudFormation template can be used to create an AWS Lambda function which can invoke the SageMaker Endpoint and return a response. This template can be deployed by running the following command run inside the `cloudformation/` directory:
```
aws cloudformation create-stack --stack-name lambda-bert-endpoint-stack \
    --template-body file://lambda-endpoint-trigger.yaml \
    --capabilities CAPABILITY_NAMED_IAM
```

## Resource Cleanup
Any resources created in this project can be simply removed by destroying the CloudFormation stacks that you created using the CloudFormation console. They can also be deleted via the AWS CLI using the following commands:
```
aws cloudformation delete-stack --stack-name lambda-bert-endpoint-stack
```

```
aws cloudformation delete-stack --stack-name sagemaker-bert-endpoint-stack
```

The SageMaker Notebook instance must be terminated yourself. **Remember to stop the instance if you aren't using it as you will be charged otherwise.**

The CloudFormation stack used to create the *SageMaker-Notebook-Role* can be deleted with the following command:
```
aws cloudformation delete-stack --stack-name sagemaker-notebook-role-stack
```

## Additional Resources
- [SageMaker Pre-built Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html)
- [BERT Deployment on SageMaker](https://aws.amazon.com/blogs/machine-learning/fine-tuning-a-pytorch-bert-model-and-deploying-it-with-amazon-elastic-inference-on-amazon-sagemaker/)
- [Lambda Inline Code - CloudFormation](https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/CloudFormation/MacrosExamples/PyPlate/python.yaml)