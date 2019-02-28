# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

__config__ = pulumi.Config('github')

base_url = __config__.get('baseUrl')
"""
The GitHub Base API URL
"""

insecure = __config__.get('insecure')
"""
Whether server should be accessed without verifying the TLS certificate.
"""

organization = __config__.require('organization')
"""
The GitHub organization name to manage.
"""

token = __config__.require('token')
"""
The OAuth token used to connect to GitHub.
"""

