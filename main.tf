terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Create a VPC
resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"
}

module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name      = "bedrock_function"
  description        = "Bedrock simple call"
  handler            = "main.lambda_handler"
  runtime            = "python3.10"
  source_path        = "${path.module}/code/"
  attach_policy_json = true
  policy_json = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["bedrock:*"]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
