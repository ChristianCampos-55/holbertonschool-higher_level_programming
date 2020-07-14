-- list records with a certain score
-- the score must be >= 10 and be in "second_table"
SELECT score, name FROM second_table WHERE score >=10 ORDER BY score DESC;
