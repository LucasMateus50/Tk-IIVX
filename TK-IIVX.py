import webbrowser

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout




#def MATH5():



KV = '''
#:import Snackbar kivymd.uix.snackbar.Snackbar
#:import Clipboard kivy.core.clipboard.Clipboard


<ContentNavigationDrawer>



    ScrollView:

        MDList:

            OneLineListItem:
                text: "Encrypt"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

        
            OneLineListItem:
                text: "TK-IIVX"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"



MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "TK-IIVX "
        md_bg_color: get_color_from_hex("#111111")
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]



    MDNavigationLayout:
        x: toolbar.height


        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"



                Image:
                    source:"math2.png"
                    pos_hint: {'center_x': .2, "center_y": .7}
                    
                Image:
                    source:"math3.png"
                    pos_hint: {'center_x': .5, "center_y": .7}
                    
                Image:
                    source:"math4.png"
                    pos_hint: {'center_x': .8, "center_y": .7}
             


                MDRoundFlatButton:
                    text_color: 'white'
                    line_color: 0.1067, 0.0933, 0, 0.4118
                    pos_hint: {'center_x': .2, "center_y": .5}
                    on_release: Snackbar(text="Site").open()
                    text: "Matlab for Engineers"
                    on_press: app.math1()
                    
                MDRoundFlatButton:
                    text_color: 'white'
                    line_color: 0.1067, 0.0933, 0, 0.4118
                    pos_hint: {'center_x': .5, "center_y": .5}
                    on_release: Snackbar(text="Site").open()
                    text: "MATLAB"
                    on_press: app.math2()
                    
                MDRoundFlatButton:
                    text_color: 'white'
                    line_color: 0.1067, 0.0933, 0, 0.4118
                    pos_hint: {'center_x': .8, "center_y": .5}
                    on_release: Snackbar(text="Site").open()
                    text: "MATH"
                    on_press: app.math3()
              
                    
                
                    
                Image:
                    source:"math5.png"
                    pos_hint: {'center_x': .2, "center_y": .3}
                
                    
                Image:
                    source:"math6.png"
                    pos_hint: {'center_x': .5, "center_y": .3}
                    
                Image:
                    source:"math1.png"
                    pos_hint: {'center_x': .8, "center_y": .3}
                    
                
                MDRoundFlatButton:
                    text_color: 'white'
                    line_color: 0.1067, 0.0933, 0, 0.4118
                    pos_hint: {'center_x': .2, "center_y": .1}
                    on_release: Snackbar(text="Site").open()
                    text: "Mathematica Data Visualization"
                    on_press: app.math4()
                    
                MDRoundFlatButton:
                    text_color: 'white'
                    line_color: 0.1067, 0.0933, 0, 0.4118
                    pos_hint: {'center_x': .5, "center_y": .1}
                    on_release: Snackbar(text="Site").open()
                    text: "MATH"
                    on_press: app.math5()
                
                
                MDRoundFlatButton:
                    text_color: 'white'
                    line_color: 0.1067, 0.0933, 0, 0.4118
                    pos_hint: {'center_x': .8, "center_y": .1}
                    on_release: Snackbar(text="Site").open()
                    text: "MATLAB for Machine Learning"
                    on_press: app.math6()
             


            MDScreen:
                name: "scr 2"



                MDLabel:
                    text: "Email: lucasmateus71849@gmail.com "
                    id: c1
                    halign: "center"
                    color:'white'
                    pos_hint:{"center_y": .48}




                MDLabel:
                    text: "14k7Dt3rG39W6pShafx7x9rk7747B5By7d"
                    halign: "center"
                    color:'white'
                    pos_hint: {"center_y": .4}


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''




class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()



class Main(MDApp):


    def build(self):
        self.theme_cls.theme_style = "Dark"

        return Builder.load_string(KV)




    def math1(self):

       webbrowser.open('https://www.elsevier.com/books/essential-matlab-for-engineers-and-scientists/valentine/978-0-12-374883-6')
       
    def math2(self):

       webbrowser.open('https://www.elsevier.com/books/programming-mathematics-using-matlab/oberbroeckling/978-0-12-817799-0')

    def math3(self):

       webbrowser.open('https://www.packtpub.com/product/practical-discrete-mathematics/9781838983147')

    def math4(self):

       webbrowser.open('https://www.packtpub.com/product/mathematica-data-visualization/9781783282999')
       
    def math5(self):

       webbrowser.open('https://www.packtpub.com/product/mathematical-foundation-for-ai-and-machine-learning-video/9781789613209')
       
    def math6(self):

       webbrowser.open('https://www.packtpub.com/product/matlab-for-machine-learning/9781788398435')


    

Main().run()
