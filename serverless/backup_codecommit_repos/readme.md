# Deploy

sam deploy --guided  --capabilities CAPABILITY_NAMED_IAM

# Clean up

aws cloudformation delete-stack --stack-name STACK_NAME

aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"