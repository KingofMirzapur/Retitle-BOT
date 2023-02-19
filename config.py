import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "8481654")

API_HASH = os.environ.get("API_HASH", "2f1a45429dd34aceb56cbd66f1516bbc")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5760131586:AAECW0ACbLdMP98bPOfplq7CG8HE-sqz5Aw") 

FORCE_SUB = os.environ.get("FORCE_SUB", "RR_Studioo") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://iamravimehra:#Rocky7763918488@cluster0.zncol70.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/e9a53e42c5843cabc360a.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '755436524').split()]

PORT = os.environ.get("PORT", "8080")
