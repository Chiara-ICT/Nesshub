-- Number of receipts for each senderVAT
SELECT sendervat, COUNT(sendervat), SUM(payableamount) -- uuid, documentid, documenttype, filename, issuedate, payableamount, receiveddate, recipientname, recipientvat, sendername, sendervat, status, processingrequest_uuid 
FROM nesshub.documents
GROUP BY sendervat
ORDER BY SUM(payableamount) DESC;

-- Number of receipts for each recipientVAT
SELECT recipientvat, COUNT(recipientvat), SUM(payableamount) -- , uuid, documentid, documenttype, filename, issuedate, payableamount, receiveddate, recipientname, recipientvat, sendername, sendervat, status, processingrequest_uuid 
FROM nesshub.documents
GROUP BY sendervat
ORDER BY SUM(payableamount) DESC;

-- Number of passive receipts (ricevute?)  
SELECT r.documenttype, COUNT(r.documenttype), SUM(payableamount) -- , d.uuid, d.documentid, d.documenttype, d.filename, d.issuedate, d.payableamount, d.receiveddate, d.recipientname, d.recipientvat, d.sendername, d.sendervat, d.status 
FROM nesshub.documents AS d
JOIN nesshub.processingrequests AS r ON d.uuid = r.uuid
WHERE r.documenttype = 'CICLO_PASSIVO' OR r.documenttype = 'NOTIFICHE'
GROUP BY r.documenttype; -- OUT

-- Number of active receipts (inviate?)
SELECT r.documenttype, COUNT(r.documenttype), SUM(payableamount) -- , d.uuid, d.documentid, d.documenttype, d.filename, d.issuedate, d.payableamount, d.receiveddate, d.recipientname, d.recipientvat, d.sendername, d.sendervat, d.status 
FROM nesshub.documents AS d
JOIN nesshub.processingrequests AS r ON d.uuid = r.uuid
WHERE r.documenttype <> 'CICLO_PASSIVO' AND r.documenttype <> 'NOTIFICHE'
GROUP BY r.documenttype; -- IN 

-- Number of receipts per day of the week
SELECT DAYNAME(issuedate), COUNT(DAYOFWEEK(issuedate)), SUM(payableamount) -- uuid, documentid, documenttype, filename, issuedate, payableamount, receiveddate, recipientname, recipientvat, sendername, sendervat, status, processingrequest_uuid 
FROM nesshub.documents
GROUP BY DAYOFWEEK(issuedate);
