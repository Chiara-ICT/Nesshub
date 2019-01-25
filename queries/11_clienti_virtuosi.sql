-- Clients ordered by number of sent receipts
SELECT sendervat, COUNT(sendervat) 
FROM nesshub.documents 
GROUP BY sendervat 
ORDER BY COUNT(uuid) DESC;

-- Clients ordered by number of received receipts 
SELECT recipientvat, COUNT(uuid)
FROM nesshub.documents
GROUP BY recipientvat 
ORDER BY COUNT(uuid) DESC;