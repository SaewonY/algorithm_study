-- Challenge 1: 모든 레코드 조회하기
SELECT
    *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

-- Challenge 2: 역순 정렬하기
SELECT
    NAME,
    DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;

-- Challenge 3: 아픈 동물 찾기
SELECT
    ANIMAL_ID,
    NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick';

-- Challenge 4: 어린 동물 찾기
SELECT
    ANIMAL_ID,
    NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged';

-- Challenge 5: 여러 기준으로 정렬하기
SELECT
    ANIMAL_ID,
    NAME,
    DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;

-- Challenge 6: 상위 n개 코드
SELECT
    NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
