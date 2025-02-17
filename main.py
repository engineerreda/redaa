from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.core.window import Window
from kivymd.uix.imagelist import imagelist
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image  # إضافة هذا السطر لاستخدام عنصر Image
from kivy.core.text import LabelBase
from kivy.clock import Clock


LabelBase.register(name="ArabicFont", fn_regular="amiri.ttf")  # استبدل amiri.ttf بخط يدعم العربية

# حقل نصي مخصص لدعم اللغة العربية
class StableArabicTextField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._original_text = ""

    def insert_text(self, substring, from_undo=False):
        # الاحتفاظ بالنص الأصلي
        self._original_text += substring
        reshaped_text = arabic_reshaper.reshape(self._original_text)
        bidi_text = get_display(reshaped_text)
        self.text = bidi_text

    def do_backspace(self, from_undo=False, mode='bkspc'):
        # التعامل مع الحذف
        if self._original_text:
            self._original_text = self._original_text[:-1]
            reshaped_text = arabic_reshaper.reshape(self._original_text)
            bidi_text = get_display(reshaped_text)
            self.text = bidi_text




def reshape_text(text):
            reshaped_text = arabic_reshaper.reshape(text)  # إعادة تشكيل النص
            bidi_text = get_display(reshaped_text)  # ترتيب النص بالاتجاه الصحيح
            return bidi_text

class ArabicApp(MDApp):
    def on_text_change(self, instance, value):
        # إذا كان النص يحتاج معالجة
            try:
                reshaped = reshape_text(value)
                if instance.text != reshaped:
                    instance.text = reshaped
            except Exception as e:
                print("Error while reshaping text:", e)
    def build(self):
        Window.size= (370, 600)
        Window.direction = 'rtl'
        self.screen_manager = ScreenManager()
        def add_background_image(screen):
            background = Image(
                source="imag.jpg",  # اسم ملف الصورة
                allow_stretch=True,  # السماح بالتمدد
                keep_ratio=False,  # عدم الحفاظ على نسبة العرض إلى الارتفاع
            )
            screen.add_widget(background)
       
        # الشاشة الرئيسية
        main_screen = MDScreen(name="main")
        add_background_image(main_screen)  # إضافة الخلفية للشاشة الرئيسية

        # دالة لتحويل النص العربي
        

        # الشاشة الرئيسية
       # main_screen = MDScreen(name="main")
       # layout = MDBoxLayout(orientation="vertical")
       

        # إنشاء شريط الأدوات
        toolbar = MDTopAppBar(
            title=reshape_text(" برنامــج الكــاش"),  # ترتيب العنوان
           # left_action_items=[["menu", lambda x: print("Menu clicked")]],
            right_action_items=[["home", lambda x: print("Home clicked")]]
        )
        toolbar.ids.label_title.font_name = "arial"  # ت
        toolbar.size_hint_y = None  # حجم ثابت
        toolbar.height = "60dp"  # ارتفاع الشريط
        toolbar.pos_hint = {"top": 1}  # يجعل الشريط في أعلى الشاشة

        main_screen.add_widget(toolbar)

        # إضافة نص عربي
      

        # دالة للتنقل بين الشاشات
        def open_screen(screen_name):
            self.screen_manager.current = screen_name

        # إضافة الأزرار بشكل إجرائي
        button1 = MDRaisedButton(
            text=reshape_text("إضافة الخطوط"),
            size_hint=(1, None),
            size=("200dp", "50dp"),  # حجم ثابت للزر
            pos_hint={"center_x": 0.5,"center_y": 0.6}, # موقع مطلق (x=100, y=500)
            on_release=lambda x: open_screen("screen_1")
        )
        button1.font_name = "arial"

        main_screen.add_widget(button1)
        button2 = MDRaisedButton(
            text=reshape_text("إضافة عملية تحويل"),
            size_hint=(1, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5,"center_y": 0.53},
            on_release=lambda x: open_screen("screen_2")
        )
        button2.font_name = "arial"

        main_screen.add_widget(button2)

        button3 = MDRaisedButton(
            text=reshape_text("إضافة عملية إستلام"),
            size_hint=(1, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5,"center_y": 0.46},
           # md_bg_color=(0, 0, 1, 1),
            on_release=lambda x: open_screen("screen_3")
        )
        button3.font_name = "arial"

        main_screen.add_widget(button3)

        button4 = MDRaisedButton(
            text=reshape_text("الشاشة 4"),
            size_hint=(1, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5,"center_y": 0.39},
            on_release=lambda x: open_screen("screen_4")
        )
        button4.font_name = "arial"

        main_screen.add_widget(button4)

        button5 = MDRaisedButton(
            text=reshape_text("الشاشة 5"),
            size_hint=(1, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5,"center_y": 0.32},
            on_release=lambda x: open_screen("screen_5")
        )
        button5.font_name = "arial"
        main_screen.add_widget(button5)

        
       
    
       
      #  main_screen.add_widget(layout)
        self.screen_manager.add_widget(main_screen)

