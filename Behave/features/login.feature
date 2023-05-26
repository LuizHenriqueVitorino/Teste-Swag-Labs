Funcionalidade: Login no sistema

    Esquema do Cenário: Logar no sistema <situacao>
        Dado que eu esteja na página de Login
        Quando eu preencher o campo usuário com <usuario>
        E preencher o campo senha com <senha>
        E Clicar no botão de Login
        Então <resultado>

    Exemplos:
    | situacao              | usuario           | senha         | resultado                         |
    | com usuario valido    | standard_user     | secret_sauce  | devo logar no sistema             |
    | com usuario bloqueado | locked_out_user   | secret_sauce  | devo receber uma mensagem de erro |