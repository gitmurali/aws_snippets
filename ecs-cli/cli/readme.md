# Create ECS cluster using ecs-cli

# add ecs cli to your command line
```bash
curl https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest -o "ecs-cli"
sudo chmod +x ./ecs-cli
sudo mv ./ecs-cli /usr/local/bin

#check
ecs-cli --version

# configure
ecs-cli configure profile --access-key <<YOUR-AWS_ACCESS_KEY_ID>> --secret-key <<YOUR-AWS_SECRET_ACCESS_KEY>>
```

# set your vpc and subnets

```bash
export CORE_STACK_NAME="ecs-core-infrastructure"
export vpc=$(aws cloudformation describe-stacks --stack-name $CORE_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`VpcId`].OutputValue' --output text)
export subnet_1=$(aws cloudformation describe-stacks --stack-name $CORE_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`PublicSubnetOne`].OutputValue' --output text)
export subnet_2=$(aws cloudformation describe-stacks --stack-name $CORE_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`PublicSubnetTwo`].OutputValue' --output text)

echo "vpc: $vpc"
echo "subnet1: $subnet_1"
echo "subnet2: $subnet_2"

```

# ecs using EC2 type

```bash
ecs-cli up --capability-iam \
--subnets $subnet_1,$subnet_2 \
--vpc $vpc \
--launch-type EC2 \
--keypair my-ecs-env \
--size 1 \
--instance-type t2.small \
--cluster ecs-ec2
```
