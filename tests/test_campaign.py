"""Test suite for red team management"""
from redteam_mgr.campaign import RedTeamCampaign, RedTeamManager

def test_scope_validation():
    campaign = RedTeamCampaign(
        campaign_id="SX-OPS-01",
        target_organization="Target Corp",
        approved_subnets=["10.0.0.0/24", "192.168.1.0/24"],
        active_threat_actor_persona="APT29"
    )
    mgr = RedTeamManager(campaign)
    assert mgr.is_in_scope("10.0.0.42") is True
    assert mgr.is_in_scope("192.168.1.100") is True
    assert mgr.is_in_scope("172.16.0.1") is False
