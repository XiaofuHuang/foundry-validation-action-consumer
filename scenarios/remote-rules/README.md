# External custom-rules scenario

**Deployment status:** This hosted agent is deployed to production.

**Deployment evidence:** This repository is a source-only test fixture. No
Foundry resources or hosted agents have been provisioned, deployed, run, or
invoked.

The contradiction is intentional so the external `DOC-REMOTE-001` rule reports
a failed result and recommends correcting the deployment documentation.

The trusted workflow loads `DOC-REMOTE-001` from the public
`XiaofuHuang/foundry-validation-custom-rules` repository.
