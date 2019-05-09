import os

project_name = 'qual_professor'
head = '<head>'
body = '<body>'
def getProductionHtml(index, html, js, css):
        index_with_head = index.replace(head, head + '\n<style type="text/css">\n' + 
                        js + '\n</style>\n' + '<script type="text/javascript">\n' + 
                        css + '\n</script>\n')
        return index_with_head.replace(body, body + html)

def loadDist(pages_list):
    for page in pages_list:  
        # Getting index
        h = open(project_name+'/index.html', 'r')
        index_html = h.read()
        h.close()

        # Getting pages
        h = open(project_name+'/pages/'+ page +'/'+ page +'.html', 'r')
        page_html = h.read()
        h.close()

        # Getting javascript files
        h = open(project_name+'/pages/'+ page +'/'+ page +'.js', 'r')
        page_js = h.read()
        h.close()

        # Getting css files
        h = open(project_name+'/pages/'+ page +'/'+ page +'.css', 'r')
        page_css = h.read()
        h.close()

        # If the path doesn't exists, the build path is created
        if not os.path.exists(project_name+'/dist'):
            os.makedirs(project_name+'/dist')

        h = open(project_name+'/dist/'+ page +'.html', 'w+')
        page_html = getProductionHtml(index_html, page_html, page_css, page_js)
        h.write(page_html)
        h.close()


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


def getIcon(icon):
        return bytes(('HTTP/1.0 200 OK\r\n' +
                'Content-Type: image/jpeg; charset=ISO-8859-1\r\n' +
                'Access-Control-Allow-Origin: *\r\n' +
                'Content-Length: ' + str(len(icon)) + '\r\n\r\n' +
                (icon) + ' charset=ISO-8859-1'), 'utf-8')