## MYSQL

[TOC]

### 실행 순서

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT



### AS

* 별명으로 처리

```mysql
SELECT DATE_FORMAT(JOINED, '%Y-%m-%d') AS JOINED
```

* NULL도 처리 가능

```mysql
SELECT NULL AS USER_ID
```



### ROUND

* 반올림
* 두번째 소수점까지 표기

```mysql
SELECT A.ADDRESS, ROUND(AVG(B.REVIEW_SCORE), 2) AS SCORE 
```



### GROUP BY ... HAVING

* GROUP BY는 특정 컬럼을 그룹화 할 때 사용
* WHERE은 그룹화 하기 전 조건
* HAVING은 그룹화한 후에 조건

```mysql
-- 코드를 입력하세요
SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, ROUND(AVG(B.REVIEW_SCORE), 2) AS SCORE 
FROM REST_INFO A
JOIN REST_REVIEW B ON A.REST_ID = B.REST_ID
-- ID별로 묶음, GROUP BY 안하는 경우 모든 가게 SCORE의 평균을 구함
-- GROUP BY 사용 시 REST_ID별 SCORE를 구해줌
GROUP BY A.REST_ID 
HAVING A.ADDRESS LIKE '서울%'
```



### WHERE 

* 날짜 형식도 부등호로 조건문이 가능

```mysql
WHERE SALES_DATE >= '2022-03-01' AND SELES_DATE < '2022-04-01'
```



### WHERE IN

* WHERE 일치하길 원하는 컬럼명 IN (조건1, 조건2, ...)



### DATE_FORMAT()

* 날짜 형식 변경
* %Y-%m-%d => '2021-12-13' 형식

```mysql
SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE AGE >= 20 AND AGE <= 29 AND DATE_FORMAT(JOINED, '%Y') = '2021'
```



### LIMIT

* 몇개까지 표시할 것인지

```mysql
ORDER BY NAME LIMIT 1
```



### IS NULL / IS NOT NULL

* NULL이 아닌 경우

```mysql
WHERE DATE_FORMAT(DATE_OF_BIRTH, '%m') = '03' 
AND GENDER = 'W'
AND TLNO IS NOT NULL
```



### IFNULL()

* 만약 NULL이라면

```mysql
SELECT IFNULL(NAME, 'No name')
```



### DISTINCT

* 중복 제거 
* NULL은 포함안함

```mysql
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
```



### JOIN .. ON .. 

* 테이블 결합

```mysql
SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM((BS.SALES * B.PRICE)) AS TOTAL_SALES
FROM BOOK_SALES BS
JOIN BOOK B ON BS.BOOK_ID = B.BOOK_ID
JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
```



### GROUP BY

* 종류별로 묶을 때 사용
* 각 종류 별 가장 상단의 정보들을 가져온다

```mysql
GROUP BY A.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID, B.CATEGORY DESC
```



### CASE

* IF문과 같은 문법
* CASE (WHEN, THEN, WHEN, THEN, ELSE)
* WHEN 컬럼 IN 조건으로 사용

```mysql
SELECT CAR_ID,
    -- 두가지 경우 생각
    CASE 
        WHEN CAR_ID IN (
            SELECT CAR_ID
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE) THEN '대여중'
        ELSE
            '대여가능'
            
    END "AVAILABILITY"
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
```





### BETWEEN

* A BETWEEN B : A 이상 B 이하

```
WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE
```

