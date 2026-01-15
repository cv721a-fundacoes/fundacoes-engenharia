# Exemplos Didáticos — Trilha Tecnológica (CV721A)

Este diretório reúne **exemplos simples, comentados e não avaliativos**, utilizados
exclusivamente para **demonstração didática** de ferramentas computacionais
aplicadas à disciplina de **Fundações (CV721A)**.

Os exemplos **não substituem** o cálculo clássico, as normas técnicas ou o
julgamento profissional em engenharia.

---

## Papel dos exemplos na disciplina

Os exemplos têm como objetivo:

- Demonstrar **conceitos mínimos de uso** de ferramentas computacionais;
- Reduzir barreiras iniciais de instalação e configuração;
- Permitir que o aluno foque no **raciocínio de engenharia**, e não na ferramenta;
- Servir como base para **experimentação guiada**, sem impacto direto na avaliação.

> Nenhum exemplo deste diretório é utilizado como critério de correção dos projetos.

---

## Organização do diretório

```text
exemplos/
├── pyrevit/
│   └── quantitativos-sapatas/
│       ├── README.md
│       └── script.py
└── (outros exemplos futuros)
Instalação — como fazer funcionar (passo a passo)
Esta seção descreve apenas o necessário para executar os exemplos com pyRevit.
Não é esperado conhecimento prévio de programação ou da API do Revit.

1. Instalação do pyRevit
Pré-requisitos mínimos:

Windows

Autodesk Revit 2023 / 2024 / 2025

pyRevit: https://github.com/eirannejad/pyRevit/releases

Passos:

Baixe:
pyRevit 5.3.1.25308 – Installer – Admin / All Users / %PROGRAMDATA%

Execute o instalador como Administrador.

Abra o Revit e verifique se existe a aba pyRevit na faixa superior.

Se a aba pyRevit não aparecer, a instalação não foi concluída corretamente.

2. Local correto das extensões
O pyRevit procura comandos em um diretório específico do usuário.

Crie (ou utilize) o seguinte caminho:

text
Copiar código
C:\Users\<USUARIO>\AppData\Roaming\pyRevit\Extensions
Substitua <USUARIO> pelo nome do seu usuário do Windows.

3. Estrutura de pastas (obrigatória)
A estrutura precisa ser exatamente esta:

text
Copiar código
Extensions
└── Foundations.extension
    └── Quantitativos.tab
        └── Sapatas.panel
            └── Concreto.pushbutton
                └── script.py
Regras importantes:

Pastas devem terminar com:

.extension

.tab

.panel

.pushbutton

Apenas script.py é um arquivo.

Não altere nomes nem extensões.

O Windows pode esconder extensões (.txt).
Confirme que o arquivo é script.py, e não script.py.txt.

4. Configuração do diretório no pyRevit
No Revit:

Abra a aba pyRevit

Clique em Settings

Vá em Custom Extension Directories

Adicione apenas o caminho abaixo:

text
Copiar código
C:\Users\<USUARIO>\AppData\Roaming\pyRevit\Extensions
Confirme e feche o Revit

Abra o Revit novamente

5. Verificação final
Após reiniciar o Revit, o botão deve aparecer em:

text
Copiar código
pyRevit
└── Quantitativos
    └── Sapatas
        └── Concreto
Se o botão aparecer, a instalação está correta.

6. Se não funcionou (diagnóstico rápido)
Antes de pedir ajuda, verifique:

 O Revit foi reiniciado após criar as pastas?

 As pastas terminam exatamente com .extension, .tab, .panel, .pushbutton?

 O arquivo é script.py (e não .txt)?

 O caminho em Custom Extension Directories está correto?

 O modelo aberto possui elementos da categoria Structural Foundation?

Em mais de 90% dos casos, o problema está na estrutura de diretórios, não no código.

Observação importante
Dificuldades técnicas de instalação não são critério de avaliação.
> 💡 Importante  
> Este exemplo foi pensado para **ensinar engenharia**, não para testar habilidade com software.  
> Erros iniciais fazem parte do processo. Persistir e diagnosticar **também é engenharia**.
