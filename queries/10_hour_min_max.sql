SELECT HOUR(receiveddate) , COUNT(HOUR(receiveddate))
FROM nesshub.documents
GROUP BY HOUR(receiveddate)
ORDER BY COUNT(HOUR(receiveddate)) DESC;

-- Best hour
SELECT HOUR(receiveddate) , COUNT(HOUR(receiveddate))
FROM nesshub.documents
GROUP BY HOUR(receiveddate)
ORDER BY COUNT(HOUR(receiveddate)) DESC
LIMIT 1;

-- Worst hour
SELECT HOUR(receiveddate) , COUNT(HOUR(receiveddate))
FROM nesshub.documents
GROUP BY HOUR(receiveddate)
ORDER BY COUNT(HOUR(receiveddate)) ASC
LIMIT 1;
