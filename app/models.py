from pydantic import BaseModel
from typing import List, Dict, Any

class WorkflowRequirement(BaseModel):
    description: str
    target_platform: str = "n8n" # n8n, zapier, native

class WorkflowExport(BaseModel):
    workflow_name: str
    platform: str
    schema_json: Dict[str, Any]
