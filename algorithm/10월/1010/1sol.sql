-- 프로그래머스 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기

select
    concat('/home/grep/src/',f.board_id,'/',f.file_id,f.file_name,f.file_ext) as file_path
from
    used_goods_file as f
join
    used_goods_board as b
on
    f.board_id = b.board_id
where
    b.views = (select max(views) from used_goods_board)
order by
    file_id desc