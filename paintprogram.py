from random import*
from pygame import*
from math import*
##from glob import*
##
##
##def getName(screen,showFiles):
##    ans = ""                   
##    arialFont = font.SysFont("Times New Roman", 16)
##    back = screen.copy()        
##    textArea = Rect(5,5,200,25)
##    screen.fill((255,255,255))
##    typing = True
##    while typing:
##        for evnt in event.get():
##            if evnt.type == QUIT:
##                event.post(e)
##                return ""
##            if evnt.type == KEYDOWN:
##                if evnt.key == K_BACKSPACE:    
##                    if len(ans)>0:
##                        ans = ans[:-1]
##                elif evnt.key == K_KP_ENTER or e.key == K_RETURN : 
##                    typing = False
##                elif evnt.key < 256:
##                    ans += evnt.unicode      
##                    
##        txtPic = arialFont.render(ans, True, (0,0,0))   
##        draw.rect(screen,(220,255,220),textArea)       
##        draw.rect(screen,(0,0,0),textArea,2)            
##        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
#----------------------------Appearance------------------------------------
#screen size
screen=display.set_mode((1024,768))
display.set_caption("Vongola Paint")


#-----------------------------music--------------------------------------

init()
mixer.music.load("songs/BAG.mp3")       # load a MUSIC object
mixer.music.play(-1)

musicRect=Rect(200,10,40,40)
music2Rect=Rect(240,10,40,40)
picVolumeC=image.load("functions/music/volumeC.png")
picVolumeW=image.load("functions/music/volumeW.png")
screen.blit(picVolumeW,(200,10))
picMuteC=image.load("functions/music/muteC.png")
picMuteW=image.load("functions/music/muteW.png")
#-------------------------------------text

#--------------------------------main background--------------------------
pic=image.load("Hitman Reborn343434.jpg")
screen.blit(pic,(0,0))

allRect=Rect(844,170,147,440)
#---------------------------------------reload-----------------------------

reloadRect = Rect(700,10,40,40)

#---------------------------------first Background--------------------------
draw.rect(screen,(230,141,161,255),(20,643,809,115))

#canvas
canvasRect=Rect(195,175,627,440)


#colour scale
colourscaleRect=Rect(834,620,175,116)
draw.rect(screen,(255,255,255),colourscaleRect,5)

#-----------------------------function--------------------------------------
#colour
c=(0,0,0)

#pencil
tool="pencil"
pencilRect = Rect(100,208,40,40)
picPencilC=image.load("functions/Pencil/pencilC.png")
picPencilW=image.load("functions/Pencil/pencilW.png")
screen.blit(picPencilW,(102,208))

#eraser
tool="eraser"
eraserRect = Rect(51,208,40,40)
picEraserC=image.load("functions/eraser/eraserC.png")
picEraserW=image.load("functions/eraser/eraserW.png")
screen.blit(picEraserW,(-132,125))

#Spray
tool="spray"
SPRect = Rect(50,259,40,40)
picSprayC=image.load("functions/spraypaint/spraypaintC.png")
picSprayW=image.load("functions/Spraypaint/spraypaintW.png")
screen.blit(picSprayW,(-10,200))

#brush
tool="brush"
brushRect = Rect(100,259,40,40)
picBrushC=image.load("functions/paintbrush/brushC.png")
picBrushW=image.load("functions/paintbrush/brushW.png")
screen.blit(picBrushW,(-28,90))


#line
tool="line"
lineRect = Rect(100,312,40,40)
picLineC=image.load("functions/line/lineC.png")
picLineW=image.load("functions/line/linew.png")
screen.blit(picLineW,(-45,155))

#square
tool="square"
squareRect = Rect(50,312,40,40)
picSquareC=image.load("functions/square/squareC.png")
picSquareW=image.load("functions/square/squarew.png")
screen.blit(picSquareW,(54,318))



#paint
tool="paint"
paintRect = Rect(50,366,40,40)
picPaintC=image.load("functions/paintcan/paintcanC.png")
picPaintW=image.load("functions/paintcan/paintcanw.png")
screen.blit(picPaintW,(53,366))


#ellipse
ellipseRect = Rect(100,366,40,40)
draw.rect(screen,(150,150,150),ellipseRect,4)
picEllipseC=image.load("functions/ellipse/ellipseC.png")
picEllipseW=image.load("functions/ellipse/ellipsew.png")
screen.blit(picEllipseW,(100,366))

