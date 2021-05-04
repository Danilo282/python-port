from datadog import initialize, api

options = {
    'api_key': '',
    'app_key': ''
}

initialize(**options)

api.GcpIntegration.delete(
    project_id="",
    client_email=""
)
