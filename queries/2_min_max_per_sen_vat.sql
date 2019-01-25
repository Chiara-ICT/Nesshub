SELECT d.sendervat, COUNT(d.sendervat), MIN(d.payableamount), MAX(d.payableamount)
FROM nesshub.documents AS d
GROUP BY d.sendervat

