from phBot import *
import phBotChat
import QtBind
 
 
# GUI
gui = QtBind.init(__name__, 'xControlSender')
y = 10
 
# Add a ComboBox for commands
commands = ['START', 'STOP', 'TRACE', 'NOTRACE', 'RETURN', 'ZERK', 'GETOUT', 'GETPOS', 'DC', 'FOLLOW', 'NOFOLLOW', 'JUMP', 'SIT']
cb_commands = QtBind.createCombobox(gui, 10, y, 200, 20)
for cmd in commands:
    item = QtBind.append(gui, cb_commands, cmd)
 
y += 25
 
# Mount type combobox
mount_types = ['fellow', 'horse', 'pick', 'transport', 'wolf']
cb_mount_types = QtBind.createCombobox(gui, 10, y+60, 150, 20)
for mount_type in mount_types:
    QtBind.append(gui, cb_mount_types, mount_type)
 
# Cape type combobox
cape_types = ['off','red', 'gray', 'blue', 'white', 'yellow']
cb_cape = QtBind.createCombobox(gui, 370, y+145, 145, 20)
for cape_type in cape_types:
    QtBind.append(gui, cb_cape, cape_type)
 
# Reverse combobox
reverse_types = ['return', 'death', 'player', 'zone']
cb_reverse_types = QtBind.createCombobox(gui, 370, y+230, 145, 20)
for reverse_type in reverse_types:
    QtBind.append(gui, cb_reverse_types, reverse_type)
 
# Buttons
tb_trace = QtBind.createLineEdit(gui, "#Player Name", 10, y+30, 150, 20)
tb_tp1 = QtBind.createLineEdit(gui, "#A", 10, y+120, 70, 20)
tb_tp2 = QtBind.createLineEdit(gui, "#B", 90, y+120, 70, 20)
tb_moveon = QtBind.createLineEdit(gui, "#Radius", 10, y+90, 150, 20)
tb_radius = QtBind.createLineEdit(gui, "#Radius", 10, y+150, 150, 20)
tb_setscript = QtBind.createLineEdit(gui, "#Path", 10, y+180, 150, 20)
tb_setarea = QtBind.createLineEdit(gui, "#Name", 10, y+210, 150, 20)
tb_profile = QtBind.createLineEdit(gui, "#Name", 10, y+240, 150, 20)
 
QtBind.createLineEdit(gui,"",365,120,1,180)
 
tb_follow1 = QtBind.createLineEdit(gui, "#Player", 370, y+105, 70, 20)
tb_follow2 = QtBind.createLineEdit(gui, "#Distance", 445, y+105, 70, 20)
tb_equip = QtBind.createLineEdit(gui, "#ItemName ", 370, y+185, 145, 20)
tb_reverse = QtBind.createLineEdit(gui, "#Player or Zone", 370, y+255, 145, 20)
 
QtBind.createButton(gui, 'send_command_party_clicked', "Send Command to Party", 10, y)
QtBind.createButton(gui, 'send_command_guild_clicked', "Send Command to Guild", 140, y)
QtBind.createButton(gui, 'send_command_party_trace_clicked'     , "    Trace (Party)    ", 170, y+30)
QtBind.createButton(gui, 'send_command_guild_trace_clicked'     , "    Trace (Guild)    ", 266, y+30)
QtBind.createButton(gui, 'send_command_no_trace_party_clicked'  , " No Trace (Party) ", 360, y+30)
QtBind.createButton(gui, 'send_command_no_trace_guild_clicked'  , "No Trace (Guild)", 452, y+30)
QtBind.createButton(gui, 'send_command_party_tp_clicked'        , "      TP (Party)      ", 170, y+120)
QtBind.createButton(gui, 'send_command_guild_tp_clicked'        , "      TP (Guild)      ", 265, y+120)
QtBind.createButton(gui, 'send_command_party_moveon_clicked'    , "  MoveOn (Party) ", 170, y+90)
QtBind.createButton(gui, 'send_command_guild_moveon_clicked'    , "  MoveOn (Guild)", 266, y+90)
QtBind.createButton(gui, 'send_command_party_mount_clicked'     , "    Mount (Party)   ", 170, y+60)
QtBind.createButton(gui, 'send_command_guild_mount_clicked'     , "    Mount (Guild)   ", 266, y+60)
QtBind.createButton(gui, 'send_command_party_dismount_clicked'  , "Dismount (Party) ", 360, y+60)
QtBind.createButton(gui, 'send_command_guild_dismount_clicked'  , "Dismount (Guild) ", 452, y+60)
QtBind.createButton(gui, 'send_command_party_setradius_clicked' , "SetRadius (Party)", 170, y+150)
QtBind.createButton(gui, 'send_command_guild_setradius_clicked' , "SetRadius (Guild)", 265, y+150)
QtBind.createButton(gui, 'send_command_party_setscript_clicked' , " SetScript (Party) ", 170, y+180)
QtBind.createButton(gui, 'send_command_guild_setscript_clicked' , " SetScript (Guild) ", 265, y+180)
QtBind.createButton(gui, 'send_command_party_setarea_clicked'   , "  SetArea (Party) ", 170, y+210)
QtBind.createButton(gui, 'send_command_guild_setarea_clicked'   , "  SetArea (Guild) ", 264, y+210)
QtBind.createButton(gui, 'send_command_party_profile_clicked'   , "    Profile (Party)  ", 170, y+240)
QtBind.createButton(gui, 'send_command_guild_profile_clicked'   , "    Profile (Guild)  ", 264, y+240)
 
