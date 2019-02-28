// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class TeamMembershipTeam extends pulumi.CustomResource {
    /**
     * Get an existing TeamMembershipTeam resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TeamMembershipTeamState, opts?: pulumi.CustomResourceOptions): TeamMembershipTeam {
        return new TeamMembershipTeam(name, <any>state, { ...opts, id: id });
    }

    public /*out*/ readonly etag: pulumi.Output<string>;
    public readonly role: pulumi.Output<string | undefined>;
    public readonly teamId: pulumi.Output<string>;
    public readonly username: pulumi.Output<string>;

    /**
     * Create a TeamMembershipTeam resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TeamMembershipTeamArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TeamMembershipTeamArgs | TeamMembershipTeamState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: TeamMembershipTeamState = argsOrState as TeamMembershipTeamState | undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["role"] = state ? state.role : undefined;
            inputs["teamId"] = state ? state.teamId : undefined;
            inputs["username"] = state ? state.username : undefined;
        } else {
            const args = argsOrState as TeamMembershipTeamArgs | undefined;
            if (!args || args.teamId === undefined) {
                throw new Error("Missing required property 'teamId'");
            }
            if (!args || args.username === undefined) {
                throw new Error("Missing required property 'username'");
            }
            inputs["role"] = args ? args.role : undefined;
            inputs["teamId"] = args ? args.teamId : undefined;
            inputs["username"] = args ? args.username : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        super("github:index/teamMembershipTeam:TeamMembershipTeam", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TeamMembershipTeam resources.
 */
export interface TeamMembershipTeamState {
    readonly etag?: pulumi.Input<string>;
    readonly role?: pulumi.Input<string>;
    readonly teamId?: pulumi.Input<string>;
    readonly username?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TeamMembershipTeam resource.
 */
export interface TeamMembershipTeamArgs {
    readonly role?: pulumi.Input<string>;
    readonly teamId: pulumi.Input<string>;
    readonly username: pulumi.Input<string>;
}