## MYSQL

[TOC]

### AS

* 별명으로 처리

```
SELECT DATE_FORMAT(JOINED, '%Y-%m-%d') AS JOINED
```



### ROUND

* 반올림
* 두번째 소수점까지 표기

```
SELECT A.ADDRESS, ROUND(AVG(B.REVIEW_SCORE), 2) AS SCORE 
```



### GROUP BY ... HAVING

* GROUP BY는 특정 컬럼을 그룹화 할 때 사용
* WHERE은 그룹화 하기 전 조건
* HAVING은 그룹화한 후에 조건

```

```





### DATE_FORMAT()

* 날짜 형식 변경
* %Y-%m-%d => '2021-12-13' 형식

```
SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE AGE >= 20 AND AGE <= 29 AND DATE_FORMAT(JOINED, '%Y') = '2021'
```



### LIMIT

* 몇개까지 표시할 것인지

```
ORDER BY NAME LIMIT 1
```



