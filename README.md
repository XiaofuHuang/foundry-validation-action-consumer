# Reusable Foundry validator Action consumer

This private repository demonstrates cross-repository use of the public
`XiaofuHuang/foundry-hosted-agent-validator-action` GitHub Action.

The pull request contains the pinned official Microsoft Agent Framework
Responses `01-basic` sample and a small caller workflow. The workflow pins the
published Action by full commit SHA. It does not contain a validation skill.

## Security boundary

- Pull-request files are untrusted evidence.
- The validator must not execute or import target code.
- The validator must not install target dependencies, use Docker, authenticate
  to or query Azure, provision, deploy, or invoke the hosted agent.
- Fork pull requests do not run the Copilot step.
- Only `.foundry/results/` may be written by validation.

## Not deployed

The sample hosted agent has not been run, provisioned, invoked, or deployed.

