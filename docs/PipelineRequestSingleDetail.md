# PipelineRequestSingleDetail

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | 
**pipeline** | **str** | [optional] 
**version** | **str** | 
**status** | **str** | 
**success** | **bool** | [optional] 
**time_created** | **datetime** | 
**time_started** | **datetime** | [optional] 
**time_completed** | **datetime** | [optional] 
**request_data** | **str** or **dict(str, str)** | [optional] 
**result** | **str** or **dict(str, str)** | [optional] 
**deployment_requests** | [**list[PipelineRequestDeploymentRequest]**](PipelineRequestDeploymentRequest.md) | 
**error_message** | **str** | [optional] 
**created_by** | **str** | [optional] [readonly] 
**notification_group** | **str** | [optional] 


