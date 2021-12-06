import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

#criar as janelas e estilos 

def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('nome')],
        [sg.Input()],
        [sg.Button('continuar')]    
    ]
    return sg.Window('login',layout=layout,finalize=True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [

        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('pizza',key='pizza')
        ,sg.Checkbox('coxinha',key='coxinha')],
        [sg.Button('voltar'),sg.Button('fazer pedido')]
       
    ]
    return sg.Window('Montar pedido',layout=layout,finalize=True)


# criar as janelas iniciais

janela1,janela2 = janela_login(),None

#criar um loop de leitura de eventos

while True:
    window,event,values = sg.read_all_windows()
    #quando fechar
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    #ir pra proxima janela
    if window == janela1 and event == 'continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'fazer pedido':
        if values['pizza'] == True and values['coxinha'] == True:
             sg.popup('Foi solicitado uma pizza e uma coxinha')
        elif values['pizza'] == True:
             sg.popup('Foi solicitado uma pizza')    
        elif values['coxinha'] == True:
             sg.popup('Foi solicitado uma coxinha')



