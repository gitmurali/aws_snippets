import { Stack, StackProps } from "aws-cdk-lib";
import { Construct } from "constructs";
import { Bucket } from "aws-cdk-lib/aws-s3";
import { NagSuppressions } from "cdk-nag";

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    // The local scope 'this' is the Stack.
    NagSuppressions.addStackSuppressions(this, [
      {
        id: "AwsSolutions-S1",
        reason: "Demonstrate a stack level suppression.",
      },
    ]);
    // Remediating AwsSolutions-S10 by enforcing SSL on the bucket.
    const bucket = new Bucket(this, "Bucket", { enforceSSL: true });
    NagSuppressions.addResourceSuppressions(bucket, [
      {
        id: "AwsSolutions-S2",
        reason: "Demonstrate a resource level suppression.",
      },
    ]);
  }
}
