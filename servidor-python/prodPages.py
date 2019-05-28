import os

# Armazenando variáveis do projeto para facilitar alterações
project_name = 'qual_professor'
head = '<head>'
body = '<body>'

# Concatenando o HTML, Css e Javascript da página em 1 único HTML
def getProductionHtml(index, html, css, js):
        index_with_head = index.replace(head, head + '\n<style type="text/css">\n' + 
                        css + '\n</style>\n' + '<script type="text/javascript">\n' + 
                        js + '\n</script>\n')
        return index_with_head.replace(body, body + html)

# Carrega a pasta de produção dist
def loadDist(pages_list):
    for page in pages_list:  
        # Pegando o index.html
        h = open(project_name+'/index.html', 'r')
        index_html = h.read()
        h.close()

        # Pegando o HTML da página
        h = open(project_name+'/pages/'+ page +'/'+ page +'.html', 'r')
        page_html = h.read()
        h.close()

        # Pegando o javascript da página
        h = open(project_name+'/pages/'+ page +'/'+ page +'.js', 'r')
        page_js = h.read()
        h.close()

        # Pegando o css da página
        h = open(project_name+'/pages/'+ page +'/'+ page +'.css', 'r')
        page_css = h.read()
        h.close()

        # Se o caminho não existir, ele é criado
        if not os.path.exists(project_name+'/dist'):
            os.makedirs(project_name+'/dist')

        # Escrevendo em 1 único arquivo que ficar na pasta gerado de produção (dist)
        h = open(project_name+'/dist/'+ page +'.html', 'w+')
        page_html = getProductionHtml(index_html, page_html, page_css, page_js)
        h.write(page_html)
        h.close()

# Retorna o arquivo dentro da página de produção no formato utf-8
def getBytesDistHtml(page):
        loadDist([page])
        h = open(project_name+'/dist/' + page + '.html', 'r')
        dist_page = h.read()
        h.close()
        header = ('HTTP/1.0 200 OK\r\n' +
                'Content-Type: text/html; charset=ISO-8859-1\r\n' +
                'Access-Control-Allow-Origin: *\r\n' +
                'Content-Length: ' + str(len(dist_page)) + '\r\n\r\n' +
                (dist_page))
        return bytes(header, 'utf-8')
