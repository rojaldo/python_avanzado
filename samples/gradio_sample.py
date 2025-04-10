import gradio as gr
import ollama

def saludo(msg):
    return ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': msg}])['message']['content']

iface = gr.Interface(fn=saludo, inputs="text", outputs="text")
iface.launch()