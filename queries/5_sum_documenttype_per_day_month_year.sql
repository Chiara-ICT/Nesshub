SELECT issuedate, COUNT(uuid), documenttype, SUM(payableamount) FROM nesshub.documents
GROUP BY documenttype, DAY(issuedate)
ORDER BY issuedate ASC;

SELECT issuedate, COUNT(uuid), documenttype, SUM(payableamount), receiveddate FROM nesshub.documents
GROUP BY documenttype, MONTH(issuedate)
ORDER BY issuedate ASC;

SELECT issuedate, COUNT(uuid), documenttype, SUM(payableamount), receiveddate FROM nesshub.documents
GROUP BY documenttype, YEAR(issuedate)
ORDER BY YEAR(issuedate);