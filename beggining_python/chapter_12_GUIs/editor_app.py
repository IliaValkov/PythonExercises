import wx
def load(event): 
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event): 
    file = open(filename.GetValue(), "w")
    file.write(contents.GetValue())
    file.close()

app = wx.App()

win = wx.Frame(None, title="Simple editor" , size=(410, 335))

bkg = wx.Panel(win)

load_btn = wx.Button(bkg, label="Open")
load_btn.Bind(wx.EVT_BUTTON, load)

save_btn = wx.Button(bkg, label="Save")
save_btn.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL )

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(load_btn, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(save_btn, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()


