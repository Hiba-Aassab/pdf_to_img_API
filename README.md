# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
## 1-install python 
 https://www.python.org/downloads/
## 2-  install fastAPI  using  this command
  `pip install fastapi`
  ## you  can install all package with this command 
   `  pip install -r requirements.txt`
## 3-You will also need an ASGI server, for production such as Uvicorn or Hypercorn.
`pip install "uvicorn[standard]"`

## 4-check if you install Tesseract  
  if you not  installl it click here
  https://github.com/UB-Mannheim/tesseract/wiki

## 5- install  python libraries  "libraries.py" file

for mor information click here https://fastapi.tiangolo.com/
## 6- Run it
`uvicorn main:app --reload` `python -m uvicorn main:app --reload`
 ### You can then run your application the same way you have done in the tutorials, but without the --reload option
           uvicorn is Asynchronous Server Gateway Interface
 `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`
 
 ## 7 file description 
    * main.py            :This is main of project.
    * methods.py         :The file that contains the function used in the APIs. 
    * object_detection.py:Our model that allows for image extraction.
    * rotated.py         :The file that contains rotation and orientation functions.
    * Other files are testing files.
`[{'IDENRECT':1,'IDENMETA':2,'REFIPO_X':221 ,'REFIPO_Y': 95 ,'RELAPO_X':  417,'RELAPO_Y': 149,'OBJERECT':1}]`
#### '[{"IDENRECT":1,"IDENMETA":2,"REFIPO_X":177 ,"REFIPO_Y": 118 ,"RELAPO_X":245,"RELAPO_Y":311,"OBJERECT":0}]'
 '

 for  library rembg,  install version  2.0.35
 `pip install rembg=2.0.35 `

 ## Note
  You may have to add Poppler to PATH to us pdf2image library
  [Download the latest version of Poppler (zip file)](https://github.com/oschwartz10612/poppler-windows/releases/)
