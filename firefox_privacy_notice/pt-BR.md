## <span class="privacy-header-policy">Aviso de privacidade do</span> <span class="privacy-header-firefox">Firefox</span>

*Vigência em 28 de setembro de 2017*
{: datetime="2017-09-28" }

## Na Mozilla, acreditamos que a privacidade é fundamental para uma Internet saudável.

É por isso que criamos o Firefox e todos os nossos produtos, a fim de proporcionar a você mais controle sobre as informações que você compartilha on-line e conosco. Nós nos esforçamos para coletar apenas o necessário para melhorar o Firefox para todos.

Nesta nota sobre privacidade, explicamos quais dados o Firefox compartilha e como configurá-lo para compartilhar ainda menos. Também aderimos às práticas descritas na [Política de privacidade](https://www.mozilla.org/privacy/) da Mozilla quanto a como recebemos, lidamos e compartilhamos informações coletadas pelo Firefox.

## Por padrão, o Firefox compartilha dados para:

### Melhorar o desempenho e a estabilidade para usuários em todo o mundo {: #health-report }

* __Dados de interação__: O Firefox envia dados sobre suas interações com ele para nós (como o número de abas e janelas abertas, número de páginas acessadas, número e tipo de extensões do Firefox instaladas e duração da sessão) e sobre os recursos dele oferecidos pela Mozilla ou por nossos parceiros (como interação com os recursos de pesquisa e referências de parceiros de pesquisa).

* __Dados técnicos__: O Firefox nos envia dados sobre a versão e idioma instalado, configuração do sistema operacional e do hardware do dispositivo, memória, informações básicas sobre travamentos e erros, resultado de processos automáticos, como atualizações, navegação segura e ativação. Quando o Firefox nos envia dados, seu endereço IP é temporariamente coletado como parte dos nossos registros de servidor.

Leia a documentação de telemetria para [Desktop](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/index.html), [Android](https://firefox-source-docs.mozilla.org/mobile/android/fennec/index.html) ou [iOS](https://github.com/mozilla-mobile/firefox-ios/wiki/Telemetry) ou saiba como [cancelar](https://support.mozilla.org/kb/send-performance-data-improve-firefox) essa coleta de dados.
{: #telemetry }

### Definir um mecanismo de pesquisa padrão {: #defaultsearch }

* __Dados de localização__: Quando você usa o Firefox pela primeira vez, ele usa seu endereço IP para definir o mecanismo de pesquisa padrão com base no seu país.  [Saiba mais](https://support.mozilla.org/kb/change-your-default-search-settings-firefox).

### Sugerir conteúdo relevante 

O Firefox exibe conteúdo, como "Snippets" (mensagens curtas da Mozilla) e Sites preferidos (sugeridos pela Mozilla para usuários novos do Firefox).

* __Dados de localização__: O Firefox usa seu endereço IP para sugerir conteúdo relevante com base no seu país.

* __Dados técnicos e de interação__: O Firefox nos envia dados como posição, tamanho e posicionamento do conteúdo sugerido por nós, além de dados básicos relacionados à sua interação com o conteúdo sugerido do Firefox. Isso inclui o número de vezes que o conteúdo sugerido é exibido ou clicado.

* __Dados de páginas da Internet para snippets__: Ao clicar no link de um snippet, é possível que recebamos dados sobre o link aberto. Essas informações não são associadas a nenhuma outra informação pessoal sua. [Saiba mais](https://abouthome-snippets-service.readthedocs.io/en/latest/data_collection.html).
{: #snippets }

### Melhorar a segurança dos usuários em todo o mundo {: #security }

* __Dados técnicos para atualizações__: As versões para computador do Firefox são periodicamente verificadas em busca de atualizações do navegador conectando-se aos servidores da Mozilla. Sua versão do Firefox, idioma e sistema operacional do dispositivo são usados para aplicar as atualizações corretas. As versões móveis do Firefox poderão se conectar a outro serviço se você usou para baixar e instalar o navegador. [Saiba mais](https://support.mozilla.org/kb/how-stop-firefox-automatically-making-connections#w_auto-update-checking).
{: #auto-updates }

* __Dados técnicos para lista de bloqueio de extensões__: O Firefox para Desktop e Android se conectam periodicamente à Mozilla para proteger você e outras pessoas contra extensões maliciosas. A versão e o idioma do seu Firefox, o sistema operacional do seu dispositivo e a lista de extensões instaladas são necessários para aplicar e atualizar a lista de bloqueio de extensões. [Saiba mais](https://support.mozilla.org/kb/how-stop-firefox-making-automatic-connections). 

* __Dados técnicos e da página da Internet para navegação segura do Google__: Para ajudar você a se proteger contra downloads maliciosos, o Firefox envia informações básicas sobre downloads não reconhecidos para o serviço de navegação segura do Google, inclusive o nome do arquivo e a URL do download.

[Saiba mais](https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work) ou leia a [Política de Privacidade do Google](https://www.google.com/policies/privacy/). O cancelamento impede o Firefox de avisar você quanto à sites ou arquivos baixados possivelmente ilegítimos ou maliciosos.

* __Dados técnicos e da página da Internet para autoridades de certificação__: Ao acessar um site seguro (normalmente identificado com uma URL contendo "HTTPS"), o Firefox valida o certificado do [site](https://support.mozilla.org/kb/secure-website-certificate). Para isso, o Firefox pode enviar determinadas informações sobre o site para a Autoridade Certificadora identificada pelo site.

O cancelamento aumenta o risco de intercepção das suas informações privadas. [Saiba mais](https://support.mozilla.org/kb/advanced-settings-browsing-network-updates-encryption#w_certificates-tab).

### Relatórios de travamentos {: #crash-reporter }
Por padrão, nas versões para computador do Firefox, solicitamos que você compartilhe com a Mozilla um relatório com informações mais detalhadas sobre travamentos, mas é possível recusar.

* __Dados confidenciais__: Os relatórios de travamentos incluem um "arquivo de despejo" de conteúdo da memória do Firefox no momento do travamento, que pode conter dados que identificam ou são confidenciais a você.

* __Dados da página da Internet__: Os relatórios de travamentos incluem a URL ativa no momento do travamento.

* __Dados técnicos__: Os relatórios de travamentos incluem dados do motivo do travamento do Firefox e do estado da memória do dispositivo e da execução durante o travamento.

Leia a documentação completa [aqui](https://firefox-source-docs.mozilla.org/toolkit/crashreporter/crashreporter/index.html).

### Medir e oferecer suporte ao nosso marketing

* __Dados de campanhas e de referência__: Isso ajuda a Mozilla a entender a eficácia das nossas campanhas de marketing.
{: #referraltracking }

    _No Desktop_: Por padrão, o Firefox envia dados HTTP à Mozilla que podem ser incluídos no instalador do navegador. Isso nos possibilita determinar o domínio do site ou a campanha de publicidade (se houver) que encaminhou você para nossa página de download. Leia a [documentação](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/data/environment.html#attribution) ou [cancele](https://support.mozilla.org/kb/desktop-privacy) antes da instalação.

    _No iOS e Android_: Por padrão, o Firefox envia dados de campanhas de dispositivos móveis para o Adjust, nosso fornecedor de análise, que tem sua própria [política de privacidade](https://www.adjust.com/privacy_policy/). Os dados de campanhas de dispositivos móveis incluem um ID de publicidade do Google, endereço IP, carimbo de data/hora, país, idioma/local, sistema operacional e versão do aplicativo. Leia a [documentação](https://firefox-source-docs.mozilla.org/mobile/android/fennec/adjust.html).
{: #thirdparty }

* __Dados técnicos e de interação__: 

    _No iOS e Android_: Por padrão, o Firefox envia dados relacionados aos recursos que você usa nele para o Leanplum, nosso fornecedor de marketing para dispositivos móveis, que tem sua própria [política de privacidade](https://www.leanplum.com/privacy/). Esses dados nos permitem testar diferentes recursos e experiências, além de fornecer mensagens e recomendações personalizadas para melhorar sua experiência com o Firefox.

    Leia a documentação para [iOS](https://github.com/mozilla-mobile/firefox-ios/blob/master/MMA.md) ou [Android](https://firefox-source-docs.mozilla.org/mobile/android/fennec/mma.html) ou saiba como [desabilitar esse recurso](https://support.mozilla.org/kb/send-anonymous-usage-data-firefox-mobile-devices).

---

## Se você usar esses recursos, o Firefox compartilhará dados para fornecer funcionalidade: {: #optional-features }

### Pesquisa

Você pode fazer pesquisas diretamente de vários lugares no Firefox, inclusive na barra de endereços inteligente, no campo de pesquisa ou uma nova aba. _A Mozilla não recebe suas consultas de pesquisa._ Os dados de consultas são enviados para seu mecanismo de pesquisa, que tem sua própria política de privacidade.

* __Sugestões de pesquisa__: Por padrão, o Firefox envia consultas de pesquisa para seu mecanismo de pesquisa a fim de ajudar você a descobrir frases comuns pesquisadas por outras pessoas e melhorar sua experiência. Esses dados não serão enviados caso seu mecanismo de pesquisa não seja compatível com sugestões de pesquisa.
{: #searchsuggestions } 

    [Saiba mais](https://support.mozilla.org/kb/use-popular-search-suggestions-firefox-search-bar), inclusive como desabilitar esse recurso.

### Conta Firefox

* __Dados da Conta Firefox__: A Mozilla recebe seu endereço de e-mail e um hash da sua senha quando você cria uma Conta Firefox. Você pode optar por incluir um nome de exibição ou imagem de perfil. Seu endereço de e-mail é enviado para nosso fornecedor de e-mail, o SalesForce Marketing Cloud, que tem sua própria [política de privacidade](https://www.marketingcloud.com/privacy-policy/website-privacy-statement/). Se você usar a sua Conta Firefox para fazer login em outros sites ou serviços (como AMO ou Pocket), receberemos o carimbo de data/hora do seu login nesses serviços. 

* __Dados de localização__: Para fins de segurança, armazenamos os endereços IP que você usa para acessar a sua Conta Firefox, a fim de aproximar sua cidade e país. Usamos esses dados para enviar alertas de e-mail para você caso detectemos atividades suspeitas, como logins de outros locais.

* __Dados de interação__: Recebemos dados como acessos e interações com o site da Conta Firefox e com as preferências do menu e interações com integração, e-mail e mensagens SMS. [Leia mais](https://www.mozilla.org/privacy/websites/) sobre as práticas de dados da Mozilla para sites e e-mail.  

* __Dados técnicos__: Para exibir quais dispositivos são sincronizados com a sua Conta Firefox e para funcionalidades, armazenamos o sistema operacional do seu dispositivo, o navegador e a versão, o carimbo de data/hora, o local e as mesmas informações para dispositivos conectados à sua conta.  

Leia a [documentação completa](https://github.com/mozilla/fxa-auth-server/blob/master/docs/metrics-events.md) ou [saiba mais](https://support.mozilla.org/kb/access-mozilla-services-firefox-accounts), inclusive sobre como [excluir sua conta](https://support.mozilla.org/kb/how-do-i-delete-my-firefox-account).

### Sync {: #sync }

* __Dados sincronizados__: Se você habilitar o Sync, a Mozilla receberá as informações sincronizadas entre os dispositivos em um formato criptografado. Elas podem incluir abas do Firefox, extensões, senhas, informações de preenchimento automático de pagamento, favoritos, histórico e preferências. A exclusão da sua Conta Firefox excluirá o conteúdo relacionado ao Firefox Sync. Você também pode ler a [documentação](https://moz-services-docs.readthedocs.io/en/latest/sync/).

* __Dados técnicos e de interação__: Se você habilitar a sincronização, o Firefox enviará periodicamente informações básicas usando telemetria sobre a tentativa mais recente de sincronização dos seus dados, como quando ela ocorreu, se ela foi bem-sucedida ou não e o tipo de dispositivo que tentou fazer a sincronização. Você também pode ler a [documentação](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/data/sync-ping.html).

[Saiba mais](https://support.mozilla.org/kb/how-do-i-set-sync-my-computer), inclusive sobre como habilitar ou desabilitar a sincronização.

### Localização {: #location-services }

* __Dados de localização para o serviço de geolocalização do Google__: O Firefox confirma antes de determinar e compartilhar sua localização com um site solicitante (por exemplo, se um site de mapa precisar da sua localização para fornecer orientações). Para determinar a localização, o Firefox poderá usar os recursos de geolocalização do seu sistema operacional, redes de Wi-Fi, torres de celular ou endereços IP e enviar esses dados para o serviço de geolocalização do Google, que tem sua própria [política de privacidade](https://www.google.com/privacy/lsf.html).

[Saiba mais](https://www.mozilla.org/firefox/geolocation/).

### Firefox Screenshots {: #screenshots }

* __Uploads de capturas de tela__: As capturas de tela que são carregadas e enviadas para a Mozilla são armazenadas pelo tempo limite indicado, que pode mudar. Podemos acessar suas capturas de tela carregadas quando razoavelmente necessário para a operação do serviço. Você pode excluir suas capturas de tela carregadas a qualquer momento.

* __Dados de interação__: Recebemos dados como acessos ao site do Firefox Screenshots, frequência de acesso e compartilhamento por você e outras pessoas das capturas de tela carregadas e suas interações com botões, blocos e movimentos do mouse relacionados à captura de telas.

    Para acessos ao site do Firefox Screenshots, nossa [nota sobre privacidade de sites](https://www.mozilla.org/privacy/websites/) descreve os tipos de dados que podemos coletar.

* __Dados técnicos__: Recebemos dados como o tamanho e número médio de suas capturas de tela carregadas, a versão do seu navegador Firefox, o sistema operacional do dispositivo e erros. O endereço de IP de acesso do site do Firefox Screenshots é temporariamente coletado como parte de um registro padrão de servidor. 

Leia a [documentação completa](https://github.com/mozilla-services/screenshots/blob/master/docs/METRICS.md) ou [saiba mais](https://wiki.mozilla.org/Firefox/Screenshots/FAQs).

### Notificação de site {: #push-notifications }

* __Dados de conexão__: Se você permitir que um site envie notificações, o Firefox se conectará à Mozilla e usará seu endereço IP para retransmitir a mensagem. A Mozilla não pode acessar o conteúdo das mensagens.

* __Dados de interação__: Recebemos dados agregados, como número de inscrições e cancelamentos de inscrição de notificações de site do Firefox, número de mensagens enviadas, carimbos de data/hora e remetentes (que podem incluir provedores específicos de sites).

Leia a [documentação completa](https://mozilla-push-service.readthedocs.io/en/latest/) ou [saiba mais](https://support.mozilla.org/kb/push-notifications-firefox), inclusive sobre como revogar as notificações de sites.

### Extensões {: #addons }

Você pode instalar extensões em addons.mozilla.org ("AMO") ou no gerenciador de extensões do Firefox, acessível no botão de menu do Firefox, na barra de ferramentas.
 
* __Consultas de pesquisa__: Consultas de pesquisa no gerenciador de extensões são enviadas para a Mozilla para fornecer à você sugestões de extensões.

* __Dados de interação__: Recebemos dados agregados sobre acessos ao site AMO e ao gerenciador de extensões do Firefox, além de interações com o conteúdo dessas páginas. Leia as práticas de dados nos [sites da Mozilla](https://www.mozilla.org/privacy/websites/).

* __Dados técnicos para atualizações__: O Firefox se conecta periodicamente à Mozilla para instalar atualizações nas extensões. Suas extensões instaladas, versão do Firefox, idioma e sistema operacional do dispositivo são usados para aplicar as atualizações corretas.

---

### Nota de rodapé

Este aviso de privacidade é referente à versão de lançamento geral mais recente do Firefox distribuída pela Mozilla. Se você obter o Firefox de outro lugar ou tiver uma versão mais antiga, sua cópia poderá conter características diferentes de privacidade.
{: #pre-release }

As versões pré-lançamento do Firefox da Mozilla (distribuídas por canais como Nightly, Beta, TestFlight e BuddyBuild) estão em desenvolvimento ativo e podem conter características diferentes de privacidade. 
