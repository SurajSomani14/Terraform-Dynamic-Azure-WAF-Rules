# Define the WAF policy resource
resource "azurerm_web_application_firewall_policy" "{app_gateway_name}" {{
  name                = "{app_gateway_name}"
  resource_group_name = "{resource_group_name}"
  location            = "{location}"

  policy_settings {{
    enabled                     = true
    mode                        = "Prevention"
    request_body_check          = true
    file_upload_limit_in_mb     = 100
    max_request_body_size_in_kb = 128
  }}

   managed_rules {{
    managed_rule_set {{
      type    = "OWASP"
      version = "3.2"
      }}
   }}

  # Custom rules section

    {custom_rules_section}  
}}