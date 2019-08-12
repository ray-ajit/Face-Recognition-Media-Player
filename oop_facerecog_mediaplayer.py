class FacePlayer():
    def __init__(self):
        import vlc
        import cv2
        import face_recognition as fc

    def userFace(self,img_path):
        self.img_path=img_path
        self.img=fc.load_image_file(self.img_path)
        self.face_location=fc.face_locations(self.img)
        self.encd=fc.face_encodings(self.img,self.face_location)[0]

        
    def run(self,path,name):
        self.path=path
        self.audio=vlc.MediaPlayer(self.path)
        self.cap=cv2.VideoCapture(0)
        self.name=name
        self.count=1
        
        while True:
            self.res=[]
            self.ret,self.frame=self.cap.read()
            self.fl1=fc.face_locations(self.frame)

            if len(self.fl1)>0:
                self.enc=fc.face_encodings(self.frame,self.fl1)[0]
                self.res=fc.compare_faces([self.encd],self.enc)
   
            if True in self.res:
                print('Hey {}'.format(self.name))
                self.audio.play()
                self.count=0
                continue
            
            else:
                if self.count==0:
                    self.audio.pause()
                    self.count+=1

            self.k=cv2.waitKey(1)
            if self.k==ord('q'):
                self.audio.stop()
                break          
                
        cv2.destroyAllWindows()
        self.cap.release
        
if __name__=='__main__':
    import vlc
    import cv2
    import face_recognition as fc

    img_path=input('Enter the image path of the User.\n')
    name=input('Enter the users name.\n')
    player=FacePlayer()
    player.userFace(img_path)
    path=input('Enter the Song Path.\n')
    player.run(path,name)
