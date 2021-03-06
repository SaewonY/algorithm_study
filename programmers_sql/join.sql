-- Challenge 1: 없어진 기록 찾기
SELECT 
    o.ANIMAL_ID,
    o.NAME
FROM ANIMAL_OUTS o
LEFT JOIN ANIMAL_INS i
ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE i.DATATIME IS NULL


-- Challenge 2: 있었는데요 없었습니다
SELECT
    o.ANIMAL_ID,
    o.NAME
FROM ANIMAL_OUTS o
LEFT JOIN ANIMAL_INS i
ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE o.DATETIME <  i.DATETIME
ORDER BY i.DATETIME


-- Challenge 3: 오랜 기간 보호한 동물(1)
SELECT
    o.ANIMAL_ID,
    o.NAME
FROM ANIMAL_OUTS o
LEFT JOIN ANIMAL_INS i
ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE o.ANIMAL_ID IS NULL
ORDER BY i.DATETIME
LIMIT 3


-- Challenge 4: 보호소에서 중성화한 동물
SELECT
    o.ANIMAL_ID,
    o.ANIMAL_TYPE,
    o.NAME
FROM ANIMAL_OUTS o
LEFT JOIN ANIMAL_INS i
ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE i.SEX_UPON_INTAKE  LIKE '%Intact%' AND o.SEX_UPON_OUTCOME NOT LIKE '%Intact%'
ORDER BY ANIMAL_ID;
