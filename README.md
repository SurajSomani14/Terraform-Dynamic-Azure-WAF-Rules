# Terraform-Dynamic-Azure-WAF-Rules
A python script that generates terraform configurations dynamically for Azure Web App Firewall Policy with custom rules. Also includes a Gitlab pipeline that will run these Terraform scripts.

## Config.json
This file contains array of azure WAF resoruces with required information.

## provider.tf
This is a terraform config file for azure provider with service principal authentication parameters. Appropriate values to be set.

## terraform_template.tpl
This is terraform template file azure WAF policy resource. It contains placeholder for custom rules to be embedded dynamically at runtime.

## customRulesTemplate.py
It contains variables for custom rules templates.

## generateTerraformUsingTemplates.py
This Python script reads config.json and for each resource, generates a terraform .tf file with custom rules. It uses terraform_template.tpl as base template generates custom rules using customRulesTemplate.py and values from waf_rules_config.json (currently only match_values are used.).

## .gitlab-ci.yml
This is a gitlab pipeline which runs pyhton script to generate terraform scripts synamically and runs them to apply custom rule changes to Azure resources.