##################################screen1
        screen1 = MDScreen(name="screen_1")
         
        add_background_image(screen1) 
       # layout = MDBoxLayout(orientation='vertical')
      #  screen_layout1 = MDBoxLayout(orientation="vertical")
        
        card = MDCard(
            size_hint=(None, None),
            size=("250dp", "40dp"),
           
            pos_hint={"center_x": 0.5,"center_y": 0.85},
            md_bg_color=(0.2, 0.2, 1, 1)  # اللون الأزرق للخلفية
        )
        
        screen1.add_widget(card)
        textphonenum = StableArabicTextField(
            hint_text=reshape_text(" رقم التليفون "),  # النص التلميحي الذي يظهر داخل الحقل
          #  helper_text="Please enter a valid username",  # النص المساعد
            helper_text_mode="on_focus",  # الوضع الذي يظهر فيه النص المساعد (on_focus, on_error)
            password=False,  # إذا كان الحقل خاص بكلمة مرور
            size_hint=(None, None),  # الحجم النسبي
            size=("200dp", "50dp"),  # الحجم الفعلي
            pos_hint={"center_x": 0.35,"center_y": 0.75}, # الموقع داخل الواجهة
            halign="right",  # محاذاة النص من اليمين
            line_color_normal=(0, 0, 1, 1),
            font_size="20sp",
       
        )  
        textphonenum.font_name_hint_text="calibrib"
        textphonenum.font_name="calibrib.ttf"

        screen1.add_widget(textphonenum) 

        walletname = StableArabicTextField(
            hint_text=reshape_text(" اسم المحفظـــة "),  # النص التلميحي الذي يظهر داخل الحقل
          #  helper_text="Please enter a valid username",  # النص المساعد
            helper_text_mode="on_focus",  # الوضع الذي يظهر فيه النص المساعد (on_focus, on_error)
            password=False,  # إذا كان الحقل خاص بكلمة مرور
            size_hint=(None, None),  # الحجم النسبي
            size=("200dp", "50dp"),  # الحجم الفعلي
            pos_hint={"center_x": 0.35,"center_y": 0.65}, # الموقع داخل الواجهة
            halign="right",  # محاذاة النص من اليمين
            line_color_normal=(0, 0, 1, 1),
            font_size="20sp",
            font_name="Amiri.ttf",
          
       
        )  
        walletname.font_name_hint_text="calibrib"
        
                                               

        walletname.bind(on_text=self.on_text_change)                         
        screen1.add_widget(walletname)

        


       # namephone = MDLabel(
        #    text=reshape_text(" اسم المحفظة    :"),
        #    halign="center",
          #  font_name="arial",
          #  pos_hint={"center_x": 0.8,"center_y": 0.65},
           # theme_text_color="Custom",
          #  text_color=(0, 0, 0, 1), 
            #font_style="H5",
          
           # font_size="70sp",
       # )
       # namephone.font_name="calibrib"
       # screen1.add_widget(namephone)   
        adress = MDLabel(
            text=reshape_text("إضافة الخطوط"),
            halign="center",
            font_name="arial",
            pos_hint={"center_x": 0.5,"center_y": 0.85},
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1), 
            #font_style="H5",
          
           # font_size="70sp",
        )
        adress.font_name="calibrib"
        screen1.add_widget(adress)
        toolbar1 = MDTopAppBar(
            #title=reshape_text(" برنامج الكاش"),  # ترتيب العنوان
            left_action_items=[["arrow-left",lambda x: open_screen("main")]],
            right_action_items=[["home", lambda x: print("Home clicked")]]
        )
        toolbar1.ids.label_title.font_name = "arial"  # ت
        toolbar1.size_hint_y = None  # حجم ثابت
        toolbar1.height = "60dp"  # ارتفاع الشريط
        toolbar1.pos_hint = {"top": 1}  # يجعل الشريط في أعلى الشاشة

      
        screen1.add_widget(toolbar1)
        self.screen_manager.add_widget(screen1)
