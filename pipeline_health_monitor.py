from datetime import datetime, timedelta

def monitor_pipeline_health(deals, stagnation_threshold_days=14):
    """
    Flags stagnant deals that haven't moved stages in X days.
    Essential for Maintaining Pipeline Integrity.
    """
    stagnant_deals = []
    now = datetime.now()
    for deal in deals:
        last_modified = datetime.strptime(deal['last_modified'], '%Y-%m-%d')
        if (now - last_modified).days > stagnation_threshold_days:
            stagnant_deals.append(deal['id'])
    return stagnant_deals
