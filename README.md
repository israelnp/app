# app_python_prometheus

## Instrumentação de aplicação com python e prometheus

### Criando Imagem do projeto

* docker build -t img_app_python .

### Executando Container

* docker run --name app_python -h my_hostname -p5000:5000 -d img_app_python

### Metricas de Aplicaçao 

* /metrics
