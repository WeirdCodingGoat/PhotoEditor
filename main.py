import inspect
import random
from PIL import Image, ImageDraw
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
        
        
    def answer_question(self, img): # this is the (image name input) button handler
        if img == "2012":
            self.manager.current = "correct"
        else:
            self.load_image(img)
    
    def image_prep(self):
        imgN=""
        # ACOMONDATING CODE FOR THE RULER FUNCTION:
        if "1" in self.ids.image.source:
            imgN=self.ids.image.source[:-5]+self.ids.image.source[-4:]
        else:
            imgN=self.ids.image.source
        name=imgN[:-4] # MAKE A FUNCTION TO MAKE A CONVENTIONAL NAME FORMAT (idk what I meant)
        img=Image.open(imgN)
        #new_img=Image.open(imgN)
    
        pixels = img.load()
        print(type(pixels))
        width, height = img.size
        
        print("(",1,2,")","\nWidth:", width, "\nHeight:", height)
        return pixels, width, height, name, img
            
            
            
            
            
            
                    #     IMAGE EDITING FUNCTIONS BELOW vvvvvvvvvvvvvvvvvvvvvv
           
    def pixal_ruler(self):
        imgN=""
    
        if "1" in self.ids.image.source:
            imgN=self.ids.image.source[:-5]+self.ids.image.source[-4:]
            self.load_image(imgN)
        
        
        
    def bluetogreenimage(self):#,name): #Blue to green function
        pixels, width, height, name, img= self.image_prep()
                    
        for y in range(img.size[1]):
            for x in range(img.size[0]):

                if pixels[x,y][2]>=55 and pixels[x,y][0]<155 and pixels[x,y][1]<155:
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
        if "edit" in name:
            name= name[:-4]
        img.save(name+"edit"+self.ids.image.source[-4:])
        self.load_image(name+"edit"+self.ids.image.source[-4:])
            
      
      
      
    def glitching(self):  # Column swaper function
        pixels, width, height, name, img = self.image_prep()
        print(name,self.ids.image.source)
        temp_pixel_list=[]
        temp_pixel=""
        times= 5
        
        for glitch in range(times):
            x = random.randint(0,img.size[0]-1//2)
  
            #y = random.randint(0,img.size[1]-1)
            def boundry_check(x,y):
                more=0
                less=0
                if x + 1 >= img.size[0]:
                    temp_pixel = pixels[x-2,y]
                    more = x-2
                else:
                    temp_pixel = pixels[x+1,y]
                    more = x+1
                if x - 1 <= img.size[0]:
                    temp_pixel = pixels[x+2,y]
                    less = x+2
                else:
                    temp_pixel = pixels[x-1,y]
                    less = x-1
                return more, less
            print("X = ",x)
            for y in range(img.size[1]-1):
                temp_pixel = pixels[x,y]
                temp_pixel_list.append(temp_pixel)
                temp_pixel = pixels[boundry_check(x,y)[0],y]
                temp_pixel_list.append(temp_pixel)
                temp_pixel = pixels[boundry_check(x,y)[1],y]
                temp_pixel_list.append(temp_pixel)
           
                
            for y in range(img.size[1]-1):
                pixels[x,y] = pixels[-1*x,y]
                pixels[boundry_check(x,y)[0],y] = pixels[boundry_check(-1*x,y)[0],y]
                pixels[boundry_check(x,y)[1],y] = pixels[boundry_check(-1*x,y)[1],y]
    
            for pixel in temp_pixel_list:
                pixels[-(pixel[0]),y]= pixel
        
        if "edit" in name:
            name= name[:-4]
        img.save(name+"edit"+self.ids.image.source[-4:])
        self.load_image(name+"edit"+self.ids.image.source[-4:])
            
        
    def sepiaimage(self): # Sepia function
        pixels, width, height, name, img = self.image_prep()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x,y][0]*0.393 + pixels[x,y][1]*0.769 + pixels[x,y][2]*0.189
                green = pixels[x,y][1]*0.769 + pixels[x,y][0]*0.393 + pixels[x,y][2]*0.189
                blue = pixels[x,y][2]*0.189 + pixels[x,y][0]*0.393 + pixels[x,y][1]*0.769
                transparency = pixels[x,y][3]
                pixels[x,y] = (int(red), int(green), int(blue),transparency)
        if "edit" in name:
            name= name[:-4]
        img.save(name+"edit"+self.ids.image.source[-4:])
        self.load_image(name+"edit"+self.ids.image.source[-4:])

    def invertion(self): # Invert image function
        pixels, width, height, name, img = self.image_prep()
        
 
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x,y][0]
                green = 255 - pixels[x,y][1]
                blue = 255 - pixels[x,y][2]
                transparency = 255 - pixels[x,y][3]
                pixels[x,y] = (red, green, blue)
        if "edit" in name:
            name= name[:-4]
        img.save(name+"edit"+self.ids.image.source[-4:])
        self.load_image(name+"edit"+self.ids.image.source[-4:])
        
    def mirror_vertical(self): # Left side and right side swaper func
        pixels, width, height, name, img = self.image_prep()
        img2 = Image.open(name+self.ids.image.source[-4:])
        pixels2=img2.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                pixels[x*-1,y] = pixels2[x,y]
    
        if "edit" in name:
            name= name[:-4]
        img.save(name+"edit"+self.ids.image.source[-4:])
        self.load_image(name+"edit"+self.ids.image.source[-4:])
      
      
    def mirror_horizontal(self):
        pixels, width, height, name, img = self.image_prep()
        img2 = Image.open(name+self.ids.image.source[-4:])
        pixels2=img2.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                pixels[x,y*-1] = pixels2[x,y]
        if "edit" in name:
            name= name[:-4]
        img.save(name+"edit"+self.ids.image.source[-4:])
        self.load_image(name+"edit"+self.ids.image.source[-4:])
      
    def pixalated_spot(self,x, y): # Pixalating a spot func
        
        def box( x, y, width, height, color):#, image, name):
            for _y_pixels in range(width-1):
                for _x_pixels in range(height-1):
                    if x+_x_pixels < width and y+_y_pixels < height:
                        pixels[x+_x_pixels,y+_y_pixels]= color
        
        pixels, width, height, name, img = self.image_prep()
        numbers="0123456789"
        run = True
        if x == "" or not x[0] in numbers:
            run = False
            self.manager.current = "wrong"
        else:
            x = int(x)
            if x >= width or x < 1:
                run = False
                self.manager.current = "wrong"
        if y == "" or not y[0] in numbers:
            run = False
            self.manager.current = "wrong"
        else:
            y = height-int(y)
            if y >= height or y < 1:
                run = False
                self.manager.current = "wrong"
        
        _y_devided=height//8
        _x_devided=width//8
        
        color=(255,255,255)
        
        if run == True:
            for _y_pixels in range(0,width,_y_devided):
                for _x_pixels in range(0,height,_x_devided):
                    if x+_x_pixels < width and y+_y_pixels < height:
                        color=pixels[_x_pixels+x,_y_pixels+y]
                    box(_x_pixels+x, _y_pixels+y, _y_devided, _x_devided, color)
            if "edit" in name:
                name= name[:-4]
            img.save(name+"edit"+self.ids.image.source[-4:])
            self.load_image(name+"edit"+self.ids.image.source[-4:])

#mirror_vertical(HatKid,HatKid2)
    
    
class CorrectScreen(Screen):
    def next(self):
        self.manager.current = "question2"
/Users/iggy/Desktop/PhotoEditor/fnafedit.jpg
/Users/iggy/Desktop/PhotoEditor/nightskyedit.png
class WrongScreen(Screen):
    def next(self):
        self.manager.current = "question2"

QuizPageApp().run()
