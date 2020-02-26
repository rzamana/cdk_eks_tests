#!/usr/bin/env python3

from aws_cdk import core

from eks_test.eks_test_stack import EksTestStack


app = core.App()
EksTestStack(app, "eks-test", env={'region': 'us-west-2'})

app.synth()
