import requests
import io
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from pypdf import PdfReader  # Import the correct PDF reading library
import warnings
from urllib3.exceptions import InsecureRequestWarning

class WebPDFReaderToolInput(BaseModel):
    """Input schema for WebPDFReaderTool."""
    url: str = Field(..., description="URL of the PDF document to read.")

class WebPDFReaderTool(BaseTool):
    name: str = "Web PDF Reader Tool"
    description: str = (
        "Reads the text content of a PDF document from a given URL."
    )
    args_schema: Type[BaseModel] = WebPDFReaderToolInput

    def _run(self, url: str) -> str:
        """
        Reads text content from a PDF hosted online.
        Args:
            url: The URL where the PDF is hosted.
        Returns:
            The extracted text content of the PDF or an error message.
        """
        try:
            
            # Suppress only the specific InsecureRequestWarning
            warnings.simplefilter('ignore', InsecureRequestWarning)

            # Send HTTP GET request to the URL
            response = requests.get(url, stream=True, timeout=30, verify=False)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

            # Check if the content type is PDF
            content_type = response.headers.get('content-type', '')
            if 'application/pdf' not in content_type.lower():
                return f"Error: URL does not point to a PDF document. Content-Type: {content_type}"

            # Read the content into memory
            pdf_content = io.BytesIO(response.content)

            # Use pypdf to read the PDF
            reader = PdfReader(pdf_content)  # Use PdfReader instead of WebPDFReaderTool
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:  # Check if text was extracted
                    text += page_text + "\n"  # Add newline between pages

            if not text:
                return "Error: Could not extract any text from the PDF. It might be image-based or corrupted."

            # Optional: Add basic cleaning (can be expanded)
            text = ' '.join(text.split())  # Remove excessive whitespace

            # Limit text length if needed (e.g., due to LLM context limits)
            # max_length = 15000  # Example limit
            # if len(text) > max_length:
            #     text = text[:max_length] + "... [truncated]"

            return text

        except requests.exceptions.RequestException as e:
            return f"Error downloading PDF from URL: {e}"
        except Exception as e:
            return f"Error processing PDF: {e}"

# --- Instantiate the Tool ---
pdf_reader_tool = WebPDFReaderTool()

print("Tool and LLM setup complete.")
# You can test the tool standalone:
# pdf_url = "https://api.bookbotkids.workers.dev/books/f60ac1f9-e513-433f-a640-6cbdf028cd98/Magnet%20Magic!.pdf"
# extracted_text = pdf_reader_tool.run(url=pdf_url)
# print(extracted_text)  # Print the first 500 characters