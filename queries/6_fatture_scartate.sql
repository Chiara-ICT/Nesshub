SELECT d.*, r.status FROM nesshub.documents AS d 
JOIN nesshub.processingrequests AS r ON d.uuid = r.uuid
WHERE d.status = 'NotificaScarto' OR r.status = 'NotificaScarto';

-- The uuid '8e244bc1-e0c2-40da-8634-c052e0dd44e5' shows d.status = 'TRASMESSO', but r.status = 'NotificaScarto'
