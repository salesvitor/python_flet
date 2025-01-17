import flet as ft


def main(pagina):

    pagina.add(ft.Text(""))


    pagina.appbar = ft.AppBar(
    title=ft.Text("Check List do Roia"),
    center_title=True,
    bgcolor=ft.Colors.GREEN_300,
    automatically_imply_leading=False,)


    #Lista de itens
    pagina.add(ft.Text("Moto"))
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Verificar fluido do radiador")]))
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Verificar calibragem dos pneus")]))    
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Verificar nível do óleo")]))
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Abastecer a moto")]))
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Verificar folga da corrente")]))
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Lubrificar a corrente")]))
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Verificar condição do filtro de ar")]))
    pagina.add(ft.Text("Suprimentos"))
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Água")]))
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Lanche")]))
    pagina.add(ft.Row([ft.Checkbox(), ft.Text("Ferramentas")]))

    pagina.update()



ft.app(target=main, view=ft.WEB_BROWSER)