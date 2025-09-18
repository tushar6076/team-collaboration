from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
import random

Builder.load_file("login_content.kv")

class LoginContent(MDBoxLayout):
    pass

class ForgotPasswordContent(MDBoxLayout):
    pass

class HomeScreen(MDScreen):

    login_dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        app = MDApp.get_running_app()
        self.screen_manager = app.screen_manager

    def menu_button(self):
        nav_drawer = self.ids.nav_drawer
        nav_drawer.set_state("toggle")
        if nav_drawer.state == "close":
            nav_drawer.set_state("open")
        else:
            None

    def login_option(self):
        if not self.login_dialog:
            self.login_dialog = MDDialog(
                title = "Please Login to Continue",
                type = "custom",
                radius = [25, 5, 25, 5],
                auto_dismiss = False,
                content_cls = LoginContent(),
                buttons = [
                    MDFlatButton(
                        text = "CANCEL",
                        theme_text_color = "Custom",
                        on_release = self.dismiss_dialog,
                    ),
                    MDFlatButton(
                        text = "LOGIN",
                        theme_text_color = "Custom",
                        on_release = self.login,
                    )
                ]
            )
        self.login_dialog.open()

    def update_text(self, instance, text):
        if instance.hint_text == "Enter your email adress":
            self.receiver = text
        else:
            self.password = text

    def dismiss_dialog(self, instance):
        if self.login_dialog:
            self.login_dialog.dismiss()

    def login(self, instance):
        if not self.ids.password:
            self.ids.password.helper_text = "Invalid Password"
            #incomplete
        else:
            subject = "Login Successful"
            body = '''Hey, This mail is sent from First Year SIH group to 
            inform you that you have successfully logged in <app_name>.\n
            Thankyou for Contacting us.'''
            self.email(subject, body)

    def forgot_password(self):
        self.login_dialog.content_cls.clear_widgets()
        self.login_dialog.content_cls.add_widget(ForgotPasswordContent())
        self.login_dialog.title = "Reset Password"
        self.login_dialog.buttons = [
            MDFlatButton(
                text = "SEND",
                halign = "center",
                pos_hint = {"center_x": 0.5, "center_y": 0.25},
                on_release = self.send_code,
            )
        ]

    def send_code(self, instance):
        try:
            self.code = random.randint(100000, 999999)
            subject = "Password Reset Code"
            body = f'''Hey, This mail is sent from First Year SIH group to 
            inform you that your code to reset your password is: {self.code}\n
            Please click on the link below to for more details.\n
            <link>\n
            Thankyou for Contacting us.'''
            self.email(subject, body)
            self.login_dialog.clear_widgets()
            self.login_dialog.add_widget(
                MDLabel(
                    text = "A code has been sent to your registered email adress."
                    "Please enter the code below to reset your password.",
                ),
                MDTextField(
                    id = "code",
                    hint_text = "Enter the code",
                    icon_right = "lock",
                ),
                MDLabel(
                    text = "[ref=https://kivymd.readthedocs.io/en/latest/][color=0000ff][u]forgot password?[/u][/color][/ref].",
                    markup = True,
                    on_ref_press = self.resend_code,
                ),
            )
            self.login_dialog.buttons = [
                MDFlatButton(
                    text = "CANCEL",
                    theme_text_color = "Custom",
                    on_release = self.dismiss_dialog,
                ),
                MDFlatButton(
                    text = "VERIFY",
                    theme_text_color = "Custom",
                    on_release = self.verify_code,
                )
            ]
        except Exception as e:
            print(e)

    def resend_code(self, instance):
        self.send_code(instance)

    def verify_code(self, instance):
        if self.code == int(self.login_dialog.ids.code.text):
            self.login_dialog.clear_widgets()
            self.login_dialog.title = "Set New Password"
            self.login_dialog.add_widget(
                MDTextField(
                    id = "new_password",
                    hint_text = "Enter new password",
                    icon_right = "lock",
                    password = True,
                ),
                MDTextField(
                    id = "confirm_password",
                    hint_text = "Confirm new password",
                    icon_right = "lock",
                    password = True,
                ),
            )
            self.login_dialog.buttons = [
                MDFlatButton(
                    text = "CANCEL",
                    theme_text_color = "Custom",
                    on_release = self.dismiss_dialog,
                ),
                MDFlatButton(
                    text = "SET PASSWORD",
                    theme_text_color = "Custom",
                    on_release = self.set_new_password,
                )
            ]
        else:
            self.login_dialog.ids.code.text = ""
            self.login_dialog.ids.code.hint_text = "Please Enter Valid Code"
            self.login_dialog.ids.code.helper_text = "Invalid Code"
            self.login_dialog.ids.code.focus = True

    def set_new_password(self, instance):
        if self.login_dialog.ids.new_password.text == self.login_dialog.ids.confirm_password.text:
            self.login_dialog.clear_widets()
            self.login_dialog.add_widget(
                MDLabel(
                    text = "Your password has been successfully reset.",
                    halign = "center",
                    pos_hint = {"center_x": 0.5, "center_y": 0.7},
                    theme_text_color = "Secondary",
                ),
                MDFlatButton(
                    text = "Okay",
                    hilign = "center",
                    pos_hint = {"center_x": 0.5, "center_y": 0.25},
                    on_release = self.dismiss_dialog,
                ),
            )
            self.email(
                subject = "Password Reset Successful",
                body = '''Hey, This mail is sent from First Year SIH group to 
                inform you that your password has been successfully reset.\n
                Thankyou for Contacting us.''' )
        else:
            self.login_dialog.ids.confirm_password.text = ""
            self.login_dialog.ids.confirm_password.hint_text = "Please enter the same password"
            self.login_dialog.ids.confirm_password.helper_text = "Password did not match"
            self.login_dialog.ids.confirm_password.focus = True

    def email(self, subject, body):
        try:
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            sender_address = 'tushardewangan7759@gmail.com'
            sender_pass = 'djjntifkeancgyjb'
            receiver_adress = self.receiver

            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_adress
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(sender_address, sender_pass)

            text = message.as_string()
            session.sendmail(sender_address, receiver_adress, text)
            session.quit()
            self.login_dialog.clear_widets()
            self.login_dialog.add_widget(
                MDLabel(
                    text = "Successfully Logged In.....",
                    halign = "center",
                    pos_hint = {"center_x": 0.5, "center_y": 0.7},
                    theme_text_color = "Secondary",
                ),
                MDFlatButton(
                    text = "Okay",
                    hilign = "center",
                    pos_hint = {"center_x": 0.5, "center_y": 0.25},
                    on_release = self.dismiss_dialog,
                ),
            )


        except smtplib.SMTPRecipientsRefused:
            self.ids.email.text=""