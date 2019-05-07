/**
 * @description Faz uma request HTTP
 * @param {string} url rota
 * @param {object} params parâmetros querystring
 */
function httpGetAsync(url, params) {
    let finalUrl = url;
    if(params) {
        finalUrl += '?';
        Object.keys(params).forEach((key, index) => {
            finalUrl += `${key}=${params[key]}`;
            if (index + 1 !== params.length)
                finalUrl += '&';
        })
    }

    const xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", finalUrl, true); // true for asynchronous
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

httpGetAsync('localhost/api/user', { a: 'mandei1', b: 'mandei2' })