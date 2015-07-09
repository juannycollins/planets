#!/Users/johnnycollins/anaconda/bin/python
import re, sys, os
import numpy
import graphics
def main():
     filename = 'to_pytot'
     """print filename"""
     fn=open(filename,'r')
     lines=fn.readlines()
     tot = numpy.double(0)
     degree = numpy.arctan(1.0)/45.0

 
     """
     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
     """
     win = graphics.GraphWin("circle",800,800)
     x_mid=[]
     y_mid=[]
     x_mid= [500,300,300,500,400]
     y_mid= [400,400,500,500,300]
     xmiddle = 400
     ymiddle = 400
     radius = 20
     totxy = tot_xy_class(x_mid,y_mid)
     totxy.pppp()
     tl=totxy.totlength()

     """
     dot the figure
     """
     ic = 0	
     totx=0
     toty=0
     for xm in x_mid:
          ym = y_mid[ic]
          pt = graphics.Point(xm,ym)
          pt.draw(win)
          totx = totx+xm
          toty = toty+ym
          ic = ic+1

     avgx = totx/ic
     avgy = toty/ic
     pt = graphics.Point(avgx,avgy)
     pt.draw(win)
     dist = 0
     icc =0
     iii = len(x_mid)
     for xmm in range(iii-1):
          ymm = y_mid[icc]
          ic=0
          xm = x_mid[icc+1]
          ym = y_mid[icc+1]

          dist = dist+(numpy.sqrt(numpy.square(xm -xmm)+numpy.square(ym-ymm)))
          icc=icc+1
	
          xm = x_mid[0]
          xmm = x_mid[iii-1]
          ym = y_mid[0]
          ymm = y_mid[iii-1]
	   
          dist = dist+(numpy.sqrt(numpy.square(xm -xmm)+numpy.square(ym-ymm)))
	
          print ("dist=",dist)
	
	
          """
          march from first point to second point
          """

          """
          make a list of angles for each point
          The angle is the angle formed between the x axcis and the
          line out to the point from avgx,avgy
          """	
     ang=[]
     for i in range(len(x_mid)):
          xm = x_mid[i]
          ym = y_mid[i]
          dnom = (avgx-xm)
          numer = (avgy-ym)
          if dnom == 0:
               dnom = 1
          frac =numer/dnom


          tmpang = (numpy.arctan(numer/dnom)/degree)




          if(dnom < 0 and numer < 0):
               ang.append(-tmpang) 
          if(dnom < 0 and numer > 0):
               ang.append(tmpang) 
          if(dnom > 0 and numer > 0):
               ang.append(tmpang+90)
          if(dnom > 0 and numer < 0):
               ang.append(tmpang+180)


     rrr = 100
     delt =1.0/100.0
     
     print (" angle list=",ang)


     for np in range(len(x_mid)):
          """
          draw dots
          """
          for np1 in range(len(x_mid)):
               if(np != np1):
                    seg = dotaline(x_mid[np],y_mid[np],x_mid[np1],y_mid[np1],win)
                    seg.pppp()
                    """seg.oval_up( tl )"""
                    seg.oval_pump(.5,(tl-100), ang[np],ang[np1])

     filename = raw_input('Enter the name of the file you want to read ')
     win.close()
	

class tot_xy_class:
     def __init__(self,xlist,ylist):
          self.xl = xlist
          self.yl = ylist
     def pppp(self):
          print (" xlist=")
          print (self.xl)
          print (" ylist=")
          print (self.yl)
     def totlength(self):
          lll = len(self.xl)
          the_length = 0
          for i in range(lll-2):
               nx = i+1
               x1 = self.xl[i]
               x2 = self.xl[nx]
               y1 = self.yl[0]
               y2 = self.yl[nx]
               print ("xyxyxyxy=",x1,x2,y1,y2)
               the_length = the_length +numpy.sqrt(numpy.square(x1-x2)+numpy.square(y1-y2))
          x1=self.xl[0]
          x2=self.xl[lll-1]
          y1=self.yl[0]
          y2=self.yl[lll-1]
          print ("xyxyxyxy=",x1,x2,y1,y2)
          the_length = the_length +numpy.sqrt(numpy.square(x1-x2)+numpy.square(y1-y2))
          return (the_length)
               

