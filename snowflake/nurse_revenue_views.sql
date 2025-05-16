-- nurse_revenue_views.sql
-- Snowflake view for nurse revenue ranking

CREATE OR REPLACE VIEW nurse_revenue_ranking AS
SELECT
    nurse_id,
    department,
    net_paid,
    net_profit,
    (net_paid + net_profit) AS revenue,
    RANK() OVER (PARTITION BY department ORDER BY (net_paid + net_profit) DESC) AS rank
FROM nurse_revenue_data;
