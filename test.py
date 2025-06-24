import flet as ft

def main(page: ft.Page):
	contenido=[]

	text_field=ft.TextField(
		value='\n'.join(contenido),
		multiline=True,
		expand=True
		)

	column = ft.Column(
		[text_field],
		scroll = ft.ScrollMode.ALWAYS,
		auto_scroll = True,
		expand=True
		)

	def agregar_contenido(e):
		contenido.append(f'Línea {len(contenido) +1}')
		text_field.value = '\n'.join(contenido)
		page.update()

	boton = ft.ElevatedButton(
		'Agregar Línea',
		on_click=agregar_contenido
		)

	page.add(column, boton)

if __name__ == '__main__':
	ft.app(target=main)
