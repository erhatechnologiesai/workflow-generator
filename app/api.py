from fastapi import FastAPI
from app.config import settings
from app.models import WorkflowRequirement, WorkflowExport
from app.services.flow_compiler import compile_workflow

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/compile-workflow", response_model=WorkflowExport)
def compile(req: WorkflowRequirement):
    name, schema = compile_workflow(req.description, req.target_platform)
    return WorkflowExport(workflow_name=name, platform=req.target_platform, schema_json=schema)
