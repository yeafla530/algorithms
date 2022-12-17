-- 코드를 입력하세요

-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회

-- 보호 시작일이 빠른 순으로 조회

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A
    JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME > B.DATETIME
ORDER BY A.DATETIME