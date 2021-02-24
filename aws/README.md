# MeanTweets - AWS
Deploying Meantweets Webapp using Lambda, API Gateway, DynamoDB and S3 with Serverless Framework

## Deploy Backend
1. `cd lambda`
2. `sls deploy` - this command will create S3 buckets, Dynamo-db table, Lambda and ApiGateway. NOTE: This might cause charges to your AWS account. Make sure to clean up after you are done.
3. deploy API: `aws apigateway create-deployment --rest-api-id <rest-api-id> --region us-east-1`  This can also be done manually using  API Gateway.
4. copy and paste the invoke url to 'app-client/src/config.js'


## Deploy Static Website
1. `cd app-client`
2. `npm install`
3. Create the production site `npm run build`
4. Copy the site to S3 bucket. `aws s3 sync ./build s3://mt-bucket-20200215`

Go to website: http://mt-bucket-20200215.s3-website-us-east-1.amazonaws.com/



## Clean up AWS resources
1. Clean up s3 bucket `aws s3 rm s3://mt-bucket-20200215/ --recursive`
2. Clean up resources `sls remove`
3. You should also navigate to AWS CloudFormation and delete the stack. This can only be done manually
