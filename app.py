#!/usr/bin/env python3

from aws_cdk import core

from eks_test.eks_test_stack import EksTestStack
from eks_test.eks_cluster import EksClusterStack


app = core.App()
main_stack = EksTestStack(app, "eks-test", env={'region': 'us-west-2'})
EksClusterStack(main_stack, 'EksCluster')

app.synth()