QtBind.createButton(gui, 'send_command_party_follow_clicked'    , "   Follow (Party)    ", 520, y+90)
QtBind.createButton(gui, 'send_command_guild_follow_clicked'    , "   Follow (Guild)    ", 620, y+90)
QtBind.createButton(gui, 'send_command_no_follow_party_clicked' , " No Follow (Party) ", 520, y+115)
QtBind.createButton(gui, 'send_command_no_follow_guild_clicked' , " No Follow (Guild) ", 620, y+115)
QtBind.createButton(gui, 'send_command_party_cape_clicked'    , "    Cape (Party)     ", 520, y+145)
QtBind.createButton(gui, 'send_command_guild_cape_clicked'    , "    Cape (Guild)     ", 620, y+145)
QtBind.createButton(gui, 'send_command_party_follow_clicked'    , "   EQUIP (Party)    ", 520, y+175)
QtBind.createButton(gui, 'send_command_guild_follow_clicked'    , "   EQUIP (Guild)    ", 620, y+175)
QtBind.createButton(gui, 'send_command_no_follow_party_clicked' , " UNEQUIP (Party) ", 520, y+200)
QtBind.createButton(gui, 'send_command_no_follow_guild_clicked' , " UNEQUIP (Guild) ", 620, y+200)
 
 
def send_command_party_clicked():
    cmd = QtBind.text(gui, cb_commands)
    if cmd:
        phBotChat.Party(cmd)
        log('[xControlSender] Sent [' + cmd + '] command to party')
 
def send_command_guild_clicked():
    cmd = QtBind.text(gui, cb_commands)
    if cmd:
        phBotChat.Guild(cmd)
        log('[xControlSender] Sent [' + cmd + '] command to guild')
 
def send_command_party_trace_clicked():
    player = QtBind.text(gui, tb_trace)
    if player:
        phBotChat.Party("TRACE " + player)
        log('[xControlSender] Sent [TRACE ' + player + '] command to party')
 
def send_command_guild_trace_clicked():
    player = QtBind.text(gui, tb_trace)
    if player:
        phBotChat.Guild("TRACE " + player)
        log('[xControlSender] Sent [TRACE ' + player + '] command to guild')
 
def send_command_no_trace_party_clicked():
    phBotChat.Party("NOTRACE")
    log('[xControlSender] Sent [NOTRACE] command to party')
 
def send_command_no_trace_guild_clicked():
    phBotChat.Guild("NOTRACE")
    log('[xControlSender] Sent [NOTRACE] command to guild')
 
def send_command_party_tp_clicked():
    tp1 = QtBind.text(gui, tb_tp1)
    tp2 = QtBind.text(gui, tb_tp2)
    if tp1 and tp2:
        phBotChat.Party("TP " + tp1 + "," + tp2)
        log(f'[xControlSender] Sent [TP {tp1},{tp2}] command to party')
 
def send_command_guild_tp_clicked():
    tp1 = QtBind.text(gui, tb_tp1)
    tp2 = QtBind.text(gui, tb_tp2)
    if tp1 and tp2:
        phBotChat.Guild("TP " + tp1 + "," + tp2)
        log(f'[xControlSender] Sent [TP {tp1},{tp2}] command to guild')
 
def send_command_party_moveon_clicked():
    radius = QtBind.text(gui, tb_moveon)
    if radius:
        phBotChat.Party("MOVEON " + radius)
        log('[xControlSender] Sent [MOVEON ' + radius + '] command to party')
 
def send_command_guild_moveon_clicked():
    radius = QtBind.text(gui, tb_moveon)
    if radius:
        phBotChat.Guild("MOVEON " + radius)
        log('[xControlSender] Sent [MOVEON ' + radius + '] command to guild')
 
def send_command_party_mount_clicked():
    mount_type = QtBind.text(gui, cb_mount_types)
    if mount_type:
        phBotChat.Party("MOUNT " + mount_type)
        log('[xControlSender] Sent [MOUNT ' + mount_type + '] command to party')
 
def send_command_guild_mount_clicked():
    mount_type = QtBind.text(gui, cb_mount_types)
    if mount_type:
        phBotChat.Guild("MOUNT " + mount_type)
        log('[xControlSender] Sent [MOUNT ' + mount_type + '] command to guild')
 
def send_command_party_dismount_clicked():
    mount_type = QtBind.text(gui, cb_mount_types)
    if mount_type:
        phBotChat.Party("DISMOUNT " + mount_type)
        log('[xControlSender] Sent [MOUNT ' + mount_type + '] command to party')
 
def send_command_guild_dismount_clicked():
    mount_type = QtBind.text(gui, cb_mount_types)
    if mount_type:
        phBotChat.Guild("DISMOUNT " + mount_type)
        log('[xControlSender] Sent [MOUNT ' + mount_type + '] command to guild')
 
def send_command_party_setradius_clicked():
    radius = QtBind.text(gui, tb_radius)
    if radius:
        phBotChat.Party("SETRADIUS " + radius)
        log('[xControlSender] Sent [SETRADIUS ' + radius + '] command to party')
 
def send_command_guild_setradius_clicked():
    radius = QtBind.text(gui, tb_radius)
    if radius:
        phBotChat.Guild("SETRADIUS " + radius)
        log('[xControlSender] Sent [SETRADIUS ' + radius + '] command to guild')
 
def send_command_party_setscript_clicked():
    script = QtBind.text(gui, tb_setscript)
    if script:
        phBotChat.Party("SETSCRIPT " + script)
        log('[xControlSender] Sent [SETSCRIPT ' + script + '] command to party')
 
def send_command_guild_setscript_clicked():
    script = QtBind.text(gui, tb_setscript)
    if script:
        phBotChat.Guild("SETSCRIPT " + script)
        log('[xControlSender] Sent [SETSCRIPT ' + script + '] command to guild')
 
def send_command_party_setarea_clicked():
    area = QtBind.text(gui, tb_setarea)
    if area:
        phBotChat.Party("SETAREA " + area)
        log('[xControlSender] Sent [SETAREA ' + area + '] command to party')
 
def send_command_guild_setarea_clicked():
    area = QtBind.text(gui, tb_setarea)
    if area:
        phBotChat.Guild("SETAREA " + area)
        log('[xControlSender] Sent [SETAREA ' + area + '] command to guild')
 
def send_command_party_profile_clicked():
    profile = QtBind.text(gui, tb_profile)
    if profile:
        phBotChat.Party("PROFILE " + profile)
        log('[xControlSender] Sent [PROFILE ' + profile + '] command to party')
 
def send_command_guild_profile_clicked():
    profile = QtBind.text(gui, tb_profile)
    if profile:
        phBotChat.Guild("PROFILE " + profile)
        log('[xControlSender] Sent [PROFILE ' + profile + '] command to guild')
 
def send_command_party_follow_clicked():
    follow = QtBind.text(gui, tb_follow1)
    distance = QtBind.text(gui, tb_follow2)
    if follow and distance:
        phBotChat.Party("FOLLOW " + follow + " " + distance)
        log(f'[xControlSender] Sent [FOLLOW {follow} {distance}] command to party')
 
def send_command_guild_follow_clicked():
    follow = QtBind.text(gui, tb_follow1)
    distance = QtBind.text(gui, tb_follow2)
    if follow and distance:
        phBotChat.Guild("FOLLOW " + follow + " " + distance)
        log(f'[xControlSender] Sent [FOLLOW {follow} {distance}] command to guild')
 
def send_command_no_follow_party_clicked():
    phBotChat.Party("NOFOLLOW")
    log('[xControlSender] Sent [NOFOLLOW] command to party')
 
def send_command_no_follow_guild_clicked():
    phBotChat.Guild("NOFOLLOW")
    log('[xControlSender] Sent [NOFOLLOW] command to guild')
 
def send_command_party_cape_clicked():
    cape = QtBind.text(gui, cb_cape)
    if cape:
        phBotChat.Party("CAPE " + cape)
        log('[xControlSender] Sent [CAPE ' + cape + '] command to party')
 
def send_command_guild_cape_clicked():
    cape = QtBind.text(gui, cb_cape)
    if cape:
        phBotChat.Guild("CAPE " + cape)
        log('[xControlSender] Sent [CAPE ' + cape + '] command to guild')