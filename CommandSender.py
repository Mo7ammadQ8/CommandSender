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
    QtBind.append(gui, cb_commands, cmd)

y += 20

# Mount type combobox
mount_types = ['fellow', 'horse', 'pick', 'transport', 'wolf']
cb_mount_types = QtBind.createCombobox(gui, 10, y+130, 150, 20)
for mount_type in mount_types:
    QtBind.append(gui, cb_mount_types, mount_type)

# Buttons
tb_trace = QtBind.createLineEdit(gui, "", 10, y+40, 150, 20)
tb_tp1 = QtBind.createLineEdit(gui, "", 10, y+70, 70, 20)
tb_tp2 = QtBind.createLineEdit(gui, "", 90, y+70, 70, 20)
tb_moveon = QtBind.createLineEdit(gui, "", 10, y+100, 150, 20)
tb_radius = QtBind.createLineEdit(gui, "", 10, y+160, 150, 20)
tb_setscript = QtBind.createLineEdit(gui, "", 10, y+190, 150, 20)
tb_setarea = QtBind.createLineEdit(gui, "", 10, y+220, 150, 20)
tb_profile = QtBind.createLineEdit(gui, "", 10, y+250, 150, 20)

QtBind.createButton(gui, 'send_command_party_clicked', "Send Command to Party", 10, y)
QtBind.createButton(gui, 'send_command_guild_clicked', "Send Command to Guild", 140, y)
QtBind.createButton(gui, 'send_command_party_trace_clicked', "Trace (Party)", 170, y+40)
QtBind.createButton(gui, 'send_command_guild_trace_clicked', "Trace (Guild)", 250, y+40)
QtBind.createButton(gui, 'send_command_no_trace_party_clicked', "No Trace (Party)", 330, y+40)
QtBind.createButton(gui, 'send_command_no_trace_guild_clicked', "No Trace (Guild)", 420, y+40)
QtBind.createButton(gui, 'send_command_party_tp_clicked', "TP (Party)", 170, y+70)
QtBind.createButton(gui, 'send_command_guild_tp_clicked', "TP (Guild)", 250, y+70)
QtBind.createButton(gui, 'send_command_party_moveon_clicked', "MoveOn (Party)", 170, y+100)
QtBind.createButton(gui, 'send_command_guild_moveon_clicked', "MoveOn (Guild)", 260, y+100)
QtBind.createButton(gui, 'send_command_party_mount_clicked', "Mount (Party)", 170, y+130)
QtBind.createButton(gui, 'send_command_guild_mount_clicked', "Mount (Guild)", 250, y+130)
QtBind.createButton(gui, 'send_command_party_dismount_clicked', "Dismount (Party)", 330, y+130)
QtBind.createButton(gui, 'send_command_guild_dismount_clicked', "Dismount (Guild)", 420, y+130)
QtBind.createButton(gui, 'send_command_party_setradius_clicked', "SetRadius (Party)", 170, y+160)
QtBind.createButton(gui, 'send_command_guild_setradius_clicked', "SetRadius (Guild)", 265, y+160)
QtBind.createButton(gui, 'send_command_party_setscript_clicked', "SetScript (Party)", 170, y+190)
QtBind.createButton(gui, 'send_command_guild_setscript_clicked', "SetScript (Guild)", 265, y+190)
QtBind.createButton(gui, 'send_command_party_setarea_clicked', "SetArea (Party)", 170, y+220)
QtBind.createButton(gui, 'send_command_guild_setarea_clicked', "SetArea (Guild)", 265, y+220)
QtBind.createButton(gui, 'send_command_party_profile_clicked', "Profile (Party)", 170, y+250)
QtBind.createButton(gui, 'send_command_guild_profile_clicked', "Profile (Guild)", 250, y+250)


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
    name = QtBind.text(gui, tb_trace)
    if name:
        phBotChat.Party("TRACE " + name)
        log('[xControlSender] Sent [TRACE ' + name + '] command to party')

def send_command_guild_trace_clicked():
    name = QtBind.text(gui, tb_trace)
    if name:
        phBotChat.Guild("TRACE " + name)
        log('[xControlSender] Sent [TRACE ' + name + '] command to guild')

def send_command_no_trace_party_clicked():
    phBotChat.Party("NOTRACE")
    log('[xControlSender] Sent [NOTRACE] command to party')

def send_command_no_trace_guild_clicked():
    phBotChat.Guild("NOTRACE")
    log('[xControlSender] Sent [NOTRACE] command to guild')
    
def send_command_party_tp_clicked():
    name1 = QtBind.text(gui, tb_tp1)
    name2 = QtBind.text(gui, tb_tp2)
    if name1 and name2:
        phBotChat.Party("TP " + name1 + "," + name2)
        log(f'[xControlSender] Sent [TP {name1},{name2}] command to party')

def send_command_guild_tp_clicked():
    name1 = QtBind.text(gui, tb_tp1)
    name2 = QtBind.text(gui, tb_tp2)
    if name1 and name2:
        phBotChat.Guild("TP " + name1 + "," + name2)
        log(f'[xControlSender] Sent [TP {name1},{name2}] command to guild')

def send_command_party_moveon_clicked():
    name = QtBind.text(gui, tb_moveon)
    if name:
        phBotChat.Party("MOVEON " + name)
        log('[xControlSender] Sent [MOVEON ' + name + '] command to party')

def send_command_guild_moveon_clicked():
    name = QtBind.text(gui, tb_moveon)
    if name:
        phBotChat.Guild("MOVEON " + name)
        log('[xControlSender] Sent [MOVEON ' + name + '] command to guild')

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
