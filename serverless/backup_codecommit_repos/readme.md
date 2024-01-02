# Deploy

```
sam deploy --guided  --capabilities CAPABILITY_NAMED_IAM
```

# Clean up

```
aws cloudformation delete-stack --stack-name STACK_NAME
```

```
aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
```

# Explanation

This CloudFormation template automates the process of backing up a CodeCommit repository to an S3 bucket using EventBridge and CodeBuild. Let's break down the key components:

S3 Bucket for CodeCommit Backups

Creates an S3 bucket to store CodeCommit backups.
Utilizes BucketOwnerEnforced ownership controls.
IAM Role for CodeBuild Project

Establishes an IAM role for the CodeBuild project.
Grants necessary permissions for CodeBuild, including CodeCommit interaction and S3 access.
CodeBuild Project

Defines a CodeBuild project to sync CodeCommit repositories to the specified S3 bucket.
Uses a Linux container with specific environment variables like BUCKET and ACCOUNT.
The source is set to an S3 location for the CodeCommit repository, and the build commands involve cloning, compressing, and uploading the repository to S3.
Lambda Function (CreateBuildspec)

Implements a Lambda function to dynamically create a buildspec.yml file in the backup bucket to run CodeBuild.
Python script within the Lambda function generates the necessary build commands for CodeBuild.
Custom Resource to Trigger Lambda (TriggerBuildspecCreation)

A custom resource triggers the Lambda function at deployment time.
IAM Role for CloudWatch Events

Defines an IAM role for CloudWatch Events to trigger AWS CodeBuild builds.
Grants permissions for CodeBuild execution.
CloudWatch Events Rule

Sets up an EventBridge (CloudWatch Events) rule to trigger the CodeBuild project when the content of a CodeCommit repository changes.
The template effectively orchestrates the backup process by combining S3, CodeBuild, Lambda, and CloudWatch Events to automate repository backups to S3