#copy
copyRect = Rect(100,416,40,40)
picCopyC=image.load("functions/copy/copyC.png")
picCopyW=image.load("functions/copy/copyw.png")
screen.blit(picCopyW,(100,416))

#paste
pasteRect = Rect(50,416,40,40)
picPasteC=image.load("functions/paste/pasteC.png")
picPasteW=image.load("functions/paste/pastew.png")
screen.blit(picPasteW,(50,419))

#save
saveRect = Rect(30,468,125,38)
picSaveC=image.load("functions/save/SaveC.png")
picSaveW=image.load("functions/save/Savew.png")
screen.blit(picSaveW,(35,478))

#undo
undoRect = Rect(30,511,125,38)
picUndoC=image.load("functions/undo/UndoC.png")
picUndoW=image.load("functions/undo/Undow.png")
screen.blit(picUndoW,(35,521))

#redo
redoRect = Rect(30,554,125,38)
picRedoC=image.load("functions/redo/RedoC.png")
picRedoW=image.load("functions/redo/Redow.png")
screen.blit(picRedoW,(35,564))

#bomb
bombRect=Rect(150,10,40,40)
draw.rect(screen,(70,70,70),bombRect)
picBombC=image.load("functions/bomb/bombC.png")
picBombW=image.load("functions/bomb/bombw.png")
screen.blit(picBombW,(33,-88))

#drop
dropRect=Rect(750,10,40,40)
draw.rect(screen,(70,70,70),dropRect)
draw.rect(screen,(150,150,150),dropRect,4)
picDropC=image.load("functions/dropper/dropperC.png")
picDropW=image.load("functions/dropper/dropperw.png")
screen.blit(picDropW,(750,10))
#-------------------------------backgrounds-------------------------------

#VongolaFamily
VFRect=Rect(859,184,118,87)
draw.rect(screen,(150,150,150),VFRect,2)
picVFBC=image.load("backgrounds/VongolaFamilyBC.png")
picVFSC=image.load("backgrounds/VongolaFamilySC.png")
picVFSW=image.load("backgrounds/VongolaFamilySW.png") 
screen.blit(picVFSW,(859,186))

#Arcobaleno
AFRect=Rect(859,292,120,87)
draw.rect(screen,(150,150,150),AFRect,2)
picAFBC=image.load("backgrounds/ArcobalenoBC.png")
picAFSC=image.load("backgrounds/ArcobalenoSC.png")
picAFSW=image.load("backgrounds/ArcobalenoSW.png")
screen.blit(picAFSW,(861,293))

#PrimoFamily
PFRect=Rect(859,394,120,87)
draw.rect(screen,(150,150,150),PFRect,2)
picPFBC=image.load("backgrounds/PrimoFamilyBC.png")
picPFSC=image.load("backgrounds/PrimoFamilySC.png")
picPFSW=image.load("backgrounds/PrimoFamilySW.png")
screen.blit(picPFSW,(861,395))

#Varia family
VaFRect=Rect(859,500,120,87)
draw.rect(screen,(150,150,150),VaFRect,2)
picVaFBC=image.load("backgrounds/Varia familyBC.png")
picVaFSC=image.load("backgrounds/Varia familySC.png")
picVaFSW=image.load("backgrounds/Varia familySW.png")
screen.blit(picVaFSW,(861,501))
#-----------------------------stamps--------------------------------------
#Tuna
Stamps1Rect=Rect(25,657,80,85)
draw.rect(screen,(150,150,150),Stamps1Rect,5)
picTunaBC=image.load("stamps/TunaBC.png")
picTunaFC=image.load("stamps/TunaFC.png")
picTunaFW=image.load("stamps/TunaFW.png")
screen.blit(picTunaFW,(27,660))

#Gokudera
Stamps2Rect=Rect(115,657,80,85)
draw.rect(screen,(150,150,150),Stamps2Rect,5)
picGokuderaBC=image.load("stamps/GokuderaBC.png")
picGokuderaFC=image.load("stamps/GokuderaFC.png")
picGokuderaFW=image.load("stamps/GokuderaFW.png")
screen.blit(picGokuderaFW,(117,660))

