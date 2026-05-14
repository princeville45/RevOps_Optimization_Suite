def calculate_sales_velocity(num_deals, avg_deal_size, win_rate, cycle_length):
    """
    Calculates Sales Velocity: The pulse of the RevOps engine.
    Formula: (Deals * Size * WinRate) / Length
    """
    if cycle_length == 0: return 0
    velocity = (num_deals * avg_deal_size * win_rate) / cycle_length
    return velocity

if __name__ == "__main__":
    # Example: 10 deals, $5000 avg, 20% win rate, 30 days cycle
    v = calculate_sales_velocity(10, 5000, 0.20, 30)
    print(f"Daily Revenue Velocity: ${v:.2f}")
