#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
from PIL import Image

player = 1
trigger = True
last = 0
Speed = 350  
score = 0
game_over = False
over = True
life = 3
level = 0

m1 = []
m2 = []
m3 = []
m4 = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []




ir = InfraredSensor() #Sensor.SetMode(4,2)
wolf1 = Image.open(r'/home/robot/images/vl1.bmp')
wolf2 = Image.open(r'/home/robot/images/vl2.bmp')
wolf3 = Image.open(r'/home/robot/images/vl3.bmp')
wolf4 = Image.open(r'/home/robot/images/vl4.bmp')

lcd.clear()
lcd.image.paste(wolf1, (0,0))
lcd.update()

Sound.beep()

for i in range(0,5):
    m1[i] = 0
    m2[i] = 0
    m3[i] = 0
    m4[i] = 0


x1[0] = 26
y1[0] = 44
x1[1] = 34
y1[1] = 49
x1[2] = 42
y1[2] = 54
x1[3] = 52
y1[3] = 61
x1[4] = 52
y1[4] = 120


x2[0] = 26
y2[0] = 72
x2[1] = 34
y2[1] = 77
x2[2] = 42
y2[2] = 82
x2[3] = 52
y2[3] = 89
x2[4] = 52
y2[4] = 120


x3[0] = 151
y3[0] = 44
x3[1] = 143
y3[1] = 49
x3[2] = 135
y3[2] = 54
x3[3] = 126
y3[3] = 61
x3[4] = 126
y3[4] = 120


x4[0] = 150
y4[0] = 73
x4[1] = 143
y4[1] = 77
x4[2] = 136
y4[2] = 82
x4[3] = 126
y4[3] = 89
x4[4] = 126
y4[4] = 120

' Запускаем подпроцесы
Thread.Run = logic
Thread.Run = screen
' отрисовка экрана
Sub screen
  While over
    If trigger = "True" Then    
      If player = 1 Then
        LCD.BmpFile(1,0,0,"/home/root/lms2012/prjs/volk/vl1")
      EndIf
      
      If player = 2 Then
        LCD.BmpFile(1,0,0,"/home/root/lms2012/prjs/volk/vl2")
      EndIf
      
      If player = 3 Then
        LCD.BmpFile(1,0,0,"/home/root/lms2012/prjs/volk/vl3")
      EndIf
      
      If player = 4 Then
        LCD.BmpFile(1,0,0,"/home/root/lms2012/prjs/volk/vl4")
      EndIf
      
      
      
      For i = 0 To 4
        If m1[i] > 0 Then
          LCD.FillCircle(1,x1[i],y1[i],3)
        EndIf
        
        If m2[i] > 0 Then
          LCD.FillCircle(1,x2[i],y2[i],3)
        EndIf
        
        If m3[i] > 0 Then
          LCD.FillCircle(1,x3[i],y3[i],3)
        EndIf
        
        If m4[i] > 0 Then
          LCD.FillCircle(1,x4[i],y4[i],3)
        EndIf  
      EndFor
      
      LCD.Text(1,40,34,1,"Life-" + life + "   " + score)
      
      If game_over = "True" Then
        LCD.BmpFile(1,0,0,"/home/root/lms2012/prjs/volk/GO")
        Speaker.Note(100,"E4",3000)
        Speaker.Wait()
        Speaker.Note(100,"D4",3000)
        Speaker.Wait()
        Speaker.Note(100,"C4",3000)
        Speaker.Wait()
        Program.End()
      EndIf
      
      trigger = "False"
    EndIf
    
    
  EndWhile
