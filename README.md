# PDF Legal Document Summarizer with Llama-Express.1-Tiny

---

This project provides a Python script to extract text from PDF documents and then leverage a large language model (LLM) to summarize the content, with a specific focus on legal points. It uses the `transformers` library by Hugging Face and the `prithivMLmods/Llama-Express.1-Tiny` model for efficient local processing.

---
## Features

* **PDF Text Extraction**: Easily extracts all textual content from a given PDF file.
* **LLM-Powered Summarization**: Utilizes a pre-trained language model to generate concise summaries.
* **Legal Focus**: The summarization prompt is tailored to emphasize legal aspects and points discussed within the document.
* **Local Model Inference**: Runs the language model locally, ensuring data privacy and potentially faster processing compared to API-based solutions.
* **Output to Text File**: Saves the generated summary to a plain text file.

---
## Requirements

Before you begin, ensure you have the following:

* **Python 3.8+**
* **Required Python Libraries**: Install them using pip:
    ```bash
    pip install torch PyPDF2 transformers accelerate
    ```
* **PDF Document**: A PDF file you wish to summarize (e.g., `contract.pdf`).

---
## Usage

1.  **Place Your PDF**: Make sure your PDF document (e.g., `contract.pdf`) is accessible to the script. Update the **`pdf_path`** variable in the script to point to your PDF's location.
    ```python
    pdf_path = "/home/company/contract.pdf" # Update this path
    ```

2.  **Run the Script**: Execute the Python script from your terminal:
    ```bash
    python your_script_name.py
    ```
    (Replace **`your_script_name.py`** with the actual name of your Python file.)

The script will:
* Extract text from the specified PDF.
* Feed the text to the **`Llama-Express.1-Tiny`** model with a legal summarization prompt.
* Print the generated summary to the console.
* Save the summary to a text file named **`my_file.txt`** in the same directory.

---
## Code Details

* **`extract_text_from_pdf(pdf_path)`**: This function uses **`PyPDF2`** to read the PDF and extract text page by page.
* **`model_id = "prithivMLmods/Llama-Express.1-Tiny"`**: This specifies the pre-trained LLM from Hugging Face that will be used for summarization. This model is chosen for its relatively small size, making it suitable for local execution.
* **`pipeline("text-generation", ...)`**: The **`transformers`** pipeline simplifies the process of using the LLM for text generation.
    * **`torch_dtype=torch.bfloat16`**: Uses **`bfloat16`** precision, which can help reduce memory usage and improve performance on compatible hardware.
    * **`device_map="cuda"`**: Attempts to load the model onto the GPU for faster inference. If you don't have a CUDA-enabled GPU or encounter issues, you can change this to **`"cpu"`** or remove it to let **`transformers`** automatically detect the device.
* **`messages`**: This list defines the conversation for the LLM.
    * The **`system`** role establishes the LLM's persona as a "lawyer" to guide its summarization style.
    * The **`user`** role provides the instruction to summarize the document, emphasizing legal points.
* **`max_new_tokens=256`**: This parameter limits the length of the generated summary to 256 new tokens. You can adjust this value based on your desired summary length.

---
## Customization

* **Change the PDF**: Simply update the **`pdf_path`** variable to point to a different PDF document.
* **Modify the Prompt**: You can refine the **`content`** within the **`user`** role in the **`messages`** list to alter the summarization focus. For example, you could ask for specific clauses, potential risks, or obligations of a particular party.
* **Experiment with LLMs**: Hugging Face offers a vast collection of language models. You can try different **`model_id`**s, keeping in mind that larger models will require more computational resources (GPU memory, RAM).
* **Output Format**: The current output is a simple text file. For more advanced reporting, you could integrate libraries to generate summaries in other formats like PDF (using **`reportlab`** or similar) or structured data (JSON, XML).
* **Summary Length**: Adjust **`max_new_tokens`** to control the verbosity of the generated summary.

---
## Troubleshooting

* **CUDA Memory Issues**: If you encounter "CUDA out of memory" errors, especially with larger models, try changing **`device_map="cuda"`** to **`device_map="auto"`** or even **`device_map="cpu"`**. You might also consider using a smaller **`max_new_tokens`** value.
* **Model Download Errors**: Ensure you have an active internet connection. If you're behind a proxy, configure your environment variables accordingly.
* **PyPDF2 Issues**: If PDF extraction fails, it might be due to a malformed PDF or a secured document. Ensure the PDF is not encrypted or password-protected.
* **Summarization Quality**: The quality of the summary depends heavily on the chosen LLM and the clarity of your prompt. Experiment with different prompts and models to achieve optimal results.

---
