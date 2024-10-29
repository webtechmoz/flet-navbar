from view.Home import ft, Home

def main(page: ft.Page):
    page.title = 'Navegation Bar'

    def router(route):
        page.views.clear()

        home = Home(page=page)

        if page.route == '/':
            page.views.append(home)
        
        page.update()
    
    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)