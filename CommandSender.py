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

y += 30

# Buttons
button_send_party = QtBind.createButton(gui, 'send_command_party_clicked', "Send Command to Party", 10, y)
button_send_guild = QtBind.createButton(gui, 'send_command_guild_clicked', "Send Command to Guild", 140, y)

# TextBox
tb_trace = QtBind.createLineEdit(gui, "", 10, y+40, 150, 20)
tb_tp1 = QtBind.createLineEdit(gui, "", 10, y+70, 70, 20)
tb_tp2 = QtBind.createLineEdit(gui, "", 90, y+70, 70, 20)
QtBind.createButton(gui, 'send_command_party_trace_clicked', "Trace (Party)", 170, y+40)
QtBind.createButton(gui, 'send_command_guild_trace_clicked', "Trace (Guild)", 250, y+40)
QtBind.createButton(gui, 'send_command_no_trace_party_clicked', "No Trace (Party)", 330, y+40)
QtBind.createButton(gui, 'send_command_no_trace_guild_clicked', "No Trace (Guild)", 420, y+40)
QtBind.createButton(gui, 'send_command_party_tp_clicked', "TP (Party)", 170, y+70)
QtBind.createButton(gui, 'send_command_guild_tp_clicked', "TP (Guild)", 250, y+70)

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