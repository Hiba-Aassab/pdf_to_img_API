
from fastapi import FastAPI, File, UploadFile
import uvicorn
from PIL  import Image
import io
from pdf2image import convert_from_bytes
import os
from starlette.middleware.cors import CORSMiddleware
import base64
poppler_path=r'poppler-0.68.0/bin'