-- 코드를 입력하세요

-- 입양 못간 동물 가장 오래된 순으로 보호소에 있었던 동물 3마리

-- 이름, 보호 시작일 조회

SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A
    LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID