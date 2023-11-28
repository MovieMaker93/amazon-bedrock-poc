# Amazon Bedrock PoC
<!-- BEGIN_TF_DOCS -->
## Abstract 
From the official Amazon (https://aws.amazon.com/bedrock/?nc1=h_ls)[documentation]:
Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) with a single API.
This simplicity ensures the smoothest development experience while maintaining security.

This PoC aims to call the Bedrock API with a newly deployed AWS Lambda function. 
The infrastructure lifecycle is handled by Terraform.

## Setting on Amazon for Bedrock
Before jumping down in the PoC, you need to activate the Foundation Model on your AWS account.
Amazon Bedrock offers plenty of FMs to get started for your desired output.
For the sake of this Demo, I choose the <b>AI21 Labs Jurassic-2 Mid </b> that accepts a prompt and generates text.
The activation of the model is not granted by default.
Follow along with this (https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)[guide] for access to your AWS account.
> [!WARNING]  
> Remember to prompt the **FM** as little as you can. The length of the response determines the amount of your bills.

## Requirements

- `pre-commit hook installed`
- `terraform`
- `Preconfigured AWS cli variables` --> more info (https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)[here]
- `python version >3.10`
- `AWS CLI installed`

## Instructions
First of all, we need to init our terraform:
```console
terraform init
```
After that:
```console
terraform plan
```
It will show a preview of the resources that will be deployed.
And finally,
```console
terraform apply
```
Now, you will have your lambda function and IAM role to prompt the Amazon Bedrock.
Let's prompt our FM with a text. For the options of the body request, check (https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-jurassic2.html)[here].





<!-- END_TF_DOCS -->
