SELECT d.recipientvat, COUNT(d.recipientvat), MIN(d.payableamount), MAX(d.payableamount)
FROM nesshub.documents AS d
GROUP BY d.recipientvat