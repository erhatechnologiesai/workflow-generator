def compile_workflow(desc: str, platform: str):
    name = f"Generated_{platform.capitalize()}_Workflow"
    schema = {
        "name": name,
        "nodes": [
            {"id": "1", "name": "Webhook Inbound", "type": "n8n-nodes-base.webhook", "position": [100, 300]},
            {"id": "2", "name": "AI Sentiment Filter", "type": "n8n-nodes-base.openAi", "position": [350, 300]},
            {"id": "3", "name": "CRM Sync", "type": "n8n-nodes-base.hubspot", "position": [600, 300]}
        ],
        "connections": {
            "Webhook Inbound": {"main": [[{"node": "AI Sentiment Filter", "type": "main", "index": 0}]]},
            "AI Sentiment Filter": {"main": [[{"node": "CRM Sync", "type": "main", "index": 0}]]}
        }
    }
    return name, schema
