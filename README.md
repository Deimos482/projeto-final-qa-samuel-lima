# Projeto Final - QA

**Nome completo:** Samuel Lima Godinho  
**Curso e semestre:** GTI - 5º Semestre  

### 1. Apresentação

Durante o semestre, tive a oportunidade de aprender sobre a importância da Garantia da Qualidade (QA) no desenvolvimento de software. Através de práticas e estudos, pude compreender como os testes contribuem para a criação de sistemas mais confiáveis e eficientes.

### 2. O que é Quality Assurance (QA)?

Quality Assurance (QA) é uma prática que visa garantir que o software atenda aos padrões de qualidade estabelecidos. No desenvolvimento de software, QA envolve processos e atividades que asseguram que o produto final seja confiável, funcional e atenda às expectativas dos usuários. É importante porque ajuda a identificar e corrigir problemas antes que o software seja lançado, evitando falhas em produção e melhorando a experiência do usuário.

### 3. Conceitos Aprendidos Durante o Semestre

### Tipos de Testes
1. **Unitário**: Testa pequenas partes isoladas do código (funções/métodos)
2. **Integração**: Verifica como diferentes módulos trabalham juntos
3. **Regressão**: Garante que novas alterações não quebrem funcionalidades existentes
4. **Acessibilidade**: Testes para inclusão digital usando WAVE

### Ferramentas Utilizadas
1. **Google Colab**: Ambiente cloud para criação e execução de testes em Python
2. **GitHub**: Versionamento e colaboração em projetos de teste
3. **Selenium**: Automação de testes em navegadores web
4. **FakeKiller**: Validação de dados e prevenção de fraudes
5. **Katalon**: Plataforma all-in-one para automação de testes
6. **Ghost Inspector**: Testes E2E em navegador real com gravação
7. **Postman**: Testes de API e integrações

### CI/CD e Automação
- Integração de testes automatizados em pipelines
- Execução contínua de suites de teste
- Relatórios automáticos de qualidade
  
### 4. Ferramentas e Sites Utilizados

- [Google Colab](https://colab.research.google.com/) - Notebooks interativos para testes
- [GitHub](https://github.com/) - Controle de versão e colaboração
- [Selenium](https://www.selenium.dev/) - Automação web
- [FakeKiller](https://www.fakekiller.com.br/) - Validação de dados
- [Katalon](https://katalon.com/) - Plataforma de automação
- [Ghost Inspector](https://ghostinspector.com/) - Testes E2E
- [WAVE](https://wave.webaim.org/) - Acessibilidade web

### 5. Explicação dos Testes Entregues

#### ✅ Teste 01 – Verificação de status da API ReqRes
- **Biblioteca:** `requests`
- **Objetivo:** Verificar se o endpoint retorna status HTTP 200
- **Resultado esperado:** Teste passa com sucesso se o status for 200
- **Arquivo:** `testes/teste_01.py`
- 📌 **Arquivo:** https://colab.research.google.com/drive/1cq98UjQ3nrCp5z-v9M8qquV8MTTr9Ltr#scrollTo=GkmIOFq1IndS

#### ✅ Teste 02 – Validação de resposta JSON da API JSONPlaceholder
- **Biblioteca:** `requests`
- **Objetivo:** Verificar se o endpoint retorna um JSON com a chave 'id' igual a 1
- **Resultado esperado:** Teste passa com sucesso se a chave 'id' for 1
- **Arquivo:** `testes/teste_02.py`
- 📌 **Arquivo:** https://colab.research.google.com/drive/1TpcSPlFhA57mRteHSQbBNOzLtPJjn0on

#### ✅ Teste 03 – Teste de função de soma
- **Biblioteca:** `unittest`
- **Objetivo:** Validar se a função de soma retorna o resultado correto
- **Resultado esperado:** Teste passa com sucesso se a soma for correta
- **Arquivo:** `testes/teste_03.py`
- 📌 **Arquivo:** https://colab.research.google.com/drive/1N5eBGQa4R_v7sQPIt5zGJGeVFGh5PJin#scrollTo=x2TQlyFBSgFh

### 6. Conclusão Final

Ao longo deste semestre, aprendi que a Garantia da Qualidade (QA) é essencial para o desenvolvimento de software de alta qualidade. Através dos testes, podemos identificar problemas precocemente, melhorar a experiência do usuário e garantir a confiabilidade do produto final. A ferramenta que mais me chamou a atenção foi o `pytest`, devido à sua simplicidade e poder na automação de testes.

