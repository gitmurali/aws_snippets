import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";

export class SampleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const hello = new lambda.Function(this, "SampleLambda", {
      runtime: lambda.Runtime.NODEJS_14_X,
      code: lambda.Code.fromInline(
        'exports.handler = async () => "hello world";'
      ),
      handler: "index.handler",
    });
  }
}
