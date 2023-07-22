from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown

Window.clearcolor = (0,0,1,1)
i=0
s=0
l=0





class Screen1(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        global l
        global s
        global i 
        
        

        but1 = Button(text ='Image',color='#fffff',size_hint_y=.5,size_hint_x=.8)
        but2 = Button(text ='Image',color='#fffff',size_hint_y=.5,size_hint_x=.8)
        but3 = Button(text ='Information',color='#fffff',size_hint_y=.5,size_hint_x=.8)
        but4 = Button(text ='Test',color='#fffff',size_hint_y=.5,size_hint_x=.8)

        but1.background_color= (.25,.25,.25,1)
        but2.background_color= (.25,.25,.25,1)
        but3.background_color= (.25,.25,.25,1)
        but4.background_color= (.25,.25,.25,1)

        layout = BoxLayout(orientation='vertical')

        # Устанавливаем цвет фона окна (например, черный)


        # Создаем изображение и задаем его в качестве фона для виджета BoxLayout
        background_image = Image(source='grad.png',mipmap=True,allow_stretch=True,keep_ratio=False)
        layout.add_widget(background_image)
        

        but2.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        but1.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        but3.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        but4.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        but3.on_press = self.triger3
        but2.on_press = self.triger
        but1.on_press = self.triger2
        but4.on_press = self.triger4
        
        lab1 = Label(text='[i]'+'Говерла',markup=True,font_size='100sp',color='#BEBEBE')
        lab1.background_normal = (0.1,0.72,0.56,1)
        main = BoxLayout(orientation = "vertical",spacing=10)
        


    
        main.add_widget(lab1)
        main.add_widget(but2)
        main.add_widget(but1)
        main.add_widget(but3)
        main.add_widget(but4)
        self.add_widget(layout)
        self.add_widget(main)

    def triger4(self):
        self.manager.current = 'but'
    def triger3(self):
        self.manager.current = 'image2'
    def triger2(self):
        self.manager.current = 'imagn'
    def triger(self):
        self.manager.current = 'video'

class Screen4(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Устанавливаем цвет фона окна (например, черный)


        # Создаем изображение и задаем его в качестве фона для виджета BoxLayout
        background_image = Image(source='grad.png',mipmap=True,allow_stretch=True,keep_ratio=False)
        layout.add_widget(background_image)
                
    
        lab = Label(text='[i]'+'Гове́рла  — найвища вершина Українських Карпат і найвища точка України, її висота становить 2 061 м над рівнем моря. Розташована в гірському масиві Чорногора на межі Надвірнянського району Івано-Франківської області та Рахівського району Закарпатської області, за 17 кілометрів від кордону з Румунією.',font_size="25px",markup=True,text_size=(800,160))

        main = BoxLayout(orientation = "vertical")
       
        but1 = Button(text="Back",size_hint_y = .3,color="#fffff")
        but1.background_color= (.25,.25,.25,1)
        but1.on_press = self.triger
        main.add_widget(lab)
        main.add_widget(but1)
        self.add_widget(layout)
        self.add_widget(main)
    
    def triger(self):
        self.manager.current ='start'

class Screen3(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Устанавливаем цвет фона окна (например, черный)


        # Создаем изображение и задаем его в качестве фона для виджета BoxLayout
        background_image = Image(source='grad.png',mipmap=True,allow_stretch=True,keep_ratio=False)
        layout.add_widget(background_image)
    
        image = Image(source="g2.jpg")
        # image.mipmap=True
        # image.mag_filter = 'linear'
        # image.allow_stretch = True
        main = BoxLayout(orientation = "vertical")
       
        but1 = Button(text="Back",size_hint_y = .3,color="#fffff")
        but1.background_color= (.25,.25,.25,1)
        but1.on_press = self.triger

        main.add_widget(image)
        main.add_widget(but1)
        self.add_widget(layout)
        self.add_widget(main)
    
    def triger(self):
        self.manager.current ='start'

class Screen5(Screen):    
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Устанавливаем цвет фона окна (например, черный)


        # Создаем изображение и задаем его в качестве фона для виджета BoxLayout
        background_image = Image(source='grad.png',mipmap=True,allow_stretch=True,keep_ratio=False)
        layout.add_widget(background_image)

        lab = Label(text="Bибери вірне твердження.",font_size='30px',markup=True)

        but1 = Button(text="Check",color='#fffff',size_hint_y=.5,size_hint_x=.8)
        but2 = Button(text="Back",color='#fffff',size_hint_y=.5,size_hint_x=.8)
        
        but1.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        but2.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        but1.on_press = self.triger
        but2.on_press = self.triger2

        but1.background_color= (.25,.25,.25,1)
        but2.background_color= (.25,.25,.25,1)

        labl1 = Label(text="висота Гове́рли становить 2061 м",font_size='20px',markup=True)
        labl2 = Label(text="Bисота Гове́рли становить 3571 м",font_size='20px',markup=True)
        labl3 = Label(text="Bисота Гове́рли становить 2981 м",font_size='20px',markup=True)

        layoutH = BoxLayout(orientation='horizontal', )
        layoutH1 = BoxLayout(orientation='horizontal', )
        layoutH2 = BoxLayout(orientation='horizontal', )
        layoutH3 = BoxLayout(orientation='horizontal', )
        layoutH4 = BoxLayout(orientation='horizontal', )
        layoutV = BoxLayout(orientation='vertical', )
        # Создание экземпляра CheckBox
        checkbox = CheckBox(
            active=False
        )
        checkbox2 = CheckBox(active=False)
        checkbox3 = CheckBox(active=False)
        # Определение обработчика события изменения состояния CheckBox
        checkbox.bind(active=self.on_checkbox_active)
        checkbox2.bind(active=self.on_checkbox_active2)
        checkbox3.bind(active=self.on_checkbox_active3)

        checkbox.color = (100,100,100,1)
        checkbox2.color = (100,100,100,1)
        checkbox3.color = (100,100,100,1)

        # Добавление CheckBox в макет
        layoutH.add_widget(lab)
        layoutH1.add_widget(checkbox)
        layoutH1.add_widget(labl1)
        layoutH2.add_widget(checkbox2)
        layoutH2.add_widget(labl2)
        layoutH3.add_widget(checkbox3)
        layoutH3.add_widget(labl3)
        layoutH4.add_widget(but2)
        layoutH4.add_widget(but1)
        layoutV.add_widget(layoutH)
        layoutV.add_widget(layoutH1)
        layoutV.add_widget(layoutH2)
        layoutV.add_widget(layoutH3)
        layoutV.add_widget(layoutH4)
        
        self.add_widget(layout)
        self.add_widget(layoutV)

    def on_checkbox_active(self, instance, value):
        global i
        # Обработчик события изменения состояния CheckBox
        if value:
            print("CheckBox выбран")
            i+=1
        else:
            print("CheckBox не выбран")
            i-=1
    def on_checkbox_active2(self, instance, value):
        global s
        # Обработчик события изменения состояния CheckBox
        if value:
            print("CheckBox выбран")
            s+=1
        else:
            print("CheckBox не выбран")
            s-=1

    def on_checkbox_active3(self, instance, value):
        global l
        # Обработчик события изменения состояния CheckBox
        if value:
            print("CheckBox выбран")
            l+=1
        else:
            print("CheckBox не выбран")
            l-=1

    def triger2(self):
        self.manager.current = 'start'
    def triger(self):
        if i == 1 and l == 0 and s == 0 :
            self.manager.current ='but1'
        else:
            self.manager.current = 'but2'


class Screen6(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Устанавливаем цвет фона окна (например, черный)


        # Создаем изображение и задаем его в качестве фона для виджета BoxLayout
        background_image = Image(source='grad.png',mipmap=True,allow_stretch=True,keep_ratio=False)
        layout.add_widget(background_image)

        main = BoxLayout(orientation = "vertical")
        lab = Label(text='Вірно',markup=True,font_size='100sp',color='#fE154')
        but = Button(text="back",size_hint_y=.5,color='#fffff')
        but.background_color= (.25,.25,.25,1)
        but.on_press = self.triger

        main.add_widget(lab)
        main.add_widget(but)

        self.add_widget(layout)
        self.add_widget(main)
    

    def triger(self):
        self.manager.current = 'start'

class Screen7(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Устанавливаем цвет фона окна (например, черный)


        # Создаем изображение и задаем его в качестве фона для виджета BoxLayout
        background_image = Image(source='grad.png',mipmap=True,allow_stretch=True,keep_ratio=False)
        layout.add_widget(background_image)

        main = BoxLayout(orientation = "vertical")
        lab = Label(text='Невірно',markup=True,font_size='100sp',color='#fE154')
        but = Button(text="back",size_hint_y=.5,color='#fffff')
        but.background_color= (.25,.25,.25,1)
        but.on_press = self.triger

        main.add_widget(lab)
        main.add_widget(but)

        self.add_widget(layout)
        self.add_widget(main)
    

    def triger(self):
        self.manager.current = 'start'



class Screen2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Устанавливаем цвет фона окна (например, черный)


        # Создаем изображение и задаем его в качестве фона для виджета BoxLayout
        background_image = Image(source='grad.png',mipmap=True,allow_stretch=True,keep_ratio=False)
        layout.add_widget(background_image)

        main = BoxLayout(orientation = "vertical")

        image = Image(source="g.jpg")
        # image.mipmap=True
        # image.mag_filter = 'linear'
        # image.allow_stretch = True
        but2 = Button(text ='Back',size_hint_y=(.3),color="#fffff")
        but2.background_color = (.25,.25,.25, 1)
        but2.on_press = self.triger

        main.add_widget(image)
            
        main.add_widget(but2)
        
        self.add_widget(layout)
        self.add_widget(main)

    def triger(self):
        self.manager.current= "start"

class MyApp(App):
    def build(self):
        sem = ScreenManager()
        sem.add_widget(Screen1(name='start'))
        sem.add_widget(Screen2(name="imagn"))
        sem.add_widget(Screen3(name="video"))
        sem.add_widget(Screen4(name='image2'))
        sem.add_widget(Screen5(name='but'))
        sem.add_widget(Screen6(name='but1'))
        sem.add_widget(Screen7(name='but2'))
        return sem

       
my_app = MyApp()

my_app.run()
