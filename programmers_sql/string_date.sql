-- Challenge 1: 루시와 엘라 찾기
SELECT
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID


-- Challenge 2: 이름에 el이 들어가는 동물 찾기
SELECT
    ANIMAL_ID,
    NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%El%' AND ANIMAL_TYPE LIKE 'Dog'
ORDER BY NAME


-- Challenge 3: 중성화 여부 파악하기
SELECT
    ANIMAL_ID,
    NAME,
    IF (SEX_UPON_INTAKE LIKE "Intact%", 'X', 'O') as '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


-- Challenge 4: 오랜 기간 보호한 동물(2)
SELECT 
    o.ANIMAL_ID, 
    o.NAME
FROM ANIMAL_OUTS o, ANIMAL_INS i
WHERE o.ANIMAL_ID = i.ANIMAL_ID
ORDER BY DATEDIFF(o.DATETIME, i.DATETIME) DESC
limit 2


-- Challenge 5: DATETIME에서 DATE로 형 변환
SELECT
    ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,'%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS





