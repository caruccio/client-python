# V1PodSecurityPolicyReview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**spec** | [**V1PodSecurityPolicyReviewSpec**](V1PodSecurityPolicyReviewSpec.md) | spec is the PodSecurityPolicy to check. | 
**status** | [**V1PodSecurityPolicyReviewStatus**](V1PodSecurityPolicyReviewStatus.md) | status represents the current information/status for the PodSecurityPolicyReview. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