class dotaline:
     def __init__(self, x_1,y_1,x_2,y_2,win):
         self.x1 = x_1
         self.x2 = x_2
         self.y1 = y_1
         self.y2 = y_2
         self.win= win
         self.degree = (numpy.arctan(1.0))/45.0
     def pppp(self):
        print (" in pppp ",self.x1,self.x2,self.y1,self.y2)
        delt =1.0/100.0
        for i in range(100):
           xp = self.x1 + i*delt*(self.x2-self.x1)
           yp = self.y1 + i*delt*(self.y2-self.y1)
           print ("i=",i)
           pt = graphics.Point(xp,yp)
           pt.draw(self.win)
     def length_it(self):
        its_length = numpy.sqrt(numpy.square(self.x2-self.x1)+numpy.square(self.y2-self.y1))
        return its_length


     def oval_up(self,rope_length):
        """
        draw elipse around two points
        """
        

        b = self.length_it()
        a = rope_length - b



        print ("ababababa=",a,b)


        halfx = .5*(self.x2+self.x1)
        halfy = .5*(self.y2+self.y1)

        line_ang = numpy.arctan((self.y2-self.y1)/(self.x2-self.x1))
        perp_ang = line_ang-2.0*numpy.arctan(1.0)

        lowx = halfx - (b-a)*numpy.cos(perp_ang)
        lowy = halfy - (b-a)*numpy.sin(perp_ang)


        """
        Draw perpindicular line
        """
        perpline = dotaline(halfx,halfy,lowx,lowy,self.win)
        perpline.pppp()
        perplen = perpline.length_it()

        denom = halfx-self.x2
        if(denom == 0):
             denom = 1
        start_angle = int( numpy.arctan((halfy-self.y2)/(denom))/self.degree)
        end_angle = start_angle + 360

        
        n = 180
        for i in range(start_angle,end_angle,1):
           ang = i*self.degree
           sang = n*self.degree
           n=n+1
           midx = halfx - a*numpy.sin(sang)*numpy.cos(perp_ang)
           midy = halfy - a*numpy.sin(sang)*numpy.sin(perp_ang)
           x = midx + perplen*numpy.cos(ang)
           y = midy + perplen*numpy.sin(ang)

           pt = graphics.Point(x,y)
           pt.draw(self.win)










     def oval_pump(self,hieght_frac, wire_length,ang1,ang2):
        
        halfx = .5*(self.x2+self.x1)
        halfy = .5*(self.y2+self.y1)
        deenom = self.x2-self.x1
        line_ang = 2.0*numpy.arctan(1.0)
        if(deenom != 0):
             line_ang = numpy.arctan((self.y2-self.y1)/(deenom))
        perp_ang = line_ang-2.0*numpy.arctan(1.0)

        diag = hieght_frac*self.length_it()

        lowx = halfx - diag*numpy.cos(perp_ang)
        lowy = halfy - diag*numpy.sin(perp_ang)

        T_totcirc = 0
        circum = dotaline(lowx,lowy,self.x1,self.y1,self.win)
        T_totcirc = T_totcirc + circum.length_it()

        circum = dotaline(lowx,lowy,self.x2,self.y2,self.win)
        T_totcirc = T_totcirc + circum.length_it()

        T_totcirc = T_totcirc + self.length_it()

        print (" T_totcirc=", T_totcirc)

        """
        Draw perpindicular line
        """
        perpline = dotaline(halfx,halfy,lowx,lowy,self.win)
        perpline.pppp()
        perplen = perpline.length_it()

        denom = halfx-self.x2
        if(denom == 0):
             denom = 1
        start_angle = int( numpy.arctan((halfy-self.y2)/(denom))/self.degree)

        end_angle = start_angle + 360

        
        n = 180

 

        for i in range(start_angle,end_angle):
           ang = i*self.degree
 
           x_loc = 0
           y_loc = 0
           (x_loc,y_loc)=self.angle_loc(i,x_loc,y_loc)

           rightd = 0
           i_totcirc = int(T_totcirc)
           the_diag = self.what_the_d(i,i_totcirc,rightd)

           print (" the_diag=",the_diag,i_totcirc)

           x = x_loc + the_diag *numpy.cos(ang)
           y = y_loc + the_diag *numpy.sin(ang)




           pt = graphics.Point(x,y)
           pt.draw(self.win)

           
     def angle_loc(self,in_angle,x_ang_loc,y_ang_loc):


          x_ang_loc = 1
          y_ang_loc = 1
          """
          in_angle is expecte in degrees (0-360)
          This routine returns the location on the line between
          x1,y1 and x2,y2 where the angle slits off to make the 
          elipse.
          Angles 90 and 270 are at the mid point between
          x1,y1 and x2,y2.
              x_ang_loc = .5*(self.x1+self.x2)
              y_ang_loc = .5*(self.y1+self.y2)
          Angle 180 
              x_ang_loc = x1
              y_ang_loc = y1
          Angle 0
              x_ang_loc = x2
              y_ang_loc = y2
          """
          while(in_angle > 360):
               in_angle = in_angle-360
          while(in_angle < 0):
               in_angle = in_angle+360

          if(in_angle < 181):
               frac = float(in_angle)/180.0
               x_ang_loc = int(float(self.x1) + frac *float(self.x2-self.x1))
               y_ang_loc = int(float(self.y1) + frac *float(self.y2-self.y1))
          else:
               frac = (float(in_angle)-180.0)/180.0
               x_ang_loc = int(float(self.x2) + frac *float(self.x1-self.x2))
               y_ang_loc = int(float(self.y2) + frac *float(self.y1-self.y2))
          return (x_ang_loc,y_ang_loc)

     def what_the_d(self,anglein,tot,rightd):
          
           
          ang = anglein*self.degree
 
          x_loc = 0
          y_loc = 0
          (x_loc,y_loc)=self.angle_loc(int(anglein),x_loc,y_loc)

          rightd = 0
          x = 0
          y = 0
          totcirc = 0
          while totcirc < tot:
               totcirc = 0
               rightd = rightd + 1
               x = x_loc + (rightd)*numpy.cos(ang)
               y = y_loc + (rightd)*numpy.sin(ang)

               circum = dotaline(x,y,self.x1,self.y1,self.win)
               totcirc = totcirc + circum.length_it()

               circum = dotaline(x,y,self.x2,self.y2,self.win)
               totcirc = totcirc + circum.length_it()

               totcirc = totcirc + self.length_it()
          print (" tot=",tot)
          return (rightd)

          
if __name__ == "__main__":
    main()
