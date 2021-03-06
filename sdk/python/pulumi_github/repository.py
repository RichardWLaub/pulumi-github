# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class Repository(pulumi.CustomResource):
    allow_merge_commit: pulumi.Output[bool]
    """
    Set to `false` to disable merge commits on the repository.
    """
    allow_rebase_merge: pulumi.Output[bool]
    """
    Set to `false` to disable rebase merges on the repository.
    """
    allow_squash_merge: pulumi.Output[bool]
    """
    Set to `false` to disable squash merges on the repository.
    """
    archived: pulumi.Output[bool]
    """
    Specifies if the repository should be archived. Defaults to `false`.
    """
    auto_init: pulumi.Output[bool]
    """
    Meaningful only during create; set to `true` to
    produce an initial commit in the repository.
    """
    default_branch: pulumi.Output[str]
    """
    The name of the default branch of the repository. **NOTE:** This can only be set after a repository has already been created,
    and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the
    initial repository creation and create the target branch inside of the repository prior to setting this attribute.
    """
    description: pulumi.Output[str]
    """
    A description of the repository.
    """
    etag: pulumi.Output[str]
    full_name: pulumi.Output[str]
    """
    A string of the form "orgname/reponame".
    """
    git_clone_url: pulumi.Output[str]
    """
    URL that can be provided to `git clone` to clone the
    repository anonymously via the git protocol.
    """
    gitignore_template: pulumi.Output[str]
    """
    Meaningful only during create, will be ignored after repository creation. Use the [name of the template](https://github.com/github/gitignore) without the extension. For example, "Haskell".
    """
    has_downloads: pulumi.Output[bool]
    """
    Set to `true` to enable the (deprecated)
    downloads features on the repository.
    """
    has_issues: pulumi.Output[bool]
    """
    Set to `true` to enable the GitHub Issues features
    on the repository.
    """
    has_projects: pulumi.Output[bool]
    """
    Set to `true` to enable the GitHub Projects features on the repository. Per the github [documentation](https://developer.github.com/v3/repos/#create) when in an organization that has disabled repository projects it will default to `false` and will otherwise default to `true`. If you specify `true` when it has been disabled it will return an error.
    """
    has_wiki: pulumi.Output[bool]
    """
    Set to `true` to enable the GitHub Wiki features on
    the repository.
    """
    homepage_url: pulumi.Output[str]
    """
    URL of a page describing the project.
    """
    html_url: pulumi.Output[str]
    """
    URL to the repository on the web.
    """
    http_clone_url: pulumi.Output[str]
    """
    URL that can be provided to `git clone` to clone the
    repository via HTTPS.
    """
    license_template: pulumi.Output[str]
    """
    Meaningful only during create, will be ignored after repository creation. Use the [name of the template](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses) without the extension. For example, "mit" or "mpl-2.0".
    """
    name: pulumi.Output[str]
    """
    The name of the repository.
    """
    private: pulumi.Output[bool]
    """
    Set to `true` to create a private repository.
    Repositories are created as public (e.g. open source) by default.
    """
    ssh_clone_url: pulumi.Output[str]
    """
    URL that can be provided to `git clone` to clone the
    repository via SSH.
    """
    svn_url: pulumi.Output[str]
    """
    URL that can be provided to `svn checkout` to check out
    the repository via GitHub's Subversion protocol emulation.
    """
    topics: pulumi.Output[list]
    """
    The list of topics of the repository.
    """
    def __init__(__self__, resource_name, opts=None, allow_merge_commit=None, allow_rebase_merge=None, allow_squash_merge=None, archived=None, auto_init=None, default_branch=None, description=None, gitignore_template=None, has_downloads=None, has_issues=None, has_projects=None, has_wiki=None, homepage_url=None, license_template=None, name=None, private=None, topics=None, __name__=None, __opts__=None):
        """
        This resource allows you to create and manage repositories within your
        GitHub organization.
        
        This resource cannot currently be used to manage *personal* repositories,
        outside of organizations.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_merge_commit: Set to `false` to disable merge commits on the repository.
        :param pulumi.Input[bool] allow_rebase_merge: Set to `false` to disable rebase merges on the repository.
        :param pulumi.Input[bool] allow_squash_merge: Set to `false` to disable squash merges on the repository.
        :param pulumi.Input[bool] archived: Specifies if the repository should be archived. Defaults to `false`.
        :param pulumi.Input[bool] auto_init: Meaningful only during create; set to `true` to
               produce an initial commit in the repository.
        :param pulumi.Input[str] default_branch: The name of the default branch of the repository. **NOTE:** This can only be set after a repository has already been created,
               and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the
               initial repository creation and create the target branch inside of the repository prior to setting this attribute.
        :param pulumi.Input[str] description: A description of the repository.
        :param pulumi.Input[str] gitignore_template: Meaningful only during create, will be ignored after repository creation. Use the [name of the template](https://github.com/github/gitignore) without the extension. For example, "Haskell".
        :param pulumi.Input[bool] has_downloads: Set to `true` to enable the (deprecated)
               downloads features on the repository.
        :param pulumi.Input[bool] has_issues: Set to `true` to enable the GitHub Issues features
               on the repository.
        :param pulumi.Input[bool] has_projects: Set to `true` to enable the GitHub Projects features on the repository. Per the github [documentation](https://developer.github.com/v3/repos/#create) when in an organization that has disabled repository projects it will default to `false` and will otherwise default to `true`. If you specify `true` when it has been disabled it will return an error.
        :param pulumi.Input[bool] has_wiki: Set to `true` to enable the GitHub Wiki features on
               the repository.
        :param pulumi.Input[str] homepage_url: URL of a page describing the project.
        :param pulumi.Input[str] license_template: Meaningful only during create, will be ignored after repository creation. Use the [name of the template](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses) without the extension. For example, "mit" or "mpl-2.0".
        :param pulumi.Input[str] name: The name of the repository.
        :param pulumi.Input[bool] private: Set to `true` to create a private repository.
               Repositories are created as public (e.g. open source) by default.
        :param pulumi.Input[list] topics: The list of topics of the repository.
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

        __props__['allow_merge_commit'] = allow_merge_commit

        __props__['allow_rebase_merge'] = allow_rebase_merge

        __props__['allow_squash_merge'] = allow_squash_merge

        __props__['archived'] = archived

        __props__['auto_init'] = auto_init

        __props__['default_branch'] = default_branch

        __props__['description'] = description

        __props__['gitignore_template'] = gitignore_template

        __props__['has_downloads'] = has_downloads

        __props__['has_issues'] = has_issues

        __props__['has_projects'] = has_projects

        __props__['has_wiki'] = has_wiki

        __props__['homepage_url'] = homepage_url

        __props__['license_template'] = license_template

        if name is None:
            raise TypeError('Missing required property name')
        __props__['name'] = name

        __props__['private'] = private

        __props__['topics'] = topics

        __props__['etag'] = None
        __props__['full_name'] = None
        __props__['git_clone_url'] = None
        __props__['html_url'] = None
        __props__['http_clone_url'] = None
        __props__['ssh_clone_url'] = None
        __props__['svn_url'] = None

        super(Repository, __self__).__init__(
            'github:index/repository:Repository',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

