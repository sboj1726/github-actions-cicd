# GitHub Actions CI/CD

CI workflow for Python validation and Docker image build.

## Workflow
Push / Pull Request -> Python validation -> Unit tests -> Docker build

The workflow intentionally does not push images to a registry. Add registry credentials through GitHub Secrets before enabling a production push stage.