#Takeshi
Stamps3Rect=Rect(205,657,80,85)
draw.rect(screen,(150,150,150),Stamps3Rect,5)
picTakeshiBC=image.load("stamps/TakeshiBC.png")
picTakeshiFC=image.load("stamps/TakeshiFC.png")
picTakeshiFW=image.load("stamps/TakeshiFW.png")
screen.blit(picTakeshiFW,(207,660))

#Reborn
Stamps4Rect=Rect(295,657,80,85)
draw.rect(screen,(150,150,150),Stamps4Rect,5)
picRebornBC=image.load("stamps/RebornBC.png")
picRebornFC=image.load("stamps/RebornFC.png")
picRebornFW=image.load("stamps/RebornFW.png")
screen.blit(picRebornFW,(297,660))

#Ryouhei
Stamps5Rect=Rect(385,657,80,85)
draw.rect(screen,(150,150,150),Stamps5Rect,5)
picRyouheiBC=image.load("stamps/RyouheiBC.png")
picRyouheiFC=image.load("stamps/RyouheiFC.png")
picRyouheiFW=image.load("stamps/RyouheiFW.png")
screen.blit(picRyouheiFW,(387,660))

#Lambo
Stamps6Rect=Rect(475,657,80,85)
draw.rect(screen,(150,150,150),Stamps6Rect,5)
picLamboBC=image.load("stamps/LamboBC.png")
picLamboFC=image.load("stamps/LamboFC.png")
picLamboFW=image.load("stamps/LamboFW.png")
screen.blit(picLamboFW,(477,660))

#Hibari
Stamps7Rect=Rect(565,657,80,85)
draw.rect(screen,(150,150,150),Stamps7Rect,5)
picHibariBC=image.load("stamps/HibariBC.png")
picHibariFC=image.load("stamps/HibariFC.png")
picHibariFW=image.load("stamps/HibariFW.png")
screen.blit(picHibariFW,(567,660))

#Kyouko
Stamps8Rect=Rect(655,657,80,85)
draw.rect(screen,(150,150,150),Stamps8Rect,5)
picKyoukoBC=image.load("stamps/KyoukoBC.png")
picKyoukoFC=image.load("stamps/KyoukoFC.png")
picKyoukoFW=image.load("stamps/KyoukoFW.png")
screen.blit(picKyoukoFW,(657,660))

#Haru
Stamps9Rect=Rect(745,657,80,85)
draw.rect(screen,(150,150,150),Stamps9Rect,5)
picHaruBC=image.load("stamps/HaruBC.png")
picHaruFC=image.load("stamps/HaruFC.png")
picHaruFW=image.load("stamps/HaruFW.png")
screen.blit(picHaruFW,(747,660))
#-----------------------------tools---------------------------------------
tool="pencil"
start = 0,0

#-----------------------------------music---------------------------------
music="on"
draw.rect(screen,(200,200,200),(musicRect))
draw.rect(screen,(0,0,255),(musicRect),2)
screen.blit(picVolumeC,(200,10))
draw.rect(screen,(200,200,200),(music2Rect))
draw.rect(screen,(230,141,161),(music2Rect),2)
screen.blit(picMuteW,(240,10))
#-------------------------------reload------------------------------------
draw.rect(screen,(255,255,255),(reloadRect))
draw.rect(screen,(200,200,200),(reloadRect),2)
picReloadC=image.load("functions/open folder/folderC.png")
picReloadW=image.load("functions/open folder/folderW.png")
screen.blit(picReloadW,(700,10))
picReload=image.load("image/myPic.jpg")
#-----------------------------Mouse---------------------------------------
dx=0
dy=0
undo=[]
redo=[]
canva=screen.subsurface(canvasRect).copy()
undo.append(canva)

size=0
running=True
##y = 20
##message = ""
canva=screen.subsurface(canvasRect).copy()
undo.append(canva)

