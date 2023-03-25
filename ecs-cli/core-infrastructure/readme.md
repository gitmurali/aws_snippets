# Create core AWS infrastructure

- VPC
- 2 subnets in 2 different AZs
- Internet Gateway (IGW)
- route tables

Command:

```bash
aws cloudformation create-stack --capabilities CAPABILITY_IAM --stack-name ecs-core-infrastructure --template-body file://./core-infrastructure-setup.yml
```