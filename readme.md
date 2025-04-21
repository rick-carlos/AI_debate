![ia-talk](talk-ai.png)

## É um projeto simples pra criar debates com modelos

### Adicionado algumas funcionalidades 🚀

1) Definir um tema de debate que será discutido pelos modelos
2) Usar um arquivo de texto como referência pro debate
3) Debate entre o usuário e o modelo
4) Todo o debate agora é salvo em um arquivo de texto no diretórioo textos/debates

#### Requirements
- Python 3.10+
- ollama

#### _Instale o ollama local para o seu sistema operacional_
https://ollama.com/

#### _Instale a bilbioteca ollama do Python_
```bash
pip install ollama
```


#### Instale os modelos
```bash
ollama pull gemma3:1b
ollama pull gemma3
```

###### Obs: ⚑


* Uso gemma3:1b pro debate entre modelos por enquanto porque são muito pequenos, rápidos e muito bem treinados em portugues e pretendo adicionar debates com mais de 2 modelos no futuro.
* Uso gemma3:4b pro xat com usuário
* Use os modelos que quiser, só troque na variável modelo_a e modelo_b em main.py



