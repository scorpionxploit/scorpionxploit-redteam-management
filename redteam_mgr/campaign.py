"""
ScorpionXploit Red Team Management Framework
Inspired by Joas Santos' Red-Team-Management
Author: Aditya Sharma (scorpionxploit)
License: MIT
"""
from dataclasses import dataclass
from typing import List, Set
import ipaddress

@dataclass
class RedTeamCampaign:
    campaign_id: str
    target_organization: str
    approved_subnets: List[str]
    active_threat_actor_persona: str

class RedTeamManager:
    def __init__(self, campaign: RedTeamCampaign):
        self.campaign = campaign
        self.networks = [ipaddress.ip_network(s) for s in campaign.approved_subnets]

    def is_in_scope(self, ip_str: str) -> bool:
        try:
            ip = ipaddress.ip_address(ip_str)
            return any(ip in net for net in self.networks)
        except ValueError:
            return False
