# Follow below steps to create codeBuildServiceRole IAM role

## create a policy called codeBuildBatchPolicy and attach the following permissions to the codeBuildServiceRole IAM role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Resource": [
                "arn:aws:codebuild:us-east-1:<your_account_number>:project/simplehttp-cb"
            ],
            "Action": [
                "codebuild:StartBuild",
                "codebuild:StopBuild",
                "codebuild:RetryBuild"
            ]
        }
    ]
}
```

## create a policy called codeBuildServiceRolePolicy and attach the following permissions to the codeBuildServiceRole IAM role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetAuthorizationToken",
                "codecommit:GitPull",
                "s3:GetBucketAcl",
                "logs:CreateLogGroup",
                "logs:PutLogEvents",
                "s3:PutObject",
                "s3:GetObject",
                "logs:CreateLogStream",
                "ecr:BatchGetImage",
                "s3:GetBucketLocation",
                "s3:GetObjectVersion",
                "ecr:BatchCheckLayerAvailability"
            ],
            "Resource": "*"
        }
    ]
}
```

## finally attach a policy called AmazonEC2ContainerRegistryPowerUser to your codeBuildServiceRole IAM role