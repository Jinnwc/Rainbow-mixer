import flet as ft

def main(page: ft.Page):
    page.title = "Rainbow Mixer"

    def update_color(e):
        page.bgcolor = f"#{int(r.value):02x}{int(g.value):02x}{int(b.value):02x}"
        page.update()

    color_display = ft.Text("Rainbow Mixer", size=20)
    r = ft.Slider(0, 255, 0, 255, on_change=update_color)
    g = ft.Slider(0, 255, 0, 255, on_change=update_color)
    b = ft.Slider(0, 255, 0, 255, on_change=update_color)

    page.add(color_display, r, g, b)

ft.app(target=main)