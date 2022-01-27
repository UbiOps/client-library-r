# PipelineVersionCreate

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**version** | **str** | 
**description** | **str** | [optional] 
**labels** | **dict(str, str)** | [optional] 
**monitoring** | **str** | [optional] 
**request_retention_time** | **int** | [optional] 
**request_retention_mode** | **str** | [optional] [default to 'full']
**default_notification_group** | **str** | [optional] 
**objects** | [**list[PipelineVersionObjectCreate]**](PipelineVersionObjectCreate.md) | [optional] 
**attachments** | [**list[AttachmentsCreate]**](AttachmentsCreate.md) | [optional] 


