# -*- coding: utf-8 -*-
import wx
import os
import pymssql
import datetime

class MyAdminFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, u'动画信息管理系统', size=(1000, 600))

        parent.Show(False)

        icon = wx.Icon(name='./image/samekichi.jpg', type=wx.BITMAP_TYPE_ANY)
        self.SetIcon(icon)
        cursor = wx.Cursor(wx.CURSOR_ARROW)
        self.SetCursor(cursor)

        font1 = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.font2 = wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD)

        toolbar = wx.ToolBar(self, -1, style=wx.TB_TEXT | wx.TB_NOICONS)
        self.ToolBar = toolbar
        animate = wx.NewId()
        original_company = wx.NewId()
        animation_company = wx.NewId()
        people = wx.NewId()
        staff = wx.NewId()
        music = wx.NewId()
        feedback = wx.NewId()
        tool1 = toolbar.AddRadioTool(animate, u'动画查询', wx.Bitmap('./image/toolbar.jpg'))
        tool2 = toolbar.AddRadioTool(original_company, u'原作公司查询', wx.Bitmap('./image/toolbar.jpg'))
        tool3 = toolbar.AddRadioTool(animation_company, u'动画公司查询', wx.Bitmap('./image/toolbar.jpg'))
        tool4 = toolbar.AddRadioTool(people, u'人物查询', wx.Bitmap('./image/toolbar.jpg'))
        tool5 = toolbar.AddRadioTool(staff, u'staff查询', wx.Bitmap('./image/toolbar.jpg'))
        tool6 = toolbar.AddRadioTool(music, u'音乐查询', wx.Bitmap('./image/toolbar.jpg'))
        tool7 = toolbar.AddRadioTool(feedback, u'管理数据', wx.Bitmap('./image/toolbar.jpg'))
        for i in range(20):
            toolbar.AddSeparator()
        return_login = wx.NewId()
        exit = wx.NewId()
        tool8 = toolbar.AddTool(return_login, u'返回登录界面', wx.Bitmap('./image/toolbar.jpg'))
        tool9 = toolbar.AddTool(exit, u'退出系统', wx.Bitmap('./image/toolbar.jpg'))

        toolbar.SetFont(font1)
        toolbar.Realize()

        if parent.MyRole == '普通用户':
            toolbar.EnableTool(feedback, False)

        self.splitter = wx.SplitterWindow(self, -1)
        self.leftpanel = wx.Panel(self.splitter)
        self.rightpanel = wx.Panel(self.splitter)
        self.splitter.SplitVertically(self.leftpanel, self.rightpanel, 100)
        self.splitter.SetMinimumPaneSize(80)
        self.rightpanel.SetBackgroundColour('White')

        self.function_choose1 = ['动画基本信息','制作类型','改编类型','原作公司','原作者','制作公司','季度','首播时间','总集数','STAFF','CV','演唱','类别']
        self.function_choose2 = ['原作公司基本信息', '被动画化的作品', '主要业务']
        self.function_choose3 = ['动画公司基本信息', '制作动画']
        self.function_choose4 = ['人物基本信息', '职业', '作品参与']
        self.function_choose5 = ['staff基本信息', '职位', '作品参与']
        self.function_choose6 = ['音乐基本信息', '季度', '歌手']
        self.function_choose7 = ['原作公司','动画公司','人物','动画(添加)','动画(删改)','动画类别','动画制作组','动画声优','动画音乐','音乐演唱']

        self.function = wx.ListBox(self.leftpanel, -1, choices=self.function_choose1, style=wx.LB_SINGLE | wx.LB_HSCROLL)
        self.Bind(wx.EVT_LISTBOX, self.OnListbox1, self.function)

        box1 = wx.BoxSizer(wx.VERTICAL)
        box1.Add(self.function, 1, flag=wx.ALL | wx.EXPAND, border=5)
        self.leftpanel.SetSizer(box1)

        hint = wx.StaticText(self.rightpanel, -1, u'←请在左侧列表框中选择查询功能', pos=(80, 80))
        hint.SetFont(self.font2)

        self.Bind(wx.EVT_TOOL, self.On_animate, tool1)
        self.Bind(wx.EVT_TOOL, self.On_original_company, tool2)
        self.Bind(wx.EVT_TOOL, self.On_animation_company, tool3)
        self.Bind(wx.EVT_TOOL, self.On_people, tool4)
        self.Bind(wx.EVT_TOOL, self.On_staff, tool5)
        self.Bind(wx.EVT_TOOL, self.On_music, tool6)
        self.Bind(wx.EVT_TOOL, self.On_feedback, tool7)
        self.Bind(wx.EVT_TOOL, self.On_return_login, tool8)
        self.Bind(wx.EVT_TOOL, self.On_exit, tool9)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, evt):
        dlg = wx.MessageDialog(None, u'确认离开？', u'关闭', wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            evt.Skip()
            frame.Show(True)
            frame.userText.Clear()
            frame.pwdText.Clear()
        dlg.Destroy()

    def On_animate(self, event):
        self.function.Set(self.function_choose1)
        self.Bind(wx.EVT_LISTBOX, self.OnListbox1, self.function)
        for child in self.rightpanel.GetChildren():
            child.Destroy()
        hint = wx.StaticText(self.rightpanel, -1, u'←请在左侧列表框中选择查询功能', pos=(80, 80))
        hint.SetFont(self.font2)

    def On_original_company(self, event):
        self.function.Set(self.function_choose2)
        self.Bind(wx.EVT_LISTBOX, self.OnListbox2, self.function)
        for child in self.rightpanel.GetChildren():
            child.Destroy()
        hint = wx.StaticText(self.rightpanel, -1, u'←请在左侧列表框中选择查询功能', pos=(80, 80))
        hint.SetFont(self.font2)

    def On_animation_company(self, event):
        self.function.Set(self.function_choose3)
        self.Bind(wx.EVT_LISTBOX, self.OnListbox3, self.function)
        for child in self.rightpanel.GetChildren():
            child.Destroy()
        hint = wx.StaticText(self.rightpanel, -1, u'←请在左侧列表框中选择查询功能', pos=(80, 80))
        hint.SetFont(self.font2)

    def On_people(self, event):
        self.function.Set(self.function_choose4)
        self.Bind(wx.EVT_LISTBOX, self.OnListbox4, self.function)
        for child in self.rightpanel.GetChildren():
            child.Destroy()
        hint = wx.StaticText(self.rightpanel, -1, u'←请在左侧列表框中选择查询功能', pos=(80, 80))
        hint.SetFont(self.font2)

    def On_staff(self, event):
        self.function.Set(self.function_choose5)
        self.Bind(wx.EVT_LISTBOX, self.OnListbox5, self.function)
        for child in self.rightpanel.GetChildren():
            child.Destroy()
        hint = wx.StaticText(self.rightpanel, -1, u'←请在左侧列表框中选择查询功能', pos=(80, 80))
        hint.SetFont(self.font2)

    def On_music(self, event):
        self.function.Set(self.function_choose6)
        self.Bind(wx.EVT_LISTBOX, self.OnListbox6, self.function)
        for child in self.rightpanel.GetChildren():
            child.Destroy()
        hint = wx.StaticText(self.rightpanel, -1, u'←请在左侧列表框中选择查询功能', pos=(80, 80))
        hint.SetFont(self.font2)

    def On_feedback(self, event):
        self.function.Set(self.function_choose7)
        self.Bind(wx.EVT_LISTBOX, self.OnListbox7, self.function)
        for child in self.rightpanel.GetChildren():
            child.Destroy()
        hint = wx.StaticText(self.rightpanel, -1, u'←请在左侧列表框中选择查询功能', pos=(80, 80))
        hint.SetFont(self.font2)

    def On_return_login(self, evt):
        self.Close()

    def On_exit(self, evt):
        frame.Close()

    def OnListbox1(self, event):
        choose = event.GetString()
        for child in self.rightpanel.GetChildren():
            child.Destroy()

        sql = "select * from 限制时间"
        cur.execute(sql)
        res = cur.fetchall()
        timelimit = ['所有']
        for i in res:
            timelimit.append(i[0])

        if choose == '动画基本信息':
            self.name = ''
            wx.StaticText(self.rightpanel, -1, u'请输入动画名称：', pos=(10, 13))
            self.animate_name = wx.TextCtrl(self.rightpanel, -1, '', size=(200, -1), style=wx.TE_RICH, pos=(120, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(350, 9))
            self.Bind(wx.EVT_BUTTON, self.OnOK1, okButton)
        if choose == '制作类型':
            wx.StaticText(self.rightpanel, -1, u'请选择动画的制作类型：', pos=(10, 13))
            type_tmp1 = ['新作','续作','衍生','重制']
            self.choice_type1 = wx.Choice(self.rightpanel, choices=type_tmp1, size=(80, -1), pos=(160, 10))
            self.choice_type1.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_jidu1 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_jidu1.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(280, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK2, okButton)
        if choose == '改编类型':
            wx.StaticText(self.rightpanel, -1, u'请选择动画的制作类型：', pos=(10, 13))
            type_tmp2 = ['漫改', '轻改', '游戏改', '原创']
            self.choice_type2 = wx.Choice(self.rightpanel, choices=type_tmp2, size=(80, -1), pos=(160, 10))
            self.choice_type2.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_jidu2 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_jidu2.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(280, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK3, okButton)
        if choose == '原作公司':
            sql = "select 名称 from 原作公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp3 = []
            for i in res:
                type_tmp3.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择原作公司名称：', pos=(10, 13))
            self.choice_type3 = wx.Choice(self.rightpanel, choices=type_tmp3, size=(200, -1), pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_jidu3 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_jidu3.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK4, okButton)
        if choose == '原作者':
            sql = "select distinct 原作者 from 动画"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp4 = []
            for i in res:
                if i[0] != None:
                    type_tmp4.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择原作者姓名：', pos=(10, 13))
            self.choice_type4 = wx.Choice(self.rightpanel, choices=type_tmp4, size=(150, -1), pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_jidu4 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_jidu4.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(350, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK5, okButton)
        if choose == '制作公司':
            sql = "select 名称 from 动画公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp5 = []
            for i in res:
                type_tmp5.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择制作公司名称：', pos=(10, 13))
            self.choice_type5 = wx.Choice(self.rightpanel, choices=type_tmp5, size=(200, -1), pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_jidu5 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_jidu5.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK6, okButton)
        if choose == '季度':
            sql = "select distinct 新番季度 from 动画"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp6 = []
            for i in res:
                type_tmp6.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择番剧季度：', pos=(10, 13))
            self.choice_type6 = wx.Choice(self.rightpanel, choices=type_tmp6, size=(80, -1), pos=(130, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(250, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK7, okButton)
        if choose == '首播时间':
            wx.StaticText(self.rightpanel, -1, u'请输入首播起始时间：', pos=(10, 13))
            self.choice_type7 = wx.TextCtrl(self.rightpanel, -1, '', size=(100, -1), style=wx.TE_RICH, pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入首播终止时间：', pos=(10, 53))
            self.choice_jidu7 = wx.TextCtrl(self.rightpanel, -1, '', size=(100, -1), style=wx.TE_RICH, pos=(160, 50))
            wx.StaticText(self.rightpanel, -1, u'时间格式为年月日，如：20180101', pos=(300, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(300, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK8, okButton)
        if choose == '总集数':
            wx.StaticText(self.rightpanel, -1, u'请选择总集数范围：', pos=(10, 13))
            self.radio1 = wx.RadioButton(self.rightpanel, -1, u'集数<=14（季番）', (160, 13), style=wx.RB_GROUP)
            self.radio2 = wx.RadioButton(self.rightpanel, -1, u'14<集数<=26（半年番）', (310, 13))
            self.radio3 = wx.RadioButton(self.rightpanel, -1, u'集数>26（长篇）', (500, 13))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_jidu8 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_jidu8.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(640, 40))
            self.Bind(wx.EVT_BUTTON, self.OnOK9, okButton)
        if choose == 'STAFF':
            type_tmp9 = ['导演','编剧','音乐','动画人设']
            wx.StaticText(self.rightpanel, -1, u'请选择STAFF职位：', pos=(10, 13))
            self.choice_type9_1 = wx.Choice(self.rightpanel, choices=type_tmp9, size=(80, -1), pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入STAFF姓名：', pos=(280, 13))
            self.choice_type9_2 = wx.TextCtrl(self.rightpanel, -1, '', size=(160, -1), style=wx.TE_RICH, pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_jidu9 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_jidu9.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(600, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK10, okButton)
        if choose == 'CV':
            wx.StaticText(self.rightpanel, -1, u'请输入声优姓名：', pos=(10, 13))
            self.choice_type10 = wx.TextCtrl(self.rightpanel, -1, '', size=(160, -1), style=wx.TE_RICH, pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_jidu10 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_jidu10.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(350, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK11, okButton)
        if choose == '演唱':
            sql = "select 姓名 from 歌手演唱动画信息"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp11 = []
            for i in res:
                type_tmp11.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择歌手/组合/乐队名：', pos=(10, 13))
            self.choice_type11 = wx.Choice(self.rightpanel, choices=type_tmp11, size=(200, -1), pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_jidu11 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_jidu11.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK12, okButton)
        if choose == '类别':
            sql = "select distinct 类别 from 动画类别"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp12 = []
            for i in res:
                type_tmp12.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择类别：', pos=(10, 33))
            wx.StaticText(self.rightpanel, -1, u'类别1', pos=(100, 10))
            self.choice_type12_1 = wx.Choice(self.rightpanel, choices=type_tmp12, size=(80, -1), pos=(100, 30))
            wx.StaticText(self.rightpanel, -1, u'类别2', pos=(220, 10))
            self.choice_type12_2 = wx.Choice(self.rightpanel, choices=type_tmp12, size=(80, -1), pos=(220, 30))
            wx.StaticText(self.rightpanel, -1, u'类别3', pos=(340, 10))
            self.choice_type12_3 = wx.Choice(self.rightpanel, choices=type_tmp12, size=(80, -1), pos=(340, 30))
            wx.StaticText(self.rightpanel, -1, u'类别4', pos=(460, 10))
            self.choice_type12_4 = wx.Choice(self.rightpanel, choices=type_tmp12, size=(80, -1), pos=(460, 30))
            wx.StaticText(self.rightpanel, -1, u'【注】将返回符合四种类别中任一种的动画', pos=(10, 70))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(600, 30))
            self.Bind(wx.EVT_BUTTON, self.OnOK13, okButton)

    def OnOK1(self, evt):
        sql = "select 名称 from 动画"
        cur.execute(sql)
        res = cur.fetchall()
        total_animate_name = []
        for i in res:
            total_animate_name.append(i[0])

        if self.animate_name.GetValue() not in total_animate_name:
            wx.MessageBox(u'系统中不存在该动画', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            self.animate_name.Clear()
            return

        if self.name != '':
            self.title.SetLabel('')
            restory2 = 1
            recast2 = 1
            remusic2 = 1
            restaff2 = 1
        else:
            restory2 = 0
            recast2 = 0
            remusic2 = 0
            restaff2 = 0

        self.name = self.animate_name.GetValue()
        self.title = wx.StaticText(self.rightpanel, -1, self.name, pos=(10, 50))
        self.title.SetBackgroundColour('Turquoise')
        self.title.SetFont(self.font2)

        story1 = wx.StaticText(self.rightpanel, -1, u'简介', (10, 92), (40, -1), wx.ALIGN_CENTER)
        story1.SetBackgroundColour('cyan')

        path = './intro/' + self.name + '.txt'
        if os.path.exists(path):
            f1 = open(path, 'r')
            intro = f1.read()
            f1.close()
        else:
            intro = ''
        if restory2 == 0:
            self.story2 = wx.TextCtrl(self.rightpanel, -1, intro, size=(300, 300), style=wx.TE_MULTILINE | wx.TE_READONLY, pos=(10, 110))
        else:
            self.story2.SetValue(intro)

        sql = "select * from 动画基本信息 where 名称 = %s"
        cur.execute(sql, self.name)
        res = cur.fetchall()[0]
        fangsong = wx.StaticText(self.rightpanel, -1, res[10]+'放送', pos=(220, 90))
        fangsong.SetBackgroundColour('Turquoise')

        tag1 = wx.StaticText(self.rightpanel, -1, res[9], (315, 110), (80, -1), wx.ALIGN_CENTER)
        tag1.SetBackgroundColour('cyan')
        tag2 = wx.StaticText(self.rightpanel, -1, res[1], (315, 140), (80, -1), wx.ALIGN_CENTER)
        tag2.SetBackgroundColour('cyan')
        tag3 = wx.StaticText(self.rightpanel, -1, res[2], (315, 170), (80, -1), wx.ALIGN_CENTER)
        tag3.SetBackgroundColour('cyan')
        tag4 = wx.StaticText(self.rightpanel, -1, '共'+str(res[11])+'集', (315, 200), (80, -1), wx.ALIGN_CENTER)
        tag4.SetBackgroundColour('cyan')

        sql = "select 类别 from 动画类别 where 名称 = %s"
        cur.execute(sql, self.name)
        res1 = cur.fetchall()
        weizhi = 392
        for i in res1:
            for j in i:
                tag5 = wx.StaticText(self.rightpanel, -1, j, (315, weizhi), (80, -1), wx.ALIGN_CENTER)
                tag5.SetBackgroundColour('cyan')
                weizhi -= 30

        sql = "select * from 每季度番剧数量 where 新番季度 = %s"
        cur.execute(sql, res[9])
        res2 = cur.fetchall()[0]
        animate_type = '本季度动画数量共'+str(res2[1])+'部\n新作动画\t'+str(res2[2])+'部\t\t漫画改编动画\t'+str(
            res2[6])+'部\n续作动画\t'+str(res2[3])+'部\t\t小说改编动画\t'+str(res2[7])+'部\n衍生动画\t'+str(
            res2[4])+'部\t\t游戏改编动画\t'+str(res2[8])+'部\n重制动画\t'+str(res2[5])+'部\t\t原创动画\t'+str(
            res2[9])+'部'
        xinxi = wx.StaticText(self.rightpanel, -1, animate_type, (10, 425), (385, 85))
        xinxi.SetBackgroundColour('Turquoise')

        sql = "select 角色,姓名,代表作 from 动画配音列表 where 动画 = %s"
        cur.execute(sql, self.name)
        res3 = cur.fetchall()
        cast_list = ''
        for i in res3:
            cast_list += i[0]+'——'+i[1]
            if i[2] != None:
                cast_list += '      \t'+i[2]+'\n'
            else:
                cast_list += '\n'
        cast_list1 = cast_list.strip('\n')
        cast1 = wx.StaticText(self.rightpanel, -1, 'CAST', (410, 50), (40, -1), wx.ALIGN_CENTER)
        cast1.SetBackgroundColour('cyan')
        if recast2 == 0:
            self.cast2 = wx.TextCtrl(self.rightpanel, -1, cast_list1, size=(460, 130), style=wx.TE_MULTILINE |
                    wx.TE_READONLY | wx.HSCROLL, pos=(410, 68))
        else:
            self.cast2.SetValue(cast_list1)

        sql = "select 类型,名称,歌手 from 动画音乐列表 where 动画 = %s"
        cur.execute(sql, self.name)
        res4 = cur.fetchall()
        music_list = ''
        for i in res4:
            music_list += i[0] + '\t' + i[1] + ' —— ' + i[2] + '\n'
        music_list1 = music_list.strip('\n')
        music1 = wx.StaticText(self.rightpanel, -1, u'音乐', (410, 213), (40, -1), wx.ALIGN_CENTER)
        music1.SetBackgroundColour('cyan')
        if remusic2 == 0:
            self.music2 = wx.TextCtrl(self.rightpanel, -1, music_list1, size=(460, 80), style=wx.TE_MULTILINE |
                    wx.TE_READONLY | wx.HSCROLL, pos=(410, 231))
        else:
            self.music2.SetValue(music_list1)

        orign_list = ''
        if res[3] != None:
            orign_list += '原作公司：' + res[3]
            if res[4] != None:
                orign_list += '\t' + res[4]
        if res[5] != None:
            orign_list += '\n原作者：' + res[5]
            if res[6] != None:
                orign_list += '\t' + res[6]
        orign1 = wx.StaticText(self.rightpanel, -1, u'原作', (410, 326), (40, -1), wx.ALIGN_CENTER)
        orign1.SetBackgroundColour('cyan')
        orign2 = wx.StaticText(self.rightpanel, -1, orign_list, (410, 344), (460, 54))
        orign2.SetBackgroundColour('Turquoise')

        sql = "select 职位,姓名,代表作 from 动画制作组列表 where 动画 = %s"
        cur.execute(sql, self.name)
        res5 = cur.fetchall()
        staff_list = ''
        for i in res5:
            staff_list += i[0] + '：' + i[1] + '\t'
            if i[2] != None:
                staff_list += i[2] + '\n'
            else:
                staff_list += '\n'
        staff_list += '动画制作：' + res[7] + '\t' + res[8]
        staff1 = wx.StaticText(self.rightpanel, -1, 'STAFF', (410, 407), (40, -1), wx.ALIGN_CENTER)
        staff1.SetBackgroundColour('cyan')
        if restaff2 == 0:
            self.staff2 = wx.TextCtrl(self.rightpanel, -1, staff_list, size=(460, 85), style=wx.TE_MULTILINE |
                    wx.TE_READONLY | wx.HSCROLL, pos=(410, 425))
        else:
            self.staff2.SetValue(staff_list)

    def OnOK2(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice1 = self.choice_type1.GetStringSelection()
        choice1_time = self.choice_jidu1.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(270, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(400, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(490, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(620, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(700, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(800, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')

        if choice1_time == '所有':
            sql = "select 名称,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 动画 where 制作类型=%s"
            cur.execute(sql, choice1)
        elif '年' in choice1_time:
            sql = "select 名称,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 动画 where 制作类型=%s and 新番季度=%s"
            cur.execute(sql, (choice1, choice1_time))
        else:
            sql = "select 名称,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 带年份的动画表 where 制作类型=%s and 年份=%s"
            cur.execute(sql, (choice1, choice1_time))

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            if i[2] != None:
                wx.StaticText(self.rightpanel, -1, i[2], pos=(270, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(400, weizhi))
            wx.StaticText(self.rightpanel, -1, i[4], pos=(490, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(620, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(700, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(800, weizhi))

    def OnOK3(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice2 = self.choice_type2.GetStringSelection()
        choice2_time = self.choice_jidu2.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(270, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(400, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(490, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(620, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(700, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(800, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')

        if choice2_time == '所有':
            sql = "select 名称,制作类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 动画 where 改编类型=%s"
            cur.execute(sql, choice2)
        elif '年' in choice2_time:
            sql = "select 名称,制作类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 动画 where 改编类型=%s and 新番季度=%s"
            cur.execute(sql, (choice2, choice2_time))
        else:
            sql = "select 名称,制作类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 带年份的动画表 where 改编类型=%s and 年份=%s"
            cur.execute(sql, (choice2, choice2_time))

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            if i[2] != None:
                wx.StaticText(self.rightpanel, -1, i[2], pos=(270, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(400, weizhi))
            wx.StaticText(self.rightpanel, -1, i[4], pos=(490, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(620, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(700, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(800, weizhi))

    def OnOK4(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice3 = self.choice_type3.GetStringSelection()
        choice3_time = self.choice_jidu3.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(280, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(380, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(470, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(600, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(680, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(780, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')

        if choice3_time == '所有':
            sql = "select 名称,制作类型,改编类型,原作者,制作公司,新番季度,首播时间,总集数 from 动画 where 原作公司=%s"
            cur.execute(sql, choice3)
        elif '年' in choice3_time:
            sql = "select 名称,制作类型,改编类型,原作者,制作公司,新番季度,首播时间,总集数 from 动画 where 原作公司=%s and 新番季度=%s"
            cur.execute(sql, (choice3, choice3_time))
        else:
            sql = "select 名称,制作类型,改编类型,原作者,制作公司,新番季度,首播时间,总集数 from 带年份的动画表 where 原作公司=%s and 年份=%s"
            cur.execute(sql, (choice3, choice3_time))

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(280, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(380, weizhi))
            wx.StaticText(self.rightpanel, -1, i[4], pos=(470, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(600, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(680, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(780, weizhi))

    def OnOK5(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice4 = self.choice_type4.GetStringSelection()
        choice4_time = self.choice_jidu4.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(270, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(340, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(470, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(600, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(680, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(780, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')

        if choice4_time == '所有':
            sql = "select 名称,制作类型,改编类型,原作公司,制作公司,新番季度,首播时间,总集数 from 动画 where 原作者=%s"
            cur.execute(sql, choice4)
        elif '年' in choice4_time:
            sql = "select 名称,制作类型,改编类型,原作公司,制作公司,新番季度,首播时间,总集数 from 动画 where 原作者=%s and 新番季度=%s"
            cur.execute(sql, (choice4, choice4_time))
        else:
            sql = "select 名称,制作类型,改编类型,原作公司,制作公司,新番季度,首播时间,总集数 from 带年份的动画表 where 原作者=%s and 年份=%s"
            cur.execute(sql, (choice4, choice4_time))

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(270, weizhi))
            wx.StaticText(self.rightpanel, -1, i[3], pos=(340, weizhi))
            wx.StaticText(self.rightpanel, -1, i[4], pos=(470, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(600, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(680, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(780, weizhi))

    def OnOK6(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        wx.StaticText(self.rightpanel, -1, '', (650, 53), (200, 30))
        choice5 = self.choice_type5.GetStringSelection()
        choice5_time = self.choice_jidu5.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(270, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(340, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(470, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(600, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(680, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(780, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')

        if choice5_time == '所有':
            sql = "select 名称,制作类型,改编类型,原作公司,原作者,新番季度,首播时间,总集数 from 动画 where 制作公司=%s"
            cur.execute(sql, choice5)
        elif '年' in choice5_time:
            sql = "select 名称,制作类型,改编类型,原作公司,原作者,新番季度,首播时间,总集数 from 动画 where 制作公司=%s and 新番季度=%s"
            cur.execute(sql, (choice5, choice5_time))
        else:
            sql = "select 名称,制作类型,改编类型,原作公司,原作者,新番季度,首播时间,总集数 from 带年份的动画表 where 制作公司=%s and 年份=%s"
            cur.execute(sql, (choice5, choice5_time))

        res = cur.fetchall()
        weizhi = 100
        count = 0
        for i in res:
            weizhi += 20
            count += 1
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(270, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(340, weizhi))
            if i[4] != None:
                wx.StaticText(self.rightpanel, -1, i[4], pos=(470, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(600, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(680, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(780, weizhi))
        if '年' in choice5_time:
            num = wx.StaticText(self.rightpanel, -1, u'本季度制作动画数量：'+str(count)+'部', pos=(650, 53))
            num.SetBackgroundColour('cyan')

    def OnOK7(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 70), (1000, 600))
        wx.StaticText(self.rightpanel, -1, '', (500, 10), (320, 70))
        choice6 = self.choice_type6.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(270, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(340, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(470, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(560, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(680, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(780, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')

        sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,首播时间,总集数 from 动画 where 新番季度=%s"
        cur.execute(sql, choice6)
        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(270, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(340, weizhi))
            if i[4] != None:
                wx.StaticText(self.rightpanel, -1, i[4], pos=(470, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(560, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(680, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(780, weizhi))

        sql = "select * from 每季度番剧数量 where 新番季度 = %s"
        cur.execute(sql, choice6)
        res1 = cur.fetchall()[0]

        num1 = wx.StaticText(self.rightpanel, -1, u'本季度番剧数量：' + str(res1[1]) + '部', pos=(10, 70))
        num1.SetBackgroundColour('cyan')

        num_list = '新作动画\t' + str(res1[2]) + '部\t\t漫画改编动画\t' + str(
            res1[6]) + '部\n续作动画\t' + str(res1[3]) + '部\t\t小说改编动画\t' + str(res1[7]) + '部\n衍生动画\t' + str(
            res1[4]) + '部\t\t游戏改编动画\t' + str(res1[8]) + '部\n重制动画\t' + str(res1[5]) + '部\t\t原创动画\t' + str(
            res1[9]) + '部'
        num2 = wx.StaticText(self.rightpanel, -1, num_list, (500, 10), (320,70))
        num2.SetBackgroundColour('Turquoise')

    def OnOK8(self, evt):
        choice7 = self.choice_type7.GetValue()
        choice7_time = self.choice_jidu7.GetValue()
        date1 = datetime.datetime.strptime(choice7, '%Y%m%d')
        date2 = datetime.datetime.strptime(choice7_time, '%Y%m%d')

        if date1 > date2:
            wx.MessageBox(u'起始时间不能晚于终止时间', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            self.choice_type7.Clear()
            self.choice_jidu7.Clear()
            return

        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(270, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(340, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(440, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(520, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(630, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(710, 100))
        label9 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(800, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')
        label9.SetBackgroundColour('Turquoise')

        sql = "select * from 动画 where 首播时间 >= convert(date,%s) and 首播时间 <= convert(date,%s) order by 首播时间"
        cur.execute(sql, (choice7, choice7_time))
        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(270, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(340, weizhi))
            if i[4] != None:
                wx.StaticText(self.rightpanel, -1, i[4], pos=(440, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(520, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(630, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(710, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[8]), pos=(800, weizhi))

    def OnOK9(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice8_time = self.choice_jidu8.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(270, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(340, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(440, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(520, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(630, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(710, 100))
        label9 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(800, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')
        label9.SetBackgroundColour('Turquoise')

        if self.radio1.GetValue() == True:
            if choice8_time == '所有':
                sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 季番表"
                cur.execute(sql)
            elif '年' in choice8_time:
                sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 季番表 where 新番季度=%s"
                cur.execute(sql, choice8_time)
            else:
                sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 季番表 where 年份=%s"
                cur.execute(sql, choice8_time)
        if self.radio2.GetValue() == True:
            if choice8_time == '所有':
                sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 半年番表"
                cur.execute(sql)
            elif '年' in choice8_time:
                sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 半年番表 where 新番季度=%s"
                cur.execute(sql, choice8_time)
            else:
                sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 半年番表 where 年份=%s"
                cur.execute(sql, choice8_time)
        if self.radio3.GetValue() == True:
            if choice8_time == '所有':
                sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 长篇表"
                cur.execute(sql)
            elif '年' in choice8_time:
                sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 长篇表 where 新番季度=%s"
                cur.execute(sql, choice8_time)
            else:
                sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 长篇表 where 年份=%s"
                cur.execute(sql, choice8_time)

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(270, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(340, weizhi))
            if i[4] != None:
                wx.StaticText(self.rightpanel, -1, i[4], pos=(440, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(520, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(630, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(710, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[8]), pos=(800, weizhi))

    def OnOK10(self, evt):
        choice9_1 = self.choice_type9_1.GetStringSelection()
        choice9_2 = self.choice_type9_2.GetValue()
        choice9_time = self.choice_jidu9.GetStringSelection()

        sql = "select 姓名 from staff"
        cur.execute(sql)
        res = cur.fetchall()
        total_staff_name = []
        for i in res:
            total_staff_name.append(i[0])

        if choice9_2 not in total_staff_name:
            wx.MessageBox(u'系统中不存在该staff', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            self.choice_type9_2.Clear()
            return

        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(270, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(340, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(440, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(520, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(630, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(710, 100))
        label9 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(800, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')
        label9.SetBackgroundColour('Turquoise')

        if choice9_1 == '导演':
            if choice9_time == '所有':
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组导演表 where 姓名=%s"
                cur.execute(sql, choice9_2)
            elif '年' in choice9_time:
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组导演表 where 姓名=%s and 新番季度=%s"
                cur.execute(sql, (choice9_2, choice9_time))
            else:
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组导演表 where 姓名=%s and 年份=%s"
                cur.execute(sql, (choice9_2, choice9_time))
        if choice9_1 == '编剧':
            if choice9_time == '所有':
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组编剧表 where 姓名=%s"
                cur.execute(sql, choice9_2)
            elif '年' in choice9_time:
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组编剧表 where 姓名=%s and 新番季度=%s"
                cur.execute(sql, (choice9_2, choice9_time))
            else:
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组编剧表 where 姓名=%s and 年份=%s"
                cur.execute(sql, (choice9_2, choice9_time))
        if choice9_1 == '音乐':
            if choice9_time == '所有':
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组音乐表 where 姓名=%s"
                cur.execute(sql, choice9_2)
            elif '年' in choice9_time:
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组音乐表 where 姓名=%s and 新番季度=%s"
                cur.execute(sql, (choice9_2, choice9_time))
            else:
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组音乐表 where 姓名=%s and 年份=%s"
                cur.execute(sql, (choice9_2, choice9_time))
        if choice9_1 == '动画人设':
            if choice9_time == '所有':
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组动画人设表 where 姓名=%s"
                cur.execute(sql, choice9_2)
            elif '年' in choice9_time:
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组动画人设表 where 姓名=%s and 新番季度=%s"
                cur.execute(sql, (choice9_2, choice9_time))
            else:
                sql = "select 动画 as 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 制作组动画人设表 where 姓名=%s and 年份=%s"
                cur.execute(sql, (choice9_2, choice9_time))

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(270, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(340, weizhi))
            if i[4] != None:
                wx.StaticText(self.rightpanel, -1, i[4], pos=(440, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(520, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(630, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(710, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[8]), pos=(800, weizhi))

    def OnOK11(self, evt):
        choice10 = self.choice_type10.GetValue()
        choice10_time = self.choice_jidu10.GetStringSelection()

        sql = "select 姓名 from 人物 where 职业 = '声优'"
        cur.execute(sql)
        res = cur.fetchall()
        total_cv_name = []
        for i in res:
            total_cv_name.append(i[0])

        if choice10 not in total_cv_name:
            wx.MessageBox(u'系统中不存在该声优', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            self.choice_type10.Clear()
            return

        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        wx.StaticText(self.rightpanel, -1, '', (650, 53), (200, 30))

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(190, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(250, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(310, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(420, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(480, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(575, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(640, 100))
        label9 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(720, 100))
        label10 = wx.StaticText(self.rightpanel, -1, u'角色名', pos=(770, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')
        label9.SetBackgroundColour('Turquoise')
        label10.SetBackgroundColour('Turquoise')

        if choice10_time == '所有':
            sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数,角色 from 声优配过的动画及信息 where 姓名=%s"
            cur.execute(sql, choice10)
        elif '年' in choice10_time:
            sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数,角色 from 声优配过的动画及信息 where 姓名=%s and 新番季度=%s"
            cur.execute(sql, (choice10, choice10_time))
        else:
            sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数,角色 from 声优配过的动画及信息 where 姓名=%s and 年份=%s"
            cur.execute(sql, (choice10, choice10_time))

        res = cur.fetchall()
        weizhi = 100
        count = 0
        for i in res:
            weizhi += 20
            count += 1
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(190, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(250, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(310, weizhi))
            if i[4] != None:
                wx.StaticText(self.rightpanel, -1, i[4], pos=(420, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(480, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(575, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(640, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[8]), pos=(720, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[9]), pos=(770, weizhi))

        if '年' in choice10_time:
            num = wx.StaticText(self.rightpanel, -1, u'本季度配音数量：'+str(count)+'部', pos=(650, 53))
            num.SetBackgroundColour('cyan')

    def OnOK12(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice11 = self.choice_type11.GetStringSelection()
        choice11_time = self.choice_jidu11.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'制作类型', pos=(200, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'改编类型', pos=(270, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'原作公司', pos=(340, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'原作者', pos=(440, 100))
        label6 = wx.StaticText(self.rightpanel, -1, u'制作公司', pos=(520, 100))
        label7 = wx.StaticText(self.rightpanel, -1, u'新番季度', pos=(630, 100))
        label8 = wx.StaticText(self.rightpanel, -1, u'首播时间', pos=(710, 100))
        label9 = wx.StaticText(self.rightpanel, -1, u'总集数', pos=(800, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')
        label8.SetBackgroundColour('Turquoise')
        label9.SetBackgroundColour('Turquoise')

        if choice11_time == '所有':
            sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 歌手演唱动画信息 where 姓名=%s"
            cur.execute(sql, choice11)
        elif '年' in choice11_time:
            sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 歌手演唱动画信息 where 姓名=%s and 新番季度=%s"
            cur.execute(sql, (choice11, choice11_time))
        else:
            sql = "select 名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数 from 歌手演唱动画信息 where 姓名=%s and 年份=%s"
            cur.execute(sql, (choice11, choice11_time))

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(270, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(340, weizhi))
            if i[4] != None:
                wx.StaticText(self.rightpanel, -1, i[4], pos=(440, weizhi))
            wx.StaticText(self.rightpanel, -1, i[5], pos=(520, weizhi))
            wx.StaticText(self.rightpanel, -1, i[6], pos=(630, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[7]), pos=(710, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[8]), pos=(800, weizhi))

    def OnOK13(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice12_1 = self.choice_type12_1.GetStringSelection()
        choice12_2 = self.choice_type12_2.GetStringSelection()
        choice12_3 = self.choice_type12_3.GetStringSelection()
        choice12_4 = self.choice_type12_4.GetStringSelection()
        choice12_list = []
        if choice12_1 not in choice12_list and choice12_1 != '':
            choice12_list.append(choice12_1)
        if choice12_2 not in choice12_list and choice12_2 != '':
            choice12_list.append(choice12_2)
        if choice12_3 not in choice12_list and choice12_3 != '':
            choice12_list.append(choice12_3)
        if choice12_4 not in choice12_list and choice12_4 != '':
            choice12_list.append(choice12_4)

        label1 = wx.StaticText(self.rightpanel, -1, u'名称', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'类别', pos=(300, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')

        res_list = []
        for choice12 in choice12_list:
            sql = "select 名称,类别2 from 类别动画类别 where 类别1=%s"
            cur.execute(sql, choice12)
            res = cur.fetchall()
            for i in res:
                if i not in res_list:
                    res_list.append(i)

        weizhi = 100
        hengxiang = 0
        last_name = ''
        for i in res_list:
            if i[0] != last_name:
                weizhi += 20
                hengxiang = 0
                wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
                last_name = i[0]
            wx.StaticText(self.rightpanel, -1, i[1], pos=(300+hengxiang, weizhi))
            hengxiang += 50

    def OnListbox2(self, event):
        choose = event.GetString()
        for child in self.rightpanel.GetChildren():
            child.Destroy()

        if choose == '原作公司基本信息':
            sql = "select 名称 from 原作公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp1 = []
            for i in res:
                type_tmp1.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择原作公司名称：', pos=(10, 13))
            self.choice_company1 = wx.Choice(self.rightpanel, choices=type_tmp1, size=(200, -1), pos=(160, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK14, okButton)
        if choose == '被动画化的作品':
            sql = "select 名称 from 原作公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp2 = []
            for i in res:
                type_tmp2.append(i[0])

            sql = "select * from 限制时间"
            cur.execute(sql)
            res = cur.fetchall()
            timelimit = ['所有']
            for i in res:
                timelimit.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择原作公司名称：', pos=(10, 13))
            self.choice_company2 = wx.Choice(self.rightpanel, choices=type_tmp2, size=(200, -1), pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_time2 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_time2.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK15, okButton)
        if choose == '主要业务':
            type_tmp3 = ['漫画出版社','轻小说出版社','游戏公司']
            wx.StaticText(self.rightpanel, -1, u'请选择原作公司业务类型：', pos=(10, 13))
            self.choice_company3 = wx.Choice(self.rightpanel, choices=type_tmp3, size=(180, -1), pos=(180, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK16, okButton)

    def OnOK14(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice1 = self.choice_company1.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'地址：', pos=(10, 130))
        label3 = wx.StaticText(self.rightpanel, -1, u'成立时间：', pos=(10, 160))
        label4 = wx.StaticText(self.rightpanel, -1, u'主要业务：', pos=(10, 190))
        label5 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 220))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')

        sql = "select * from 原作公司 where 名称=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0]
        wx.StaticText(self.rightpanel, -1, res[0], pos=(100, 100))
        if res[1] != None:
            wx.StaticText(self.rightpanel, -1, res[1], pos=(100, 130))
        if res[2] != None:
            wx.StaticText(self.rightpanel, -1, res[2], pos=(100, 160))
        if res[3] != None:
            wx.StaticText(self.rightpanel, -1, res[3], pos=(100, 190))
        if res[4] != None:
            wx.StaticText(self.rightpanel, -1, res[4], pos=(100, 220))

    def OnOK15(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice2 = self.choice_company2.GetStringSelection()
        choice2_time = self.choice_time2.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'地址：', pos=(10, 130))
        label3 = wx.StaticText(self.rightpanel, -1, u'成立时间：', pos=(10, 160))
        label4 = wx.StaticText(self.rightpanel, -1, u'主要业务：', pos=(10, 190))
        label5 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 220))
        label6 = wx.StaticText(self.rightpanel, -1, u'作品数量：', pos=(10, 250))
        wx.StaticText(self.rightpanel, -1, u'（当前放送时间限制范围内）', pos=(180, 250))
        label7 = wx.StaticText(self.rightpanel, -1, u'被动画化的作品：', pos=(10, 280))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')
        label7.SetBackgroundColour('Turquoise')

        if choice2_time == '所有':
            sql = "select 名称,地址,成立时间,主要业务,代表作,动画 from 原作公司被动画化作品 where 名称=%s"
            cur.execute(sql, choice2)
        elif '年' in choice2_time:
            sql = "select 名称,地址,成立时间,主要业务,代表作,动画 from 原作公司被动画化作品 where 名称=%s and 新番季度=%s"
            cur.execute(sql, (choice2, choice2_time))
        else:
            sql = "select 名称,地址,成立时间,主要业务,代表作,动画 from 原作公司被动画化作品 where 名称=%s and 年份=%s"
            cur.execute(sql, (choice2, choice2_time))

        res = cur.fetchall()
        count = 0
        if res != []:
            wx.StaticText(self.rightpanel, -1, res[0][0], pos=(150, 100))
            if res[0][1] != None:
                wx.StaticText(self.rightpanel, -1, res[0][1], pos=(150, 130))
            if res[0][2] != None:
                wx.StaticText(self.rightpanel, -1, res[0][2], pos=(150, 160))
            if res[0][3] != None:
                wx.StaticText(self.rightpanel, -1, res[0][3], pos=(150, 190))
            if res[0][4] != None:
                wx.StaticText(self.rightpanel, -1, res[0][4], pos=(150, 220))
            weizhi = 280
            for i in res:
                wx.StaticText(self.rightpanel, -1, i[5], pos=(150, weizhi))
                weizhi += 30
                count += 1
        wx.StaticText(self.rightpanel, -1, str(count), pos=(150, 250))

    def OnOK16(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice3 = self.choice_company3.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'主要业务：', pos=(200, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')

        if '漫画' in choice3:
            sql = "select 名称,主要业务 from 原作公司被动画化作品 where 改编类型='漫改'"
        elif '轻小说' in choice3:
            sql = "select 名称,主要业务 from 原作公司被动画化作品 where 改编类型='轻改'"
        else:
            sql = "select 名称,主要业务 from 原作公司被动画化作品 where 改编类型='游戏改'"

        cur.execute(sql)
        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            if i[1] != None:
                wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))

    def OnListbox3(self, event):
        choose = event.GetString()
        for child in self.rightpanel.GetChildren():
            child.Destroy()

        if choose == '动画公司基本信息':
            sql = "select 名称 from 动画公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp1 = []
            for i in res:
                type_tmp1.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择动画公司名称：', pos=(10, 13))
            self.choice_make1 = wx.Choice(self.rightpanel, choices=type_tmp1, size=(200, -1), pos=(160, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK17, okButton)
        if choose == '制作动画':
            sql = "select 名称 from 动画公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp2 = []
            for i in res:
                type_tmp2.append(i[0])

            sql = "select * from 限制时间"
            cur.execute(sql)
            res = cur.fetchall()
            timelimit = ['所有']
            for i in res:
                timelimit.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择动画公司名称：', pos=(10, 13))
            self.choice_make2 = wx.Choice(self.rightpanel, choices=type_tmp2, size=(200, -1), pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_time3 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_time3.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK18, okButton)

    def OnOK17(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice1 = self.choice_make1.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'地址：', pos=(10, 130))
        label3 = wx.StaticText(self.rightpanel, -1, u'成立时间：', pos=(10, 160))
        label4 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 190))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')

        sql = "select * from 动画公司 where 名称=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0]
        wx.StaticText(self.rightpanel, -1, res[0], pos=(100, 100))
        if res[1] != None:
            wx.StaticText(self.rightpanel, -1, res[1], pos=(100, 130))
        if res[2] != None:
            wx.StaticText(self.rightpanel, -1, res[2], pos=(100, 160))
        if res[3] != None:
            wx.StaticText(self.rightpanel, -1, res[3], pos=(100, 190))

    def OnOK18(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice2 = self.choice_make2.GetStringSelection()
        choice2_time = self.choice_time3.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'地址：', pos=(10, 130))
        label3 = wx.StaticText(self.rightpanel, -1, u'成立时间：', pos=(10, 160))
        label4 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 190))
        label5 = wx.StaticText(self.rightpanel, -1, u'作品数量：', pos=(10, 220))
        wx.StaticText(self.rightpanel, -1, u'（当前放送时间限制范围内）', pos=(180, 220))
        label6 = wx.StaticText(self.rightpanel, -1, u'制作动画作品：', pos=(10, 250))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')
        label6.SetBackgroundColour('Turquoise')

        if choice2_time == '所有':
            sql = "select 名称,地址,成立时间,代表作,动画 from 动画公司制作作品 where 名称=%s"
            cur.execute(sql, choice2)
        elif '年' in choice2_time:
            sql = "select 名称,地址,成立时间,代表作,动画 from 动画公司制作作品 where 名称=%s and 新番季度=%s"
            cur.execute(sql, (choice2, choice2_time))
        else:
            sql = "select 名称,地址,成立时间,代表作,动画 from 动画公司制作作品 where 名称=%s and 年份=%s"
            cur.execute(sql, (choice2, choice2_time))

        res = cur.fetchall()
        count = 0
        if res != []:
            wx.StaticText(self.rightpanel, -1, res[0][0], pos=(150, 100))
            if res[0][1] != None:
                wx.StaticText(self.rightpanel, -1, res[0][1], pos=(150, 130))
            if res[0][2] != None:
                wx.StaticText(self.rightpanel, -1, res[0][2], pos=(150, 160))
            if res[0][3] != None:
                wx.StaticText(self.rightpanel, -1, res[0][3], pos=(150, 190))

            weizhi = 250
            for i in res:
                wx.StaticText(self.rightpanel, -1, i[4], pos=(150, weizhi))
                weizhi += 30
                count += 1
        wx.StaticText(self.rightpanel, -1, str(count), pos=(150, 220))

    def OnListbox4(self, event):
        choose = event.GetString()
        for child in self.rightpanel.GetChildren():
            child.Destroy()

        if choose == '人物基本信息':
            wx.StaticText(self.rightpanel, -1, u'请输入人物/组合姓名：', pos=(10, 13))
            self.choice_people1 = wx.TextCtrl(self.rightpanel, -1, '', size=(200, -1), style=wx.TE_RICH, pos=(160, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK19, okButton)
        if choose == '职业':
            type_tmp1 = ['漫画家', '小说家', '声优']
            type_tmp2 = ['所有', '男', '女']
            wx.StaticText(self.rightpanel, -1, u'请选择人物职业：', pos=(10, 13))
            self.choice_people2 = wx.Choice(self.rightpanel, choices=type_tmp1, size=(100, -1), pos=(150, 10))
            wx.StaticText(self.rightpanel, -1, u'仅支持漫画家、小说家、声优的查询', pos=(280, 13))
            wx.StaticText(self.rightpanel, -1, u'请选择声优性别：', pos=(10, 53))
            self.choice_time4 = wx.Choice(self.rightpanel, choices=type_tmp2, size=(100, -1), pos=(150, 50))
            self.choice_time4.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'只适用于限制声优性别', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(500, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK20, okButton)
        if choose == '作品参与':
            sql = "select distinct 新番季度 from 动画"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp3 = []
            for i in res:
                type_tmp3.append(i[0])
            type_tmp4 = ['原作漫画作者', '原作小说作者', '原作游戏作者', '声优配音', '音乐演唱']

            wx.StaticText(self.rightpanel, -1, u'请选择新番季度：', pos=(10, 13))
            self.choice_people3 = wx.Choice(self.rightpanel, choices=type_tmp3, size=(100, -1), pos=(150, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择参与方式：', pos=(10, 53))
            self.choice_time5 = wx.Choice(self.rightpanel, choices=type_tmp4, size=(100, -1), pos=(150, 50))
            wx.StaticText(self.rightpanel, -1, u'按照参与动画数量降序排序', pos=(300, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(300, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK21, okButton)

    def OnOK19(self, evt):
        choice1 = self.choice_people1.GetValue()

        sql = "select 姓名 from 人物"
        cur.execute(sql)
        res = cur.fetchall()
        total_people_name = []
        for i in res:
            total_people_name.append(i[0])

        if choice1 not in total_people_name:
            wx.MessageBox(u'系统中不存在该人物/组合', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            self.choice_people1.Clear()
            return

        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))

        label1 = wx.StaticText(self.rightpanel, -1, u'姓名：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'性别：', pos=(10, 130))
        label3 = wx.StaticText(self.rightpanel, -1, u'出生日期：', pos=(10, 160))
        label4 = wx.StaticText(self.rightpanel, -1, u'职业：', pos=(10, 190))
        label5 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 220))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')

        sql = "select * from 人物 where 姓名=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0]
        wx.StaticText(self.rightpanel, -1, res[0], pos=(100, 100))
        if res[1] != None:
            wx.StaticText(self.rightpanel, -1, res[1], pos=(100, 130))
        if res[2] != None:
            wx.StaticText(self.rightpanel, -1, res[2], pos=(100, 160))
        wx.StaticText(self.rightpanel, -1, res[3], pos=(100, 190))
        if res[4] != None:
            wx.StaticText(self.rightpanel, -1, res[4], pos=(100, 220))

    def OnOK20(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice2 = self.choice_people2.GetStringSelection()
        choice2_time = self.choice_time4.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'姓名', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'性别', pos=(100, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'出生日期', pos=(150, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'代表作', pos=(250, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')

        if choice2 == '漫画家' or choice2 == '小说家':
            sql = "select 姓名,性别,出生日期,代表作 from 人物 where 职业=%s"
            cur.execute(sql, choice2)
        elif choice2_time == '所有':
            sql = "select 姓名,性别,出生日期,代表作 from 人物 where 职业='声优'"
            cur.execute(sql)
        else:
            sql = "select 姓名,性别,出生日期,代表作 from 人物 where 职业='声优' and 性别=%s"
            cur.execute(sql, choice2_time)

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            if i[1] != None:
                wx.StaticText(self.rightpanel, -1, i[1], pos=(100, weizhi))
            if i[2] != None:
                wx.StaticText(self.rightpanel, -1, i[2], pos=(150, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(250, weizhi))

    def OnOK21(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice3 = self.choice_people3.GetStringSelection()
        choice3_time = self.choice_time5.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'姓名', pos=(10,100))
        label2 = wx.StaticText(self.rightpanel, -1, u'作品参与数量', pos=(80, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'性别', pos=(160, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'出生日期', pos=(190, 100))
        label5 = wx.StaticText(self.rightpanel, -1, u'代表作', pos=(290, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')
        label5.SetBackgroundColour('Turquoise')

        if '漫画' in choice3_time:
            sql = "select 姓名,参与数量,性别,出生日期,代表作 from 原作作者参与动画 where 新番季度=%s and 改编类型='漫改' order by 参与数量 desc"
            cur.execute(sql, choice3)
        elif '小说' in choice3_time:
            sql = "select 姓名,参与数量,性别,出生日期,代表作 from 原作作者参与动画 where 新番季度=%s and 改编类型='轻改' order by 参与数量 desc"
            cur.execute(sql, choice3)
        elif '游戏' in choice3_time:
            sql = "select 姓名,参与数量,性别,出生日期,代表作 from 原作作者参与动画 where 新番季度=%s and 改编类型='游戏改' order by 参与数量 desc"
            cur.execute(sql, choice3)
        elif '声优' in choice3_time:
            sql = "select 姓名,参与数量,性别,出生日期,代表作 from 声优参与动画 where 新番季度=%s order by 参与数量 desc"
            cur.execute(sql, choice3)
        else:
            sql = "select 姓名,参与数量,性别,出生日期,代表作 from 歌手组合参与动画 where 新番季度=%s order by 参与数量 desc"
            cur.execute(sql, choice3)

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, str(i[1]), pos=(80, weizhi))
            if i[2] != None:
                wx.StaticText(self.rightpanel, -1, i[2], pos=(160, weizhi))
            if i[3] != None:
                wx.StaticText(self.rightpanel, -1, i[3], pos=(190, weizhi))
            if i[4] != None:
                wx.StaticText(self.rightpanel, -1, i[4], pos=(290, weizhi))

    def OnListbox5(self, event):
        choose = event.GetString()
        for child in self.rightpanel.GetChildren():
            child.Destroy()

        if choose == 'staff基本信息':
            wx.StaticText(self.rightpanel, -1, u'请输入staff姓名：', pos=(10, 13))
            self.choice_staff1 = wx.TextCtrl(self.rightpanel, -1, '', size=(200, -1), style=wx.TE_RICH, pos=(160, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK22, okButton)
        if choose == '职位':
            type_tmp2 = ['导演', '编剧', '音乐', '动画人设']
            wx.StaticText(self.rightpanel, -1, u'请选择staff职位：', pos=(10, 13))
            self.choice_staff2 = wx.Choice(self.rightpanel, choices=type_tmp2, size=(100, -1), pos=(150, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(300, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK23, okButton)
        if choose == '作品参与':
            sql = "select * from 限制时间"
            cur.execute(sql)
            res = cur.fetchall()
            timelimit = ['所有']
            for i in res:
                timelimit.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请输入staff姓名：', pos=(10, 13))
            self.choice_staff3 = wx.TextCtrl(self.rightpanel, -1, '', size=(200, -1), style=wx.TE_RICH, pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_time6 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_time6.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK24, okButton)

    def OnOK22(self, evt):
        choice1 = self.choice_staff1.GetValue()

        sql = "select 姓名 from staff"
        cur.execute(sql)
        res = cur.fetchall()
        total_staff_name = []
        for i in res:
            total_staff_name.append(i[0])

        if choice1 not in total_staff_name:
            wx.MessageBox(u'系统中不存在该staff', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            self.choice_staff1.Clear()
            return

        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))

        label1 = wx.StaticText(self.rightpanel, -1, u'姓名：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 130))
        label3 = wx.StaticText(self.rightpanel, -1, u'担任过的职位：', pos=(10, 160))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')

        res_list = []
        sql = "select distinct 姓名,代表作 from 制作组导演表 where 姓名=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()
        if res != []:
            if res_list == []:
                res_list.append(res[0][0])
                res_list.append(res[0][1])
            res_list.append('导演')

        sql = "select distinct 姓名,代表作 from 制作组编剧表 where 姓名=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()
        if res != []:
            if res_list == []:
                res_list.append(res[0][0])
                res_list.append(res[0][1])
            res_list.append('编剧')

        sql = "select distinct 姓名,代表作 from 制作组音乐表 where 姓名=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()
        if res != []:
            if res_list == []:
                res_list.append(res[0][0])
                res_list.append(res[0][1])
            res_list.append('音乐')

        sql = "select distinct 姓名,代表作 from 制作组动画人设表 where 姓名=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()
        if res != []:
            if res_list == []:
                res_list.append(res[0][0])
                res_list.append(res[0][1])
            res_list.append('动画人设')

        wx.StaticText(self.rightpanel, -1, res_list[0], pos=(150, 100))
        if res_list[1] != None:
            wx.StaticText(self.rightpanel, -1, res_list[1], pos=(150, 130))
        hengxiang = 0
        for i in range(2, len(res_list)):
            wx.StaticText(self.rightpanel, -1, res_list[i], pos=(150 + hengxiang, 160))
            hengxiang += 50


    def OnOK23(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 60), (1000, 600))
        choice2 = self.choice_staff2.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'姓名', pos=(10,60))
        label2 = wx.StaticText(self.rightpanel, -1, u'代表作', pos=(200, 60))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')

        if choice2 == '导演':
            sql = "select 姓名,代表作 from 制作组导演表"
        elif choice2 == '编剧':
            sql = "select 姓名,代表作 from 制作组编剧表"
        elif choice2 == '音乐':
            sql = "select 姓名,代表作 from 制作组音乐表"
        else:
            sql = "select 姓名,代表作 from 制作组动画人设表"

        cur.execute(sql)
        res = cur.fetchall()
        weizhi = 60
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            if i[1] != None:
                wx.StaticText(self.rightpanel, -1, i[1], pos=(200, weizhi))

    def OnOK24(self, evt):
        choice3 = self.choice_staff3.GetValue()
        choice3_time = self.choice_time6.GetStringSelection()

        sql = "select 姓名 from staff"
        cur.execute(sql)
        res = cur.fetchall()
        total_staff_name = []
        for i in res:
            total_staff_name.append(i[0])

        if choice3 not in total_staff_name:
            wx.MessageBox(u'系统中不存在该staff', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            self.choice_staff3.Clear()
            return

        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))

        label1 = wx.StaticText(self.rightpanel, -1, u'姓名：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 130))
        label3 = wx.StaticText(self.rightpanel, -1, u'参与制作动画数量：', pos=(10, 160))
        wx.StaticText(self.rightpanel, -1, u'（当前放送时间限制范围内）', pos=(250, 160))
        label4 = wx.StaticText(self.rightpanel, -1, u'参与制作的动画及职位：', pos=(10, 190))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')

        if choice3_time == '所有':
            sql = "select 姓名,代表作,动画,职位 from staff参与动画 where 姓名=%s"
            cur.execute(sql, choice3)
        elif '年' in choice3_time:
            sql = "select 姓名,代表作,动画,职位 from staff参与动画 where 姓名=%s and 新番季度=%s"
            cur.execute(sql, (choice3, choice3_time))
        else:
            sql = "select 姓名,代表作,动画,职位 from staff参与动画 where 姓名=%s and 年份=%s"
            cur.execute(sql, (choice3, choice3_time))

        res = cur.fetchall()
        if res != []:
            wx.StaticText(self.rightpanel, -1, res[0][0], pos=(200, 100))
            if res[0][1] != None:
                wx.StaticText(self.rightpanel, -1, res[0][1], pos=(200, 130))
            hengxiang = 0
            count = 0
            for i in res:
                wx.StaticText(self.rightpanel, -1, i[2], pos=(200, 190 + hengxiang))
                wx.StaticText(self.rightpanel, -1, i[3], pos=(400, 190 + hengxiang))
                hengxiang += 30
                count += 1
            wx.StaticText(self.rightpanel, -1, str(count), pos=(200, 160))


    def OnListbox6(self, event):
        choose = event.GetString()
        for child in self.rightpanel.GetChildren():
            child.Destroy()

        if choose == '音乐基本信息':
            sql = "select 名称 from 音乐"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp1 = []
            for i in res:
                type_tmp1.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择音乐名称：', pos=(10, 13))
            self.choice_music1 = wx.Choice(self.rightpanel, choices=type_tmp1, size=(300, -1), pos=(160, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(500, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK25, okButton)
        if choose == '季度':
            sql = "select distinct 新番季度 from 动画"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp2 = []
            for i in res:
                type_tmp2.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择新番季度：', pos=(10, 13))
            self.choice_music2 = wx.Choice(self.rightpanel, choices=type_tmp2, size=(100, -1), pos=(150, 10))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(300, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK26, okButton)
        if choose == '歌手':
            sql = "select distinct 姓名 from 演唱"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp3 = []
            for i in res:
                type_tmp3.append(i[0])
            if '纯音乐' in type_tmp3:
                type_tmp3.remove('纯音乐')

            sql = "select * from 限制时间"
            cur.execute(sql)
            res = cur.fetchall()
            timelimit = ['所有']
            for i in res:
                timelimit.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'请选择歌手/组合姓名：', pos=(10, 13))
            self.choice_music3 = wx.Choice(self.rightpanel, choices=type_tmp3, size=(200, -1), pos=(160, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择放送时间限制：', pos=(10, 53))
            self.choice_time7 = wx.Choice(self.rightpanel, choices=timelimit, size=(80, -1), pos=(160, 50))
            self.choice_time7.SetSelection(0)
            wx.StaticText(self.rightpanel, -1, u'可限制年份和季度，格式如：“所有”、“2018”、“2018年春”', pos=(280, 53))
            okButton = wx.Button(self.rightpanel, -1, u'确定', pos=(400, 10))
            self.Bind(wx.EVT_BUTTON, self.OnOK27, okButton)

    def OnOK25(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice1 = self.choice_music1.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'类型：', pos=(10, 130))
        label3 = wx.StaticText(self.rightpanel, -1, u'出自动画：', pos=(10, 160))
        label4 = wx.StaticText(self.rightpanel, -1, u'演唱：', pos=(10, 190))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')

        sql = "select 名称,类型,动画,歌手 from 动画音乐列表 where 名称=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0]
        wx.StaticText(self.rightpanel, -1, res[0], pos=(100, 100))
        wx.StaticText(self.rightpanel, -1, res[1], pos=(100, 130))
        wx.StaticText(self.rightpanel, -1, res[2], pos=(100, 160))
        wx.StaticText(self.rightpanel, -1, res[3], pos=(100, 190))

    def OnOK26(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 60), (1000, 600))
        choice2 = self.choice_music2.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 60))
        label2 = wx.StaticText(self.rightpanel, -1, u'类型：', pos=(300, 60))
        label3 = wx.StaticText(self.rightpanel, -1, u'出自动画：', pos=(350, 60))
        label4 = wx.StaticText(self.rightpanel, -1, u'演唱：', pos=(540, 60))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')

        sql = "select 名称,类型,动画,歌手 from 季度新番动画音乐 where 新番季度=%s"
        cur.execute(sql, choice2)
        res = cur.fetchall()
        weizhi = 60
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(300, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(350, weizhi))
            wx.StaticText(self.rightpanel, -1, i[3], pos=(540, weizhi))

    def OnOK27(self, evt):
        wx.StaticText(self.rightpanel, -1, '', (0, 100), (1000, 600))
        choice3 = self.choice_music3.GetStringSelection()
        choice3_time = self.choice_time7.GetStringSelection()

        label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 100))
        label2 = wx.StaticText(self.rightpanel, -1, u'类型：', pos=(300, 100))
        label3 = wx.StaticText(self.rightpanel, -1, u'出自动画：', pos=(350, 100))
        label4 = wx.StaticText(self.rightpanel, -1, u'演唱：', pos=(540, 100))
        label1.SetBackgroundColour('Turquoise')
        label2.SetBackgroundColour('Turquoise')
        label3.SetBackgroundColour('Turquoise')
        label4.SetBackgroundColour('Turquoise')

        if choice3_time == '所有':
            sql = "select 名称,类型,动画,歌手 from 演唱动画音乐 where 姓名=%s"
            cur.execute(sql, choice3)
        elif '年' in choice3_time:
            sql = "select 名称,类型,动画,歌手 from 演唱动画音乐 where 姓名=%s and 新番季度=%s"
            cur.execute(sql, (choice3, choice3_time))
        else:
            sql = "select 名称,类型,动画,歌手 from 演唱动画音乐 where 姓名=%s and 年份=%s"
            cur.execute(sql, (choice3, choice3_time))

        res = cur.fetchall()
        weizhi = 100
        for i in res:
            weizhi += 20
            wx.StaticText(self.rightpanel, -1, i[0], pos=(10, weizhi))
            wx.StaticText(self.rightpanel, -1, i[1], pos=(300, weizhi))
            wx.StaticText(self.rightpanel, -1, i[2], pos=(350, weizhi))
            wx.StaticText(self.rightpanel, -1, i[3], pos=(540, weizhi))

    def OnListbox7(self, event):
        choose = event.GetString()
        for child in self.rightpanel.GetChildren():
            child.Destroy()

        if choose == '原作公司':
            sql = "select 名称 from 原作公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp1 = []
            for i in res:
                type_tmp1.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项，修改操作要求先进行查询，再在查询结果基础上进行修改', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入想要添加的数据：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'地址：', pos=(10, 73))
            label3 = wx.StaticText(self.rightpanel, -1, u'成立时间：', pos=(10, 103))
            label4 = wx.StaticText(self.rightpanel, -1, u'主要业务：', pos=(10, 133))
            label5 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 163))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')
            label3.SetBackgroundColour('Turquoise')
            label4.SetBackgroundColour('Turquoise')
            label5.SetBackgroundColour('Turquoise')

            self.data1_add1 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 40))
            self.data1_add2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 70))
            self.data1_add3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 100))
            self.data1_add4 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 130))
            self.data1_add5 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 160))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            okButton1 = wx.Button(self.rightpanel, -1, u'添加', pos=(440, 160))
            self.Bind(wx.EVT_BUTTON, self.OnOK28, okButton1)

            wx.StaticText(self.rightpanel, -1, u'请选择原作公司名称：', pos=(10, 220))
            label6 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 253))
            label7 = wx.StaticText(self.rightpanel, -1, u'地址：', pos=(10, 283))
            label8 = wx.StaticText(self.rightpanel, -1, u'成立时间：', pos=(10, 313))
            label9 = wx.StaticText(self.rightpanel, -1, u'主要业务：', pos=(10, 343))
            label10 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 373))
            label6.SetBackgroundColour('Turquoise')
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')
            label9.SetBackgroundColour('Turquoise')
            label10.SetBackgroundColour('Turquoise')

            self.data1_modify1 = wx.Choice(self.rightpanel, choices=type_tmp1, size=(300, -1), pos=(100, 250))
            self.data1_modify2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 280))
            self.data1_modify3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 310))
            self.data1_modify4 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 340))
            self.data1_modify5 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 370))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 255))
            okButton2 = wx.Button(self.rightpanel, -1, u'查询', pos=(440, 370))
            self.Bind(wx.EVT_BUTTON, self.OnOK29, okButton2)
            okButton3 = wx.Button(self.rightpanel, -1, u'修改', pos=(570, 370))
            self.Bind(wx.EVT_BUTTON, self.OnOK30, okButton3)

            wx.StaticText(self.rightpanel, -1, u'请选择原作公司名称：', pos=(10, 430))
            label11 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 463))
            label11.SetBackgroundColour('Turquoise')

            self.data1_delete1 = wx.Choice(self.rightpanel, choices=type_tmp1, size=(300, -1), pos=(100, 460))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 465))
            okButton4 = wx.Button(self.rightpanel, -1, u'删除', pos=(440, 460))
            self.Bind(wx.EVT_BUTTON, self.OnOK31, okButton4)
        if choose == '动画公司':
            sql = "select 名称 from 动画公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp2 = []
            for i in res:
                type_tmp2.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项，修改操作要求先进行查询，再在查询结果基础上进行修改', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入想要添加的数据：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'地址：', pos=(10, 73))
            label3 = wx.StaticText(self.rightpanel, -1, u'成立时间：', pos=(10, 103))
            label4 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 133))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')
            label3.SetBackgroundColour('Turquoise')
            label4.SetBackgroundColour('Turquoise')

            self.data2_add1 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 40))
            self.data2_add2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 70))
            self.data2_add3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 100))
            self.data2_add4 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 130))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            okButton1 = wx.Button(self.rightpanel, -1, u'添加', pos=(440, 130))
            self.Bind(wx.EVT_BUTTON, self.OnOK32, okButton1)

            wx.StaticText(self.rightpanel, -1, u'请选择动画公司名称：', pos=(10, 190))
            label5 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 223))
            label6 = wx.StaticText(self.rightpanel, -1, u'地址：', pos=(10, 253))
            label7 = wx.StaticText(self.rightpanel, -1, u'成立时间：', pos=(10, 283))
            label8 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 313))
            label5.SetBackgroundColour('Turquoise')
            label6.SetBackgroundColour('Turquoise')
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')

            self.data2_modify1 = wx.Choice(self.rightpanel, choices=type_tmp2, size=(300, -1), pos=(100, 220))
            self.data2_modify2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 250))
            self.data2_modify3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 280))
            self.data2_modify4 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 310))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 225))
            okButton2 = wx.Button(self.rightpanel, -1, u'查询', pos=(440, 310))
            self.Bind(wx.EVT_BUTTON, self.OnOK33, okButton2)
            okButton3 = wx.Button(self.rightpanel, -1, u'修改', pos=(570, 310))
            self.Bind(wx.EVT_BUTTON, self.OnOK34, okButton3)

            wx.StaticText(self.rightpanel, -1, u'请选择动画公司名称：', pos=(10, 370))
            label9 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 403))
            label9.SetBackgroundColour('Turquoise')

            self.data2_delete1 = wx.Choice(self.rightpanel, choices=type_tmp2, size=(300, -1), pos=(100, 400))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 405))
            okButton4 = wx.Button(self.rightpanel, -1, u'删除', pos=(440, 400))
            self.Bind(wx.EVT_BUTTON, self.OnOK35, okButton4)
        if choose == '人物':
            sql = "select 姓名 from 人物"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp3 = []
            for i in res:
                type_tmp3.append(i[0])
            type_tmp3_2 = ['', '男', '女']

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项，修改操作要求先进行查询，再在查询结果基础上进行修改', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入想要添加的数据：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'姓名：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'性别：', pos=(10, 73))
            label3 = wx.StaticText(self.rightpanel, -1, u'出生日期：', pos=(10, 103))
            label4 = wx.StaticText(self.rightpanel, -1, u'职业：', pos=(10, 133))
            label5 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 163))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')
            label3.SetBackgroundColour('Turquoise')
            label4.SetBackgroundColour('Turquoise')
            label5.SetBackgroundColour('Turquoise')

            self.data3_add1 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 40))
            self.data3_add2 = wx.Choice(self.rightpanel, choices=type_tmp3_2, size=(300, -1), pos=(100, 70))
            self.data3_add3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 100))
            self.data3_add4 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 130))
            self.data3_add5 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 160))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 135))
            wx.StaticText(self.rightpanel, -1, u'如漫画家、小说家、声优等', pos=(440, 133))
            okButton1 = wx.Button(self.rightpanel, -1, u'添加', pos=(440, 160))
            self.Bind(wx.EVT_BUTTON, self.OnOK36, okButton1)

            wx.StaticText(self.rightpanel, -1, u'请选择人物姓名：', pos=(10, 220))
            label6 = wx.StaticText(self.rightpanel, -1, u'姓名：', pos=(10, 253))
            label7 = wx.StaticText(self.rightpanel, -1, u'性别：', pos=(10, 283))
            label8 = wx.StaticText(self.rightpanel, -1, u'出生日期：', pos=(10, 313))
            label9 = wx.StaticText(self.rightpanel, -1, u'职业：', pos=(10, 343))
            label10 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 373))
            label6.SetBackgroundColour('Turquoise')
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')
            label9.SetBackgroundColour('Turquoise')
            label10.SetBackgroundColour('Turquoise')

            self.data3_modify1 = wx.Choice(self.rightpanel, choices=type_tmp3, size=(300, -1), pos=(100, 250))
            self.data3_modify2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 280))
            self.data3_modify3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 310))
            self.data3_modify4 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 340))
            self.data3_modify5 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 370))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 255))
            wx.StaticText(self.rightpanel, -1, u'留空或“男”或“女”', pos=(440, 283))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 345))
            wx.StaticText(self.rightpanel, -1, u'如漫画家、小说家、声优等', pos=(440, 343))
            okButton2 = wx.Button(self.rightpanel, -1, u'查询', pos=(440, 370))
            self.Bind(wx.EVT_BUTTON, self.OnOK37, okButton2)
            okButton3 = wx.Button(self.rightpanel, -1, u'修改', pos=(570, 370))
            self.Bind(wx.EVT_BUTTON, self.OnOK38, okButton3)

            wx.StaticText(self.rightpanel, -1, u'请选择人物姓名：', pos=(10, 430))
            label11 = wx.StaticText(self.rightpanel, -1, u'姓名：', pos=(10, 463))
            label11.SetBackgroundColour('Turquoise')

            self.data3_delete1 = wx.Choice(self.rightpanel, choices=type_tmp3, size=(300, -1), pos=(100, 460))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 465))
            okButton4 = wx.Button(self.rightpanel, -1, u'删除', pos=(440, 460))
            self.Bind(wx.EVT_BUTTON, self.OnOK39, okButton4)
        if choose == '动画(添加)':
            type_tmp4_1 = ['新作', '续作', '衍生', '重制']
            type_tmp4_2 = ['漫改', '轻改', '游戏改', '原创']

            sql = "select 名称 from 原作公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp4_3 = ['']
            for i in res:
                type_tmp4_3.append(i[0])

            sql = "select 姓名 from 人物"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp4_4 = ['']
            for i in res:
                type_tmp4_4.append(i[0])

            sql = "select 名称 from 动画公司"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp4_5 = []
            for i in res:
                type_tmp4_5.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入想要添加的数据：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'制作类型：', pos=(10, 73))
            label3 = wx.StaticText(self.rightpanel, -1, u'改编类型：', pos=(10, 103))
            label4 = wx.StaticText(self.rightpanel, -1, u'原作公司：', pos=(10, 133))
            label5 = wx.StaticText(self.rightpanel, -1, u'原作者：', pos=(10, 163))
            label6 = wx.StaticText(self.rightpanel, -1, u'制作公司：', pos=(10, 193))
            label7 = wx.StaticText(self.rightpanel, -1, u'新番季度：', pos=(10, 223))
            label8 = wx.StaticText(self.rightpanel, -1, u'首播时间：', pos=(10, 253))
            label9 = wx.StaticText(self.rightpanel, -1, u'总集数：', pos=(10, 283))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')
            label3.SetBackgroundColour('Turquoise')
            label4.SetBackgroundColour('Turquoise')
            label5.SetBackgroundColour('Turquoise')
            label6.SetBackgroundColour('Turquoise')
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')
            label9.SetBackgroundColour('Turquoise')

            self.data4_add1 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 40))
            self.data4_add2 = wx.Choice(self.rightpanel, choices=type_tmp4_1, size=(300, -1), pos=(100, 70))
            self.data4_add3 = wx.Choice(self.rightpanel, choices=type_tmp4_2, size=(300, -1), pos=(100, 100))
            self.data4_add4 = wx.Choice(self.rightpanel, choices=type_tmp4_3, size=(300, -1), pos=(100, 130))
            self.data4_add5 = wx.Choice(self.rightpanel, choices=type_tmp4_4, size=(300, -1), pos=(100, 160))
            self.data4_add6 = wx.Choice(self.rightpanel, choices=type_tmp4_5, size=(300, -1), pos=(100, 190))
            self.data4_add7 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 220))
            self.data4_add8 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 250))
            self.data4_add9 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 280))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 75))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 105))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 195))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 225))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 255))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 285))
            wx.StaticText(self.rightpanel, -1, u'“新作”或“续作”或“衍生”或“重制”', pos=(440, 73))
            wx.StaticText(self.rightpanel, -1, u'“漫改”或“轻改”或“游戏改”或“原创”', pos=(440, 103))
            wx.StaticText(self.rightpanel, -1, u'格式为4位年份+"年"+"春"/"夏"/"秋"/"冬"', pos=(440, 225))
            wx.StaticText(self.rightpanel, -1, u'时间格式为年月日，如：20180101', pos=(440, 255))
            wx.StaticText(self.rightpanel, -1, u'填入数字，未知时填入0', pos=(440, 285))
            okButton1 = wx.Button(self.rightpanel, -1, u'添加', pos=(440, 310))
            self.Bind(wx.EVT_BUTTON, self.OnOK40, okButton1)
        if choose == '动画(删改)':
            sql = "select 名称 from 动画"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp4_6 = []
            for i in res:
                type_tmp4_6.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项，修改操作要求先进行查询，再在查询结果基础上进行修改', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请选择动画名称：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'制作类型：', pos=(10, 73))
            label3 = wx.StaticText(self.rightpanel, -1, u'改编类型：', pos=(10, 103))
            label4 = wx.StaticText(self.rightpanel, -1, u'原作公司：', pos=(10, 133))
            label5 = wx.StaticText(self.rightpanel, -1, u'原作者：', pos=(10, 163))
            label6 = wx.StaticText(self.rightpanel, -1, u'制作公司：', pos=(10, 193))
            label7 = wx.StaticText(self.rightpanel, -1, u'新番季度：', pos=(10, 223))
            label8 = wx.StaticText(self.rightpanel, -1, u'首播时间：', pos=(10, 253))
            label9 = wx.StaticText(self.rightpanel, -1, u'总集数：', pos=(10, 283))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')
            label3.SetBackgroundColour('Turquoise')
            label4.SetBackgroundColour('Turquoise')
            label5.SetBackgroundColour('Turquoise')
            label6.SetBackgroundColour('Turquoise')
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')
            label9.SetBackgroundColour('Turquoise')

            self.data4_modify1 = wx.Choice(self.rightpanel, choices=type_tmp4_6, size=(300, -1), pos=(100, 40))
            self.data4_modify2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 70))
            self.data4_modify3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 100))
            self.data4_modify4 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 130))
            self.data4_modify5 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 160))
            self.data4_modify6 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 190))
            self.data4_modify7 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 220))
            self.data4_modify8 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 250))
            self.data4_modify9 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 280))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 75))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 105))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 195))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 225))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 255))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 285))
            wx.StaticText(self.rightpanel, -1, u'“新作”或“续作”或“衍生”或“重制”', pos=(440, 73))
            wx.StaticText(self.rightpanel, -1, u'“漫改”或“轻改”或“游戏改”或“原创”', pos=(440, 103))
            wx.StaticText(self.rightpanel, -1, u'格式为4位年份+"年"+"春"/"夏"/"秋"/"冬"', pos=(440, 225))
            wx.StaticText(self.rightpanel, -1, u'时间格式为年月日，如：20180101', pos=(440, 255))
            wx.StaticText(self.rightpanel, -1, u'填入数字，未知时填入0', pos=(440, 285))
            okButton2 = wx.Button(self.rightpanel, -1, u'查询', pos=(440, 310))
            self.Bind(wx.EVT_BUTTON, self.OnOK41, okButton2)
            okButton3 = wx.Button(self.rightpanel, -1, u'修改', pos=(570, 310))
            self.Bind(wx.EVT_BUTTON, self.OnOK42, okButton3)

            wx.StaticText(self.rightpanel, -1, u'请选择动画名称：', pos=(10, 370))
            label10 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 403))
            label10.SetBackgroundColour('Turquoise')

            self.data4_delete1 = wx.Choice(self.rightpanel, choices=type_tmp4_6, size=(300, -1), pos=(100, 400))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 405))
            wx.StaticText(self.rightpanel, -1, u'请先确保删除相应的动画制作组', pos=(100, 433))
            okButton4 = wx.Button(self.rightpanel, -1, u'删除', pos=(440, 400))
            self.Bind(wx.EVT_BUTTON, self.OnOK43, okButton4)
        if choose == '动画类别':
            sql = "select 名称 from 动画"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp5 = []
            for i in res:
                type_tmp5.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项，修改操作要求先进行查询，再在查询结果基础上进行修改', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入想要添加的数据：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'类别：', pos=(10, 73))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')

            self.data5_add1 = wx.Choice(self.rightpanel, choices=type_tmp5, size=(300, -1), pos=(100, 40))
            self.data5_add2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 70))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 75))
            okButton1 = wx.Button(self.rightpanel, -1, u'添加', pos=(440, 70))
            self.Bind(wx.EVT_BUTTON, self.OnOK44, okButton1)

            wx.StaticText(self.rightpanel, -1, u'请选择动画名称：', pos=(10, 130))
            label3 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 163))
            label4 = wx.StaticText(self.rightpanel, -1, u'旧类别：', pos=(10, 193))
            label5 = wx.StaticText(self.rightpanel, -1, u'修改前旧类别：', pos=(10, 223))
            label6 = wx.StaticText(self.rightpanel, -1, u'修改后新类别：', pos=(10, 253))
            label3.SetBackgroundColour('Turquoise')
            label4.SetBackgroundColour('Turquoise')
            label5.SetBackgroundColour('Turquoise')
            label6.SetBackgroundColour('Turquoise')

            self.data5_modify1 = wx.Choice(self.rightpanel, choices=type_tmp5, size=(300, -1), pos=(100, 160))
            self.data5_modify2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 220))
            self.data5_modify3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 250))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 165))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 225))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 255))
            okButton2 = wx.Button(self.rightpanel, -1, u'查询', pos=(440, 250))
            self.Bind(wx.EVT_BUTTON, self.OnOK45, okButton2)
            okButton3 = wx.Button(self.rightpanel, -1, u'修改', pos=(570, 250))
            self.Bind(wx.EVT_BUTTON, self.OnOK46, okButton3)

            wx.StaticText(self.rightpanel, -1, u'请选择动画名称：', pos=(10, 310))
            label7 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 343))
            label8 = wx.StaticText(self.rightpanel, -1, u'删除的类别：', pos=(10, 373))
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')

            self.data5_delete1 = wx.Choice(self.rightpanel, choices=type_tmp5, size=(300, -1), pos=(100, 340))
            self.data5_delete2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 370))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 345))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 375))
            okButton4 = wx.Button(self.rightpanel, -1, u'删除', pos=(440, 370))
            self.Bind(wx.EVT_BUTTON, self.OnOK47, okButton4)
        if choose == '动画制作组':
            sql = "select 名称 from 动画"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp6 = []
            for i in res:
                type_tmp6.append(i[0])
            type_tmp6_2 = [''] + type_tmp6

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项，修改操作要求先进行查询，再在查询结果基础上进行修改', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入想要添加的数据：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'动画：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'职位：', pos=(10, 73))
            label3 = wx.StaticText(self.rightpanel, -1, u'姓名：', pos=(10, 103))
            label4 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 133))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')
            label3.SetBackgroundColour('Turquoise')
            label4.SetBackgroundColour('Turquoise')

            self.data6_add1 = wx.Choice(self.rightpanel, choices=type_tmp6, size=(300, -1), pos=(100, 40))
            self.data6_add2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 70))
            self.data6_add3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 100))
            self.data6_add4 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 130))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 75))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 105))
            wx.StaticText(self.rightpanel, -1, u'检查staff表中是否已有这位职员\n若有，则无需输入代表作', pos=(550, 105))
            self.data_check1 = wx.StaticText(self.rightpanel, -1, u'', pos=(100, 160))
            okButton00 = wx.Button(self.rightpanel, -1, u'查看输入格式', pos=(440, 70))
            self.Bind(wx.EVT_BUTTON, self.OnOK48, okButton00)
            okButton0 = wx.Button(self.rightpanel, -1, u'check', pos=(440, 100))
            self.Bind(wx.EVT_BUTTON, self.OnOK49, okButton0)
            okButton1 = wx.Button(self.rightpanel, -1, u'添加', pos=(440, 130))
            self.Bind(wx.EVT_BUTTON, self.OnOK50, okButton1)

            wx.StaticText(self.rightpanel, -1, u'请选择动画名称：', pos=(10, 190))
            label5 = wx.StaticText(self.rightpanel, -1, u'动画：', pos=(10, 223))
            label6 = wx.StaticText(self.rightpanel, -1, u'职位：', pos=(10, 253))
            label7 = wx.StaticText(self.rightpanel, -1, u'姓名：', pos=(10, 283))
            label8 = wx.StaticText(self.rightpanel, -1, u'代表作：', pos=(10, 313))
            label5.SetBackgroundColour('Turquoise')
            label6.SetBackgroundColour('Turquoise')
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')

            self.data6_modify1 = wx.Choice(self.rightpanel, choices=type_tmp6_2, size=(300, -1), pos=(100, 220))
            self.data6_modify2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 250))
            self.data6_modify3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 280))
            self.data6_modify4 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 310))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 285))
            okButton2 = wx.Button(self.rightpanel, -1, u'查询', pos=(440, 280))
            self.Bind(wx.EVT_BUTTON, self.OnOK51, okButton2)
            okButton3 = wx.Button(self.rightpanel, -1, u'修改', pos=(440, 310))
            self.Bind(wx.EVT_BUTTON, self.OnOK52, okButton3)
            self.data6_modify5 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, 120), style=wx.TE_MULTILINE |
                    wx.TE_READONLY | wx.HSCROLL, pos=(560, 223))

            wx.StaticText(self.rightpanel, -1, u'请选择动画名称：', pos=(10, 370))
            label9 = wx.StaticText(self.rightpanel, -1, u'动画：', pos=(10, 403))
            label10 = wx.StaticText(self.rightpanel, -1, u'姓名：', pos=(10, 433))
            label9.SetBackgroundColour('Turquoise')
            label10.SetBackgroundColour('Turquoise')

            self.data6_delete1 = wx.Choice(self.rightpanel, choices=type_tmp6, size=(300, -1), pos=(100, 400))
            self.data6_delete2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 430))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 405))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 435))
            okButton4 = wx.Button(self.rightpanel, -1, u'删除', pos=(440, 430))
            self.Bind(wx.EVT_BUTTON, self.OnOK53, okButton4)
        if choose == '动画声优':
            sql = "select 名称 from 动画"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp7_1 = []
            for i in res:
                type_tmp7_1.append(i[0])

            sql = "select 姓名 from 人物 where 职业='声优'"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp7_2 = []
            for i in res:
                type_tmp7_2.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项，修改操作要求先进行查询，再在查询结果基础上进行修改', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入想要添加的数据：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'动画：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'声优：', pos=(10, 73))
            label3 = wx.StaticText(self.rightpanel, -1, u'角色：', pos=(10, 103))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')
            label3.SetBackgroundColour('Turquoise')

            self.data7_add1 = wx.Choice(self.rightpanel, choices=type_tmp7_1, size=(300, -1), pos=(100, 40))
            self.data7_add2 = wx.Choice(self.rightpanel, choices=type_tmp7_2, size=(300, -1), pos=(100, 70))
            self.data7_add3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 100))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 75))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 105))
            okButton1 = wx.Button(self.rightpanel, -1, u'添加', pos=(440, 100))
            self.Bind(wx.EVT_BUTTON, self.OnOK54, okButton1)

            wx.StaticText(self.rightpanel, -1, u'请选择动画名称及声优姓名：', pos=(10, 160))
            label4 = wx.StaticText(self.rightpanel, -1, u'动画：', pos=(10, 193))
            label5 = wx.StaticText(self.rightpanel, -1, u'声优：', pos=(10, 223))
            label6 = wx.StaticText(self.rightpanel, -1, u'角色：', pos=(10, 253))
            label4.SetBackgroundColour('Turquoise')
            label5.SetBackgroundColour('Turquoise')
            label6.SetBackgroundColour('Turquoise')

            self.data7_modify1 = wx.Choice(self.rightpanel, choices=type_tmp7_1, size=(300, -1), pos=(100, 190))
            self.data7_modify2 = wx.Choice(self.rightpanel, choices=type_tmp7_2, size=(300, -1), pos=(100, 220))
            self.data7_modify3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 250))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 195))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 225))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 255))
            okButton2 = wx.Button(self.rightpanel, -1, u'查询', pos=(440, 250))
            self.Bind(wx.EVT_BUTTON, self.OnOK55, okButton2)
            okButton3 = wx.Button(self.rightpanel, -1, u'修改', pos=(570, 250))
            self.Bind(wx.EVT_BUTTON, self.OnOK56, okButton3)

            wx.StaticText(self.rightpanel, -1, u'请选择动画名称及声优姓名：', pos=(10, 310))
            label7 = wx.StaticText(self.rightpanel, -1, u'动画：', pos=(10, 343))
            label8 = wx.StaticText(self.rightpanel, -1, u'声优：', pos=(10, 373))
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')

            self.data7_delete1 = wx.Choice(self.rightpanel, choices=type_tmp7_1, size=(300, -1), pos=(100, 340))
            self.data7_delete2 = wx.Choice(self.rightpanel, choices=type_tmp7_2, size=(300, -1), pos=(100, 370))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 345))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 375))
            okButton4 = wx.Button(self.rightpanel, -1, u'删除', pos=(440, 370))
            self.Bind(wx.EVT_BUTTON, self.OnOK57, okButton4)
        if choose == '动画音乐':
            type_tmp8_1 = ['OP','ED']
            sql = "select 名称 from 动画"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp8_2 = []
            for i in res:
                type_tmp8_2.append(i[0])

            sql = "select 名称 from 音乐"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp8_3 = []
            for i in res:
                type_tmp8_3.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项，修改操作要求先进行查询，再在查询结果基础上进行修改', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入想要添加的数据：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'类型：', pos=(10, 73))
            label3 = wx.StaticText(self.rightpanel, -1, u'动画：', pos=(10, 103))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')
            label3.SetBackgroundColour('Turquoise')

            self.data8_add1 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 40))
            self.data8_add2 = wx.Choice(self.rightpanel, choices=type_tmp8_1, size=(300, -1), pos=(100, 70))
            self.data8_add3 = wx.Choice(self.rightpanel, choices=type_tmp8_2, size=(300, -1), pos=(100, 100))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 75))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 105))
            wx.StaticText(self.rightpanel, -1, u'“OP”或“ED”', pos=(440, 75))
            okButton1 = wx.Button(self.rightpanel, -1, u'添加', pos=(440, 100))
            self.Bind(wx.EVT_BUTTON, self.OnOK58, okButton1)

            wx.StaticText(self.rightpanel, -1, u'请选择音乐名称：', pos=(10, 160))
            label4 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 193))
            label5 = wx.StaticText(self.rightpanel, -1, u'修改前旧类型：', pos=(10, 223))
            label6 = wx.StaticText(self.rightpanel, -1, u'修改前旧动画：', pos=(10, 253))
            label7 = wx.StaticText(self.rightpanel, -1, u'修改后新类型：', pos=(10, 283))
            label8 = wx.StaticText(self.rightpanel, -1, u'修改后新动画：', pos=(10, 313))
            label4.SetBackgroundColour('Turquoise')
            label5.SetBackgroundColour('Turquoise')
            label6.SetBackgroundColour('Turquoise')
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')

            self.data8_modify1 = wx.Choice(self.rightpanel, choices=type_tmp8_3, size=(300, -1), pos=(100, 190))
            self.data8_modify2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH | wx.TE_READONLY, pos=(100, 220))
            self.data8_modify3 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH | wx.TE_READONLY, pos=(100, 250))
            self.data8_modify4 = wx.Choice(self.rightpanel, choices=type_tmp8_1, size=(300, -1), pos=(100, 280))
            self.data8_modify5 = wx.Choice(self.rightpanel, choices=type_tmp8_2, size=(300, -1), pos=(100, 310))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 195))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 225))
            wx.StaticText(self.rightpanel, -1, u'“OP”或“ED”', pos=(440, 225))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 255))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 285))
            wx.StaticText(self.rightpanel, -1, u'“OP”或“ED”', pos=(440, 285))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 315))
            okButton2 = wx.Button(self.rightpanel, -1, u'查询', pos=(440, 310))
            self.Bind(wx.EVT_BUTTON, self.OnOK59, okButton2)
            okButton3 = wx.Button(self.rightpanel, -1, u'修改', pos=(570, 310))
            self.Bind(wx.EVT_BUTTON, self.OnOK60, okButton3)

            wx.StaticText(self.rightpanel, -1, u'请选择音乐名称：', pos=(10, 370))
            label9 = wx.StaticText(self.rightpanel, -1, u'名称：', pos=(10, 403))
            label9.SetBackgroundColour('Turquoise')

            self.data8_delete1 = wx.Choice(self.rightpanel, choices=type_tmp8_3, size=(300, -1), pos=(100, 400))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 405))
            okButton4 = wx.Button(self.rightpanel, -1, u'删除', pos=(440, 400))
            self.Bind(wx.EVT_BUTTON, self.OnOK61, okButton4)
        if choose == '音乐演唱':
            sql = "select 名称 from 音乐"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp9_1 = []
            for i in res:
                type_tmp9_1.append(i[0])

            sql = "select 姓名 from 人物"
            cur.execute(sql)
            res = cur.fetchall()
            type_tmp9_2 = []
            for i in res:
                type_tmp9_2.append(i[0])

            wx.StaticText(self.rightpanel, -1, u'【注】带*为必填项，修改操作要求先进行查询，再在查询结果基础上进行修改', pos=(400, 10))
            wx.StaticText(self.rightpanel, -1, u'请输入想要添加的数据：', pos=(10, 10))
            label1 = wx.StaticText(self.rightpanel, -1, u'音乐名称：', pos=(10, 43))
            label2 = wx.StaticText(self.rightpanel, -1, u'歌手姓名：', pos=(10, 73))
            label1.SetBackgroundColour('Turquoise')
            label2.SetBackgroundColour('Turquoise')

            self.data9_add1 = wx.Choice(self.rightpanel, choices=type_tmp9_1, size=(300, -1), pos=(100, 40))
            self.data9_add2 = wx.Choice(self.rightpanel, choices=type_tmp9_2, size=(300, -1), pos=(100, 70))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 45))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 75))
            okButton1 = wx.Button(self.rightpanel, -1, u'添加', pos=(440, 70))
            self.Bind(wx.EVT_BUTTON, self.OnOK62, okButton1)

            wx.StaticText(self.rightpanel, -1, u'请选择音乐名称：', pos=(10, 130))
            label3 = wx.StaticText(self.rightpanel, -1, u'音乐名称：', pos=(10, 163))
            label4 = wx.StaticText(self.rightpanel, -1, u'歌手列表：', pos=(10, 193))
            label5 = wx.StaticText(self.rightpanel, -1, u'修改前旧歌手：', pos=(10, 223))
            label6 = wx.StaticText(self.rightpanel, -1, u'修改后新歌手：', pos=(10, 253))
            label3.SetBackgroundColour('Turquoise')
            label4.SetBackgroundColour('Turquoise')
            label5.SetBackgroundColour('Turquoise')
            label6.SetBackgroundColour('Turquoise')

            self.data9_modify1 = wx.Choice(self.rightpanel, choices=type_tmp9_1, size=(300, -1), pos=(100, 160))
            self.data9_modify2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 220))
            self.data9_modify3 = wx.Choice(self.rightpanel, choices=type_tmp9_2, size=(300, -1), pos=(100, 250))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 165))
            self.singer = wx.StaticText(self.rightpanel, -1, u'', pos=(100, 193))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 225))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 255))
            okButton2 = wx.Button(self.rightpanel, -1, u'查询', pos=(440, 250))
            self.Bind(wx.EVT_BUTTON, self.OnOK63, okButton2)
            okButton3 = wx.Button(self.rightpanel, -1, u'修改', pos=(570, 250))
            self.Bind(wx.EVT_BUTTON, self.OnOK64, okButton3)

            wx.StaticText(self.rightpanel, -1, u'请选择音乐名称：', pos=(10, 310))
            label7 = wx.StaticText(self.rightpanel, -1, u'音乐名称：', pos=(10, 343))
            label8 = wx.StaticText(self.rightpanel, -1, u'删除的歌手：', pos=(10, 373))
            label7.SetBackgroundColour('Turquoise')
            label8.SetBackgroundColour('Turquoise')

            self.data9_delete1 = wx.Choice(self.rightpanel, choices=type_tmp9_1, size=(300, -1), pos=(100, 340))
            self.data9_delete2 = wx.TextCtrl(self.rightpanel, -1, '', size=(300, -1), style=wx.TE_RICH, pos=(100, 370))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 345))
            wx.StaticText(self.rightpanel, -1, u'*', pos=(410, 375))
            okButton4 = wx.Button(self.rightpanel, -1, u'删除', pos=(440, 370))
            self.Bind(wx.EVT_BUTTON, self.OnOK65, okButton4)

    def OnOK28(self, evt):
        choice1 = self.data1_add1.GetValue()
        choice2 = self.data1_add2.GetValue()
        choice3 = self.data1_add3.GetValue()
        choice4 = self.data1_add4.GetValue()
        choice5 = self.data1_add5.GetValue()

        if choice1 == '':
            wx.MessageBox(u'请输入原作公司名称', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        try:
            sql = "insert into 原作公司 values(%s,%s,%s,%s,%s)"
            cur.execute(sql, (choice1, choice2, choice3, choice4, choice5))
            if choice2 == '':
                sql = "update 原作公司 set 地址=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice3 == '':
                sql = "update 原作公司 set 成立时间=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice4 == '':
                sql = "update 原作公司 set 主要业务=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice5 == '':
                sql = "update 原作公司 set 代表作=null where 名称=%s"
                cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'添加成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'添加失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

        self.data1_add1.Clear()
        self.data1_add2.Clear()
        self.data1_add3.Clear()
        self.data1_add4.Clear()
        self.data1_add5.Clear()

    def OnOK29(self, evt):
        self.data1_modify2.Clear()
        self.data1_modify3.Clear()
        self.data1_modify4.Clear()
        self.data1_modify5.Clear()
        choice1 = self.data1_modify1.GetStringSelection()
        sql = "select * from 原作公司 where 名称=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0]
        if res[1] != None:
            self.data1_modify2.SetValue(res[1])
        if res[2] != None:
            self.data1_modify3.SetValue(res[2])
        if res[3] != None:
            self.data1_modify4.SetValue(res[3])
        if res[4] != None:
            self.data1_modify5.SetValue(res[4])
        wx.MessageBox(u'查询成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK30(self, evt):
        choice1 = self.data1_modify1.GetStringSelection()
        choice2 = self.data1_modify2.GetValue()
        choice3 = self.data1_modify3.GetValue()
        choice4 = self.data1_modify4.GetValue()
        choice5 = self.data1_modify5.GetValue()

        try:
            sql = "update 原作公司 set 地址=%s,成立时间=%s,主要业务=%s,代表作=%s where 名称=%s"
            cur.execute(sql, (choice2, choice3, choice4, choice5, choice1))
            if choice2 == '':
                sql = "update 原作公司 set 地址=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice3 == '':
                sql = "update 原作公司 set 成立时间=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice4 == '':
                sql = "update 原作公司 set 主要业务=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice5 == '':
                sql = "update 原作公司 set 代表作=null where 名称=%s"
                cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'修改成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'修改失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK31(self, evt):
        choice1 = self.data1_delete1.GetStringSelection()

        try:
            sql = "delete from 原作公司 where 名称=%s"
            cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'删除成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'删除失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK32(self, evt):
        choice1 = self.data2_add1.GetValue()
        choice2 = self.data2_add2.GetValue()
        choice3 = self.data2_add3.GetValue()
        choice4 = self.data2_add4.GetValue()

        if choice1 == '':
            wx.MessageBox(u'请输入动画公司名称', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        try:
            sql = "insert into 动画公司 values(%s,%s,%s,%s)"
            cur.execute(sql, (choice1, choice2, choice3, choice4))
            if choice2 == '':
                sql = "update 动画公司 set 地址=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice3 == '':
                sql = "update 动画公司 set 成立时间=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice4 == '':
                sql = "update 动画公司 set 代表作=null where 名称=%s"
                cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'添加成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'添加失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

        self.data2_add1.Clear()
        self.data2_add2.Clear()
        self.data2_add3.Clear()
        self.data2_add4.Clear()

    def OnOK33(self, evt):
        self.data2_modify2.Clear()
        self.data2_modify3.Clear()
        self.data2_modify4.Clear()
        choice1 = self.data2_modify1.GetStringSelection()
        sql = "select * from 动画公司 where 名称=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0]
        if res[1] != None:
            self.data2_modify2.SetValue(res[1])
        if res[2] != None:
            self.data2_modify3.SetValue(res[2])
        if res[3] != None:
            self.data2_modify4.SetValue(res[3])
        wx.MessageBox(u'查询成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK34(self, evt):
        choice1 = self.data2_modify1.GetStringSelection()
        choice2 = self.data2_modify2.GetValue()
        choice3 = self.data2_modify3.GetValue()
        choice4 = self.data2_modify4.GetValue()

        try:
            sql = "update 动画公司 set 地址=%s,成立时间=%s,代表作=%s where 名称=%s"
            cur.execute(sql, (choice2, choice3, choice4, choice1))
            if choice2 == '':
                sql = "update 动画公司 set 地址=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice3 == '':
                sql = "update 动画公司 set 成立时间=null where 名称=%s"
                cur.execute(sql, choice1)
            if choice4 == '':
                sql = "update 动画公司 set 代表作=null where 名称=%s"
                cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'修改成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'修改失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK35(self, evt):
        choice1 = self.data2_delete1.GetStringSelection()

        try:
            sql = "delete from 动画公司 where 名称=%s"
            cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'删除成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'删除失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK36(self, evt):
        choice1 = self.data3_add1.GetValue()
        choice2 = self.data3_add2.GetStringSelection()
        choice3 = self.data3_add3.GetValue()
        choice4 = self.data3_add4.GetValue()
        choice5 = self.data3_add5.GetValue()

        if choice1 == '':
            wx.MessageBox(u'请输入人物姓名', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice4 == '':
            wx.MessageBox(u'请输入人物职业', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        try:
            sql = "insert into 人物 values(%s,%s,%s,%s,%s)"
            cur.execute(sql, (choice1, choice2, choice3, choice4, choice5))
            if choice2 == '':
                sql = "update 人物 set 性别=null where 姓名=%s"
                cur.execute(sql, choice1)
            if choice3 == '':
                sql = "update 人物 set 出生日期=null where 姓名=%s"
                cur.execute(sql, choice1)
            if choice5 == '':
                sql = "update 人物 set 代表作=null where 姓名=%s"
                cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'添加成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'添加失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

        self.data3_add1.Clear()
        self.data3_add3.Clear()
        self.data3_add4.Clear()
        self.data3_add5.Clear()

    def OnOK37(self, evt):
        self.data3_modify2.Clear()
        self.data3_modify3.Clear()
        self.data3_modify4.Clear()
        self.data3_modify5.Clear()
        choice1 = self.data3_modify1.GetStringSelection()
        sql = "select * from 人物 where 姓名=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0]
        if res[1] != None:
            self.data3_modify2.SetValue(res[1])
        if res[2] != None:
            self.data3_modify3.SetValue(res[2])
        self.data3_modify4.SetValue(res[3])
        if res[4] != None:
            self.data3_modify5.SetValue(res[4])
        wx.MessageBox(u'查询成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK38(self, evt):
        choice1 = self.data3_modify1.GetStringSelection()
        choice2 = self.data3_modify2.GetValue()
        choice3 = self.data3_modify3.GetValue()
        choice4 = self.data3_modify4.GetValue()
        choice5 = self.data3_modify5.GetValue()

        try:
            sql = "update 人物 set 性别=%s,出生日期=%s,职业=%s,代表作=%s where 姓名=%s"
            cur.execute(sql, (choice2, choice3, choice4, choice5, choice1))
            if choice2 == '':
                sql = "update 人物 set 性别=null where 姓名=%s"
                cur.execute(sql, choice1)
            if choice3 == '':
                sql = "update 人物 set 出生日期=null where 姓名=%s"
                cur.execute(sql, choice1)
            if choice5 == '':
                sql = "update 人物 set 代表作=null where 姓名=%s"
                cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'修改成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'修改失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK39(self, evt):
        choice1 = self.data3_delete1.GetStringSelection()

        try:
            sql = "delete from 人物 where 姓名=%s"
            cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'删除成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'删除失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK40(self, evt):
        choice1 = self.data4_add1.GetValue()
        choice2 = self.data4_add2.GetStringSelection()
        choice3 = self.data4_add3.GetStringSelection()
        choice4 = self.data4_add4.GetStringSelection()
        choice5 = self.data4_add5.GetStringSelection()
        choice6 = self.data4_add6.GetStringSelection()
        choice7 = self.data4_add7.GetValue()
        choice8 = self.data4_add8.GetValue()
        choice9 = self.data4_add9.GetValue()

        if choice1 == '':
            wx.MessageBox(u'请输入动画名称', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice2 == '':
            wx.MessageBox(u'请选择动画制作类型', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice3 == '':
            wx.MessageBox(u'请选择动画改编类型', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice6 == '':
            wx.MessageBox(u'请选择动画制作公司', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice7 == '':
            wx.MessageBox(u'请输入动画新番季度', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice8 == '':
            wx.MessageBox(u'请输入动画首播时间', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice9 == '':
            wx.MessageBox(u'请输入动画总集数', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        try:
            if choice4 == '':
                sql = "insert into 动画 values(%s,%s,%s,null,null,%s,%s,convert(date,%s),%d)"
                cur.execute(sql, (choice1, choice2, choice3, choice6, choice7, choice8, choice9))
            elif choice5 == '':
                sql = "insert into 动画 values(%s,%s,%s,%s,null,%s,%s,convert(date,%s),%d)"
                cur.execute(sql, (choice1, choice2, choice3, choice4, choice6, choice7, choice8, choice9))
            else:
                sql = "insert into 动画 values(%s,%s,%s,%s,%s,%s,%s,convert(date,%s),%d)"
                cur.execute(sql, (choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9))
            conn.commit()
            wx.MessageBox(u'添加成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'添加失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

        self.data4_add1.Clear()
        self.data4_add7.Clear()
        self.data4_add8.Clear()
        self.data4_add9.Clear()

    def OnOK41(self, evt):
        self.data4_modify2.Clear()
        self.data4_modify3.Clear()
        self.data4_modify4.Clear()
        self.data4_modify5.Clear()
        self.data4_modify6.Clear()
        self.data4_modify7.Clear()
        self.data4_modify8.Clear()
        self.data4_modify9.Clear()

        choice1 = self.data4_modify1.GetStringSelection()
        sql = "select * from 动画 where 名称=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0]
        self.data4_modify2.SetValue(res[1])
        self.data4_modify3.SetValue(res[2])
        if res[3] != None:
            self.data4_modify4.SetValue(res[3])
        if res[4] != None:
            self.data4_modify5.SetValue(res[4])
        self.data4_modify6.SetValue(res[5])
        self.data4_modify7.SetValue(res[6])
        self.data4_modify8.SetValue(res[7])
        self.data4_modify9.SetValue(str(res[8]))
        wx.MessageBox(u'查询成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK42(self, evt):
        choice1 = self.data4_modify1.GetStringSelection()
        choice2 = self.data4_modify2.GetValue()
        choice3 = self.data4_modify3.GetValue()
        choice4 = self.data4_modify4.GetValue()
        choice5 = self.data4_modify5.GetValue()
        choice6 = self.data4_modify6.GetValue()
        choice7 = self.data4_modify7.GetValue()
        choice8 = self.data4_modify8.GetValue()
        choice9 = self.data4_modify9.GetValue()

        try:
            if choice4 == '':
                sql = "update 动画 set 制作类型=%s,改编类型=%s,原作公司=null,原作者=null,制作公司=%s,新番季度=%s,首播时间=convert(date,%s),总集数=%d where 名称=%s"
                cur.execute(sql, (choice2, choice3, choice6, choice7, choice8, choice9, choice1))
            elif choice5 == '':
                sql = "update 动画 set 制作类型=%s,改编类型=%s,原作公司=%s,原作者=null,制作公司=%s,新番季度=%s,首播时间=convert(date,%s),总集数=%d where 名称=%s"
                cur.execute(sql, (choice2, choice3, choice4, choice6, choice7, choice8, choice9, choice1))
            else:
                sql = "update 动画 set 制作类型=%s,改编类型=%s,原作公司=%s,原作者=%s,制作公司=%s,新番季度=%s,首播时间=convert(date,%s),总集数=%d where 名称=%s"
                cur.execute(sql, (choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice1))
            conn.commit()
            wx.MessageBox(u'修改成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'修改失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK43(self, evt):
        choice1 = self.data4_delete1.GetStringSelection()

        try:
            sql = "delete from 动画 where 名称=%s"
            cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'删除成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'删除失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK44(self, evt):
        choice1 = self.data5_add1.GetStringSelection()
        choice2 = self.data5_add2.GetValue()

        if choice1 == '':
            wx.MessageBox(u'请选择动画名称', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice2 == '':
            wx.MessageBox(u'请输入动画类别', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        try:
            sql = "insert into 动画类别 values(%s,%s)"
            cur.execute(sql, (choice1, choice2))
            conn.commit()
            wx.MessageBox(u'添加成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'添加失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

        self.data5_add2.Clear()

    def OnOK45(self, evt):
        wx.StaticText(self.rightpanel, -1, size=(800,20), pos=(100, 193))
        self.data5_modify2.Clear()
        self.data5_modify3.Clear()

        choice1 = self.data5_modify1.GetStringSelection()

        sql = "select 类别 from 动画类别 where 名称=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()
        hengxiang = 100
        for i in res:
            wx.StaticText(self.rightpanel, -1, i[0], pos=(hengxiang, 193))
            hengxiang += 50

        wx.MessageBox(u'查询成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK46(self, evt):
        choice1 = self.data5_modify1.GetStringSelection()
        choice2 = self.data5_modify2.GetValue()
        choice3 = self.data5_modify3.GetValue()

        try:
            sql = "update 动画类别 set 类别=%s where 名称=%s and 类别=%s"
            cur.execute(sql, (choice3, choice1, choice2))
            conn.commit()
            wx.MessageBox(u'修改成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'修改失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK47(self, evt):
        choice1 = self.data5_delete1.GetStringSelection()
        choice2 = self.data5_delete2.GetValue()

        try:
            sql = "delete from 动画类别 where 名称=%s and 类别=%s"
            cur.execute(sql, (choice1, choice2))
            conn.commit()
            wx.MessageBox(u'删除成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except :
            conn.rollback()
            wx.MessageBox(u'删除失败\n', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK48(self, evt):
        wx.MessageBox(u'    职位有“导演”、“编剧”、“音乐”、“动画人设”4种，而且可叠加，叠加时必须按照顺序，中间用'
                      u'“、”分隔\n\n一共有16种输入：\n导演\n编剧\n音乐\n动画人设\n'
                      u'导演、编剧\n导演、音乐\n导演、动画人设\n编剧、音乐\n编剧、动画人设\n'
                      u'音乐、动画人设\n导演、编剧、音乐\n导演、编剧、动画人设\n导演、音乐、动画人设\n'
                      u'编剧、音乐、动画人设\n导演、编剧、音乐、动画人设', u'职位输入格式', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK49(self, evt):
        choice1 = self.data6_add3.GetValue()
        sql = "select * from staff where 姓名=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()
        if res == []:
            self.data_check1.SetLabel(u'需要输入代表作')
            self.data_check2 = 1
        else:
            self.data_check1.SetLabel(u'不需要输入代表作')
            self.data_check2 = 0

    def OnOK50(self, evt):
        choice1 = self.data6_add1.GetStringSelection()
        choice2 = self.data6_add2.GetValue()
        choice3 = self.data6_add3.GetValue()
        choice4 = self.data6_add4.GetValue()

        if choice1 == '':
            wx.MessageBox(u'请选择动画名称', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice2 == '':
            wx.MessageBox(u'请输入制作人员职位', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice3 == '':
            wx.MessageBox(u'请输入制作人员姓名', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        try:
            if self.data_check2 == 1:
                if choice4 == '':
                    sql = "insert into staff values(%s,null)"
                    cur.execute(sql, choice3)
                else:
                    sql = "insert into staff values(%s,%s)"
                    cur.execute(sql, (choice3, choice4))

            sql = "insert into 制作 values(%s,%s,%s)"
            cur.execute(sql, (choice3, choice1, choice2))
            conn.commit()
            wx.MessageBox(u'添加成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'添加失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

        self.data6_add2.Clear()
        self.data6_add3.Clear()
        self.data6_add4.Clear()
        self.data_check1.SetLabel('')

    def OnOK51(self, evt):
        self.data6_modify2.Clear()
        self.data6_modify3.Clear()
        self.data6_modify4.Clear()
        self.data6_modify5.Clear()

        choice1 = self.data6_modify1.GetStringSelection()

        if choice1 == '':
            wx.MessageBox(u'查询时请选择非空的动画名称', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        sql = "select * from 动画制作组列表 where 动画=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()
        res_str = ''
        for i in res:
            res_str += i[0]+'\t'+i[1]+'\t'+i[2]
            if i[3] != None:
                res_str +='\t' + i[3] + '\n'
            else:
                res_str += '\n'
        res_str.strip('\n')
        self.data6_modify5.SetValue(res_str)

        wx.MessageBox(u'查询成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK52(self, evt):
        choice1 = self.data6_modify1.GetStringSelection()
        choice2 = self.data6_modify2.GetValue()
        choice3 = self.data6_modify3.GetValue()
        choice4 = self.data6_modify4.GetValue()

        try:
            if choice4 == '':
                sql = "update staff set 代表作=null where 姓名=%s"
                cur.execute(sql, choice3)
            else:
                sql = "update staff set 代表作=%s where 姓名=%s"
                cur.execute(sql, (choice4, choice3))
            if choice1 != '':
                sql = "update 制作 set 职位=%s where 姓名=%s and 动画=%s"
                cur.execute(sql, (choice2, choice3, choice1))
            conn.commit()
            wx.MessageBox(u'修改成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'修改失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK53(self, evt):
        choice1 = self.data6_delete1.GetStringSelection()
        choice2 = self.data6_delete2.GetValue()

        try:
            sql = "delete from 制作 where 姓名=%s and 动画=%s"
            cur.execute(sql, (choice2, choice1))

            sql = "select count(*) from 制作 where 姓名=%s"
            cur.execute(sql, choice2)
            res = cur.fetchall()
            if res[0][0] == 0:
                sql = "delete from staff where 姓名=%s"
                cur.execute(sql, choice2)

            conn.commit()
            wx.MessageBox(u'删除成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'删除失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK54(self, evt):
        choice1 = self.data7_add1.GetStringSelection()
        choice2 = self.data7_add2.GetStringSelection()
        choice3 = self.data7_add3.GetValue()

        if choice1 == '':
            wx.MessageBox(u'请选择动画名称', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice2 == '':
            wx.MessageBox(u'请选择声优姓名', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        try:
            sql = "insert into cast values(%s,%s,%s)"
            cur.execute(sql, (choice2, choice1, choice3))
            conn.commit()
            wx.MessageBox(u'添加成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'添加失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

        self.data7_add3.Clear()

    def OnOK55(self, evt):
        self.data7_modify3.Clear()

        choice1 = self.data7_modify1.GetStringSelection()
        choice2 = self.data7_modify2.GetStringSelection()

        sql = "select 角色 from cast where 姓名=%s and 动画=%s"
        cur.execute(sql, (choice2, choice1))
        res = cur.fetchall()[0][0]
        self.data7_modify3.SetValue(res)

        wx.MessageBox(u'查询成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK56(self, evt):
        choice1 = self.data7_modify1.GetStringSelection()
        choice2 = self.data7_modify2.GetStringSelection()
        choice3 = self.data7_modify3.GetValue()

        try:
            sql = "update cast set 角色=%s where 姓名=%s and 动画=%s"
            cur.execute(sql, (choice3, choice2, choice1))
            conn.commit()
            wx.MessageBox(u'修改成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'修改失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK57(self, evt):
        choice1 = self.data7_delete1.GetStringSelection()
        choice2 = self.data7_delete2.GetStringSelection()

        try:
            sql = "delete from cast where 姓名=%s and 动画=%s"
            cur.execute(sql, (choice2, choice1))
            conn.commit()
            wx.MessageBox(u'删除成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'删除失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK58(self, evt):
        choice1 = self.data8_add1.GetValue()
        choice2 = self.data8_add2.GetStringSelection()
        choice3 = self.data8_add3.GetStringSelection()

        if choice1 == '':
            wx.MessageBox(u'请输入音乐名称', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice2 == '':
            wx.MessageBox(u'请选择音乐类型', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice3 == '':
            wx.MessageBox(u'请选择音乐出自动画', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        try:
            sql = "insert into 音乐 values(%s,%s,%s)"
            cur.execute(sql, (choice1, choice2, choice3))
            conn.commit()
            wx.MessageBox(u'添加成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'添加失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

        self.data8_add1.Clear()

    def OnOK59(self, evt):
        self.data8_modify2.Clear()
        self.data8_modify3.Clear()

        choice1 = self.data8_modify1.GetStringSelection()

        sql = "select 类型,动画 from 音乐 where 名称=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0]
        self.data8_modify2.SetValue(res[0])
        self.data8_modify3.SetValue(res[1])

        wx.MessageBox(u'查询成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK60(self, evt):
        choice1 = self.data8_modify1.GetStringSelection()
        choice2 = self.data8_modify4.GetStringSelection()
        choice3 = self.data8_modify5.GetStringSelection()

        try:
            sql = "update 音乐 set 类型=%s,动画=%s where 名称=%s"
            cur.execute(sql, (choice2, choice3, choice1))
            conn.commit()
            wx.MessageBox(u'修改成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'修改失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK61(self, evt):
        choice1 = self.data8_delete1.GetStringSelection()

        try:
            sql = "exec pr_删除音乐时级联删除演唱 @音乐=%s"
            cur.execute(sql, choice1)
            conn.commit()
            wx.MessageBox(u'删除成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'删除失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK62(self, evt):
        choice1 = self.data9_add1.GetStringSelection()
        choice2 = self.data9_add2.GetStringSelection()

        if choice1 == '':
            wx.MessageBox(u'请选择音乐名称', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return
        if choice2 == '':
            wx.MessageBox(u'请选择歌手姓名', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            return

        try:
            sql = "insert into 演唱 values(%s,%s)"
            cur.execute(sql, (choice2, choice1))
            conn.commit()
            wx.MessageBox(u'添加成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'添加失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK63(self, evt):
        self.data9_modify2.Clear()

        choice1 = self.data9_modify1.GetStringSelection()

        sql = "select 歌手 from 动画音乐列表 where 名称=%s"
        cur.execute(sql, choice1)
        res = cur.fetchall()[0][0]
        if res != None:
            self.singer.SetLabel(res)
        else:
            self.singer.SetLabel('')

        wx.MessageBox(u'查询成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK64(self, evt):
        choice1 = self.data9_modify1.GetStringSelection()
        choice2 = self.data9_modify2.GetValue()
        choice3 = self.data9_modify3.GetStringSelection()

        try:
            sql = "update 演唱 set 姓名=%s where 音乐=%s and 姓名=%s"
            cur.execute(sql, (choice3, choice1, choice2))
            conn.commit()
            wx.MessageBox(u'修改成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'修改失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

    def OnOK65(self, evt):
        choice1 = self.data9_delete1.GetStringSelection()
        choice2 = self.data9_delete2.GetValue()

        try:
            sql = "delete from 演唱 where 音乐=%s and 姓名=%s"
            cur.execute(sql, (choice1, choice2))
            conn.commit()
            wx.MessageBox(u'删除成功', u'SUCCEED', wx.OK | wx.ICON_INFORMATION, self)
        except:
            conn.rollback()
            wx.MessageBox(u'删除失败', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)

class MyLoginFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'动画信息管理系统', size=(800, 600))
        icon = wx.Icon(name='./image/wadanohara.jpg', type=wx.BITMAP_TYPE_ANY)
        self.SetIcon(icon)
        cursor = wx.Cursor(wx.CURSOR_ARROW)
        self.SetCursor(cursor)
        self.menuBar = wx.MenuBar()

        self.panel = wx.Panel(self)
        self.SetBackgroundColour('White')
        font1 = wx.Font(40, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.title = wx.StaticText(self, -1, u'动画信息管理系统', pos=(170, 80))
        self.title.SetFont(font1)

        self.statusbar = self.CreateStatusBar()

        font2 = wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.userName = wx.StaticText(self, -1, u'用户名：', pos=(240, 270))
        self.userName.SetFont(font2)
        self.userText = wx.TextCtrl(self, -1, '', size=(200, -1), style=wx.TE_RICH, pos=(350, 270))
        self.userText.SetFont(font2)
        self.userText.SetInsertionPoint(0)

        self.password = wx.StaticText(self, -1, u'密码：', pos=(240, 370))
        self.password.SetFont(font2)
        self.pwdText = wx.TextCtrl(self, -1, '', size=(200, -1), style=wx.TE_PASSWORD | wx.TE_RICH, pos=(350, 370))
        self.pwdText.SetFont(font2)

        self.remind = wx.StaticText(self, -1, u'【注】普通用户登录无需输入密码', pos=(350, 400))

        okButton = wx.Button(self, -1, u'确定', pos=(600, 320))
        self.Bind(wx.EVT_BUTTON, self.OnOK, okButton)

        self.Login_way = '普通用户'
        self.myRole = ''
        self.myName = ''

        Login = wx.Menu()
        Login.Append(201, u'普通用户(&U)\tCtrl+U', u'普通用户登录方式', wx.ITEM_RADIO)
        Login.Append(202, u'管理员(&A)\tCtrl+A', u'管理员登录方式', wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU_RANGE, self.OnLogin, id=201, id2=202)
        self.menuBar.Append(Login, u'登录(&L)')
        self.menuBar.Check(201, True)

        About = wx.Menu()
        Author = wx.NewId()
        About.Append(Author, u'作者(&T)\tF1', u'作者信息')
        self.Bind(wx.EVT_MENU, self.OnHelp, id=Author)
        self.menuBar.Append(About, u'关于(&B)')

        self.SetMenuBar(self.menuBar)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnLogin(self, evt):
        if evt.GetId() == 201:
            if self.Login_way != '普通用户':
                self.userName.SetLabel(u'用户名：')
                self.Login_way = '普通用户'
                self.userText.Clear()
                self.pwdText.Clear()
        if evt.GetId() == 202:
            if self.Login_way != '管理员':
                self.userName.SetLabel(u'管理账号：')
                self.Login_way = '管理员'
                self.userText.Clear()
                self.pwdText.Clear()

    def OnOK(self, evt):
        if self.Login_way == '管理员':
            if self.userText.GetValue() == '' and self.pwdText.GetValue() == '':
                wx.MessageBox(u'请输入管理账号和密码', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            elif self.userText.GetValue() == '':
                wx.MessageBox(u'请输入管理账号', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            elif self.pwdText.GetValue() == '':
                wx.MessageBox(u'请输入密码', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            elif self.userText.GetValue() == 'QTH' and self.pwdText.GetValue() == 'animation':
                self.MyRole = '管理员'
                self.Adminframe = MyAdminFrame(self)
                self.Adminframe.Show(True)
                self.Adminframe.Center(wx.BOTH)
            else:
                wx.MessageBox(u'管理账号或密码不正确', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
                self.userText.Clear()
                self.pwdText.Clear()
        if self.Login_way == '普通用户':
            if self.userText.GetValue() == '':
                wx.MessageBox(u'请输入用户名', u'ERROR', wx.OK | wx.ICON_INFORMATION, self)
            else:
                self.MyRole = '普通用户'
                self.myName = self.userText.GetValue()
                self.Userframe = MyAdminFrame(self)
                self.Userframe.Show(True)
                self.Userframe.Center(wx.BOTH)

    def OnHelp(self, evt):
        wx.MessageBox(u'动画信息管理系统\n\n学号：10152130122\n姓名：钱庭涵\n',
                  u'数据库大作业', wx.OK | wx.ICON_INFORMATION, self)

    def OnClose(self, evt):
        dlg = wx.MessageDialog(None, u'确认离开？', u'关闭', wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            evt.Skip()
        dlg.Destroy()
        cur.close()


if __name__ == u'__main__':
    conn = pymssql.connect(host="", server="", user="sa", password="sql123",
                           database="Animation_MS", charset="utf8")
    cur = conn.cursor()
    if not cur:
        raise (NameError, 'connect failed')
    app = wx.App()
    frame = MyLoginFrame()
    frame.Show(True)
    frame.Center(wx.BOTH)
    app.MainLoop()