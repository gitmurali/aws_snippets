# Create ECS cluster based on EC2

Command to apply the CloudFormation template

Launchtype _EC2_:  

```bash
aws cloudformation create-stack --stack-name ecs-type-ec2 --capabilities CAPABILITY_IAM --template-body file://./ecs-ec2-with-cf.yml
```