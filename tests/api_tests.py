import os
import urllib.request

import pytest
import boto3

NEO_DEMO_FE_PORT = 80


@pytest.fixture
def neo_demo_url():
    session = boto3.session.Session(aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                                    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
                                    region_name="eu-west-1")
    elb = session.client("elb")
    elbs = elb.describe_load_balancers().get("LoadBalancerDescriptions", [])
    for elb in elbs:
        for listener in elb["ListenerDescriptions"]:
            if listener.get("Listener", {}).get("LoadBalancerPort") == NEO_DEMO_FE_PORT:
                return elb["DNSName"]


def test_frontend_mq(neo_demo_url):
    api_request = urllib.request.Request(f"http://{neo_demo_url}/mq?data=hello")
    response = urllib.request.urlopen(api_request).read()
    assert b'200 OK' == response