while running:
    click=False
    mx,my=mouse.get_pos()
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
        if evnt.type==MOUSEBUTTONDOWN:
            click = True
            if canvasRect.collidepoint(mx,my) and evnt.button==1:
                redo=[]
            if evnt.button==1:
                screenpic = screen.copy()
            if evnt.button==3:
                screenpic = screen.copy()
            if evnt.button == 1:
                start = evnt.pos
            if evnt.button == 1:
                bmx,bmy = evnt.pos
            if evnt.button == 3:
                bmx,bmy = evnt.pos
            if evnt.button == 4:
               size += 1
               if size==15:
                   size=14
            if evnt.button == 5:
               size -= 1
               if size==-9:
                   size=-8
        if evnt.type==MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my) or allRect.collidepoint(mx,my):
                if evnt.button==1:
                    canva=screen.subsurface(canvasRect).copy()
                    undo.append(canva)
                if evnt.button==3:
                    canva=screen.subsurface(canvasRect).copy()
                    undo.append(canva)                
                
                
                
                
            
    nmx,nmy=mouse.get_pos()
    mb=mouse.get_pressed()
#-----------------------------save---------------------------------------
    draw.rect(screen,(0,0,255),saveRect,5)
    screen.blit(picSaveW,(35,478))
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,(150,150,150),saveRect,5)
        screen.blit(picSaveC,(35,478))
        if mb[0]==1:
            image.save(screen.subsurface(canvasRect),"image/myPic.jpg")

    picReload=image.load("image/myPic.jpg")
    draw.rect(screen,(200,200,200),(reloadRect),2)
    screen.blit(picReloadW,(700,10))
    if reloadRect.collidepoint(mx,my):
       draw.rect(screen,(255,0,0),(reloadRect),2)
       screen.blit(picReloadC,(700,10))
       if mb[0]==1:
           screen.blit(picReload,(195,175))
#-----------------------------undo & redo--------------------------------
    draw.rect(screen,(0,0,255),undoRect,5)
    screen.blit(picUndoW,(35,521))
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,(150,150,150),undoRect,5)
        screen.blit(picUndoC,(35,521))
    if click and undoRect.collidepoint(mx,my):
        if len(undo)>1:
            redo.append(undo[-1])
            undo.remove(undo[-1])
            pic=undo[-1]
            screen.blit(pic,(195,175))

    draw.rect(screen,(0,0,255),redoRect,5)
    screen.blit(picRedoW,(35,564))
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,(150,150,150),redoRect,5)
        screen.blit(picRedoC,(35,564))
    if click and redoRect.collidepoint(mx,my):
        if len(redo)>0:
            undo.append(redo[-1])
            redo.remove(redo[-1])
            pic=undo[-1]
            screen.blit(pic,(195,175))

#================================colour==================================
    draw.rect(screen,(c),(834,740,175,20))
    draw.rect(screen,(255,255,255),(834,740,175,20),5)
    if mb[0]==1 and colourscaleRect.collidepoint(mx,my):
        c=screen.get_at((mx,my))
 #---------------------------------function------------------------------   


#pencil
    draw.rect(screen,(150,150,150),pencilRect,4)
    screen.blit(picPencilW,(102,208))
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),pencilRect,4)
        screen.blit(picPencilC,(102,208))
        if mb[0]==1:
            tool="pencil"
    if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[0]==1 and canvasRect.collidepoint(nmx,nmy):
            if tool=="pencil":
                screen.set_clip(canvasRect)
                draw.line(screen,(c),(mx,my),(nmx,nmy),1)
            screen.set_clip(None)



#eraser
    draw.rect(screen,(150,150,150),eraserRect,4)
    screen.blit(picEraserW,(-132,125))
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),eraserRect,4)
        screen.blit(picEraserC,(-132,125))
        if mb[0]==1:
            tool="eraser"

    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="eraser":
            screen.set_clip(canvasRect)
            dx = mx-nmx
            dy = my-nmy
            distance=(dx**2+dy**2)**0.5
            if distance==0:
                draw.circle(screen,(255,255,255),(mx,my),10+size)
            else:
                for a in range(int(distance+1)):
                    sx=dx/distance
                    sy=dy/distance
                    draw.circle(screen,(255,255,255),(int(nmx+sx*a),int(nmy+sy*a)),10+size)
            screen.set_clip(None)
#bomb
    draw.rect(screen,(150,150,150),bombRect,4)
    screen.blit(picBombW,(33,-88))
    if bombRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),bombRect,4)
        screen.blit(picBombC,(33,-88))
    if mb[0]==1 and bombRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,255),canvasRect)


