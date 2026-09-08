from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/foundry-validation.yml"


class WorkflowLoader(yaml.SafeLoader):
    pass


WorkflowLoader.yaml_implicit_resolvers = {
    key: [
        resolver
        for resolver in resolvers
        if resolver[0] != "tag:yaml.org,2002:bool"
    ]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def test_consumer_pins_public_action_and_contains_no_skill() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    workflow = yaml.load(text, Loader=WorkflowLoader)
    assert {"pull_request", "merge_group", "push", "workflow_dispatch"} <= set(
        workflow["on"]
    )
    assert workflow["permissions"] == {
        "contents": "read",
        "copilot-requests": "write",
    }
    assert "head.repo.full_name == github.repository" in workflow["jobs"]["validate"]["if"]
    assert re.search(
        r"uses: XiaofuHuang/foundry-hosted-agent-validator-action@[0-9a-f]{40}",
        text,
    )
    assert "github-token: ${{ github.token }}" in text
    assert "agent-path: ." in text
    assert "pull_request_target" not in text
    assert not (ROOT / ".github/skills").exists()
