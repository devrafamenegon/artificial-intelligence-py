## Como Rodar o Python e Instalar o scikit-learn (sklearn)

Este guia fornecerá instruções passo a passo sobre como rodar Python em seu sistema e instalar a biblioteca scikit-learn (sklearn) usando o gerenciador de pacotes `pip`.

### Rodando Python

#### Windows:

1. **Instalação do Python:**
   - Baixe o instalador Python mais recente do site oficial: [Python Downloads](https://www.python.org/downloads/).
   - Execute o instalador baixado e siga as instruções na tela.
2. **Verificação da Instalação:**
   - Abra o Prompt de Comando (cmd).
   - Digite `python --version` e pressione Enter. Deverá ser exibida a versão do Python instalada.

#### macOS:

1. **Instalação do Python:**

   - O macOS geralmente já vem com o Python pré-instalado. Você pode verificar digitando `python --version` no Terminal.

2. **Atualização do Python (opcional):**
   - Se preferir uma versão mais recente, você pode instalar o Python usando o Homebrew ou baixando o instalador do site oficial Python.

#### Linux:

1. **Instalação do Python:**
   - A maioria das distribuições Linux já possui o Python instalado. Para verificar, digite `python3 --version` no Terminal.
   - Se não estiver instalado, você pode usar o gerenciador de pacotes da sua distribuição para instalar o Python.

### Instalando o scikit-learn (sklearn)

1. Abra um terminal ou Prompt de Comando.

2. Para garantir que o pip (gerenciador de pacotes do Python) esteja atualizado, execute o seguinte comando:

   ```
   pip install --upgrade pip
   ```

3. Para instalar o scikit-learn, use o seguinte comando:

   ```
   pip install -U scikit-learn
   ```

4. Após a instalação, você pode verificar se o scikit-learn foi instalado corretamente importando-o em um script Python:
   ```python
   import sklearn
   print(sklearn.__version__)
   ```

Com esses passos, você deverá ser capaz de rodar Python em seu sistema e instalar o scikit-learn com sucesso usando o pip. Certifique-se de substituir `pip` por `pip3` no Linux e macOS, caso sua instalação do Python use o nome `python3` ao invés de `python`.
