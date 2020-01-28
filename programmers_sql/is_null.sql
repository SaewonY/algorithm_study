-- Challenge 1: 이름이 없는 동물의 아이디
SELECT
    ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL


-- Challenge 2: 이름이 있는 동물의 아이디
SELECT
    ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL


-- Challenge 3: NULL 처리하기
SELECT
    ANIMAL_TYPE,
    IFNULL(NAME, "No name") AS NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS
