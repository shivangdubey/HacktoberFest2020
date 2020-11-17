import wx

if __name__  == '__main__':
    app = wx.App()
    dialog = wx.MessageDialog(None, "Do you wanna quit?", "Display window", wx.YES_NO | wx.ICON_QUESTION)
    retcode = dialog.ShowModal()
    if(retcode == wx.ID_YES):
        print("YOU ARE OUT OF THE WINDOW")
    else:
        print("CAN'T CLOSE WITHOUT YOUR PERMISSION")
        dialog.Destroy()
        retcode = wx.MessageBox("Are you sure?", "Confirmation window", wx.YES_NO | wx.ICON_QUESTION)
