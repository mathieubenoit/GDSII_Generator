#!/usr/bin/python
import os
import numpy
import gdspy

print('Using gdspy module version ' + gdspy.__version__)


def GeneratePixel(pitchX,pitchY,ALinner_width,Alouter_width,IMPinner_width,IMPouter_width,PORadius,cellname='PIXEL'):
    
    pixel_cell = gdspy.Cell(cellname)

    ## Aluminium Layer
    center = (0,0)
    #ALinner_width = 15
    #ALouter_width = 20
    hiw= ALinner_width/2.0
    radius = (ALouter_width - ALinner_width) / 2.0

    ##### Body
    pixel_cell.add(gdspy.Rectangle(0,(-ALinner_width/2.0+center[0],-ALinner_width/2.0+center[1]), (ALinner_width/2.0+center[0], ALinner_width/2.0+center[1])))
    ##### Sides
    pixel_cell.add(gdspy.Rectangle(0,(hiw,-hiw),(hiw+radius,hiw)))
    pixel_cell.add(gdspy.Rectangle(0,(-hiw,-hiw),(hiw,-hiw - radius)))
    pixel_cell.add(gdspy.Rectangle(0,(-hiw,hiw),(-hiw-radius,-hiw)))
    pixel_cell.add(gdspy.Rectangle(0,(hiw,hiw),(-hiw,hiw+radius)))

    ##### Rounded corners
    pixel_cell.add(gdspy.Round(0, (-hiw, -hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(0, (hiw,-hiw), radius, inner_radius=0,
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
    pixel_cell.add(gdspy.Round(0, (hiw, hiw), radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(0, (-hiw, hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi/2.0,
                          final_angle=numpy.pi))


    ## Implant Layer
    center = (0,0)
    #IMPinner_width = 12
    #IMPouter_width = 15
    hiw= IMPinner_width/2.0
    radius = (IMPouter_width - IMPinner_width) / 2.0

    ##### Body
    pixel_cell.add(gdspy.Rectangle(1,(-IMPinner_width/2.0+center[0],-IMPinner_width/2.0+center[1]), (IMPinner_width/2.0+center[0], IMPinner_width/2.0+center[1])))
16    ##### Sides
    pixel_cell.add(gdspy.Rectangle(1,(hiw,-hiw),(hiw+radius,hiw)))
    pixel_cell.add(gdspy.Rectangle(1,(-hiw,-hiw),(hiw,-hiw - radius)))
    pixel_cell.add(gdspy.Rectangle(1,(-hiw,hiw),(-hiw-radius,-hiw)))
    pixel_cell.add(gdspy.Rectangle(1,(hiw,hiw),(-hiw,hiw+radius)))

    ##### Rounded corners
    pixel_cell.add(gdspy.Round(1, (-hiw, -hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(1, (hiw,-hiw), radius, inner_radius=0,
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
    pixel_cell.add(gdspy.Round(1, (hiw, hiw), radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(1, (-hiw, hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi/2.0,
                          final_angle=numpy.pi))

    # Contact Layer

    #pixel_cell.add(gdspy.Round(2, (3*pitchX/16., 3*pitchY/16.), 2.5))
    #pixel_cell.add(gdspy.Round(2, (-3*pitchX/16., -3*pitchY/16.), 2.5))
    #pixel_cell.add(gdspy.Round(2, (-3*pitchX/16., 3*pitchY/16.), 2.5))
    #pixel_cell.add(gdspy.Round(2, (3*pitchX/16.,-3*pitchY/16.), 2.5))
    pixel_cell.add(gdspy.Round(2,(0,0),8))
    # Passivation Opening
    pixel_cell.add(gdspy.Round(3, (0,0), PORadius))



def GeneratePixelArray(pixelcellname='PIXEL',nX=256,nY=256,pitchX=55,pitchY=55,topcellname='TOP') : 
    mpx_cell = gdspy.Cell(topcellname)
    mpx_cell.add(gdspy.CellArray(pixelcellname, nX, nY,(pitchX,pitchY),(pitchX/2.,pitchY/2.)))
    mpx_cell.add(gdspy.CellArray('GR', 1, 1,(0,0),(nX*pitchX/2.,nY*pitchY/2.)))

def GenerateGuardRings(inner_size_X,inner_size_Y, positions, inner_edge, outer_edge, doping_width, cellname='GR',bump_radius=10.) :
        gr_cell = gdspy.Cell(cellname)
        for i,position in enumerate(positions) :
            print "building GR %i position : %f"%(i,position)
            ## Aluminium Layer
            center = (0,0)
            ALinner_width = 15
            ALouter_width = 20
            hiw= ALinner_width/2.0
            radius = position+outer_edge[i]
            ##### Sides
            gr_cell.add(gdspy.Rectangle(0,(inner_size_X/2.+position-inner_edge[i],-inner_size_X/2.),(inner_size_X/2.+position+outer_edge[i],inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(0,(inner_size_X/2.,inner_size_X/2.+position - inner_edge[i]),(-inner_size_X/2.,inner_size_X/2.+position+outer_edge[i])))
            gr_cell.add(gdspy.Rectangle(0,(-inner_size_X/2.-position+inner_edge[i],inner_size_X/2.),(-inner_size_X/2.-position-outer_edge[i],-inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(0,(-inner_size_X/2.,-inner_size_X/2.-position + inner_edge[i]),(inner_size_X/2,-inner_size_X/2.-position - outer_edge[i])))

            ##### Rounded corners
            gr_cell.add(gdspy.Round(0, (inner_size_X/2.,inner_size_X/2.), radius, inner_radius=position-inner_edge[i],
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
            gr_cell.add(gdspy.Round(0, (inner_size_X/2.,-inner_size_X/2.), radius, inner_radius=position-inner_edge[i],
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
            gr_cell.add(gdspy.Round(0, (-inner_size_X/2., inner_size_X/2.), radius, inner_radius=position-inner_edge[i],
                          initial_angle=numpy.pi/2.,
                          final_angle=numpy.pi))
            gr_cell.add(gdspy.Round(0, (-inner_size_X/2., -inner_size_X/2.), radius, inner_radius=position-inner_edge[i],
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi/2.))

            #Implant Layer
            ## Doping Layer
            center = (0,0)
            ALinner_width = 15
            ALouter_width = 20
            hiw= ALinner_width/2.0
            dw=doping_width/2.
            radius = position+dw
            ##### Sides
            gr_cell.add(gdspy.Rectangle(1,(inner_size_X/2.+position-dw,-inner_size_X/2.),(inner_size_X/2.+position+dw,inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(1,(inner_size_X/2.,inner_size_X/2.+position - dw),(-inner_size_X/2.,inner_size_X/2.+position+dw)))
            gr_cell.add(gdspy.Rectangle(1,(-inner_size_X/2.-position+dw,inner_size_X/2.),(-inner_size_X/2.-position-dw,-inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(1,(-inner_size_X/2.,-inner_size_X/2.-position + dw),(inner_size_X/2,-inner_size_X/2.-position - dw)))

            ##### Rounded corners
            gr_cell.add(gdspy.Round(1, (inner_size_X/2.,inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
            gr_cell.add(gdspy.Round(1, (inner_size_X/2.,-inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
            gr_cell.add(gdspy.Round(1, (-inner_size_X/2., inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=numpy.pi/2.,
                          final_angle=numpy.pi))
            gr_cell.add(gdspy.Round(1, (-inner_size_X/2., -inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi/2.))
           #Contact Layer
            ## Doping Layer
            center = (0,0)
            ALinner_width = 15
            ALouter_width = 20
            hiw= ALinner_width/2.0
            dw=doping_width/2.
            radius = position+dw
            ##### Sides
            gr_cell.add(gdspy.Rectangle(2,(inner_size_X/2.+position-dw,-inner_size_X/2.),(inner_size_X/2.+position+dw,inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(2,(inner_size_X/2.,inner_size_X/2.+position - dw),(-inner_size_X/2.,inner_size_X/2.+position+dw)))
            gr_cell.add(gdspy.Rectangle(2,(-inner_size_X/2.-position+dw,inner_size_X/2.),(-inner_size_X/2.-position-dw,-inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(2,(-inner_size_X/2.,-inner_size_X/2.-position + dw),(inner_size_X/2,-inner_size_X/2.-position - dw)))

            ##### Rounded corners
            gr_cell.add(gdspy.Round(2, (inner_size_X/2.,inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
            gr_cell.add(gdspy.Round(2, (inner_size_X/2.,-inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
            gr_cell.add(gdspy.Round(2, (-inner_size_X/2., inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=numpy.pi/2.,
                          final_angle=numpy.pi))
            gr_cell.add(gdspy.Round(2, (-inner_size_X/2., -inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi/2.))

            #Passivation Opening
            #Ground Ring bump contact`
            if i==0 : 
                gr_cell.add(gdspy.Round(3, (inner_size_X/2.+position,+inner_size_X/6.), bump_radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=2*numpy.pi))
                gr_cell.add(gdspy.Round(3, (inner_size_X/2.+position,-inner_size_X/6.), bump_radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=2*numpy.pi))
                gr_cell.add(gdspy.Round(3, (-inner_size_X/2.-position,inner_size_X/6.), bump_radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=2*numpy.pi))
                gr_cell.add(gdspy.Round(3, (-inner_size_X/2.-position,-inner_size_X/6.), bump_radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=2*numpy.pi))
            #Probing Opening
            opw=0.1*(outer_edge[i]+inner_edge[i])
            gr_cell.add(gdspy.Rectangle(3,(inner_size_X/2.+ position - inner_edge[i] + opw,-inner_size_X/2.),(inner_size_X/2.+ position + outer_edge[i]-opw,- inner_size_X/2.+ 500.)))

        return gr_cell

'''
#Sensor parameters (CLICPix)
pitchX = 25.0
pitchY = 25.0
npix_X = 64
npix_Y = 64
#AL Layer
ALinner_width = 15
ALouter_width = 20
#Implant Laver
IMPinner_width = 12
IMPouter_width = 15
#Passivation Opening
PORadius = 7.5

GeneratePixel(pitchX,pitchY,ALinner_width,ALouter_width,IMPinner_width,IMPouter_width,PORadius,'PIXEL')
GeneratePixelArray('PIXEL',npix_X,npix_Y,pitchX,pitchY,'TOP')


# Save GDSII to File 
name = os.path.abspath(os.path.dirname(os.sys.argv[0])) + os.sep +\
       'CLICPix-Example'
gdspy.gds_print(name + '.gds', unit=1.0e-6, precision=1.0e-9)
print('Sample gds file saved: ' + name + '.gds')
'''


#Sensor parameters (Medipix/Timepix)
pitchX = 55.0
pitchY = 55.0
npix_X = 10
npix_Y = 10
#AL Layer
ALinner_width = 32.5
ALouter_width = 37.5
#Implant Laver
IMPinner_width = 37.5
IMPouter_width = 47.5
#Passivation Opening
PORadius = 10

GeneratePixel(pitchX,pitchY,ALinner_width,ALouter_width,IMPinner_width,IMPouter_width,PORadius,'PIXEL')
GenerateGuardRings(npix_X*pitchX,npix_Y*pitchY, [30., 70., 95, 130, 180, 260, 400], [25.,10.,15,20,32,64,128], [25,5,5,5,5,5,5], 5., cellname='GR')
GeneratePixelArray('PIXEL',npix_X,npix_Y,pitchX,pitchY,'TOP')

# Save GDSII to File 
name = os.path.abspath(os.path.dirname(os.sys.argv[0])) + os.sep +\
       'MPX-Example'
gdspy.gds_print(name + '.gds', unit=1.0e-6, precision=1.0e-9)
print('Sample gds file saved: ' + name + '.gds')


'''
#Sensor parameters (Medipix/Timepix, 3x3 model)
pitchX = 55.0
pitchY = 55.0
npix_X = 3
npix_Y = 3
#AL Layer
ALinner_width = 37.5
ALouter_width = 47.5
#Implant Laver
IMPinner_width = 32.5
IMPouter_width = 37.5
#Passivation Opening
PORadius = 10

GeneratePixel(pitchX,pitchY,ALinner_width,ALouter_width,IMPinner_width,IMPouter_width,PORadius,'PIXEL')
GeneratePixelArray('PIXEL',npix_X,npix_Y,pitchX,pitchY,'TOP')


# Save GDSII to File 
name = os.path.abspath(os.path.dirname(os.sys.argv[0])) + os.sep +\
       'MPX-Example_3x3'
gdspy.gds_print(name + '.gds', unit=1.0e-6, precision=1.0e-9)
print('Sample gds file saved: ' + name + '.gds')
'''




'''
#Sensor parameters (Medipix/Timepix, 3x3 model)
pitchX = 25.0
pitchY = 25.0
npix_X = 3
npix_Y = 3
#AL Layer
ALinner_width = 15
ALouter_width = 20
#Implant Laver
IMPinner_width = 12
IMPouter_width = 15
#Passivation Opening
PORadius = 7.5
GeneratePixel(pitchX,pitchY,ALinner_width,ALouter_width,IMPinner_width,IMPouter_width,PORadius,'PIXEL')
GeneratePixelArray('PIXEL',npix_X,npix_Y,pitchX,pitchY,'TOP')


# Save GDSII to File 
name = os.path.abspath(os.path.dirname(os.sys.argv[0])) + os.sep +\
       'CLICPix-Example_3x3'
gdspy.gds_print(name + '.gds', unit=1.0e-6, precision=1.0e-9)
print('Sample gds file saved: ' + name + '.gds')
'''
