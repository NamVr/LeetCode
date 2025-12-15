# G1_23BCT10010_Naman-Vrati_SESSION3

SELECT s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s
LEFT JOIN
Confirmations as c
ON s.user_id= c.user_id
GROUP BY user_id;
