#### This is A deep learning model for Arabic handwriting text recognition with precision 93.5% .
 
## How to run the code.
you have to install python > 3.7.0, you can download python for windows from here: https://www.python.org/downloads/windows/

### Create Virtual Evironment
```
pip install --upgrade virtualenv
virtualenv  envname
cd envname/
cd bin/
activate
cd ..
cd ..

pip install -r requirements.txt
```
### Run the predicition script  
```
python detect.py --source text.jpg --weights arabic_handwritten_text.pt --save-crop
```
The results will be saved at ```runs/detect/exp/text.jpg```

### Run the trainning script  
```
python train.py --img 640 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt

```  
### Run the Colab notebook  
open this link: https://colab.research.google.com/drive/1hSUhID3UHnn5NkZvkEv_qJqA8D6N7Wd3?usp=sharing  
Run all the cells to get the output of the text image sample. 


