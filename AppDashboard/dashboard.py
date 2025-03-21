import dash
from dash import Dash, dcc, html, Input, Output, State
from django_plotly_dash import DjangoDash
from django.contrib.staticfiles.storage import staticfiles_storage



# Instância do Dash
app = DjangoDash('DashboardApp', external_stylesheets=[
    staticfiles_storage.url('AppDashboard/assets/styledashboard.css'),
])

app.title = 'Login | ManageFlow'

#======================================== Layout principal =================================================
app.layout = html.Div(id='body', children=[
html.Div(id='main', children=[

    html.Div(id='painel-esquerdo', className='painel-visivel', children=[

        html.P(['Manage', html.Br(), 'Flow'], id='title-manageflow'),
        html.Hr(className='linha-divisoria'),

        html.Button(children=['Atendimento'], className='btn-menu-esquerdo', id='btn-atendimento'),
        html.Button(children=['Triagem'], className='btn-menu-esquerdo', id='btn-triagem'),
        html.Button(children=['Monitoramento'], className='btn-menu-esquerdo', id='btn-monitoramento'),
        html.Button(children=['Conf Triagem'], className='btn-menu-esquerdo', id='btn-conf-triagem'),

        html.H3(['ADMINISTRAÇÃO'], id='title-administracao'),
        html.Button(children=['Relatórios'], className='btn-menu-esquerdo-adm', id='btn-relatorios'),
        html.Button(children=['Configurações'], className='btn-menu-esquerdo-adm', id='btn-configuracoes'),
     
    ]),

    html.Div(id='body2', children=[

        html.Div(id='cabecalho', children=[
            html.Div(id='area-btn-recolher', children=[
                html.Button('<', id='btn-recolher')
            ]),

           html.Div(id='area-btn-select-unidade', children=[
                html.Button('Selecionar Unidade', id='btn-select-unidade'),
            ]),

            html.Div(id='area-cabecalho-controle-usuario', children=[
                html.Img(src='assets/img/engrenagem.png', style={'margin-right': '10px'}),
                html.Img(src='assets/img/avatar.png'),
            ])
        ]),
        
        html.Div(id='area-de-trabalho', children=[]),

        html.Div(id='rodape', children=[
            html.H5('Todos os direitos reservados | 2024', id='direitos')
        ])
    ]),
])])

    

if __name__ == '__main__':
    app.run_server(debug=True, port="")
