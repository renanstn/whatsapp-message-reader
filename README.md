# Whatsapp Message Reader

O intuito deste projeto é criar um "bot" que fica monitorando as mensagens recebinas pelo whatsapp, e, ao detectar mensagens novas, ele as **lê** para você, para que assim você não precise se distrair dando *alt+tab* nas suas abas.

## Checklist de Tarefas

### Principais funcionalidades

- [x] Monitorar as atividades no whatsapp web
- [x] Detectar as mensagens novas e capturá-las
- [ ] Ler a mensagem (usar a lib gtts)

### Opcionais

- [ ] Notificar a mensagem em uma *popup* para que o usuário possa aceitar ou não a leitura naquele momento
- [ ] Poder ouvir novamente a mesma mensagem
- [ ] Se houver mídia tocando na máquina, abaixar o volume da mesma antes de executar o áudio
- [ ] Persistir a sessão anterior, para que o usuário não precise ler o QR code toda vez que inicializar o programa

## Desenvolvimento
- Rodar o script que baixa o geckodriver
    - `sh get-geckodriver.sh`
- Instalar dependências e iniciar o ambiente virtual
    - `pipenv install`
    - `pipenv shell`
