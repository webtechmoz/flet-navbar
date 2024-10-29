import flet as ft

class Home(ft.View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.bg = BG(page=page, image_path='bg_image.jpg')
        self.button_menu = ButtonMenu(page=page)
        self.nav_bar = NavBar(page=page)
        page.overlay.append(self.button_menu)
        self.route = '/'
        self.padding = ft.padding.all(0)
        self.controls = [
            ft.Stack(
                controls=[
                    self.bg,
                    self.nav_bar
                ]
            )
        ]

        self.button_menu.on_click = self.show_navbar
    
    def show_navbar(self, e: ft.ControlEvent):
        if self.nav_bar.offset.x == -1.50:
            self.nav_bar.offset.x = 0
            self.button_menu.content.name = ft.icons.CLOSE
        
        else:
            self.nav_bar.offset.x = -1.50
            self.button_menu.content.name = ft.icons.MENU
        
        e.page.update()

class BG(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        image_path: str
    ):
        super().__init__()
        self.width = page.width
        self.height = page.height
        self.image = ft.DecorationImage(
            src=image_path,
            fit=ft.ImageFit.COVER
        )

class ButtonMenu(ft.Container):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.width = 45
        self.height = 45
        self.top, self.left = (10, 10)
        self.border_radius = 10
        self.alignment = ft.alignment.center
        self.bgcolor = ft.colors.WHITE
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=self.width,
            color=ft.colors.BLACK,
            offset=ft.Offset(x=1, y=1),
            blur_style=ft.ShadowBlurStyle.OUTER
        )
        self.content = ft.Icon(
            name=ft.icons.MENU,
            color=ft.colors.GREEN,
            size=25
        )

class NavBar(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        title: str = 'Dev Python'
    ):
        super().__init__()
        self.width = page.width * 0.18
        self.height = page.height
        self.bgcolor = ft.colors.with_opacity(0.4, 'black')
        self.offset = ft.Offset(x=-1.5, y=0)
        self.animate_offset = ft.Animation(
            duration=350,
            curve=ft.AnimationCurve.DECELERATE
        )
        self.content = ft.Column(
            controls=[
                ft.Container(
                    padding=ft.padding.only(
                        right=10,
                        top=15
                    ),
                    content=ft.Text(
                        value=title.upper(),
                        size=25,
                        color=ft.colors.WHITE,
                        weight='bold'
                    ),
                    alignment=ft.alignment.center_right
                ),
                ft.Column(
                    controls=[
                        ActionsNavBar(
                            page=page,
                            icon=ft.icons.HOME,
                            text='Home'
                        ) for _ in range(5)
                    ],
                    spacing=1
                )
            ],
            spacing=25
        )


class ActionsNavBar(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        icon: ft.icons,
        text: str
    ):
        super().__init__()
        self.padding = ft.padding.only(
            left=10
        )

        self.height = 45
        self.content = ft.Row(
            controls=[
                ft.Icon(
                    name=icon,
                    color=ft.colors.with_opacity(0.6, 'white'),
                    size=20
                ),
                ft.Text(
                    value=text,
                    size=18,
                    color=ft.colors.with_opacity(0.6, 'white')
                )
            ],
            spacing=4
        )

        self.on_hover = self.hover
    
    def hover(self, e: ft.HoverEvent):
        if e.data == 'true':
            self.bgcolor = ft.colors.BLUE
            self.content.controls[0].color = ft.colors.WHITE
            self.content.controls[1].color = ft.colors.WHITE
            self.content.controls[1].weight = 'bold'
        
        else:
            self.bgcolor = None
            self.content.controls[0].color = ft.colors.with_opacity(0.6, 'white')
            self.content.controls[1].color = ft.colors.with_opacity(0.6, 'white')
            self.content.controls[1].weight = None
        
        e.page.update()