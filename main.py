import flet as ft
from flet import *
import requests
import webbrowser

def main(page:Page):
    ################ [window properties] ############################
    page.title = 'Panda Sender Pro'
    page.window.width = 390
    page.window.height = 800
    page.window.top = 10
    page.window.left = 850
    page.window.bgcolor= colors.DEEP_PURPLE_ACCENT_700
    page.vertical_alignment = "center"
    page.horizontal_alignment ="center"
    
    #################[ Don't touch  ]#####################################
    
    def telegram (t):
        webbrowser.open_new('https://t.me/shopandbuyy')

    def whatsapp(w):
        webbrowser.open_new('https://wa.me/qr/ENLYCD65EQZAK1')   





    def show(e): 
        v1 = en3.value
        pp=requests.get('https://pastebin.com/raw/cQF7wPFY').text

        if v1 == pp :
            Alert9 = AlertDialog(
                title=Text("Your key is valid but not active"),
                content=Text("To contact the admin click on: YES"),
                actions=[
                    TextButton("Yes", on_click=telegram),
                    TextButton("No", on_click=telegram),
                    


                ],
                

            )
            page.overlay.append(Alert9)
            Alert9.open=True
            page.update()


        else: 
            
            Alert8 = AlertDialog(
                modal=True,
                title=Text('Your key is not Valid',),
                content=Text("To buy a key click on: BUY"),
                actions=[
                    TextButton("BUY", on_click=telegram),
                    TextButton("NO", on_click=telegram),
                    


                ],
                

            )
                

            page.overlay.append(Alert8)
            Alert8.open=True
            page.update()

        

    en =Text('Welcome To Panda Sender Pro', weight=FontWeight.W_900 ,size= 40 , rtl=True , width=390 , text_align='center', color=colors.DEEP_PURPLE_800)
    en1 = Row([
                        Image(src=f'https://pic.funnygifsbox.com/uploads/2020/07/funnygifsbox.com-2020-07-18-07-46-26-90.gif',width=280)

                    ],alignment=MainAxisAlignment.CENTER)
    en2 = Text('Enjoy With Bulk SMS Worldwide',weight=FontWeight.W_900 ,size= 40 , rtl=True , width=390 , text_align='center' , color=colors.DEEP_PURPLE_800)
    en3 = TextField(label="Enter Your License Key", password=True, can_reveal_password=True ,icon=icons.EMOJI_EMOTIONS, text_align='center')
    en4 = Row([
                        ElevatedButton(text="Submit" ,bgcolor=colors.GREEN_ACCENT_700, adaptive=True ,icon=icons.SAFETY_CHECK  , on_click=show  )


                    ],alignment=MainAxisAlignment.CENTER)
    en5 = Column([ ft.Text(""),])
    en6 = Row([
                        TextButton('@pan998da'  ,icon=icons.TELEGRAM, on_click=telegram ),
                        TextButton('WhatsApp: +16157459609'  ,icon=icons.WIFI_CALLING_ROUNDED,  on_click=whatsapp )

                    ])





    
    #####################################################################

    page.add(en,en1,en2,en3,en4,en5,en6,)
    page.update  
app(main)    