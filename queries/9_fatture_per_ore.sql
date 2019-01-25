SELECT HOUR(receiveddate) , COUNT(HOUR(receiveddate))
FROM nesshub.documents
GROUP BY HOUR(receiveddate);