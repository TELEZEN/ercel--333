class script(object):
    START_TXT = """Hᴇʏ {},
        Mʏ ɴᴀᴍᴇ ɪs <a href=https://t.me/{}>{}</a>,【Pʟᴇᴀsᴇ ᴜsᴇ ᴛʜᴇ ʙᴇʟᴏᴡ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ】"""
    HELP_TXT = """𝙷𝙴𝚈 {}
Tʜᴇsᴇ Aʀᴇ Tʜᴇ Aᴠᴀɪʟᴀʙʟᴇ Lɪsᴛ Oғ Mʏ Cᴏᴍᴍᴀɴᴅs."""
    ABOUT_TXT = """I AM: {}
  ✫ Cʀᴇᴀᴛᴏʀ:  <a href=@Lisa_My_Lub>Arjun Pradeep</a>
  ✫ Bᴏᴛ Uᴘᴅᴀᴛᴇs:  <a href=https://t.me/+WqhO2sfnZxcxYjk1>ERCEL</a>
  ✫ Lɪʙʀᴀʀʏ:  𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
  ✫ Lᴀɴɢᴜᴀɢᴇ:  𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
  ✫ Dᴀᴛᴀ Bᴀsᴇ:  𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
  ✫ Bᴏᴛ Sᴇʀᴠᴇʀ:  𝙷𝙴𝚁𝙾𝙺𝚄"""
    ERCEL_TXT = """I AM: {}
  𝗖𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆, 𝗙𝗶𝗹𝘁𝗲𝗿𝘀 𝗮𝗿𝗲 𝗶𝗻 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲..  
  𝘐 𝘸𝘪𝘭𝘭 𝘭𝘦𝘵 𝘺𝘰𝘶 𝘬𝘯𝘰𝘸 𝘸𝘩𝘦𝘯 𝘵𝘩𝘪𝘴 𝘧𝘶𝘯𝘤𝘵𝘪𝘰𝘯 𝘪𝘴 𝘳𝘦𝘢𝘥𝘺..."""
    SOURCE_TXT = """<b>NOTE:</b>
- Ercel is a clone of Eva Maria - a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=@Lisa_My_Lub>Arjun Pradeep</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Ercel will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Ercel should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Ercel Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Ercel supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+WqhO2sfnZxcxYjk1)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ TOTAL FILES SAVED: <code>{}</code>
★ ERCEL USERS: <code>{}</code>
★ TOTAL CHAT: <code>{}</code>
★ STORAGE USED: <code>{}</code> 𝙼𝚒𝙱
★ AVAILABLE STORAGE: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
