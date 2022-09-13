import gradio as gr
from main import detect_web

gr.Interface(fn=detect_web, 
             inputs=gr.Image(type="filepath"),
             outputs=[gr.Gallery().style(grid=4),
             gr.Textbox()],
             examples=["image.webp"]).launch(share=False, 
                                                debug=False, 
                                                max_threads=8,
                                                server_name='0.0.0.0', 
                                                server_port=80)