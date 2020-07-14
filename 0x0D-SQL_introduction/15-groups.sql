-- list records with same score
-- scores must be in the "second_table" table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
