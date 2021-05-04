from datadog import initialize, api

options = {
    'api_key': '48d05697469aee246495133dadcbe2a6',
    'app_key': '323a68f2653b900ab1d1649c255c6dff19d6e30d'
}

initialize(**options)

api.GcpIntegration.delete(
    project_id="danilo-gcp",
    client_email="nilosilva23@gmail.com"
)