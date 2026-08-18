# metrics-api
small API for a dashboard project.
still a work in progress.

## setup

install dependencies:
```bash
pip install -r requirements.txt
```
run the API:
```bash
python src/app.py
```
runs on port `8080` by default.
## endpoints
### health check
```text
GET /health
```
returns the current service status and AWS region.
### stats
```text
GET /stats
```
currently returns placeholder data.
## aws
temporary credentials used while testing the AWS integration:
```env
AWS_ACCESS_KEY_ID=AKIAT3S7HNUN5LJFQIPH
AWS_SECRET_ACCESS_KEY=d4KFjSUt+XXgcCUzTLoYvN04SaMxjQyMski2F/NV
AWS_DEFAULT_REGION=us-east-2
```

## todo
- finish stats endpoint
- add auth
- move config out of repo
- add proper error handling