import flet as ft

def main(page: ft.Page):
    page.title = "Flet 카운터 예제"

    counter = ft.Text("0")

    def increment(e):
        counter.value = str(int(counter.value) + 1)
        page.update()

    page.add(
        counter,
        ft.ElevatedButton("증가", on_click=increment)
    )

ft.app(target=main)