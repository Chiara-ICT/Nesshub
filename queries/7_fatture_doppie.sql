SELECT uuid, COUNT(uuid), issuedate, sendername, sendervat, recipientname, recipientvat, payableamount FROM nesshub.documents
GROUP BY sendername, sendervat, recipientname, recipientvat, payableamount
HAVING COUNT(uuid) > 1;

