-- Challenge 1: 고양이와 개는 몇마리 있을까
SELECT
    ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS COUNT
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE


-- Challenge 2: 동명 동물 수 찾기
SELECT 
    NAME, COUNT(NAME) AS COUNT 
FROM ANIMAL_INS 
WHERE NAME IS NOT NULL
GROUP BY NAME 
HAVING COUNT >= 2


-- Challenge 3: 동명 동물 수 찾기
SELECT 
    SUBSTRING(DATETIME, 12, 2) AS HOUR,
    COUNT(DATETIME) AS HOUR_COUNT 
FROM ANIMAL_OUTS 
GROUP BY HOUR 
HAVING HOUR BETWEEN 9 AND 19


-- Challenge 4: 입양 시각 구하기 (1)
SELECT
    SUBSTRING(DATETIME, 12, 2) AS HOUR,
    COUNT(DATETIME) AS HOUR_COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR BETWEEN 9 AND 19;


-- Challenge 4: 입양 시각 구하기 (2)
set @hour = -1;
select
    (@hour := @hour +1) as HOUR,
    (select count(*) from animal_outs where hour(`datetime`) = @hour) as `COUNT`
from animal_outs 
where @hour < 23

