def ler_html():
    arq = open('teste.html','r')
    conteudo = arq.read()
    arq.close()
    l = []
    tag = ['<html>','<head>','<title>','<body>','<p>','<img','<a']
    arquivo = open('relatorio.txt', 'a')
    for i in tag:
        a = conteudo.count(i)
        l.append(a)
        arquivo.write(str(i) + ' - ' + str(a) + '\n')
    arquivo.close()
    return True

def linhas():
    arq = open('teste.html','r')
    conteudo = arq.read()
    conteudo = conteudo.replace(">","\n")
    arq.close()
    tag = ['<html','<head','<title','<body','<p','<img','<a']
    cont = 0
    lf = []
    conteudo2 = conteudo.split("\n")
    for a in conteudo2:
        for i in tag:
            if i in a:
                cont+=1
                lf.append(i)
                lf.append("- linha:")
                lf.append(cont)
    return lf
print(linhas())