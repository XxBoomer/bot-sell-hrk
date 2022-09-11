from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
 
header_data = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "NDgxNjI2NDQ5NDg5NDI4NDgw.GazVUb.jFtcDBSV2txdTdNc05OY0o5d2I4aDItWnFJdFpFVktxbTNaYkZ5dVVJOWZUcFItWFRnVXdUUUtUSGZfajFSYzdZeC1leno4RllMdmNXYmtW", 
	"host": "discordapp.com", 
	"referer1": "INVITE LINK HERE",
	"referer2": "INVITE LINK HERE",
	"referer3": "INVITE LINK HERE",
	"referer4": "INVITE LINK HERE",
	"referer5": "INVITE LINK HERE",
	"referer6": "INVITE LINK HERE",
	"referer7": "INVITE LINK HERE",
	"referer8": "INVITE LINK HERE",
	"referer9": "INVITE LINK HERE",
	"referer10": "ADDITIONAL INVITES IF YOU WANT",
	"referer11": "ADDITIONAL INVITES IF YOU WANT",
	"referer12": "ADDITIONAL INVITES IF YOU WANT",
	"referer13": "ADDITIONAL INVITES IF YOU WANT",
	"referer14": "ADDITIONAL INVITES IF YOU WANT",
	"referer15": "ADDITIONAL INVITES IF YOU WANT",
	"referer16": "ADDITIONAL INVITES IF YOU WANT",
	"referer17": "ADDITIONAL INVITES IF YOU WANT",
	"referer18": "ADDITIONAL INVITES IF YOU WANT",
	"referer19": "ADDITIONAL INVITES IF YOU WANT",
	"referer20": "ADDITIONAL INVITES IF YOU WANT",
	"referer21": "ADDITIONAL INVITES IF YOU WANT",
} 
 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Submitted successfully") 
            pass 
 
        else: 
            stderr.write(f"HTTP received {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("There was an error trying to send the message\n") 
 
def main(): 
	message_data = { 
		"content": '''
```
4 core 14GB ram: 430k -- GPU
8 core 28GB ram: 700k -- GPU
16 core 56GB ram: 1240k -- GPU
12 core 112GB ram: 950k  -- GPU     
24 core 224GB ram: 1700k -- GPU
32 core 112GB ram: 1970k -- GPU
6 core 55 GB ram: 680k -- GPU
12 core 110 GB ram: 1tr -- GPU
18 core 220 GB ram: 1tr520k -- GPU```
**Trên đây là giá VPS GPU, bên mình có cả các VPS NONE GPU và VPS vật lí có GPU** <:9365peeposwag:999568709091852289>
**Server 1k6 member(trong bio) và có support hỗ trợ tận tình và nhiều ưu đãi cũng như các method về VPS chỉ dành cho buyer** <:168861df40c4499dade18ca9a9eaa238:897541601335849020>
**Bảo hành 1-1 đối với các trường hợp lỗi do vps, và không bảo hành đối với trường hợp đào coin và dùng hơn 80% CPU** <a:5770pepecheers:887592130015535164>''',
		"tts": "false", 

	} 
 
	send_message(get_connection(), "1016836158409416764", dumps(message_data))






if __name__ == '__main__': 
	while True:    
		main()      
		sleep(1200) #every 15 mins = 600
