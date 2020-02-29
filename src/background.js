chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
        console.log("The color is green.");
    });
});

// Comando que fala
chrome.tts.speak('Boa noite!', {
    'lang': 'pt-BR'
});

// Comando que fala, respeitando a fila
chrome.tts.speak('Bátima Bernardes!', {
    'lang': 'pt-BR',
    'enqueue': true
});

const content = document.getElementsByTagName('html')[0].innerHTML;

console.log(content); // Funciona, mas ele pega o html do manifest.json
