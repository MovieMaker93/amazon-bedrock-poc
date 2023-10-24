import boto3
import json

bedrock = boto3.client(
  service_name='bedrock-runtime',
  region_name="us-east-1"
)

def lambda_handler(event, context):

  print("boto3 version"+ boto3.__version__)
  print(event['text'])


  prompt = """
  Write a medium blog post on how to use
  Amazon Bedrock to write an article on how to use Amazon Bedrock.
  """

  body = json.dumps({
      "prompt": prompt,
      "maxTokens": 200,
      "temperature": 0.75,
      "topP": 1,
      "stopSequences": [],
      "countPenalty": {"scale":0},
      "presencePenalty": {"scale":0},
      "frequencyPenalty": {"scale":0}
  })

  modelId = 'ai21.j2-mid-v1'
  accept = 'application/json'
  contentType = 'application/json'

  response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

  response_body = json.loads(response.get('body').read())

  result= response_body['completions'][0]['data']['text']

  print(result)

  return result
