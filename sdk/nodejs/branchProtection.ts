// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class BranchProtection extends pulumi.CustomResource {
    /**
     * Get an existing BranchProtection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BranchProtectionState, opts?: pulumi.CustomResourceOptions): BranchProtection {
        return new BranchProtection(name, <any>state, { ...opts, id: id });
    }

    public readonly branch: pulumi.Output<string>;
    public readonly enforceAdmins: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly etag: pulumi.Output<string>;
    public readonly repository: pulumi.Output<string>;
    public readonly requiredPullRequestReviews: pulumi.Output<{ dismissStaleReviews?: boolean, dismissalTeams?: string[], dismissalUsers?: string[], includeAdmins?: boolean, requireCodeOwnerReviews?: boolean } | undefined>;
    public readonly requiredStatusChecks: pulumi.Output<{ contexts?: string[], includeAdmins?: boolean, strict?: boolean } | undefined>;
    public readonly restrictions: pulumi.Output<{ teams?: string[], users?: string[] } | undefined>;

    /**
     * Create a BranchProtection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BranchProtectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BranchProtectionArgs | BranchProtectionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: BranchProtectionState = argsOrState as BranchProtectionState | undefined;
            inputs["branch"] = state ? state.branch : undefined;
            inputs["enforceAdmins"] = state ? state.enforceAdmins : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["repository"] = state ? state.repository : undefined;
            inputs["requiredPullRequestReviews"] = state ? state.requiredPullRequestReviews : undefined;
            inputs["requiredStatusChecks"] = state ? state.requiredStatusChecks : undefined;
            inputs["restrictions"] = state ? state.restrictions : undefined;
        } else {
            const args = argsOrState as BranchProtectionArgs | undefined;
            if (!args || args.branch === undefined) {
                throw new Error("Missing required property 'branch'");
            }
            if (!args || args.repository === undefined) {
                throw new Error("Missing required property 'repository'");
            }
            inputs["branch"] = args ? args.branch : undefined;
            inputs["enforceAdmins"] = args ? args.enforceAdmins : undefined;
            inputs["repository"] = args ? args.repository : undefined;
            inputs["requiredPullRequestReviews"] = args ? args.requiredPullRequestReviews : undefined;
            inputs["requiredStatusChecks"] = args ? args.requiredStatusChecks : undefined;
            inputs["restrictions"] = args ? args.restrictions : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        super("github:index/branchProtection:BranchProtection", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BranchProtection resources.
 */
export interface BranchProtectionState {
    readonly branch?: pulumi.Input<string>;
    readonly enforceAdmins?: pulumi.Input<boolean>;
    readonly etag?: pulumi.Input<string>;
    readonly repository?: pulumi.Input<string>;
    readonly requiredPullRequestReviews?: pulumi.Input<{ dismissStaleReviews?: pulumi.Input<boolean>, dismissalTeams?: pulumi.Input<pulumi.Input<string>[]>, dismissalUsers?: pulumi.Input<pulumi.Input<string>[]>, includeAdmins?: pulumi.Input<boolean>, requireCodeOwnerReviews?: pulumi.Input<boolean> }>;
    readonly requiredStatusChecks?: pulumi.Input<{ contexts?: pulumi.Input<pulumi.Input<string>[]>, includeAdmins?: pulumi.Input<boolean>, strict?: pulumi.Input<boolean> }>;
    readonly restrictions?: pulumi.Input<{ teams?: pulumi.Input<pulumi.Input<string>[]>, users?: pulumi.Input<pulumi.Input<string>[]> }>;
}

/**
 * The set of arguments for constructing a BranchProtection resource.
 */
export interface BranchProtectionArgs {
    readonly branch: pulumi.Input<string>;
    readonly enforceAdmins?: pulumi.Input<boolean>;
    readonly repository: pulumi.Input<string>;
    readonly requiredPullRequestReviews?: pulumi.Input<{ dismissStaleReviews?: pulumi.Input<boolean>, dismissalTeams?: pulumi.Input<pulumi.Input<string>[]>, dismissalUsers?: pulumi.Input<pulumi.Input<string>[]>, includeAdmins?: pulumi.Input<boolean>, requireCodeOwnerReviews?: pulumi.Input<boolean> }>;
    readonly requiredStatusChecks?: pulumi.Input<{ contexts?: pulumi.Input<pulumi.Input<string>[]>, includeAdmins?: pulumi.Input<boolean>, strict?: pulumi.Input<boolean> }>;
    readonly restrictions?: pulumi.Input<{ teams?: pulumi.Input<pulumi.Input<string>[]>, users?: pulumi.Input<pulumi.Input<string>[]> }>;
}
