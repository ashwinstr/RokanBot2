# ported from kensurBot to ultroid by @Kakashi_HTK(tg)/@ashwinstr(gh)
"""
✘ Commands Available -
"`.fban <id/username> <reason>`"
"\nUsage: Bans user from connected federations."
"\nYou can reply to the user whom you want to fban or manually pass the username/id."
"\n`.dfban` does the same but deletes the replied message."
"\n\n`>.unfban <id/username> <reason>`"
"\nUsage: Same as fban but unbans the user"
"\n\n>`.addf <name>`"
"\nUsage: Adds current group and stores it as <name> in connected federations."
"\nAdding one group is enough for one federation."
"\n\n>`.delf`"
"\nUsage: Removes current group from connected federations."
"\n\n>`.listf`"
"\nUsage: Lists all connected federations by specified name."
"\n\n>`.clearf`"
"\nUsage: Disconnects from all connected federations. Use it carefully."
"""

from . import *



@ultroid_cmd(pattern=r"^\.addf(?: |$)(.*)", ignore_dualmode=True)
async def addf_(event):
    chat_id = event.chat_id
    name_ = evant.pattern_match.group(1)
    flist = udB.get("FLIST").split("\n")
    for one in flist:
        if chat_id in one:
            udB.delete("FLIST", one)
            proverb = "updated"
        else:
            proverb = "added"
    udB.append("FLIST", f"'{chat_id}' - {name_}\n")
    await event.edit(f"<b>'{chat_id}' - {name}</b> {proverb} in FEDLIST...")
    
    
@ultroid_cmd(pattern=r"^\.delf(?: |$)(.*)", ignore_dualmode=True)
async def delf_(event):
    chat_id = event.chat_id
    flist = udB.get("FLIST").split("\n")
    for one in flist:
        if chat_id in one:
            udB.delete("FLIST", one)
            await event.edit(f"<b>{one}</b> deleted from FEDLIST...")
        else:
            await event.edit(f"Chat not found in FEDLIST...")
    
    