##################################screen2

        screen2 = MDScreen(name="screen_2")
        add_background_image(screen2) 
      #  screen_layout2 = MDBoxLayout(orientation="vertical")
        screen_label2 = MDLabel(
            text=reshape_text("مرحبًا في الشاشة 2"),
            halign="center",
            font_name="arial",
        )
        screen2.add_widget(screen_label2)
        back_button2 = MDRaisedButton(
            text=reshape_text("<<<"),
            size_hint=(None, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5},
            on_release=lambda x: open_screen("main")
        )
        toolbar2 = MDTopAppBar(
            #title=reshape_text(" برنامج الكاش"),  # ترتيب العنوان
            left_action_items=[["arrow-left",lambda x: open_screen("main")]],
           # right_action_items=[["home", lambda x: print("Home clicked")]]
        )
        toolbar2.ids.label_title.font_name = "arial"  # ت
        toolbar2.size_hint_y = None  # حجم ثابت
        toolbar2.height = "60dp"  # ارتفاع الشريط
        toolbar2.pos_hint = {"top": 1}  # يجعل الشريط في أعلى الشاشة

      
        screen2.add_widget(toolbar2)
       


        screen2.add_widget(back_button2)
       # screen2.add_widget(screen_layout2)
        self.screen_manager.add_widget(screen2)
##################################screen3

        screen3 = MDScreen(name="screen_3")
        add_background_image(screen3) 

       # screen_layout3 = MDBoxLayout(orientation="vertical")
        screen_label3 = MDLabel(
            text=reshape_text("مرحبًا في الشاشة 3"),
            halign="center",
            font_name="arial",
        )
        screen3.add_widget(screen_label3)
        back_button3 = MDRaisedButton(
            text=reshape_text("العودة"),
            size_hint=(None, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5},
            on_release=lambda x: open_screen("main")
        )
        toolbar3 = MDTopAppBar(
            #title=reshape_text(" برنامج الكاش"),  # ترتيب العنوان
            left_action_items=[["arrow-left",lambda x: open_screen("main")]],
           # right_action_items=[["home", lambda x: print("Home clicked")]]
        )
        toolbar3.ids.label_title.font_name = "arial"  # ت
        toolbar3.size_hint_y = None  # حجم ثابت
        toolbar3.height = "60dp"  # ارتفاع الشريط
        toolbar3.pos_hint = {"top": 1}  # يجعل الشريط في أعلى الشاشة

      
        screen3.add_widget(toolbar3)
        
       

        screen3.add_widget(back_button3)
       # screen3.add_widget(screen_layout3)
        self.screen_manager.add_widget(screen3)
##################################screen4

        screen4 = MDScreen(name="screen_4")
        add_background_image(screen4) 

      #  screen_layout4 = MDBoxLayout(orientation="vertical")
        screen_label4 = MDLabel(
            text=reshape_text("مرحبًا في الشاشة 4"),
            halign="center",
            font_name="arial",
        )
        screen4.add_widget(screen_label4)
        back_button4 = MDRaisedButton(
            text=reshape_text("العودة"),
            size_hint=(None, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5},
            on_release=lambda x: open_screen("main")
        )
        toolbar4 = MDTopAppBar(
            #title=reshape_text(" برنامج الكاش"),  # ترتيب العنوان
            left_action_items=[["arrow-left",lambda x: open_screen("main")]],
           # right_action_items=[["home", lambda x: print("Home clicked")]]
        )
        toolbar4.ids.label_title.font_name = "arial"  # ت
        toolbar4.size_hint_y = None  # حجم ثابت
        toolbar4.height = "60dp"  # ارتفاع الشريط
        toolbar4.pos_hint = {"top": 1}  # يجعل الشريط في أعلى الشاشة

      
        screen4.add_widget(toolbar4)


        screen4.add_widget(back_button4)
        #screen4.add_widget(screen_layout4)
        self.screen_manager.add_widget(screen4)
##################################screen5

        screen5 = MDScreen(name="screen_5")
        add_background_image(screen5) 

    #    screen_layout5 = MDBoxLayout(orientation="vertical")
        screen_label5 = MDLabel(
            text=reshape_text("مرحبًا في الشاشة 5"),
            halign="center",
            font_name="arial",
        )
        screen5.add_widget(screen_label5)
        back_button5 = MDRaisedButton(
            text=reshape_text("العودة"),
            size_hint=(None, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5},
            on_release=lambda x: open_screen("main")
        )

        toolbar5 = MDTopAppBar(
            #title=reshape_text(" برنامج الكاش"),  # ترتيب العنوان
            left_action_items=[["arrow-left",lambda x: open_screen("main")]],
           # right_action_items=[["home", lambda x: print("Home clicked")]]
        )
        toolbar5.ids.label_title.font_name = "arial"  # ت
        toolbar5.size_hint_y = None  # حجم ثابت
        toolbar5.height = "60dp"  # ارتفاع الشريط
        toolbar5.pos_hint = {"top": 1}  # يجعل الشريط في أعلى الشاشة

      
        screen5.add_widget(toolbar5)
        screen5.add_widget(back_button5)
        self.screen_manager.add_widget(screen5)

        return self.screen_manager
        

if __name__ == "__main__":
    ArabicApp().run()
