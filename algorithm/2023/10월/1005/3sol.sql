-- solvesql 버뮤다 삼각지대에 들어가버린 택배

select
  strftime ('%Y-%m-%d', order_delivered_carrier_date) as delivered_carrier_date,
  count(*) as orders
from
  olist_orders_dataset
where
  order_delivered_carrier_date >= '2017-01-01'
  and order_delivered_carrier_date < '2017-02-01'
  and order_delivered_customer_date is null
group by
  delivered_carrier_date