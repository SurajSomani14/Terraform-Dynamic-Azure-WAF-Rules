import json
import os
import customRulesTemplate as rules

current_dir = os.getcwd()

    # Construct the file path by joining the current directory path and the Filelocation
file_path = os.path.join(current_dir, "config.json")


# Read the configuration from the config.json file
with open(file_path, "r") as config_file:
    configList = json.load(config_file)

for config in configList:

    file_path = os.path.join(current_dir, config["waf_rules_config"])

    # Read the JSON configuration file for WAF rules
    with open(file_path, "r") as waf_rules_file:
        waf_rules = json.load(waf_rules_file)

    file_path = os.path.join(current_dir, "terraform_template.tpl")

    # Read the Terraform template from the separate file
    with open(file_path, "r") as template_file:
        tf_template = template_file.read()

    # Generate the custom rules section dynamically
    custom_rules_section = ""
    for rule in waf_rules:    
        custom_rule = getattr(rules, rule["name"])
        custom_rule=custom_rule.format(values=rule["match_values"])

        custom_rules_section += custom_rule
        custom_rules_section +="\n"

    # Fill in the template with the configuration values and custom rules section
    tf_config = tf_template.format(
        app_gateway_name=config["resource_name"],
        resource_group_name=config["resource_group_name"],
        location=config["location"],
        custom_rules_section=custom_rules_section.replace("'",'"')
    )

    # Save the generated Terraform configuration to a file
    with open("TerraformArtifacts/"+config["resource_name"]+"_generated.tf", "w") as tf_file:
        tf_file.write(tf_config)

# Read the Azure provider tf file and copy to artifacts 
file_path = os.path.join(current_dir,"provider.tf")

with open(file_path, "r") as provider_file:
    provider = provider_file.read()

    # Save the generated Terraform configuration to a file
with open("TerraformArtifacts/provider.tf", "w") as tf_file:
    tf_file.write(provider)