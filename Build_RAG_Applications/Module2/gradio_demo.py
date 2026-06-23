import gradio as gr

def process_text(input_text):
    # Placeholder for processing logic
    return f"Processed: {input_text}"

def count_files(files):
    return f"Number of files uploaded: {len(files)}"

# cannot use it for multiple things like uploading files and processing text at the same time. You would need to create separate interfaces for each functionality or combine them in a single function that handles both inputs.
# This is where we use gr.Blocks to create a more complex interface that can handle multiple inputs and outputs. For example, you can create a block that allows users to upload files and another block that processes text input, all within the same interface.

# demo = gr.Interface(
#     fn=process_text,
#     inputs = gr.Textbox(label="Input", placeholder="Enter your text here..."),
#     outputs = gr.Textbox(label = "Output", placeholder="Processed output will appear here..."),
# )

# Option 1 with blocks
import gradio as gr

def process_text(input_text):
    return f"Processed: {input_text}"

def count_files(files):
    return f"Number of files uploaded: {len(files)}"

with gr.Blocks() as demo:
    gr.Markdown("# Text Processor & File Counter")

    # Text processing section
    with gr.Tab("Text Processor"):
        text_input = gr.Textbox(
            label="Input",
            placeholder="Enter your text here..."
        )
        text_output = gr.Textbox(
            label="Output"
        )

        process_btn = gr.Button("Process")
        process_btn.click(
            process_text,
            inputs=text_input,
            outputs=text_output
        )

    # File upload section
    with gr.Tab("File Counter"):
        file_input = gr.File(
            file_count="multiple",
            file_types=[".txt", ".pdf", ".docx"]
        )

        file_output = gr.Textbox(label="File Count")

        count_btn = gr.Button("Count Files")
        count_btn.click(
            count_files,
            inputs=file_input,
            outputs=file_output
        )

demo.launch()

# option 2 with interface:
# import gradio as gr

# def process_text(input_text):
#     return f"Processed: {input_text}"

# def count_files(files):
#     return f"Number of files uploaded: {len(files)}"

# text_demo = gr.Interface(
#     fn=process_text,
#     inputs=gr.Textbox(),
#     outputs=gr.Textbox()
# )

# file_demo = gr.Interface(
#     fn=count_files,
#     inputs=gr.File(file_count="multiple"),
#     outputs=gr.Textbox()
# )

# demo = gr.TabbedInterface(
#     [text_demo, file_demo],
#     ["Text Processor", "File Counter"]
# )

# demo.launch()
