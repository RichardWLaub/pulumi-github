// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package github

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// This resource allows you to create and manage projects for GitHub repository.
type RepositoryProject struct {
	s *pulumi.ResourceState
}

// NewRepositoryProject registers a new resource with the given unique name, arguments, and options.
func NewRepositoryProject(ctx *pulumi.Context,
	name string, args *RepositoryProjectArgs, opts ...pulumi.ResourceOpt) (*RepositoryProject, error) {
	if args == nil || args.Name == nil {
		return nil, errors.New("missing required argument 'Name'")
	}
	if args == nil || args.Repository == nil {
		return nil, errors.New("missing required argument 'Repository'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["body"] = nil
		inputs["name"] = nil
		inputs["repository"] = nil
	} else {
		inputs["body"] = args.Body
		inputs["name"] = args.Name
		inputs["repository"] = args.Repository
	}
	inputs["etag"] = nil
	inputs["url"] = nil
	s, err := ctx.RegisterResource("github:index/repositoryProject:RepositoryProject", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RepositoryProject{s: s}, nil
}

// GetRepositoryProject gets an existing RepositoryProject resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRepositoryProject(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RepositoryProjectState, opts ...pulumi.ResourceOpt) (*RepositoryProject, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["body"] = state.Body
		inputs["etag"] = state.Etag
		inputs["name"] = state.Name
		inputs["repository"] = state.Repository
		inputs["url"] = state.Url
	}
	s, err := ctx.ReadResource("github:index/repositoryProject:RepositoryProject", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RepositoryProject{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *RepositoryProject) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *RepositoryProject) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The body of the project.
func (r *RepositoryProject) Body() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["body"])
}

func (r *RepositoryProject) Etag() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["etag"])
}

// The name of the project.
func (r *RepositoryProject) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The repository of the project.
func (r *RepositoryProject) Repository() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["repository"])
}

// URL of the project
func (r *RepositoryProject) Url() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["url"])
}

// Input properties used for looking up and filtering RepositoryProject resources.
type RepositoryProjectState struct {
	// The body of the project.
	Body interface{}
	Etag interface{}
	// The name of the project.
	Name interface{}
	// The repository of the project.
	Repository interface{}
	// URL of the project
	Url interface{}
}

// The set of arguments for constructing a RepositoryProject resource.
type RepositoryProjectArgs struct {
	// The body of the project.
	Body interface{}
	// The name of the project.
	Name interface{}
	// The repository of the project.
	Repository interface{}
}
