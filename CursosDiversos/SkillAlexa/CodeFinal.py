class SantaPortalIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NoticiaSantaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        def ler_elementos_com_classe(url, classe):
            try:
                # Faz a requisição HTTP para obter o conteúdo da página
                response = requests.get(url)
                
                # Verifica se a requisição foi bem sucedida
                if response.status_code == 200:
                    # Obtém o conteúdo HTML da página
                    html_content = response.text
                    
                    # Cria um objeto BeautifulSoup para analisar o HTML
                    soup = BeautifulSoup(html_content, 'html.parser')
                    
                    # Encontra todos os elementos com a classe especificada
                    elementos_com_classe = soup.find_all(class_=classe)
                    
                    # Inicializa uma lista para armazenar o conteúdo dos elementos encontrados
                    conteudo_elementos = []
                    
                    # Itera sobre os elementos encontrados
                    for elemento in elementos_com_classe:
                        # Extrai o conteúdo do elemento e adiciona à lista
                        conteudo_elementos.append(elemento.text.strip())
                    
                    return conteudo_elementos
                else:
                    #print(f"Erro ao fazer a requisição: {response.status_code}")
                    speak_output = 'Erro ao fazer a requisição'
                    #print(speak_output)
                    return None
            except requests.exceptions.RequestException as e:
                #print(f"Erro na requisição: {e}")
                speak_output = 'Erro ao fazer a requisição2'
                #print(speak_output)
                return None
        # URL da página que você deseja ler os elementos com a classe 'text'
        url = 'https://santaportal.com.br/noticias/'
        
        # Classe dos elementos que você deseja ler
        classe_desejada = 'title'
        
        # Chama a função para ler os elementos com a classe 'text' na página
        elementos_com_classe_text = ler_elementos_com_classe(url, classe_desejada)
        
        if elementos_com_classe_text:
            for elemento in elementos_com_classe_text:
                conteudo = (conteudo + elemento + '.')
            frase = conteudo
            # Dividir a frase em sentenças com base nos pontos
            sentencas = frase.split('.')
            # Remover espaços em branco extras antes e depois de cada sentença
            sentencas = [sentenca.strip() for sentenca in sentencas if sentenca.strip()]
            # Exibir as strings entre os pontos
            for sentenca in sentencas:
                if sentenca != 'Páginas' and sentenca != 'Categorias' and sentenca != 'Multimídia' and sentenca != 'Blogs':
                    final = (final + sentenca + '\n')
                    #speak_output = final
                    #print(speak_output)
            #print(speak_output)
            speak_output = final
        
        else:
            #print("Falha ao ler os elementos com a classe 'title' na página.")
            speak_output = 'Falha ao ler os elementos com a classe "title" na página.'
            #print(speak_output)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

