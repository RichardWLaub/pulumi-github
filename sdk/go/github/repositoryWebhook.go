// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package github

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// This resource allows you to create and manage webhooks for repositories within your
// GitHub organization.
// 
// This resource cannot currently be used to manage webhooks for *personal* repositories,
// outside of organizations.
type RepositoryWebhook struct {
	s *pulumi.ResourceState
}

// NewRepositoryWebhook registers a new resource with the given unique name, arguments, and options.
func NewRepositoryWebhook(ctx *pulumi.Context,
	name string, args *RepositoryWebhookArgs, opts ...pulumi.ResourceOpt) (*RepositoryWebhook, error) {
	if args == nil || args.Events == nil {
		return nil, errors.New("missing required argument 'Events'")
	}
	if args == nil || args.Name == nil {
		return nil, errors.New("missing required argument 'Name'")
	}
	if args == nil || args.Repository == nil {
		return nil, errors.New("missing required argument 'Repository'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["active"] = nil
		inputs["configuration"] = nil
		inputs["events"] = nil
		inputs["name"] = nil
		inputs["repository"] = nil
	} else {
		inputs["active"] = args.Active
		inputs["configuration"] = args.Configuration
		inputs["events"] = args.Events
		inputs["name"] = args.Name
		inputs["repository"] = args.Repository
	}
	inputs["etag"] = nil
	inputs["url"] = nil
	s, err := ctx.RegisterResource("github:index/repositoryWebhook:RepositoryWebhook", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RepositoryWebhook{s: s}, nil
}

// GetRepositoryWebhook gets an existing RepositoryWebhook resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRepositoryWebhook(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RepositoryWebhookState, opts ...pulumi.ResourceOpt) (*RepositoryWebhook, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["active"] = state.Active
		inputs["configuration"] = state.Configuration
		inputs["etag"] = state.Etag
		inputs["events"] = state.Events
		inputs["name"] = state.Name
		inputs["repository"] = state.Repository
		inputs["url"] = state.Url
	}
	s, err := ctx.ReadResource("github:index/repositoryWebhook:RepositoryWebhook", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RepositoryWebhook{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *RepositoryWebhook) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *RepositoryWebhook) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Indicate of the webhook should receive events. Defaults to `true`.
func (r *RepositoryWebhook) Active() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["active"])
}

// key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`.
func (r *RepositoryWebhook) Configuration() *pulumi.Output {
	return r.s.State["configuration"]
}

func (r *RepositoryWebhook) Etag() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["etag"])
}

// A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/)
func (r *RepositoryWebhook) Events() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["events"])
}

// The type of the webhook. See a list of [available hooks](https://api.github.com/hooks).
func (r *RepositoryWebhook) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The repository of the webhook.
func (r *RepositoryWebhook) Repository() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["repository"])
}

// URL of the webhook
func (r *RepositoryWebhook) Url() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["url"])
}

// Input properties used for looking up and filtering RepositoryWebhook resources.
type RepositoryWebhookState struct {
	// Indicate of the webhook should receive events. Defaults to `true`.
	Active interface{}
	// key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`.
	Configuration interface{}
	Etag interface{}
	// A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/)
	Events interface{}
	// The type of the webhook. See a list of [available hooks](https://api.github.com/hooks).
	Name interface{}
	// The repository of the webhook.
	Repository interface{}
	// URL of the webhook
	Url interface{}
}

// The set of arguments for constructing a RepositoryWebhook resource.
type RepositoryWebhookArgs struct {
	// Indicate of the webhook should receive events. Defaults to `true`.
	Active interface{}
	// key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`.
	Configuration interface{}
	// A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/)
	Events interface{}
	// The type of the webhook. See a list of [available hooks](https://api.github.com/hooks).
	Name interface{}
	// The repository of the webhook.
	Repository interface{}
}
