import wx
from pylab import *

class myapp(wx.App):
    def OnInit(self):
        frame=wx.Frame(parent=None,
                       title='fEUVplot',
                       pos=(100,50),
                       size=(800,600)) 
        panel=wx.Panel(frame,-1)

        #shotnumber
        #shotnum label setting
        numlabel=wx.StaticText(panel,
                                 -1,
                                 'ShotNumber:',
                                 pos=(100,100),
                                 size=(100,30))

        numtext=wx.TextCtrl(panel,
                                -1,
                                'input num',
                                pos=(200,100),
                                size=(100,30))
                                        
        #shotnum button defination
        numprebut=wx.Button(panel,
                              -1,
                              'Previous shot',
                              pos=(350,100),
                              size=(120,30))
        
        numnexbut=wx.Button(panel,
                              -1,
                              'Next shot',
                              pos=(500,100),
                              size=(100,30))

        #Timeslice
        #Timeslice label setting
        timelabel=wx.StaticText(panel,
                                 -1,
                                 'TimeSlice:',
                                 pos=(100,200),
                                 size=(100,30))

        timetext=wx.TextCtrl(panel,
                                -1,
                                'input time',
                                pos=(190,200),
                                size=(90,30))

        timelabel2=wx.StaticText(panel,
                                 -1,
                                 '(s)',
                                 pos=(280,200),
                                 size=(30,30))
                                 


        
        #Timeslice button defination
        pretimebut=wx.Button(panel,
                              -1,
                              'Previous',
                              pos=(330,200),
                              size=(100,30))

        
        timeprebut=wx.Button(panel,
                              -1,
                              'Next',
                              pos=(450,200),
                              size=(100,30))

        #Plotbutton defination
        self.plotbut=wx.Button(panel,
                          -1,
                          'Plot',
                          pos=(600,185),
                          size=(100,60))
        self.Bind(wx.EVT_BUTTON,self.OnPlotButton,self.plotbut)
        

        #axes defination
        xlimlabel=wx.StaticText(panel,
                                -1,
                                'xlim',
                                pos=(120,300),
                                size=(50,30))
        xbegin=wx.TextCtrl(panel,
                           -1,
                           '20',
                           pos=(170,300),
                           size=(50,30))
        xend=wx.TextCtrl(panel,
                           -1,
                           '150',
                           pos=(230,300),
                           size=(50,30))  

        ylimlabel=wx.StaticText(panel,
                                -1,
                                'ylim',
                                pos=(340,300),
                                size=(50,30))
        ybegin=wx.TextCtrl(panel,
                           -1,
                           '0',
                           pos=(390,300),
                           size=(50,30))
        yend=wx.TextCtrl(panel,
                           -1,
                           '20',
                           pos=(450,300),
                           size=(50,30))

        #overlay setting
        olaylabel=wx.StaticText(panel,
                                -1,
                                'Overlay',
                                pos=(280,400),
                                size=(80,30))

        self.radio1=wx.RadioButton(panel,
                                   -1,
                                   'ON  (Max. 7)',
                                   pos=(360,400),
                                   size=(140,30),
                                   style=wx.RB_GROUP)
        
        self.radio2=wx.RadioButton(panel,
                                   -1,
                                   'OFF',
                                   pos=(500,400),
                                   size=(50,30))
        

        frame.Show()
        return True

    def OnPlotButton(self,event):
        #dialog = mydialog()
        #result = dialog.ShowModal()

        #dialog.Destroy()
        x=np.linspace(-np.pi,np.pi,256,endpoint=True)
        C,S=np.cos(x),np.sin(x)

        plot(x,C)
        plot(x,S)

        show()
      

#class mydialog(wx.Dialog):
  #  def __init__(self):
    #    wx.Dialog.__init__(self, None, -1, 'figure******',size=(1120, 560))
        
        

app=myapp()  
app.MainLoop()

















        
