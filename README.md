# Amazon Bedrock PoC
## Abstract
Referencing the official [Amazon Bedrock documentation](https://aws.amazon.com/bedrock/?nc1=h_ls):   
Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) with a single API.  
This simplicity ensures the smoothest development experience while maintaining security.  

This PoC demonstrates invoking the Bedrock API using a newly deployed AWS Lambda function, with infrastructure management handled by Terraform.  

## Setting on Amazon for Bedrock
Before proceeding with the PoC, it's essential to activate the Foundation Model on your AWS account.   
Amazon Bedrock offers a range of FMs for diverse outputs.   
For the sake of this Demo, the AI21 Labs Jurassic-2 Mid model is selected, capable of generating text based on prompts.     
Model activation is not granted by default, so follow this guide to enable model access to your AWS account [guide](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).    

> [!WARNING]
> Minimize prompt usage, as the input/response length directly affects costs.  

## Requirements

- `pre-commit hook installed`  
- `terraform`  
- `Preconfigured AWS cli variables` --> more info [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)  
- `python version >3.10`  
- `AWS CLI installed`  

## Instructions
1. Navigate to the root of the repository and initialize Terraform:
```console
terraform init
```
2. Execute a Terraform plan:
```console
terraform plan
```
This provides a preview of the resources to be deployed.    
3. Apply the Terraform configuration:
```console
terraform apply
```
This sets up the Lambda function and IAM role for interacting with Amazon Bedrock.    

The AWS lambda function is configured with a basic body request.   
Each model offers different kinds of parameters to configure. [Check this out](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-jurassic2.html) for a detailed explanation of parameters used in the PoC for the body.  

4. To prompt the FM, use the text stored in the events.json file:
events.json
```json
{
    "text": "write an article about amazon bedrock"
}
```

5. Invoke the lambda function through the **AWS CLI**:  
```console
aws lambda invoke --region us-east-1 --function-name bedrock_function --cli-binary-format raw-in-base64-out --payload file://events.json response.json
```

The output will be stored in the **response.json** file.  
The text will be 200 characters long, as previously configured in the body request.  
Example Bedrock-generated text: 
```console
"\n  Amazon Bedrock is a service that allows you to build and deploy serverless applications.\n  \n  It is easy to use and does not require any infrastructure to manage.\n  \n  In this article, we will show you how to write and deploy a simple serverless application using Amazon Bedrock.\n  \n  We will also show you how to use Amazon Bedrock to deploy your application to AWS Lambda.\n  \n  Let's get started!\n  \n  First, you will need to sign up for the Amazon Bedrock service.\n  You can do this by visiting the Amazon Bedrock website and clicking on the \"Sign Up\" button.\n  \n  Once you have signed up for Amazon Bedrock, you will need to create a new project.\n  You can do this by clicking on the \"Create Project\" button and following the instructions on the screen.\n  \n  Once you have created your project, you will need to create a new serverless application.\n  You can do this by clicking on the \"Create Application\" button and following the instructions on the screen.\n  \n  Once you have created your application, you will need to write some code.\n  You can do this by clicking on the \"Code\" button and following the instructions on the screen.\n  \n  Once you have written some code, you will need to deploy your application.\n  You can do this by clicking on the \"Deploy\" button"
```

## Wrap up
Amazon's serverless approach with predefined Foundation Models allows us to develop an app in a glimpse of light.  
Key advantages include:
- **Simplicity**: Easy initiation by calling an API.
- **Diverse FM Options**: Various Foundation Models to choose from.
- **Fine-tuning Capability**: Customize Bedrock models with your labeled training dataset.

However, consider the downside:
- **Cost**: On-demand mode can be relatively expensive.

