-- 코드를 입력하세요
-- 공간의 아이디, 이름, 임대 가능한 일수
-- 공간의 아이디순
-- 예약 가능한 날이 없는 공간은 제외
SELECT A.ID, A.NAME, COUNT(*) AS "임대 가능일" 
FROM PLACES A
JOIN SCHEDULES B ON A.ID = B.PLACE_ID
GROUP BY A.ID HAVING COUNT(*) > 1
ORDER BY A.ID