EndSub
' процедура обработки яйца
Sub logic
  While over
    ' процедура увеличивания сложности игры
    Speed = 1000 / (0.03*score+1)
    
    ' процедура рождения яйца
    If EV3.Time > (last + (Speed*2)) Then
      If m1[0] = 0 And m1[1] = 0 And Math.Round(Math.GetRandomNumber(100)) = 10 Then
        m1[0] = EV3.Time
        last = m1[0]
        trigger = "True"
      EndIf
    EndIf
    
    If EV3.Time > (last + (Speed*2)) Then
      If m2[0] = 0 And m2[1] = 0  And Math.Round(Math.GetRandomNumber(100)) = 20 Then
        m2[0] = EV3.Time
        last = m2[0]
        trigger = "True"
      EndIf 
    EndIf
    
    If EV3.Time > (last + (Speed*2)) Then    
      If m3[0] = 0 And m3[1] = 0  And Math.Round(Math.GetRandomNumber(100)) = 30 Then
        m3[0] = EV3.Time
        last = m3[0]
        trigger = "True"
      EndIf 
    EndIf
    
    If EV3.Time > (last + (Speed*2)) Then      
      If m4[0] = 0 And m4[1] = 0  And Math.Round(Math.GetRandomNumber(100)) = 40 Then
        m4[0] = EV3.Time
        last = m4[0]
        trigger = "True"
      EndIf  
    EndIf
    
    ' цикл для перемещения яйца
    For i = 0 To 4
      If m1[i]  <> 0 And m1[i] + (Speed*(i+1)) < EV3.Time Then
        m1[i+1] = m1[i]
        m1[i] = 0 
        trigger = "True"
        Speaker.Note(100,"C4",150)
      EndIf
      
      If m2[i]  <> 0 And m2[i] + (Speed*(i+1)) < EV3.Time Then
        m2[i+1] = m2[i]
        m2[i] = 0
        trigger = "True"
        Speaker.Note(100,"C4",150)
      EndIf
      
      If m3[i]  <> 0 And m3[i] + (Speed*(i+1)) < EV3.Time Then
        m3[i+1] = m3[i]
        m3[i] = 0
        trigger = "True"
        Speaker.Note(100,"C4",150)
      EndIf
      
      If m4[i]  <> 0 And m4[i] + (Speed*(i+1)) < EV3.Time Then
        m4[i+1] = m4[i]
        m4[i] = 0
        trigger = "True"
        Speaker.Note(100,"C4",150)
      EndIf
    EndFor
    ' Проверка на забирание яйца
    
    If m1[3] > 0 And player = 1 And m1[3] + (Speed*3.5) < EV3.Time Then
      score = score+1
      m1[3] = 0
      trigger = "True"
      Speaker.Note(100,"C5",250)
    EndIf
    
    If m2[3] > 0 And player = 2 And m2[3] + (Speed*3.5) < EV3.Time Then
      score = score+1
      m2[3] = 0
      trigger = "True"
      Speaker.Note(100,"C5",250)
    EndIf
    
    If m3[3] > 0 And player = 3 And m3[3] + (Speed*3.5) < EV3.Time Then
      score = score+1
      m3[3] = 0
      trigger = "True"
      Speaker.Note(100,"C5",250)
    EndIf
    
    If m4[3] > 0 And player = 4 And m4[3] + (Speed*3.5) < EV3.Time Then
      score = score+1
      m4[3] = 0
      trigger = "True"
      Speaker.Note(100,"C5",250)
    EndIf
    ' Проверяем не упалоли яйцо
    
    If m1[4] > 0 Then
      Program.Delay(1500)
      Speaker.Note(100,"E4",500)
      Speaker.Wait()
      Speaker.Note(100,"D4",250)
      Speaker.Wait()
      Speaker.Note(100,"C4",250)
      Speaker.Wait()
      
      life = life - 1
      If life = 0 Then
        game_over = "True"
      EndIf
      m1[4] = 0
      trigger = "True"
      Program.Delay(1500)
    EndIf
    
    If m2[4] > 0 Then
      Program.Delay(1500)
      Speaker.Note(100,"E4",500)
      Speaker.Wait()
      Speaker.Note(100,"D4",250)
      Speaker.Wait()
      Speaker.Note(100,"C4",250)
      Speaker.Wait()
      
      life = life - 1
      If life = 0 Then
        game_over = "True"
      EndIf
      m2[4] = 0
      trigger = "True"
      Program.Delay(1500)
    EndIf
    
    If m3[4] > 0 Then
      Program.Delay(1500)
      Speaker.Note(100,"E4",500)
      Speaker.Wait()
      Speaker.Note(100,"D4",250)
      Speaker.Wait()
      Speaker.Note(100,"C4",250)
      Speaker.Wait()
      
      life = life - 1
      If life = 0 Then
        game_over = "True"
      EndIf
      m3[4] = 0
      trigger = "True"
      Program.Delay(1500)
    EndIf
    
    If m4[4] > 0 Then
      Program.Delay(1500)
      Speaker.Note(100,"E4",500)
      Speaker.Wait()
      Speaker.Note(100,"D4",250)
      Speaker.Wait()
      Speaker.Note(100,"C4",250)
      Speaker.Wait()
      
      life = life - 1
      If life = 0 Then
        game_over = "True"
      EndIf
      m4[4] = 0
      trigger = "True"
      Program.Delay(1500)
    EndIf
  EndWhile
EndSub
' процедура считывания покозаний ИК-датчика

Speaker.Note(100,"E4",1000)
Speaker.Wait()
Speaker.Note(100,"D4",1000)
Speaker.Wait()        

While over
  If Sensor.ReadRawValue(4,0) = 1 Then
    If player <> 1 Then
      player = 1
      trigger = "True"
    EndIf
  EndIf
  
  If Sensor.ReadRawValue(4,0) = 2 Then
    If player <> 2 Then
      player = 2
      trigger = "True"
    EndIf
  EndIf
  
  If Sensor.ReadRawValue(4,0) = 3 Then
    If player <> 3 Then
      player = 3
      trigger = "True"
    EndIf
  EndIf
  
  If Sensor.ReadRawValue(4,0) = 4 Then
    If player <> 4 Then
      player = 4
      trigger = "True"
    EndIf
  EndIf
EndWhile