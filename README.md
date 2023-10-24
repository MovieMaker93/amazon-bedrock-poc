# Amazon-bedrock-poc
<!-- BEGIN_TF_DOCS -->
This sample poc is an example on how to deploy an aws lambda function calling Amazon bedrock serverless service.
IaC made with Terraform (provision lambda function) and boto3 client for the lambda handler function.


## Requirements

pre-commit hook installed via client --> pre-commit install
terraform installed --> terraform init, plan and apply
preconfigured aws cli variables
python 3.10
aws cli installed

Step by step:
1. terraform init, plan and apply
2. aws lambda invoke --blabla
3. See the result prompt

| Name | Version |
|------|---------|
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 5.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 5.22.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_lambda_function"></a> [lambda\_function](#module\_lambda\_function) | terraform-aws-modules/lambda/aws | n/a |

## Resources

| Name | Type |
|------|------|
| [aws_vpc.example](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc) | resource |

## Inputs

No inputs.

## Outputs

No outputs.
<!-- END_TF_DOCS -->
