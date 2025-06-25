import flet as ft
from modules.data_management import load_data
import modules.generator as gen
import random
import os
#import modules.caos as cao

from statistics import mean

total=[]

def main (page: ft.Page):
    page.title='Oráculo D&D'
    page.vertical_aligment=ft.MainAxisAlignment.START
    page.update()

    #The directory path (relative to main.py)
    path_data = os.path.join(os.path.dirname(__file__), 'data')
    datos = load_data(path_data) #Load the data when de app is iniciated

    contenido=[] #Empty list where all lines of the textfield will be included

    #Minus function
    def minus_click(e, data):
        #data is a variable to control which text_field is selected
        if data == 0:
            txt_dicenumber.value = str(int(txt_dicenumber.value)-1)
            if txt_dicenumber.value < str(1):
                txt_dicenumber.value = str(1)
        elif data == 1:
            txt_bonus.value = str(int(txt_bonus.value)-1)
        page.update()

    def plus_click (e, data):
        #data is a variable to control which text_field is selected
        if data == 0:
            txt_dicenumber.value = str(int(txt_dicenumber.value) + 1)
        elif data == 1:
            txt_bonus.value = str(int(txt_bonus.value) + 1)
        page.update()

    #Radiogroup selecction, when is active d20 Aventage and disavantage es active
    def radiogroup_selection(e,dice):
        dado = int(dice)
        if dado == 20:
            radioavendisaven.disabled=False
            if int(radioavendisaven.value) == 0:
                txt_dicenumber.disabled=False
            else:
                txt_dicenumber.disabled=True
        else:
            radioavendisaven.disabled=True
            txt_dicenumber.disabled=False
        page.update()


    #Update textfield and autoscroll function
    def add_text(data):
        contenido.append(data)
        txt_salida.value = '\n'.join(contenido)
        page.update()

    def add_texto(e,data):
        contenido.append(data)
        txt_salida.value = '\n'.join(contenido)
        txt_entrada.value = ' '
        page.update()

    #Change the label of the txt_entrada TextField
    def change_scene(e,data):
        escena = f'{data}'
        txt_entrada.label = escena
        escena = '*'+escena
        add_text(escena)
        txt_entrada.value=' '
        txt_entrada.update()
        

    def rolldice (e):
        ndados = int(txt_dicenumber.value)
        dado = int(radiodados.value)
        bonus = int(txt_bonus.value)
        global total
        total=[]
        if dado == 20 and int(radioavendisaven.value) != 0 and ndados == 1:
            for i in range(2):
                j = random.randint(1,dado)
                total.append(j)
            if int(radioavendisaven.value) == 1:
                salida = f'Tirada con Ventaja: {total}'
                total.remove(min(total))
                add_text(salida)
            if int(radioavendisaven.value) == -1:
                salida = f'Tirada con Desventaja: {total}'
                total.remove(max(total))
                add_text(salida)
        else:
            for i in range(ndados):
                j = random.randint(1, dado)
                total.append(j)
        salida = f'Tirada ({ndados}d{dado}): {total}'
        add_text(salida)
        #txt_salida.value = txt_salida.value + salida
        if chbox_media.value:
            media = str(round(mean(total),1))
            media = f'Media: {media}'
            add_text(media)
            #txt_salida.value = txt_salida.value + f'Media: {media:.1f}\n'
        if chbox_suma.value:
            suma = str(sum(total))
            suma = f'Suma: {suma}'
            add_text(suma)
            #txt_salida.value = txt_salida.value + f'Suma: {suma}\n'
        if chbox_max.value:
            maximo = str(max(total))
            maximo = f'Valor máximo: {maximo}'
            add_text(maximo)
            #txt_salida.value = txt_salida.value + f'Valor máximo: {maximo}\n'
        if chbox_min.value:
            minimo = str(min(total))
            minimo = f'Valor mínimo: {minimo}'
            add_text(minimo)
            #txt_salida.value = txt_salida.value + f'Valor mínimo: {minimo}\n'
        if chbox_total.value:
            total_bonus = str(sum(total) + bonus)
            total_bonus = f'Bonus: {bonus}\nTotal: {total_bonus}'
            add_text(total_bonus)
            #txt_salida.value =  txt_salida.value + f'Total: {total_bonus}\n'
        salto='\n'
        add_text(salto)
        page.update()

    def aplicar (e):
        global total
        ndados = int(txt_dicenumber.value)
        dado = int(radiodados.value)
        bonus = int(txt_bonus.value)
        salida = f'Tirada ({ndados}d{dado}): {total}'
        add_text(salida)
        if chbox_media.value:
            media = str(round(mean(total),1))
            media = f'Media: {media}'
            add_text(media)
            #txt_salida.value = txt_salida.value + f'Media: {media:.1f}\n'
        if chbox_suma.value:
            suma = str(sum(total))
            suma = f'Suma: {suma}'
            add_text(suma)
            #txt_salida.value = txt_salida.value + f'Suma: {suma}\n'
        if chbox_max.value:
            maximo = str(max(total))
            maximo = f'Valor máximo: {maximo}'
            add_text(maximo)
            #txt_salida.value = txt_salida.value + f'Valor máximo: {maximo}\n'
        if chbox_min.value:
            minimo = str(min(total))
            minimo = f'Valor mínimo: {minimo}'
            add_text(minimo)
            #txt_salida.value = txt_salida.value + f'Valor mínimo: {minimo}\n'
        if chbox_total.value:
            total_bonus = str(sum(total) + bonus)
            total_bonus = f'Bonus: {bonus}\nTotal: {total_bonus}'
            add_text(total_bonus)
            #txt_salida.value =  txt_salida.value + f'Total: {total_bonus}\n'
        salto='\n'
        add_text(salto)
        '''if chbox_media.value:
            media = mean(total)
            txt_salida.value = f'Media: {media:.1f}\n' + txt_salida.value
        if chbox_suma.value:
            suma = str(sum(total))
            txt_salida.value = f'Suma: {suma}\n' + txt_salida.value
        if chbox_max.value:
            maximo = str(max(total))
            txt_salida.value = f'Valor máximo: {maximo}\n' + txt_salida.value
        if chbox_min.value:
            minimo = str(min(total))
            txt_salida.value = f'Valor mínimo: {minimo}\n' + txt_salida.value
        if chbox_total.value:
            total_bonus = str(sum(total) + int(txt_bonus.value))
            txt_salida.value = f'Total: {total_bonus}\n' + txt_salida.value'''
        page.update()


    #Function which preditcs what happen in next acction
    def oraculo(e):
        tirada = random.randint(1, 20)
        match tirada:
            case 1:
                text = f'El oráculo dice ({tirada}): Fracaso absoluto\n'
                add_text(text)
            case 2 | 3 | 4 | 5:
                text = f'El oráculo dice ({tirada}): No\n'
                add_text(text)
            case 6 | 7 | 8 | 9:
                text = f'El oráculo dice ({tirada}): No, pero... algo pasa\n'
                add_text(text)
            case 10:
                text = f'El oráculo dice ({tirada}): Estoy indeciso\n'
                add_text(text)
            case 11 | 12 | 13 | 14 | 15:
                text = f'El oráculo dice ({tirada}): Sí, pero... algo pasa\n'
                add_text(text)
            case 16 | 17 | 18 | 19:
                text = f'El oráculo dice ({tirada}): Sí\n'
                add_text(text)
            case 20:
                text = f'El oráculo dice ({tirada}): Éxito absoluto\n'
                add_text(text)
        page.update()

    def reset(e):
        radiodados.value=4
        txt_dicenumber.value=str(1)
        txt_bonus.value=str(0)
        chbox_max.value=False
        chbox_min.value=False
        chbox_suma.value=False
        chbox_media.value=False
        chbox_total.value=True
        radioavendisaven.disabled=True
        page.update()

    def generador_ponderado(e, dictio):
        generator_instance = gen.Generator([],[],[],[],[],[])
        valor = generator_instance.elegir_clave_ponderada(dictio)
        text = f'Encuentro: {valor}\n'
        add_text(text)
        page.update()

    def generador (e, lista):
        generator_instance = gen.Generator([],[],[],[],[],[])
        valor = generator_instance.elegir_lista(lista)
        text = f'{valor}\n'
        add_text(text)

    def generar_npc(e):
        generator_instance = gen.Generator([],[],[],[],[],[])
        valor = generator_instance.generar_npc()
        text = f'{valor}\n'
        add_text(text)
        page.update()

    def generar_taberna(e):
        generator_instance = gen.Generator([],[],[],[],[],[])
        valor = generator_instance.taberna()
        text = f'{valor}\n'
        add_text(text)
        page.update()

    radiodados= ft.RadioGroup(
        content=ft.Row(
            [
            ft.Radio(value=4, label='1d4', active_color=ft.colors.RED),
            ft.Radio(value=6, label='1d6', active_color=ft.colors.ORANGE),
            ft.Radio(value=8, label='1d8', active_color=ft.colors.YELLOW,),
            ft.Radio(value=10, label='1d10', active_color=ft.colors.GREEN),
            ft.Radio(value=12, label='1d12', active_color=ft.colors.PURPLE),
            ft.Radio(value=20, label='1d20', active_color=ft.colors.INDIGO, ),
            ft.Radio(value=100, label='1d100', active_color=ft.colors.BLUE)
            ]
            ),
        value=4,
        on_change = lambda e: radiogroup_selection(e,radiodados.value),
        )

    #Spinbox for the dice number
    txt_dicenumber = ft.TextField(value='1', label = 'Nº dados', text_align='center', width=100, filled=True)

    #Button for rolling the dice

    boton_roll = ft.FilledButton (text='Lanzar', on_click=rolldice)

    page.add(
        ft.Row([
        radiodados,
        ft.IconButton(ft.icons.REMOVE, on_click = lambda e: minus_click(e,0)), 
        txt_dicenumber,
        ft.IconButton(ft.icons.ADD, on_click = lambda e: plus_click(e,0)),
        boton_roll
        ],
        alignment=ft.MainAxisAlignment.START
        )
        )
    
    #Checkbox for operation with de dice rolled
    chbox_suma = ft.Checkbox (label='Suma', value=False)
    chbox_media = ft.Checkbox (label='Media', value=False)
    chbox_max = ft.Checkbox (label='Valor Máximo', value=False)
    chbox_min = ft.Checkbox (label='Valor Mínimo', value=False)
    chbox_total = ft.Checkbox(label='Total', value=True)

    #Bonuses to apply to the Rolled button
    txt_bonus = ft.TextField(value='0', label='Bonus', text_align='center', width=100, filled=True)

    #Button for reset
    boton_reset = ft.FilledButton(text='RESET', on_click=reset)

    #Button for apply the checkboxes
    boton_aplicar=ft.FilledButton(text='Aplicar', on_click=aplicar)

    page.add(
        ft.Row(
            [chbox_total,
            chbox_suma,
            chbox_media,
            chbox_max,
            chbox_min,
            boton_aplicar,
            ft.IconButton(ft.icons.REMOVE, on_click = lambda e: minus_click(e,1)), 
            txt_bonus,
            ft.IconButton(ft.icons.ADD, on_click = lambda e: plus_click(e,1)),
            boton_reset
            ]
            )
        )

    #Oracle button which predicts the actions
    boton_oraculo = ft.FilledButton(text='Oráculo', on_click = oraculo)

    #Aventage or disaventage checkboxes, only are active when d20 is selected
    #chbox_aven = ft.Checkbox(label="Ventaja", value=False, disabled= True)
    #chbox_disaven = ft.Checkbox (label = "Desventaja", value = False, disabled= True)
    radioavendisaven= ft.RadioGroup(
        content=ft.Row(
            [
            ft.Radio(value=1, label='Ventaja', active_color=ft.colors.GREEN),
            ft.Radio(value=-1, label='Desventaja', active_color=ft.colors.RED),
            ft.Radio(value=0, label='Normal', )
            ]
            ),
        value=0,
        disabled = True,
        on_change = lambda e: radiogroup_selection(e,20),
        )

    page.add(
        ft.Row([boton_oraculo, radioavendisaven])
        )

    boton_airelibre = ft.FilledButton(text='Encuentro al aire libre',
        on_click = lambda e: generador_ponderado(e, dict(zip(gen.airelibre, gen.pesos_airelibre))))
    boton_mazmorra = ft.FilledButton(text='Encuentro en la mazmorra',
        on_click = lambda e: generador_ponderado(e, dict(zip(gen.mazmorra, gen.pesos_mazmorra))))
    boton_urbano = ft.FilledButton(text='Encuentro en la ciudad',
        on_click = lambda e: generador_ponderado(e, dict(zip(gen.urbanos, gen.pesos_urbanos))))
    boton_mision = ft.FilledButton(text='Generar misión',
        on_click = lambda e: generador(e, gen.misiones))
    boton_origenmision = ft.FilledButton(text='Origen mision',
        on_click = lambda e: generador(e, gen.origenmision))
    boton_accion = ft.FilledButton(text='Acción',
        on_click = lambda e: generador(e,gen.acciones))
    boton_npc = ft.FilledButton(text='NPC',
        on_click = generar_npc)
    boton_taberna = ft.FilledButton(text ='Taberna',
        on_click = generar_taberna)

    page.add(
        ft.Row([
            boton_airelibre,
            boton_mazmorra,
            boton_urbano,
            boton_mision,
            boton_origenmision,
            boton_npc,
            boton_accion,
            boton_taberna
            ])
        )

    txt_salida=ft.TextField(multiline=True, min_lines=10, expand=True, 
                            read_only=True, filled=True, value='\n'.join(contenido))

    
    #TextField where some text is written and after added to txt_salida
    txt_entrada = ft.TextField(multiline=True, 
        min_lines=5,
        max_lines=5, 
        expand=True, 
        label='Describe la escena. Escena nº: ...')

    boton_enviar = ft.FilledButton(text='Enviar', on_click = lambda e: add_texto(e, txt_entrada.value))
    bonton_escena = ft.FilledButton(text='Nueva Escena', on_click = lambda e: change_scene(e,txt_entrada.value))

    #Create the container with autoscroll
    column = ft.Column(
        [txt_salida],
        scroll = ft.ScrollMode.ALWAYS,
        auto_scroll = True,
        expand = True
        )
    contenedor1= ft.Container(content=column)
    contenedor2= ft.Container(content=ft.Row([txt_entrada,ft.Column([boton_enviar, bonton_escena])]))
    page.add( 
        column,
        ft.Row([txt_entrada,ft.Column([boton_enviar, bonton_escena])])
        )

    text = f"¡Bienvenido al Oráculo de D&D!\n"
    add_text(text)

    page.update()
    if datos: # only add this if there is data.
        text=f"Listo\n"
        add_text(text)
    else:
        text=f"No data loaded.  Check the 'data' directory.\n"
        add_text(text)
    page.update()


if __name__ == '__main__':
    ft.app(target=main) #view=ft.WEB_BROWSER)