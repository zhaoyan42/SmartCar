# -*- coding: utf-8 -*- # 
# by oldj http://oldj.net/ #  
import pythoncom 
import pyHook    
def onMouseEvent(event): 
    
   # ��������¼�     
   print "MessageName:",event.MessageName     
   print "Message:", event.Message     
   print "Time:", event.Time     
   print "Window:", event.Window     
   print "WindowName:", event.WindowName     
   print "Position:", event.Position     
   print "Wheel:", event.Wheel     
   print "Injected:", event.Injected           
   print"---"
  
   # ���� True �Ա㽫�¼����������������     
   # ע�⣬���������� False ��������¼�����ȫ������     
   # Ҳ����˵�����꿴�����Ὡ���Ƕ����ƺ�ʧȥ��Ӧ��     
   return True
 
def onKeyboardEvent(event):
  # ���������¼�     
   print "MessageName:", event.MessageName     
   print "Message:", event.Message     
   print "Time:", event.Time     
   print "Window:", event.Window     
   print "WindowName:", event.WindowName     
   print "Ascii:", event.Ascii, chr(event.Ascii)     
   print "Key:", event.Key     
   print "KeyID:", event.KeyID     
   print "ScanCode:", event.ScanCode     
   print "Extended:", event.Extended     
   print "Injected:", event.Injected     
   print "Alt", event.Alt     
   print "Transition", event.Transition     
   print "---"      
   # ͬ����¼����������ķ���ֵ     
   return True 

def main():     
   # ����һ�������ӡ��������     
   hm = pyHook.HookManager()      
   # �������м����¼�     
   hm.KeyDown = onKeyboardEvent     
   # ���ü��̡����ӡ�     
   hm.HookKeyboard()      
   # ������������¼�     
   hm.MouseAll = onMouseEvent     
   # ������ꡰ���ӡ�     
   hm.HookMouse()      
   # ����ѭ�����粻�ֶ��رգ�����һֱ���ڼ���״̬     
   pythoncom.PumpMessages() 

if __name__ == "__main__":     
   main()