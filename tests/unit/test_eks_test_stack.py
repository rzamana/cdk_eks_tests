import json
import pytest

from aws_cdk import core
from eks_test.eks_test_stack import EksTestStack


def get_template():
    app = core.App()
    EksTestStack(app, "eks-test")
    return json.dumps(app.synth().get_stack("eks-test").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
