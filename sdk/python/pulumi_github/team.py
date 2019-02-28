# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class Team(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    A description of the team.
    """
    etag: pulumi.Output[str]
    ldap_dn: pulumi.Output[str]
    """
    The LDAP Distinguished Name of the group where membership will be synchronized. Only available in GitHub Enterprise.
    """
    name: pulumi.Output[str]
    """
    The name of the team.
    """
    parent_team_id: pulumi.Output[int]
    """
    The ID of the parent team, if this is a nested team.
    """
    privacy: pulumi.Output[str]
    """
    The level of privacy for the team. Must be one of `secret` or `closed`.
    Defaults to `secret`.
    """
    slug: pulumi.Output[str]
    """
    The slug of the created team, which may or may not differ from `name`,
    depending on whether `name` contains "URL-unsafe" characters.
    Useful when referencing the team in [`github_branch_protection`](https://www.terraform.io/docs/providers/github/r/branch_protection.html).
    """
    def __init__(__self__, resource_name, opts=None, description=None, ldap_dn=None, name=None, parent_team_id=None, privacy=None, __name__=None, __opts__=None):
        """
        Provides a GitHub team resource.
        
        This resource allows you to add/remove teams from your organization. When applied,
        a new team will be created. When destroyed, that team will be removed.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the team.
        :param pulumi.Input[str] ldap_dn: The LDAP Distinguished Name of the group where membership will be synchronized. Only available in GitHub Enterprise.
        :param pulumi.Input[str] name: The name of the team.
        :param pulumi.Input[int] parent_team_id: The ID of the parent team, if this is a nested team.
        :param pulumi.Input[str] privacy: The level of privacy for the team. Must be one of `secret` or `closed`.
               Defaults to `secret`.
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

        __props__['description'] = description

        __props__['ldap_dn'] = ldap_dn

        if name is None:
            raise TypeError('Missing required property name')
        __props__['name'] = name

        __props__['parent_team_id'] = parent_team_id

        __props__['privacy'] = privacy

        __props__['etag'] = None
        __props__['slug'] = None

        super(Team, __self__).__init__(
            'github:index/team:Team',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

