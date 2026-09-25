import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestWorkflowGen(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_compilation(self):
        res = self.client.post("/compile-workflow", json={"description": "Sync stripe to hubspot with AI filtering", "target_platform": "n8n"})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["platform"], "n8n")
        self.assertIn("nodes", data["schema_json"])

if __name__ == "__main__":
    unittest.main()