##text
##    draw.rect(screen,(150,150,150),textRect,4)
##    if textRect.collidepoint(mx,my):
##        draw.rect(screen,(0,0,255),textRect,4)
##        tool="text"
##    if mb[0]==1 and canvasRect.collidepoint(mx,my):
##        if tool=="text":
##            txt = getName(screen,False)
##            txtPic = comicFont.render(txt, True, (255,0,0))
##            screen.blit(txtPic,(mx,my))
        

#ellipse
    draw.rect(screen,(150,150,150),ellipseRect,4)
    screen.blit(picEllipseW,(100,366))
    if ellipseRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),ellipseRect,4)
        screen.blit(picEllipseC,(100,366))
        if mb[0]==1:
            tool="ellipse"


    if mb[2]==1 and canvasRect.collidepoint(bmx,bmy):
        if tool=="ellipse":
            screen.set_clip(canvasRect)
            screen.blit(screenpic,(0,0))
            elli=Rect(bmx,bmy,mx-bmx,my-bmy)
            elli.normalize()
            draw.ellipse(screen,(c),elli)
            screen.set_clip(None)
    if mb[0]==1 and canvasRect.collidepoint(bmx,bmy):
        if tool=="ellipse":
            screen.set_clip(canvasRect)
            screen.blit(screenpic,(0,0))
            elli=Rect(bmx,bmy,mx-bmx,my-bmy)
            elli.normalize()
            if (mx-bmx)>=4 and (my-bmy)>=4 or (mx-bmx)>=4 and (my-bmy)<=-4 or (mx-bmx)<=-4 and (my-bmy)>=4 or (mx-bmx)<=-4 and (my-bmy)<=-4:
                draw.ellipse(screen,(c),elli,2)
                screen.set_clip(None)
        

#spray can
    draw.rect(screen,(150,150,150),SPRect,4)
    screen.blit(picSprayW,(-10,200))
    if SPRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),SPRect,4)
        screen.blit(picSprayC,(-10,200))
        if mb[0]==1:
            tool="spray"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="spray":
            screen.set_clip(canvasRect)
            for i in range(50):
                dx=randint(mx-10-size,mx+10+size)
                dy=randint(my-10-size,my+10+size)
                d=((dx-mx)**2+(dy-my)**2)**0.5
                if d<=10+size:
                    screen.set_at((dx,dy),(c))
            screen.set_clip(None)

#paint brush
    draw.rect(screen,(150,150,150),brushRect,4)
    screen.blit(picBrushW,(-28,90))
    if brushRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,225),brushRect,4)
        screen.blit(picBrushC,(-28,90))
        if mb[0]==1:
            tool="brush"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="brush":
            screen.set_clip(canvasRect)
            dx = mx-nmx
            dy = my-nmy
            distance=(dx**2+dy**2)**0.5
            if distance==0:
                draw.circle(screen,c,(mx,my),10+size)
            else:
                for k in range(int(distance+1)):
                    sx=dx/distance
                    sy=dy/distance
                    draw.circle(screen,c,(int(nmx+sx*k),int(nmy+sy*k)),10+size)
            screen.set_clip(None)
#lines
    draw.rect(screen,(150,150,150),lineRect,4)
    screen.blit(picLineW,(-45,155))
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),lineRect,4)
        screen.blit(picLineC,(-45,155))
        if mb[0]==1:
            tool="line"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="line":
            screen.set_clip(canvasRect) 
            screen.blit(screenpic,(0,0))
            draw.line(screen, (c), start,(mx,my), 5)
            screen.set_clip(None)
#square
    draw.rect(screen,(150,150,150),squareRect,4)
    screen.blit(picSquareW,(54,318))
    if squareRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),squareRect,4)
        screen.blit(picSquareC,(54,318))
        if mb[0]==1:
            tool="square"


    if mb[0]==1 and canvasRect.collidepoint(bmx,bmy):
        if tool=="square":
            screen.set_clip(canvasRect)
            screen.blit(screenpic,(0,0))
            draw.rect(screen,(c),(bmx,bmy,mx-bmx,my-bmy),3)
            screen.set_clip(None)

    if mb[2]==1 and canvasRect.collidepoint(bmx,bmy):
        if tool=="square":
            screen.set_clip(canvasRect)
            screen.blit(screenpic,(0,0))
            draw.rect(screen,(c),(bmx,bmy,mx-bmx,my-bmy))
            screen.set_clip(None)

