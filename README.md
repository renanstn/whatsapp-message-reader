# Whatsapp Message Reader

O intuito deste projeto é criar uma extensão do Chrome que fica monitorando as mensagens recebidas pelo whatsapp, e, ao detectar mensagens novas, ele as **lê** para você, para que assim você não precise se distrair dando *alt+tab* nas suas abas.

## Checklist de Tarefas

### Principais funcionalidades

- [ ] Monitorar as atividades no whatsapp web
- [ ] Detectar as mensagens novas de um contato específico e capturá-las
- [ ] Detectar as mensagens novas de **todos** os contatos e capturá-las
- [ ] No caso acima, sempre antes de ler a mensagem, ler o nome de quem a enviou
- [ ] Ler a mensagem

### Opcionais

- [ ] Notificar a mensagem em uma *popup* para que o usuário possa aceitar ou não a leitura naquele momento
- [ ] Poder ouvir novamente a mesma mensagem
- [ ] Se houver mídia tocando na máquina, abaixar o volume da mesma antes de executar o áudio

## Desenvolvimento
- Ativando a extensão para desenvolvimento
    - Acesse em seu navegador `chrome://extensions`
    - Ative o Developer Mode
    - Clique em Load Unpacked / Carregar sem compactação
    - Seleciona a pasta src

- Plano:
    - Injetar um script de **scrap** na página do whatsapp web
    - Identificar as mensagens novas e capturá-las (JQuery talvez ajude)
    - Fazer este script se comunicar com o script da extensão
    - Falar a mensagem recebida

## Links úteis:
- Index de APIs: https://developer.chrome.com/extensions/api_index
- Documentação API TTS: https://developer.chrome.com/extensions/tts
- Documentação API Tabs (para comunicação entre abas): https://developer.chrome.com/extensions/tabs
- JQuery na extensão: https://stackoverflow.com/questions/21317476/how-to-use-jquery-in-chrome-extension
- Adicionando scripts nas páginas existentes: https://developer.chrome.com/extensions/content_scripts
