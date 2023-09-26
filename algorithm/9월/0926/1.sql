-- 코드를 입력하세요

select a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS, date_format(b.created_date, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD  a, USED_GOODS_REPLY b
where (a.created_date between '2022-10-01' and '2022-10-31')
and a.board_id = b.board_id
order by b.created_date, a.title