// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package github

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a GitHub team membership resource.
// 
// This resource allows you to add/remove users from teams in your organization. When applied,
// the user will be added to the team. If the user hasn't accepted their invitation to the
// organization, they won't be part of the team until they do. When
// destroyed, the user will be removed from the team.
type TeamMembershipTeam struct {
	s *pulumi.ResourceState
}

// NewTeamMembershipTeam registers a new resource with the given unique name, arguments, and options.
func NewTeamMembershipTeam(ctx *pulumi.Context,
	name string, args *TeamMembershipTeamArgs, opts ...pulumi.ResourceOpt) (*TeamMembershipTeam, error) {
	if args == nil || args.TeamId == nil {
		return nil, errors.New("missing required argument 'TeamId'")
	}
	if args == nil || args.Username == nil {
		return nil, errors.New("missing required argument 'Username'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["role"] = nil
		inputs["teamId"] = nil
		inputs["username"] = nil
	} else {
		inputs["role"] = args.Role
		inputs["teamId"] = args.TeamId
		inputs["username"] = args.Username
	}
	inputs["etag"] = nil
	s, err := ctx.RegisterResource("github:index/teamMembershipTeam:TeamMembershipTeam", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TeamMembershipTeam{s: s}, nil
}

// GetTeamMembershipTeam gets an existing TeamMembershipTeam resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTeamMembershipTeam(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TeamMembershipTeamState, opts ...pulumi.ResourceOpt) (*TeamMembershipTeam, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["etag"] = state.Etag
		inputs["role"] = state.Role
		inputs["teamId"] = state.TeamId
		inputs["username"] = state.Username
	}
	s, err := ctx.ReadResource("github:index/teamMembershipTeam:TeamMembershipTeam", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TeamMembershipTeam{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *TeamMembershipTeam) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *TeamMembershipTeam) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *TeamMembershipTeam) Etag() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["etag"])
}

// The role of the user within the team.
// Must be one of `member` or `maintainer`. Defaults to `member`.
func (r *TeamMembershipTeam) Role() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["role"])
}

// The GitHub team id
func (r *TeamMembershipTeam) TeamId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["teamId"])
}

// The user to add to the team.
func (r *TeamMembershipTeam) Username() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["username"])
}

// Input properties used for looking up and filtering TeamMembershipTeam resources.
type TeamMembershipTeamState struct {
	Etag interface{}
	// The role of the user within the team.
	// Must be one of `member` or `maintainer`. Defaults to `member`.
	Role interface{}
	// The GitHub team id
	TeamId interface{}
	// The user to add to the team.
	Username interface{}
}

// The set of arguments for constructing a TeamMembershipTeam resource.
type TeamMembershipTeamArgs struct {
	// The role of the user within the team.
	// Must be one of `member` or `maintainer`. Defaults to `member`.
	Role interface{}
	// The GitHub team id
	TeamId interface{}
	// The user to add to the team.
	Username interface{}
}