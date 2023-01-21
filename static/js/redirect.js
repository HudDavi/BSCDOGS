const sites = {
    'en': '/en',
    'es': '/es',
    'pt': '/pt',
    'pt-br': '/pt',
};

var lang = navigator.language || navigator.userLanguage;
lang = lang.toLowerCase();
if(typeof sites[lang] !== 'undefined') {
    window.location.replace(sites[lang]);
}
else{
    window.location.replace(sites['en']);
}