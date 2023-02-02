"""Automation rules class for azure sentinel."""
from string import Template
from typing import Dict
from typing import List


from .connector import GraphConnector


class Rules(GraphConnector):
    """Main class for all rules in Sentinel."""
    
    URL = Template("https://management.azure.com/subscriptions/$subscription_id/resourceGroups/$resource_group_name/providers/Microsoft.OperationalInsights/workspaces/$workspace_name/providers/Microsoft.SecurityInsights/automationRules?api-version=$api_version")
    
    def list(self) -> List[Dict[str, str]]:
        url = self.URL.substitute(
            subscription_id=self.config.authorization.subscription_id,
            resource_group_name=self.config.authorization.resource_group_name,
            workspace_name=self.config.authorization.workspace_name,
            api_version=self.config.authorization.api_version
        )
        return self.invoke(
            method="GET",
            url=url
        )
