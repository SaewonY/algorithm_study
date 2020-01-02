-- Challenge 1: 최댓값 구하기
SELECT
    DATETIME AS '시간'
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;


-- Challenge 2: 최솟값 구하기 
SELECT
    DATETIME AS '시간'
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;


-- Challenge 3: 동물 수 구하기 
SELECT
    COUNT(*)
FROM ANIMAL_INS;


-- Challenge 4: 중복 제거하기 
SELECT
    COUNT(DISTINCT(Name)) AS count
FROM ANIMAL_INS;


-- Challenge 5: 중복 제거하기 
