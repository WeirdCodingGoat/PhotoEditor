
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
    def display_image(self):
        return ""
    def answer_question(self, num):
        if num == "2012":
            self.manager.current = "correct"
        else:
            self.manager.current = "wrong"
            
    def bluetogreenimage(image,name): #Blue to green function
      pixels = image.load()
      for y in range(image.size[1]):
        for x in range(image.size[0]):
          
          if pixels[x,y][2]>=50 and pixels[x,y][0]<100 and pixels[x,y][1]<100:
            temp=pixels[x,y][1]
            red = pixels[x,y][0]
            green = pixels[x,y][2]
            blue = temp
          else:
            temp=pixels[x,y][1]
            red = pixels[x,y][0]
            green = pixels[x,y][1]
            blue = pixels[x,y][2]
            
          pixels[x,y] = (int(red), int(green), int(blue))
          temp=0
      #image.save(name+"bluetogreen.png")
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
        
    def sepiaimage(image,name): # Sepia function
      pixels = image.load()
      for y in range(image.size[1]):
        for x in range(image.size[0]):
          red = pixels[x,y][0]*0.393 + pixels[x,y][1]*0.769 + pixels[x,y][2]*0.189
          green = pixels[x,y][1]*0.769 + pixels[x,y][0]*0.393 + pixels[x,y][2]*0.189
          blue = pixels[x,y][2]*0.189 + pixels[x,y][0]*0.393 + pixels[x,y][1]*0.769
          transparency = pixels[x,y][3]
          
    def invert(image,name): # Invert image function
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
          
        def pixalated_spot(image, x, y, width, height, name): # Pixalating a spot func
          _y_devided=height//8
          _x_devided=width//8
          color=(0,0,0)

          for _y_pixels in range(0,width,_y_devided):
            for _x_pixels in range(0,height,_x_devided):
              color=pixels[_x_pixels+x,_y_pixels+y]
              box(_x_pixels+x, _y_pixels+y, _y_devided, _x_devided, color)
  #image.save(name+" spot pixalated.png")

#mirror_vertical(HatKid,HatKid2)

def mirror_horizontal(image,image2): # Top and bottom swaper func
  pixels = image.load()
  pixels2 = image2.load()
  for y in range(image.size[1]):
    for x in range(image.size[0]):
      pixels2[x,y*-1] = pixels[x,y]
  image2.save("Yreversed Hat kid.png")
    
    
class CorrectScreen(Screen):
    def next(self):
        self.manager.current = "question2"

class WrongScreen(Screen):
    def next(self):
        self.manager.current = "question2"

QuizPageApp().run()
