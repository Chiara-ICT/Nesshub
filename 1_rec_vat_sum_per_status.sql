SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

SELECT d.sendervat, d.recipientvat, SUM(d.payableamount), d.status
FROM nesshub.documents AS d
GROUP BY d.status, d.recipientvat