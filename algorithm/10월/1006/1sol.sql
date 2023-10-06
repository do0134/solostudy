-- solvesql 쇼핑몰의 일일 매출액

select
  strftime('%Y-%m-%d',a.order_purchase_timestamp) as dt,
  round(sum(b.payment_value),2) as revenue_daily
from
  olist_orders_dataset a
join
  olist_order_payments_dataset b
on
  a.order_id = b.order_id and dt >= '2018-01-01'
group by dt
order by dt