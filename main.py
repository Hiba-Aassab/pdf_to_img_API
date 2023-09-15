from libraries import *
app = FastAPI()

# @app.get("/")
# def welcome():
#     return {"message": 'api Hello world '}


origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_methods=["*"], allow_headers=["*"])
         
# @app.post('/hello')
# async def hello():
#     return "Hello world"

@app.post('/conversion')
async def pdf_to_base64Image(file: UploadFile = File(...)):
    try:
        pdf_bytes = await file.read()

        images = convert_from_bytes(pdf_bytes, poppler_path=poppler_path)

        base64_images = []
        for i, image in enumerate(images):
            img_byte_array = io.BytesIO()
            image.save(img_byte_array, format='PNG')  # You can choose other image formats if needed
            img_byte_array = img_byte_array.getvalue()
            base64_image = base64.b64encode(img_byte_array).decode('utf-8')
            base64_images.append({"page": i + 1, "base64": base64_image})

        return {"pages": base64_images}
    except Exception as e:
        return {"error": str(e)}

@app.post('/conversion')
async def image_to_pdf(file: UploadFile = File(...)):
    try:
        # Read the uploaded image
        image_bytes = await file.read()
        
        # Convert image bytes to PIL image
        image = Image.open(io.BytesIO(image_bytes))
        
        # Create a PDF from the image
        pdf_byte_array = io.BytesIO()
        image.save(pdf_byte_array, format='PDF')
        pdf_byte_array = pdf_byte_array.getvalue()
        
        # Convert PDF bytes to base64
        base64_pdf = base64.b64encode(pdf_byte_array).decode('utf-8')
        
        return {"pdf_base64": base64_pdf}
    except Exception as e:
        return {"error": str(e)}
    

def convert_to_base64(images):
    base64_images = []
    print(type(images))
    for i, image in enumerate(images):
        img_data = image_to_base64(image)
        base64_images.append({"page": i+1, "base64": img_data})
    return base64_images


def image_to_base64(image):
    img_byte_array = image.convert('RGB').tobytes()
    base64_data = base64.b64encode(img_byte_array).decode('utf-8')
    return base64_data

# @app.post('/conversion')
# async def Pdf_to_image(file: UploadFile = File(...)):
#     try:
#         pdf_bytes = await file.read()
#         images = convert_from_bytes(pdf_bytes)
#         image_urls = saveImage(images)
#         return {"url": image_urls}
#     except Exception as e:
#         return {"error": str(e), "type": type(e).__name__}

# # save the images to desktop and return their urls


# def saveImage(image):
#     image_urls = []
#     for i, image in enumerate(image):
#         image_path = f'image_{i}.png'
#         # Create the static folder (dir) if it does not exist
#         if not os.path.exists('static'):
#             os.mkdir('static')
#         image.save(f'static/{image_path}', "PNG")
#         image_urls.append(image_path)
#     return image_urls

######## This takes saved image from local storage and encode them to base64 #####
# @app.post('/converted_images_base64')
# def get_converted_images_base64():
#     base64_images = []
#     for i, image_path in enumerate(os.listdir('static')):
#         with open(os.path.join('static', image_path), "rb") as image_file:
#             image_data = image_file.read()
#             base64_image = base64.b64encode(image_data).decode('utf-8')
#             base64_images.append({"page": i+1, "base64": base64_image})
#     return base64_images
