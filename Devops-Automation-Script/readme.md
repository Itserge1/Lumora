## Setup Virtual Environment

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

---

## Install and Use the Tool

To install the tool in editable mode (for local development):

```bash
pip install --editable .
```

Run the CLI command:

```shell
export AWS_PROFILE=AdministratorAccess-318526443004
```

```bash
devops-auto create-db-creds --dbname lumora-dev
```

---

## Updating After Changes

If you make updates to the application package or dependencies, uninstall the old version first:

```bash
pip uninstall devops-auto
```

Then update your dependencies file:

```bash
pip freeze > requirements.txt
```