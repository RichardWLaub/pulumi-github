# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class RepositoryWebhook(pulumi.CustomResource):
    active: pulumi.Output[bool]
    """
    Indicate of the webhook should receive events. Defaults to `true`.
    """
    configuration: pulumi.Output[dict]
    """
    key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`.
    """
    etag: pulumi.Output[str]
    events: pulumi.Output[list]
    """
    A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/)
    """
    name: pulumi.Output[str]
    """
    The type of the webhook. See a list of [available hooks](https://api.github.com/hooks).
    """
    repository: pulumi.Output[str]
    """
    The repository of the webhook.
    """
    url: pulumi.Output[str]
    """
    URL of the webhook
    """
    def __init__(__self__, resource_name, opts=None, active=None, configuration=None, events=None, name=None, repository=None, __name__=None, __opts__=None):
        """
        This resource allows you to create and manage webhooks for repositories within your
        GitHub organization.
        
        This resource cannot currently be used to manage webhooks for *personal* repositories,
        outside of organizations.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Indicate of the webhook should receive events. Defaults to `true`.
        :param pulumi.Input[dict] configuration: key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`.
        :param pulumi.Input[list] events: A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/)
        :param pulumi.Input[str] name: The type of the webhook. See a list of [available hooks](https://api.github.com/hooks).
        :param pulumi.Input[str] repository: The repository of the webhook.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['active'] = active

        __props__['configuration'] = configuration

        if events is None:
            raise TypeError('Missing required property events')
        __props__['events'] = events

        if name is None:
            raise TypeError('Missing required property name')
        __props__['name'] = name

        if repository is None:
            raise TypeError('Missing required property repository')
        __props__['repository'] = repository

        __props__['etag'] = None
        __props__['url'] = None

        super(RepositoryWebhook, __self__).__init__(
            'github:index/repositoryWebhook:RepositoryWebhook',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

