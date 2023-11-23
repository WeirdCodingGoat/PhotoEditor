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
            
    def image_size(self):
        img=Image.open(self.ids.image.source)
        pixels = img.load()
        width, height = img.size
        return pixels, width
        
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
        width, height = img.size
        
        #print("(",1,2,")","\nWidth:", width, "\nHeight:", height)
        return pixels, width, height, name, img
            
            
            
            
            
            
                    #     IMAGE EDITING FUNCTIONS BELOW vvvvvvvvvvvvvvvvvvvvvv
    def pixal_ruler(self):
        pixels, width, height, name, img= self.image_prep()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if x > img.size[0]//20: # X SPACE FOR CORNER
                    if x % 100 == 0 and y < img.size[1]//15: # BIG MARKERS
                        if pixels[x,y][0] > 255//2 and pixels[x,y][1] > 255//2 or pixels[x,y][0] > 255//2 and pixels[x,y][2] > 255//2 or pixels[x,y][1] > 255//2 and pixels[x,y][2] > 255//2:
                            pixels[x,y] = (0,0,0)
                            pixels[x-1,y] = (0,0,0)
                            pixels[x+1,y] = (0,0,0)
                        else:
                            pixels[x,y] = (255,255,255)
                            pixels[x-1,y] = (255,255,255)
                            pixels[x+1,y] = (255,255,255)
                        if "png" in self.ids.image.source:
                            pixels[x,y] = (pixels[x,y][0],pixels[x,y][1],pixels[x,y][2],255)
                            pixels[x-1,y] = (pixels[x,y][0],pixels[x-1,y][1],pixels[x-1,y][2],255)
                            pixels[x+1,y] = (pixels[x,y][0],pixels[x+1,y][1],pixels[x+1,y][2],255)
                    elif x % 10 == 0 and y < (img.size[1]/15)//2: # SMALL MARKERS
                        if pixels[x,y][0] > 255//2 and pixels[x,y][1] > 255//2 or pixels[x,y][0] > 255//2 and pixels[x,y][2] > 255//2 or pixels[x,y][1] > 255//2 and pixels[x,y][2] > 255//2:
                            pixels[x,y] = (0,0,0)
                        else:
                            pixels[x,y] = (255,255,255)
                        if "png" in self.ids.image.source:
                            pixels[x,y] = (pixels[x,y][0],pixels[x,y][1],pixels[x,y][2],255)
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if y > img.size[1]//20: # Y SPACE FOR CORNER
                    if y % 100 == 0 and x < img.size[0]//10: # BIG MARKERS
                        if pixels[x,y][0] > 255//2 and pixels[x,y][1] > 255//2 or pixels[x,y][0] > 255//2 and pixels[x,y][2] > 255//2 or pixels[x,y][1] > 255//2 and pixels[x,y][2] > 255//2:
                            pixels[x,y] = (0,0,0)
                            pixels[x,y-1] = (0,0,0)
                            pixels[x,y+1] = (0,0,0)
                        else:
                            pixels[x,y] = (255,255,255)
                            pixels[x,y-1] = (255,255,255)
                            pixels[x,y+1] = (255,255,255)
                        if "png" in self.ids.image.source:
                            pixels[x,y] = (pixels[x,y][0],pixels[x,y][1],pixels[x,y][2],255)
                            pixels[x,y-1] = (pixels[x,y-1][0],pixels[x,y-1][1],pixels[x,y-1][2],255)
                            pixels[x,y+1] = (pixels[x,y+1][0],pixels[x,y+1][1],pixels[x,y+1][2],255)
                    elif y % 10 == 0 and x < (img.size[0]/15)//2: # SMALL MARKERS
                        if pixels[x,y][0] > 255//2 and pixels[x,y][1] > 255//2 or pixels[x,y][0] > 255//2 and pixels[x,y][2] > 255//2 or pixels[x,y][1] > 255//2 and pixels[x,y][2] > 255//2:
                            pixels[x,y] = (0,0,0)
                        else:
                            pixels[x,y] = (255,255,255)
                        if "png" in self.ids.image.source:
                            pixels[x,y] = (pixels[x,y][0],pixels[x,y][1],pixels[x,y][2],255)
        imgN=self.ids.image.source[:-4]+"1"+self.ids.image.source[-4:]
        img.save(imgN)
        self.load_image(imgN)
           
    def ruler_toggle(self):
        imgN=""
        pixels, width, height, name, img= self.image_prep()
        if "1" in self.ids.image.source:
            imgN=self.ids.image.source[:-5]+self.ids.image.source[-4:]
            self.load_image(imgN)
        else:
            self.pixal_ruler()
            

        
        
        
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
        temp_pixel_list=[]
        temp_pixel=""
        times= 5
        next_pix=0
        
        def boundry_check(x):
            more=0
            less=0
            if x + 1 >= img.size[0]:
                more = x-2
            else:
                more = x+1
            if x - 1 <= 0:
                less = x+2
            else:
                less = x-1
            return more, less
        for glitch in range(times):
            x = random.randint(0,(img.size[0]-1)//2)
            #y = random.randint(0,img.size[1]-1)
            right=boundry_check(x)[0]
            left=boundry_check(x)[1]
            for y in range(img.size[1]-1):
                temp_pixel = pixels[x,y] #MIDLE
                
                if len(temp_pixel_list) <= x:
                    while len(temp_pixel_list) <= x:
                        temp_pixel_list.append([])
                #print(len(temp_pixel_list)<x)
                temp_pixel_list[x].append(temp_pixel)
                
                temp_pixel = pixels[right,y] # RIGHT SIDE
                if len(temp_pixel_list) <= right:
                    while len(temp_pixel_list) <= right:
                        temp_pixel_list.append([])
                temp_pixel_list[right].append(temp_pixel)
                
                temp_pixel = pixels[left,y] # LEFT SIDE
                if len(temp_pixel_list) <= left:
                    while len(temp_pixel_list) <= left:
                        temp_pixel_list.append([])
                temp_pixel_list[left].append(temp_pixel)
           
                
            for y in range(img.size[1]-1):
                pixels[x,y] = pixels[-1*x,y]
                pixels[right,y] = pixels[right*-1,y]
                pixels[left,y] = pixels[left*-1,y]
            
            for y in range(img.size[1]-1):
                pixels[-1*x,y] = temp_pixel_list[x][y]
                pixels[-1*right,y] = temp_pixel_list[right][y]
                pixels[-1*left,y] = temp_pixel_list[left][y]
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
                if ".png" in self.ids.image.source:
                    transparency = pixels[x,y][3]
                    pixels[x,y] = (int(red), int(green), int(blue),transparency)
                else:
                    pixels[x,y] = (int(red), int(green), int(blue))
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
                #transparency = 255 - pixels[x,y][3]
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
        pixels, width, height, name, img = self.image_prep()
        numbers="0123456789"
        x_length = 0
        y_length = 0
        run = True
        
        def box( x, y, width, height, color):# Individual pixel spots
            #print(" W=",width,"H=",height)
            for _y_pixels in range(width):
                for _x_pixels in range(height):
                    #print("",x+_x_pixels,y+_y_pixels)
                    if x+_x_pixels < img.size[0] and y+_y_pixels < img.size[1]:
                        pixels[x+_x_pixels,y+_y_pixels]= color
                
        
        if x == "" or not x[0] in numbers or not "," in x or "." in x:
            run = False
            self.manager.current = "wrong"
        else:
            x_length = int(x[x.find(",")+1:])
            x = int(x[:x.find(",")])
            if x+x_length >= width or x < 0:
                run = False
                self.manager.current = "wrong"
        if y == "" or not y[0] in numbers or not "," in y or "." in y:
            run = False
            self.manager.current = "wrong"
        else:
            y_length = int(y[y.find(",")+1:])
            y = int(y[:y.find(",")])
            if y+y_length >= height or y < 0:
                run = False
                self.manager.current = "wrong"
        _y_devided=y_length//8
        _x_devided=x_length//8
        
        color=(0,0,0) #25,100 70,100 Creeper.png
        if run == True:
            for _y_pixels in range(0,y_length,_y_devided):
                for _x_pixels in range(0,x_length,_x_devided):
                   # print(" 1y=",_y_pixels,"1x=",_x_pixels)
                    color=pixels[_x_pixels+x,_y_pixels+y]
                   # print(_x_pixels+x, _y_pixels+y, _y_devided, _x_devided, color)
                    if x+_x_pixels < img.size[0] and y+_y_pixels < img.size[1]:
                        box(_x_pixels+x, _y_pixels+y, _y_devided, _x_devided, color)
            if "edit" in name:
                name= name[:-4]
            img.save(name+"edit"+self.ids.image.source[-4:])
            self.load_image(name+"edit"+self.ids.image.source[-4:])

#mirror_vertical(HatKid,HatKid2)
    
    
class CorrectScreen(Screen):
    def next(self):
        self.manager.current = "question2"

class WrongScreen(Screen):
    def next(self):
        self.manager.current = "question2"

QuizPageApp().run()
