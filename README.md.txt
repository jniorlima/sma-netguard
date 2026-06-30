# SMA NetGuard

Sistema Multiagente para Monitoramento Inteligente de Redes de Computadores.

## Descrição

O SMA NetGuard é um protótipo desenvolvido como trabalho acadêmico que utiliza uma arquitetura baseada em agentes para monitorar a disponibilidade de hosts, latência e tráfego de rede, classificando eventos e exibindo alertas em um dashboard web.

## Funcionalidades

- Monitoramento de host por ICMP
- Análise de latência
- Monitoramento de tráfego
- Classificação de eventos por severidade
- Dashboard em tempo real
- Arquitetura baseada em agentes

## Tecnologias

- Python 3
- Flask
- psutil
- ping3
- HTML/CSS
- JavaScript

## Estrutura

```
agents/
models/
services/
templates/
logs/
main.py
dashboard.py
config.py
requirements.txt
```

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/jniorlima/sma-netguard.git
cd sma-netguard
```

### 2. Criar ambiente virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o sistema

Em um terminal:

```bash
python main.py
```

Em outro terminal:

```bash
python dashboard.py
```

Acesse:

```
http://127.0.0.1:5000
```

## Autor

Júnior Lima

## Licença

Projeto desenvolvido para fins acadêmicos.
