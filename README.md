# LLM REPOSITORIO - MARKDOWN ETIQUETACIÓN DE CÓDIGO
Repositorio de trabajo con modelo de lenguaje largo usando ollama

## 1. Para instalar Ollama 

Para instalar Ollama se accede a la página de [ollama](https://ollama.com/download/linux) 

````bash
curl -fsSL https://ollama.com/install.sh | sh
````

## 2.Ejecutar el servidor

Una vez instalado ejecutar el servidor ollama con el siguiente comando
````bash
ollama serve
````
Abrir otra terminal

## 3. Descargar algún modelo

En la página de [modelos](https://ollama.com/library) de ollama se búsca el modelo deseado y se descarga el siguiente comando:

````bash
ollama pull tinyllama
````
## 3. indexar
````bash
git add
````

Hacer un commit
````bash
git commit -m "UPDATE README.md"
````
 ## 4. Subir el commit al repositorio de github
 ````bash
git push -u origin main
````
## 6. Verificar quien realizó los cambios
 ````bash
git config --global user.email santiago.varelah@ecci.edu.co
git config --gloabal user.name "Santiago-2
````

## 4.1 Prueba de requeste a las API REST

Para relaizar uan paeticióna olla se sigue la siguiente estructura

````
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}'
````

### 4.2 Guaradar en un archivo

````
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}' -o salida.md
````

### 4.3 Sin formato stream
````
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
````