-- 코드를 입력하세요

-- 동물 이름 중 두번이상 쓰인 이름 AND 해당 이름이 쓰인 횟수 조회

-- 이때 결과 이름없는 동물은 제외, 결과는 이름순

SELECT NAME, COUNT(*) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME