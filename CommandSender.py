from phBot import *
import phBotChat
import QtBind
 
pName = 'ControlHelper'
pVersion = '1.0.3'
pUrl = 'https://raw.githubusercontent.com/Mo7ammadQ8/CommandSender/main/CommandSender.py'

# GUI
gui = QtBind.init(__name__,pName)
QtBind.createLabel(gui,'* Make Sure to have xControl Plugin Installed',400,10)
QtBind.createLabel(gui,'- Working Perfectly With xControl v.1.9.1',400,25)
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
 
# TextBox Group 1
tb_trace = QtBind.createLineEdit(gui, "#Player Name", 10, y+30, 150, 20)
tb_tp1 = QtBind.createLineEdit(gui, "#A", 10, y+120, 70, 20)
tb_tp2 = QtBind.createLineEdit(gui, "#B", 90, y+120, 70, 20)
tb_moveon = QtBind.createLineEdit(gui, "#Radius", 10, y+90, 150, 20)
tb_radius = QtBind.createLineEdit(gui, "#Radius", 10, y+150, 150, 20)
tb_setscript = QtBind.createLineEdit(gui, "#Path", 10, y+180, 150, 20)
tb_setarea = QtBind.createLineEdit(gui, "#Name", 10, y+210, 150, 20)
tb_profile = QtBind.createLineEdit(gui, "#Name", 10, y+240, 150, 20)
 
# Seperate Line
QtBind.createLineEdit(gui,"",362,125,1,190)
 
# TextBox Group 2
tb_follow1 = QtBind.createLineEdit(gui, "#Player", 370, y+105, 70, 20)
tb_follow2 = QtBind.createLineEdit(gui, "#Distance", 445, y+105, 70, 20)
tb_equip = QtBind.createLineEdit(gui, "#ItemName ", 370, y+185, 145, 20)
tb_reverse = QtBind.createLineEdit(gui, "#Player or Zone", 370, y+255, 145, 20)
 
# Button 1
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
 
# Button 2
QtBind.createButton(gui, 'send_command_party_follow_clicked'    , "   Follow (Party)    ", 520, y+90)
QtBind.createButton(gui, 'send_command_guild_follow_clicked'    , "   Follow (Guild)    ", 620, y+90)
QtBind.createButton(gui, 'send_command_no_follow_party_clicked' , " No Follow (Party) ", 520, y+115)
QtBind.createButton(gui, 'send_command_no_follow_guild_clicked' , " No Follow (Guild) ", 620, y+115)
QtBind.createButton(gui, 'send_command_party_cape_clicked'    , "    Cape (Party)     ", 520, y+145)
QtBind.createButton(gui, 'send_command_guild_cape_clicked'    , "    Cape (Guild)     ", 620, y+145)
QtBind.createButton(gui, 'send_command_party_equip_clicked'    , "   EQUIP (Party)    ", 520, y+175)
QtBind.createButton(gui, 'send_command_guild_equip_clicked'    , "   EQUIP (Guild)    ", 620, y+175)
QtBind.createButton(gui, 'send_command_party_unequip_clicked' , " UNEQUIP (Party) ", 520, y+200)
QtBind.createButton(gui, 'send_command_guild_unequip_clicked' , " UNEQUIP (Guild) ", 620, y+200)
QtBind.createButton(gui, 'send_command_party_reverse_clicked' , " REVERSE (Party) ", 520, y+245)
QtBind.createButton(gui, 'send_command_guild_reverse_clicked' , " REVERSE (Guild) ", 620, y+245)
 
#Buttons Functionality
def send_command_party_clicked():
    cmd = QtBind.text(gui, cb_commands)
    if cmd:
        phBotChat.Party(cmd)
        log('[ControlHelper] Sent [' + cmd + '] command to party')
 
def send_command_guild_clicked():
    cmd = QtBind.text(gui, cb_commands)
    if cmd:
        phBotChat.Guild(cmd)
        log('[ControlHelper] Sent [' + cmd + '] command to guild')
 
def send_command_party_trace_clicked():
    player = QtBind.text(gui, tb_trace)
    if player:
        phBotChat.Party("TRACE " + player)
        log('[ControlHelper] Sent [TRACE ' + player + '] command to party')
 
def send_command_guild_trace_clicked():
    player = QtBind.text(gui, tb_trace)
    if player:
        phBotChat.Guild("TRACE " + player)
        log('[ControlHelper] Sent [TRACE ' + player + '] command to guild')
 
def send_command_no_trace_party_clicked():
    phBotChat.Party("NOTRACE")
    log('[ControlHelper] Sent [NOTRACE] command to party')
 
def send_command_no_trace_guild_clicked():
    phBotChat.Guild("NOTRACE")
    log('[ControlHelper] Sent [NOTRACE] command to guild')
 
def send_command_party_tp_clicked():
    tp1 = QtBind.text(gui, tb_tp1)
    tp2 = QtBind.text(gui, tb_tp2)
    if tp1 and tp2:
        phBotChat.Party("TP " + tp1 + "," + tp2)
        log(f'[ControlHelper] Sent [TP {tp1},{tp2}] command to party')
 
def send_command_guild_tp_clicked():
    tp1 = QtBind.text(gui, tb_tp1)
    tp2 = QtBind.text(gui, tb_tp2)
    if tp1 and tp2:
        phBotChat.Guild("TP " + tp1 + "," + tp2)
        log(f'[ControlHelper] Sent [TP {tp1},{tp2}] command to guild')
 
def send_command_party_moveon_clicked():
    radius = QtBind.text(gui, tb_moveon)
    if radius:
        phBotChat.Party("MOVEON " + radius)
        log('[ControlHelper] Sent [MOVEON ' + radius + '] command to party')
 
def send_command_guild_moveon_clicked():
    radius = QtBind.text(gui, tb_moveon)
    if radius:
        phBotChat.Guild("MOVEON " + radius)
        log('[ControlHelper] Sent [MOVEON ' + radius + '] command to guild')
 
def send_command_party_mount_clicked():
    mount_type = QtBind.text(gui, cb_mount_types)
    if mount_type:
        phBotChat.Party("MOUNT " + mount_type)
        log('[ControlHelper] Sent [MOUNT ' + mount_type + '] command to party')
 
def send_command_guild_mount_clicked():
    mount_type = QtBind.text(gui, cb_mount_types)
    if mount_type:
        phBotChat.Guild("MOUNT " + mount_type)
        log('[ControlHelper] Sent [MOUNT ' + mount_type + '] command to guild')
 
def send_command_party_dismount_clicked():
    mount_type = QtBind.text(gui, cb_mount_types)
    if mount_type:
        phBotChat.Party("DISMOUNT " + mount_type)
        log('[ControlHelper] Sent [MOUNT ' + mount_type + '] command to party')
 
def send_command_guild_dismount_clicked():
    mount_type = QtBind.text(gui, cb_mount_types)
    if mount_type:
        phBotChat.Guild("DISMOUNT " + mount_type)
        log('[ControlHelper] Sent [MOUNT ' + mount_type + '] command to guild')
 
def send_command_party_setradius_clicked():
    radius = QtBind.text(gui, tb_radius)
    if radius:
        phBotChat.Party("SETRADIUS " + radius)
        log('[ControlHelper] Sent [SETRADIUS ' + radius + '] command to party')
 
def send_command_guild_setradius_clicked():
    radius = QtBind.text(gui, tb_radius)
    if radius:
        phBotChat.Guild("SETRADIUS " + radius)
        log('[ControlHelper] Sent [SETRADIUS ' + radius + '] command to guild')
 
def send_command_party_setscript_clicked():
    script = QtBind.text(gui, tb_setscript)
    if script:
        phBotChat.Party("SETSCRIPT " + script)
        log('[ControlHelper] Sent [SETSCRIPT ' + script + '] command to party')
 
def send_command_guild_setscript_clicked():
    script = QtBind.text(gui, tb_setscript)
    if script:
        phBotChat.Guild("SETSCRIPT " + script)
        log('[ControlHelper] Sent [SETSCRIPT ' + script + '] command to guild')
 
def send_command_party_setarea_clicked():
    area = QtBind.text(gui, tb_setarea)
    if area:
        phBotChat.Party("SETAREA " + area)
        log('[ControlHelper] Sent [SETAREA ' + area + '] command to party')
 
def send_command_guild_setarea_clicked():
    area = QtBind.text(gui, tb_setarea)
    if area:
        phBotChat.Guild("SETAREA " + area)
        log('[ControlHelper] Sent [SETAREA ' + area + '] command to guild')
 
def send_command_party_profile_clicked():
    profile = QtBind.text(gui, tb_profile)
    if profile:
        phBotChat.Party("PROFILE " + profile)
        log('[ControlHelper] Sent [PROFILE ' + profile + '] command to party')
 
def send_command_guild_profile_clicked():
    profile = QtBind.text(gui, tb_profile)
    if profile:
        phBotChat.Guild("PROFILE " + profile)
        log('[ControlHelper] Sent [PROFILE ' + profile + '] command to guild')
 
def send_command_party_follow_clicked():
    follow = QtBind.text(gui, tb_follow1)
    distance = QtBind.text(gui, tb_follow2)
    if follow and distance:
        phBotChat.Party("FOLLOW " + follow + " " + distance)
        log(f'[ControlHelper] Sent [FOLLOW {follow} {distance}] command to party')
 
def send_command_guild_follow_clicked():
    follow = QtBind.text(gui, tb_follow1)
    distance = QtBind.text(gui, tb_follow2)
    if follow and distance:
        phBotChat.Guild("FOLLOW " + follow + " " + distance)
        log(f'[ControlHelper] Sent [FOLLOW {follow} {distance}] command to guild')
 
def send_command_no_follow_party_clicked():
    phBotChat.Party("NOFOLLOW")
    log('[ControlHelper] Sent [NOFOLLOW] command to party')
 
def send_command_no_follow_guild_clicked():
    phBotChat.Guild("NOFOLLOW")
    log('[ControlHelper] Sent [NOFOLLOW] command to guild')
 
def send_command_party_cape_clicked():
    cape = QtBind.text(gui, cb_cape)
    if cape:
        phBotChat.Party("CAPE " + cape)
        log('[ControlHelper] Sent [CAPE ' + cape + '] command to party')
 
def send_command_guild_cape_clicked():
    cape = QtBind.text(gui, cb_cape)
    if cape:
        phBotChat.Guild("CAPE " + cape)
        log('[ControlHelper] Sent [CAPE ' + cape + '] command to guild')

def send_command_party_equip_clicked():
    equip = QtBind.text(gui, tb_equip)
    if equip:
        phBotChat.Party("EQUIP " + equip)
        log('[ControlHelper] Sent [EQUIP ' + equip + '] command to party')

def send_command_guild_equip_clicked():
    equip = QtBind.text(gui, tb_equip)
    if equip:
        phBotChat.Guild("EQUIP " + equip)
        log('[ControlHelper] Sent [EQUIP ' + equip + '] command to guild')

def send_command_party_unequip_clicked():
    equip = QtBind.text(gui, tb_equip)
    if equip:
        phBotChat.Party("UNEQUIP " + equip)
        log('[ControlHelper] Sent [UNEQUIP ' + equip + '] command to party')

def send_command_guild_unequip_clicked():
    equip = QtBind.text(gui, tb_equip)
    if equip:
        phBotChat.Guild("UNEQUIP " + equip)
        log('[ControlHelper] Sent [UNEQUIP ' + equip + '] command to guild')

def send_command_party_reverse_clicked():
    reverse_type = QtBind.text(gui, cb_reverse_types)
    reverse_player_or_zone = QtBind.text(gui, tb_reverse)
    if reverse_type:
        phBotChat.Party("REVERSE " + reverse_type + " " + (reverse_player_or_zone or ''))
        log(f'[ControlHelper] Sent [REVERSE {reverse_type} {reverse_player_or_zone or ""}] command to party')

def send_command_guild_reverse_clicked():
    reverse_type = QtBind.text(gui, cb_reverse_types)
    reverse_player_or_zone = QtBind.text(gui, tb_reverse)
    if reverse_type:
        phBotChat.Guild("REVERSE " + reverse_type + " " + (reverse_player_or_zone or ''))
        log(f'[ControlHelper] Sent [REVERSE {reverse_type} {reverse_player_or_zone or ""}] command to guild')

# Plugin loaded
log("Plugin: "+pName+" v"+pVersion+" successfully loaded")