#paint
    draw.rect(screen,(150,150,150),paintRect,4)
    screen.blit(picPaintW,(53,366))
    if paintRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),paintRect,4)
        screen.blit(picPaintC,(53,366))
        if mb[0]==1:
            tool="paint"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="paint":
            draw.rect(screen,(c),canvasRect)
            
#copy

    screen.blit(picCopyW,(100,416))
    draw.rect(screen,(150,150,150),copyRect,4)
    if copyRect.collidepoint(mx,my):

        screen.blit(picCopyC,(100,416))
        draw.rect(screen,(0,0,255),copyRect,4)
        if mb[0]==1:
            tool="copy"

    if mb[0]==1 and canvasRect.collidepoint(bmx,bmy):
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            if tool=="copy":
                screen.blit(screenpic,(0,0))
                dx=(mx-bmx)
                dy=(my-bmy)
                draw.rect(screen,(220,220,220),(bmx,bmy,dx,dy),1)
                copy1Rect=(bmx,bmy,dx,dy)
    if mb[2]==1 and tool=="copy":
        image.save(screen.subsurface(copy1Rect),"image/copy1.jpg")
#paste
    screen.blit(picPasteW,(50,419))    
    draw.rect(screen,(150,150,150),pasteRect,4)
    if pasteRect.collidepoint(mx,my):
        screen.blit(picPasteC,(50,419))
        draw.rect(screen,(0,0,255),pasteRect,4)
        if mb[0]==1:
            tool="paste"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool =="paste":
            piccopy1=image.load("image/copy1.jpg")
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect)
            screen.blit(piccopy1,(mx-(dx/2),my-(dy/2)))
            screen.set_clip(None)
#drop
    screen.blit(picDropW,(750,10))
    draw.rect(screen,(150,150,150),dropRect,4)
    if dropRect.collidepoint(mx,my):
        screen.blit(picDropC,(750,10))
        draw.rect(screen,(0,0,255),dropRect,4)
        tool="drop"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool =="drop":
            c=screen.get_at((mx,my))
    
        
#----------------------------background-----------------------------------
#VongolaFamily
    screen.blit(picVFSW,(859,186))
    draw.rect(screen,(150,150,150),VFRect,2)
    if mb[0]==1 and VFRect.collidepoint(mx,my):
        tool=""
        screen.blit(picVFBC,(195,176)) 
    if VFRect.collidepoint(mx,my):
        screen.blit(picVFSC,(859,186)) 
        draw.rect(screen,(255,0,0),VFRect,2)

#Arcobaleno
    screen.blit(picAFSW,(861,293))
    draw.rect(screen,(150,150,150),AFRect,2)
    if mb[0]==1 and AFRect.collidepoint(mx,my):
        tool=""
        screen.blit(picAFBC,(195,176)) 
    if AFRect.collidepoint(mx,my):
        screen.blit(picAFSC,(861,293)) 
        draw.rect(screen,(255,0,0),AFRect,2)

#PrimoFamily
    screen.blit(picPFSW,(861,395))
    draw.rect(screen,(150,150,150),PFRect,2)
    if mb[0]==1 and PFRect.collidepoint(mx,my):
        tool=""
        screen.blit(picPFBC,(195,176)) 
    if PFRect.collidepoint(mx,my):
        screen.blit(picPFSC,(861,395)) 
        draw.rect(screen,(255,0,0),PFRect,2)    

#Varia family
    screen.blit(picVaFSW,(861,501))
    draw.rect(screen,(150,150,150),VaFRect,2)
    if mb[0]==1 and VaFRect.collidepoint(mx,my):
        tool=""
        screen.blit(picVaFBC,(195,176)) 
    if VaFRect.collidepoint(mx,my):
        screen.blit(picVaFSC,(861,501)) 
        draw.rect(screen,(255,0,0),VaFRect,2)        
#--------------------------stamp---------------------------------------------        
#tuna

    draw.rect(screen,(150,150,150),Stamps1Rect,5)
    screen.blit(picTunaFW,(27,660))
    if Stamps1Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),Stamps1Rect,5)
        screen.blit(picTunaFC,(27,660))
        if mb[0]==1:
            tool="stamp1"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="stamp1":
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect) 
            screen.blit(picTunaBC,(mx-50,my-100))
            screen.set_clip(None)

