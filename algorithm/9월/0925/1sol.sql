
select a.BOARD_ID, a.WRITER_ID, a.TITLE, a.PRICE,
case
    when (a.STATUS = 'DONE') then '거래완료'
    when (a.STATUS = 'RESERVED') then '예약중'
    when (a.STATUS = 'SALE') then '판매중'
end as STATUS
from USED_GOODS_BOARD a
where date_format(a.created_date, '%Y-%m-%d') = '2022-10-05'
order by a.BOARD_ID desc