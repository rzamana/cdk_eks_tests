from aws_cdk import (
    aws_cloudformation as cfn,
    aws_eks as eks,
    core
)

class EksClusterStack(cfn.NestedStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        eks.Cluster(self, 'EKSCluster')