#Gokudera
    draw.rect(screen,(150,150,150),Stamps2Rect,5)
    screen.blit(picGokuderaFW,(117,660))
    if Stamps2Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),Stamps2Rect,5)
        screen.blit(picGokuderaFC,(117,660))
        if mb[0]==1:
            tool="stamp2"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="stamp2":
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect) 
            screen.blit(picGokuderaBC,(mx-50,my-100))
            screen.set_clip(None)

#Takeshi
    draw.rect(screen,(150,150,150),Stamps3Rect,5)
    screen.blit(picTakeshiFW,(207,660))
    if Stamps3Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),Stamps3Rect,5)
        screen.blit(picTakeshiFC,(207,660))
        if mb[0]==1:
            tool="stamp3"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="stamp3":
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect) 
            screen.blit(picTakeshiBC,(mx-50,my-100))
            screen.set_clip(None)

#Reborn
    draw.rect(screen,(150,150,150),Stamps4Rect,5)
    screen.blit(picRebornFW,(297,660))
    if Stamps4Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),Stamps4Rect,5)
        screen.blit(picRebornFC,(297,660))
        if mb[0]==1:
            tool="stamp4"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="stamp4":
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect) 
            screen.blit(picRebornBC,(mx-50,my-75))
            screen.set_clip(None)

#Ryouhei
    draw.rect(screen,(150,150,150),Stamps5Rect,5)
    screen.blit(picRyouheiFW,(387,660))
    if Stamps5Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),Stamps5Rect,5)
        screen.blit(picRyouheiFC,(387,660))
        if mb[0]==1:
            tool="stamp5"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="stamp5":
            
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect) 
            screen.blit(picRyouheiBC,(mx-50,my-100))
            screen.set_clip(None)

#Lambo
    draw.rect(screen,(150,150,150),Stamps6Rect,5)
    screen.blit(picLamboFW,(477,660))
    if Stamps6Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),Stamps6Rect,5)
        screen.blit(picLamboFC,(477,660))
        if mb[0]==1:
            tool="stamp6"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="stamp6":
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect) 
            screen.blit(picLamboBC,(mx-50,my-75))
            screen.set_clip(None)


#Hibari
    draw.rect(screen,(150,150,150),Stamps7Rect,5)
    screen.blit(picHibariFW,(567,660))
    if Stamps7Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),Stamps7Rect,5)
        screen.blit(picHibariFC,(567,660))
        if mb[0]==1:
            tool="stamp7"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="stamp7":
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect) 
            screen.blit(picHibariBC,(mx-50,my-100))
            screen.set_clip(None)

#Kyouko
    draw.rect(screen,(150,150,150),Stamps8Rect,5)
    screen.blit(picKyoukoFW,(657,660))
    if Stamps8Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),Stamps8Rect,5)
        screen.blit(picKyoukoFC,(657,660))
        if mb[0]==1:
            tool="stamp8"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="stamp8":
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect) 
            screen.blit(picKyoukoBC,(mx-50,my-100))
            screen.set_clip(None)

#Haru
    draw.rect(screen,(150,150,150),Stamps9Rect,5)
    screen.blit(picHaruFW,(747,660))
    if Stamps9Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),Stamps9Rect,5)
        screen.blit(picHaruFC,(747,660))
        if mb[0]==1:
            tool="stamp9"
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="stamp9":
            screen.blit(screenpic,(0,0))
            screen.set_clip(canvasRect) 
            screen.blit(picHaruBC,(mx-50,my-100))
            screen.set_clip(None)
    
#------------------------music---------------------------------------
#Music       
#off
    if mb[0]==1 and music=="off" and musicRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),(musicRect),2)
        draw.rect(screen,(230,141,161),(music2Rect),2)
        screen.blit(picVolumeC,(200,10))
        screen.blit(picMuteW,(240,10))
        mixer.music.unpause()
        music="on"
#on
    elif mb[0]==1 and music=="on" and music2Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),(music2Rect),2)
        draw.rect(screen,(230,141,161),(musicRect),2)
        screen.blit(picVolumeW,(200,10))
        screen.blit(picMuteC,(240,10))
        mixer.music.pause()
        music="off"
        
    display.flip()
##font.quit()
##del comicFont
    
quit()


