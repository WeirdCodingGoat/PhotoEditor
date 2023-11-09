from PIL import Image
import inspect
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("PhotoEdit.kv")


class QuizPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass

class Question2Screen(Screen):
    # IMAGE LOADING
    def display_image(self):
        return ""
        
    def load_image(self,name):
        self.ids.image.source = name
        
        
    def answer_question(self, img): # this is the image text input button handler
        if img == "2012":
            self.manager.current = "correct"
        else:
            self.load_image(img)
            
            
                    #  IMAGE EDITING FUNCTIONS BELOW vvvvvvv
           
    def pixal_ruler(self):
        imgN=""
    
        if "1" in self.ids.image.source:
            imgN=self.ids.image.source[:-5]+self.ids.image.source[-4:]
            self.load_image(imgN)
        
        
        
    def bluetogreenimage(self):#,name): #Blue to green function
        imgN=""
        # ADD SET UP CODE FOR THE RULER FUNCTION! (if 1 in self.ids.image.source:
        if "1" in self.ids.image.source:
            imgN=self.ids.image.source[:-5]+self.ids.image.source[-4:]
        else:
            imgN=self.ids.image.source
        name=imgN[:-4] # MAKE A FUNCTION TO MAKE A NAME FORMAT
        img=Image.open(imgN)
        #new_img=Image.open(imgN)
    
        pixels = img.load()
        print(type(pixels))
        width, height = img.size
        
        print("(",1,2,")","\nWidth:", width, "\nHeight:", height)
                    
        for y in range(img.size[1]):
            for x in range(img.size[0]):

                if pixels[x,y][2]>=100 and pixels[x,y][0]<170 and pixels[x,y][1]<170:
                    temp=pixels[x,y][1]
                    red = pixels[x,y][0]
                    green = pixels[x,y][2]
                    blue = green-temp
                else:
                    temp=pixels[x,y][1]
                    red = pixels[x,y][0]
                    green = pixels[x,y][1]
                    blue = pixels[x,y][2]
            
                pixels[x,y] = (int(red), int(green), int(blue))
            temp=0
        img.save(name+"btg"+self.ids.image.source[-4:])
        self.load_image(name+"btg"+self.ids.image.source[-4:])
        
    def pointillism(image):  # Pointillism function
      pixels = image.load()
      canvas = Image.new("RGB",(image.size[0],image.size[1]), "white")
      for _process in range(10000):
        x = random.randint(0,image.size[0]-1)
        y = random.randint(0,image.size[0]-1)
        size = random.randint(3,5)
        ellipsebox=[(x,y),(x+size,y+size)]
        draw = ImageDraw.Draw(canvas)
        draw.ellipse(ellipsebox,fill=(pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]))
        del draw
        canvas.save("pointillism.png")
        
    def sepiaimage(self,image,name): # Sepia function
      pixels = image.load()
      for y in range(image.size[1]):
        for x in range(image.size[0]):
          red = pixels[x,y][0]*0.393 + pixels[x,y][1]*0.769 + pixels[x,y][2]*0.189
          green = pixels[x,y][1]*0.769 + pixels[x,y][0]*0.393 + pixels[x,y][2]*0.189
          blue = pixels[x,y][2]*0.189 + pixels[x,y][0]*0.393 + pixels[x,y][1]*0.769
          transparency = pixels[x,y][3]
          
    def invert(self,image,name): # Invert image function
      pixels = image.load()
      for y in range(image.size[1]):
        for x in range(image.size[0]):
          red = 255 - pixels[x,y][0]
          green = 255 - pixels[x,y][1]
          blue = 255 - pixels[x,y][2]
          transparency = 255 - pixels[x,y][3]
          pixels[x,y] = (red, green, blue)
      #image.save(name+"inverted.png")
        
        def mirror_vertical(image,image2): # Left side and right side swaper func
          pixels = image.load()
          pixels2 = image2.load()
          for y in range(image.size[1]):
            for x in range(image.size[0]):
              pixels2[x*-1,y] = pixels[x,y]
          #image2.save("Xreversed Hat kid.png")
          
        def mirror_horizontal(image,image2):
          pixels = image.load()
          pixels2 = image2.load()
          for y in range(image.size[1]):
            for x in range(image.size[0]):
              pixels2[x,y*-1] = pixels[x,y]
          #image2.save("Yreversed Hat kid.png")
          
        def pixalated_spot(self,image, x, y, width, height, name): # Pixalating a spot func
          _y_devided=height//8
          _x_devided=width//8
          color=(0,0,0)

          for _y_pixels in range(0,width,_y_devided):
            for _x_pixels in range(0,height,_x_devided):
              color=pixels[_x_pixels+x,_y_pixels+y]
              box(_x_pixels+x, _y_pixels+y, _y_devided, _x_devided, color)
  #image.save(name+" spot pixalated.png")

#mirror_vertical(HatKid,HatKid2)
    
    
class CorrectScreen(Screen):
    def next(self):
        self.manager.current = "question2"

class WrongScreen(Screen):
    def next(self):
        self.manager.current = "question2"

QuizPageApp().run()
