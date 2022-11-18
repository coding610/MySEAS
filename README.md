# MySEAS
## Introduction
This is the second version of SEAS, called MySEAS. The old SEAS will be rewritten in this repo, but still simillar two its cousin. This is used for educational purposes only, aimed at one who is new to coding and game development. You'll best understand the code if your familiar with OOP, but you dont have to understand it
to use it. The game engine is written in python ontop of pygame. Pygame is amazing and I've worked with it for a while but I wanted to tackle a new challenge. This is no way a replacment for pygame but I like the structure this provides.

## Why
As I mentioned in the introduction I built this for me only. I was in no way hoping for other people to use this when I made the first version, and I'm still against it. Your of course welcome to use it as you wish. If you would use it I'd recommend using it for educational purposes only. You can learn it yourself if
you're part of the targetted audince. Theres a "documentation.md" in the base folder. There is everything you need to know!

## A quick demo
```
import MySEAS

MySEAS.MOEC.setWnDimensions([1280, 800])
mainScene = MySEAS.MOEC.newScene(name='mainScene', isTargeted=True)

mainScene.newObject(name='Ob1',
                    components=[MySEAS.RenderPoly(),
                    MySEAS.transformPoly([100, 100], [150, 150], [170, 180])])

MySEAS.run()
```
This demo is minimal and great if you encounter any problems downloading the module. MOEC stands for "My Over Engineered Core". Theres also MOES for scene and more.

## Download
This project is available at pypi by the name of My-SEAS. Ive linked it below in the "Refered" tab. Just install it by using pip. If you find trouble getting the latest version try

```
pip3 install My-SEAS==<version>
```

## Refered links
https://pypi.org/project/My-SEAS/
