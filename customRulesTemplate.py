BlockIP="""custom_rules {{
      name          = "BlockIP"
      priority      = 10
      action        = "Block"
      enabled   = true
      rule_type     = "MatchRule"
      match_conditions {{
      match_variables {{
        variable_name = "RemoteAddr"
        }}
        match_values = {values}
        operator = "IPMatch"
        negation_condition = false
    
      }}
    }}"""

AllowIP="""custom_rules {{
      name          = "AllowIP"
      priority      = 20
      action        = "Allow"
      rule_type     = "MatchRule"
      match_conditions {{
      match_variables {{
        variable_name = "RemoteAddr"
        }}
        match_values = {values}
        operator = "IPMatch"
        negation_condition = false
    
      }}
    }}
"""

BlockUri="""custom_rules {{
      name          = "BlockUri"
      priority      = 30
      action        = "Block"
      rule_type     = "MatchRule"
      match_conditions {{
      match_variables {{
        variable_name = "RequestUri"
        }}
        match_values = ["example.com"]
        operator = "Contains"
        negation_condition = false
    
      }}
    }}
"""